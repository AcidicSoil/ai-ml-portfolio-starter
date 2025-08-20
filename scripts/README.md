scripts/

gemini.sh — wrapper for the `gemini` CLI aligned with GEMINI.md

Features

- Uses `GEMINI.md` as hierarchical context (auto-loaded by the CLI).
- Interactive and one-shot modes.
- Extracts unified diff blocks (***Begin Patch ...*** End Patch) to `.agent/last.patch`.

Prerequisites

- The `gemini` CLI installed. Override the binary with env `GEMINI_CMD` (or `GEMINI_CLI_CMD`) or `--cmd`.

Usage

- Interactive:
  - `scripts/gemini.sh`
    - The CLI auto-loads `GEMINI.md`; no extra flags needed.

- One-shot with diff capture:
  - `scripts/gemini.sh --task "Add email validation to signup endpoint per AC"`
  - Output is logged to `.agent/logs/session_*.log`.
  - If the agent emits patch blocks, they are saved to `.agent/last.patch`.

- Custom CLI command:
  - `scripts/gemini.sh --cmd genai --task "..."`

- Disable diff extraction or choose output path:
  - `scripts/gemini.sh --no-diff --task "..."`
  - `scripts/gemini.sh --diff-out .agent/patches/feature.patch --task "..."`

Notes

- The CLI loads `GEMINI.md` automatically as context; manage scopes via `.gemini/settings.json` if needed.
- Review `.agent/last.patch` before applying via `git apply` or your preferred patch workflow.
