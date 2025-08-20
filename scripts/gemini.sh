#!/usr/bin/env bash
set -euo pipefail

# gemini.sh — wrapper for gemini-cli to enforce repo guardrails
# - Injects GEMINI.md as system instructions
# - Supports interactive and one-shot modes
# - Optionally captures unified diffs (*** Begin Patch ... *** End Patch) to .agent/last.patch

ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
SYSTEM_FILE="$ROOT_DIR/GEMINI.md"
AGENT_DIR="$ROOT_DIR/.agent"
LOG_DIR="$AGENT_DIR/logs"
mkdir -p "$LOG_DIR"

# Underlying CLI command (override with env GEMINI_CMD or GEMINI_CLI_CMD)
# Default binary per upstream docs is `gemini`.
CLI_CMD="${GEMINI_CMD:-${GEMINI_CLI_CMD:-gemini}}"

usage() {
  cat <<'USAGE'
Usage:
  scripts/gemini.sh [options]

Options:
  -t, --task "TEXT"     One-shot mode with the given task prompt
  -i, --interactive      Interactive mode (default if no --task)
  --diff-out PATH        Extract unified diff blocks to PATH (default: .agent/last.patch)
  --no-diff              Do not extract diffs
  --cmd CMD              Underlying CLI command (default: gemini)
  --help                 Show this help

Behavior:
  - Gemini CLI auto-loads GEMINI.md as hierarchical context; no flags required.
  - One-shot mode uses `gemini -p "<task>"` and logs output.
  - If the session outputs patch blocks, they are extracted to the chosen path.
USAGE
}

TASK=""
MODE="interactive"
DIFF_OUT="${ROOT_DIR}/.agent/last.patch"
EXTRACT_DIFF=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    -t|--task)
      TASK=${2:-}
      MODE="oneshot"
      shift 2
      ;;
    -i|--interactive)
      MODE="interactive"
      shift
      ;;
    --diff-out)
      DIFF_OUT=$(realpath "${2:-${DIFF_OUT}}")
      shift 2
      ;;
    --no-diff)
      EXTRACT_DIFF=0
      shift
      ;;
    --cmd)
      CLI_CMD=${2:-$CLI_CMD}
      shift 2
      ;;
    --help|-h)
      usage; exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage; exit 1
      ;;
  esac
done

if ! command -v "$CLI_CMD" >/dev/null 2>&1; then
  echo "Error: underlying CLI '$CLI_CMD' not found. Set GEMINI_CLI_CMD or install gemini-cli." >&2
  exit 127
fi

if [[ ! -f "$SYSTEM_FILE" ]]; then
  echo "Error: System instructions not found at $SYSTEM_FILE" >&2
  exit 1
fi

SYSTEM_CONTENT="$(cat "$SYSTEM_FILE")"

# Build base command (gemini CLI auto-loads context from GEMINI.md; no system flag injection needed)
CMD=("$CLI_CMD")

timestamp() { date +"%Y-%m-%d_%H-%M-%S"; }

extract_diffs() {
  local infile="$1" outpath="$2"
  awk '/^\*\*\* Begin Patch/{flag=1} flag{print} /^\*\*\* End Patch/{flag=0}' "$infile" \
    | sed '/^$/q' > "$outpath" || true
  if [[ -s "$outpath" ]]; then
    echo "Saved patch to $outpath"
  else
    rm -f "$outpath"
    echo "No patch blocks found in output."
  fi
}

trap - EXIT

mkdir -p "$AGENT_DIR"

if [[ "$MODE" == "oneshot" ]]; then
  if [[ -z "$TASK" ]]; then
    echo "Error: --task requires text." >&2
    exit 1
  fi
  LOG_FILE="$LOG_DIR/session_$(timestamp).log"

  # Run underlying CLI in non-interactive mode using -p/--prompt and capture output
  set +e
  "${CMD[@]}" -p "$TASK" | tee "$LOG_FILE"
  STATUS=${PIPESTATUS[0]}
  set -e

  if [[ $EXTRACT_DIFF -eq 1 ]]; then
    mkdir -p "$(dirname "$DIFF_OUT")"
    extract_diffs "$LOG_FILE" "$DIFF_OUT"
  fi

  exit "$STATUS"
else
  # Interactive
  echo "Starting interactive session with $CLI_CMD"
  echo "Using context file: $SYSTEM_FILE (auto-loaded by CLI)"
  echo "Tip: Use --task for one-shot mode with diff capture."

  "${CMD[@]}"
fi
