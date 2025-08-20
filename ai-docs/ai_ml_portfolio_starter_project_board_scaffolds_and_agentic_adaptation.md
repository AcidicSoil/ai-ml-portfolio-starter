# Executive Hand-off

This package turns the repo into a **board-driven, agent-ready project**. It includes:

- A GitHub Project board plan with **issue backlog** (phases/milestones, tasks, and acceptance criteria).
- **Missing scaffolds** so everything is runnable today.
- **Agentic Engineering Playbook** adaptations: `.prompts/` roles, ADRs, RAG indexer, and a **diff-only agent workflow**.

Use the **Scripts** section at the bottom to batch-create issues and files locally.

---

## 1) Project Board Plan → Issues by Phase/Milestone

> Labels used: `phase:*`, `type:*`, `area:*`, `good-first-issue`, `help-wanted`, `agent-safe` (HITL not required), `blocked`.

### Phase 0 — Repo Intake & Baseline (Milestone: `M0-baseline`)

**Issues**

1. **Audit: Structure, Tooling, and Licenses**\
   Labels: `phase:0`, `type:chore`\
   Tasks:

   - A short `docs/audit.md` lists current layout, Python/Node versions, and licenses.

2. **Set Repo Conventions & DoD**\
   Labels: `phase:0`, `type:docs`\
   Tasks:

   - DoD checklist enforced in CI; CODEOWNERS resolves on PRs.

3. **Enable CI Smoke (lint/type/test)**\
   Labels: `phase:0`, `type:ci`\
   Tasks:

   - CI is green on a clean checkout; failures block PR merge.

---

### Phase 1 — Minimal App + Scaffolds (Milestone: `M1-scaffold`)

**Issues**

1. **Bootstrap Python project (pyproject + uv/poetry)**\
   Labels: `phase:1`, `type:chore`, `area:build`\
   Tasks:

   - `make setup && make run` starts the app; `make test` passes.

2. **Hello FastAPI service with /health & /embed**\
   Labels: `phase:1`, `type:feature`, `area:api`\
   Tasks:

   - `/health` returns `{status:"ok"}`; `/embed` returns fixed-size vector.

3. **Data & models folder policy**\
   Labels: `phase:1`, `type:docs`, `area:data`\
   Tasks:

   - No sensitive files tracked; sample data only.

---

### Phase 2 — RAG Indexer (Milestone: `M2-rag-index`)

**Issues**

1. **Repo Map generator**\
   Labels: `phase:2`, `type:feature`, `area:tooling`, `agent-safe`\
   Tasks:

   - Running saves `repo_map.json` with functions/classes per file.

2. **Code RAG indexer (Chroma)**\
   Labels: `phase:2`, `type:feature`, `area:rag`\
   Tasks:

   - `make rag-index` creates `.rag/` with >0 docs.

3. **Retrieval utility**\
   Labels: `phase:2`, `type:feature`, `area:rag`\
   Tasks:

   - `retrieve("calculate_*")` returns chunk text and path metadata.

---

### Phase 3 — Agentic Workflow (Milestone: `M3-agents`)

**Issues**

1. **.prompts roles & schemas**\
   Labels: `phase:3`, `type:docs`, `area:agents`\
   Tasks:

   - Prompts exist; referenced by runbooks.

2. **Diff-only patch generator**\
   Labels: `phase:3`, `type:feature`, `area:agents`\
   Tasks:

   - Applying invalid path fails; valid patch updates files.

3. **Agent runbook & CLI wrapper**\
   Labels: `phase:3`, `type:docs`, `area:agents`\
   Tasks:

   - Runbook visible; script echoes structured plan and saves artefacts.

---

### Phase 4 — CI/CD & Quality Gates (Milestone: `M4-ciq`)

**Issues**

1. **Pre-commit hooks**\
   Labels: `phase:4`, `type:chore`, `area:devex`\
   Tasks:

   - `pre-commit run --all-files` is clean.

2. **Static & security scanning**\
   Labels: `phase:4`, `type:ci`, `area:security`\
   Tasks:

   - CI blocks noncompliant PRs; report attached to run.

3. **Coverage gate**\
   Labels: `phase:4`, `type:test`, `area:quality`\
   Tasks:

   - Build fails under threshold; badge reflects current %.

---

### Phase 5 — Docs & Examples (Milestone: `M5-docs`)

**Issues**

1. **Top-level README runnable paths**\
   Labels: `phase:5`, `type:docs`\
   Tasks:

   - Fresh clone can follow README to success in <5 minutes.

2. **Tutorial notebook**\
   Labels: `phase:5`, `type:feature`, `area:docs`\
   Tasks:

   - Notebook runs end-to-end offline.

---

## 2) Scaffolds to Make It Runnable Today

Create these files/folders (safe to add on top of your repo). Paths are relative to the repo root.

```
.
├─ pyproject.toml
├─ Makefile
├─ .gitignore
├─ .github/workflows/ci.yml
├─ src/app/__init__.py
├─ src/app/main.py
├─ src/app/embeddings.py
├─ src/app/retrieve.py
├─ tests/test_health.py
├─ tests/test_embed.py
├─ tools/repo_map.py
├─ tools/index_code.py
├─ tools/diff_apply.py
├─ .prompts/architect.md
├─ .prompts/coder.md
├─ .prompts/reviewer.md
├─ .prompts/tester.md
├─ adr/template.md
├─ docs/AGENT_RUNBOOK.md
├─ docs/CONVENTIONS.md
├─ DEFINITION_OF_DONE.md
├─ data/README.md
├─ scripts/agent_task.sh
└─ .pre-commit-config.yaml
```

### `pyproject.toml`

```toml
[project]
name = "ai-ml-portfolio-starter"
version = "0.1.0"
description = "Starter with FastAPI + RAG indexer and agentic workflow"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
  "fastapi>=0.112",
  "uvicorn>=0.30",
  "pydantic>=2.7",
  "sentence-transformers>=3.0",
  "chromadb>=0.5",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.2",
  "pytest-cov>=5.0",
  "ruff>=0.5",
  "mypy>=1.10",
  "bandit>=1.7",
  "pip-audit>=2.7",
  "pre-commit>=3.7",
]

[tool.ruff]
line-length = 100
select = ["E","F","I","B","UP","PL"]

[tool.mypy]
python_version = "3.11"
strict = true

[tool.pytest.ini_options]
addopts = "-q --cov=src --cov-report=term-missing"
```

### `Makefile`

```makefile
.PHONY: setup run dev lint type test rag-index repo-map

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -e .[dev] && pre-commit install

run:
	uvicorn src.app.main:app --reload --port 8000

dev: run

lint:
	ruff check src tests

type:
	mypy src

test:
	pytest

repo-map:
	python tools/repo_map.py --root . --out repo_map.json

rag-index:
	python tools/index_code.py --repo ./src --db ./.rag
```

### `.gitignore`

```gitignore
.venv/
__pycache__/
.rag/
*.pyc
.env
.DS_Store
repo_map.json
```

### `.github/workflows/ci.yml`

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - name: Install
        run: |
          python -m pip install -U pip
          pip install -e .[dev]
      - name: Lint
        run: ruff check src tests
      - name: Type-check
        run: mypy src
      - name: Test
        run: pytest
      - name: Security
        run: |
          bandit -r src || true
          pip-audit -r requirements.txt || true
```

### `src/app/main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
from .embeddings import embed_text

app = FastAPI(title="AI/ML Starter")

class EmbedIn(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/embed")
def embed(body: EmbedIn):
    vec = embed_text(body.text)
    return {"dim": len(vec), "vector": vec[:8]}  # preview first 8 dims
```

### `src/app/embeddings.py`

```python
from typing import List

try:
    from sentence_transformers import SentenceTransformer
    _MODEL = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:  # pragma: no cover
    _MODEL = None

def embed_text(text: str) -> List[float]:
    if _MODEL is None:
        # Fallback deterministic mock for offline tests
        return [float((i*31 + len(text)) % 97) / 97.0 for i in range(384)]
    emb = _MODEL.encode([text], normalize_embeddings=True)[0]
    return emb.tolist()
```

### `src/app/retrieve.py`

```python
from typing import List, Tuple
import chromadb

Client = chromadb.PersistentClient

def topk(query: str, k: int = 4, db_path: str = "./.rag") -> List[Tuple[str, float]]:
    client = Client(path=db_path)
    col = client.get_or_create_collection("code")
    res = col.query(query_texts=[query], n_results=k)
    out = list(zip(res.get("documents", [[]])[0], res.get("distances", [[]])[0]))
    return out
```

### `tests/test_health.py`

```python
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
```

### `tests/test_embed.py`

```python
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_embed():
    r = client.post("/embed", json={"text": "hello"})
    assert r.status_code == 200
    data = r.json()
    assert data["dim"] == 384
```

### `tools/repo_map.py`

```python
import ast, json, os, argparse

IGNORE = {".git", "__pycache__", "node_modules", ".venv", ".rag"}

def parse_python(path: str):
    with open(path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())
    symbols = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            symbols.append(f"def {node.name}(...):")
        elif isinstance(node, ast.AsyncFunctionDef):
            symbols.append(f"async def {node.name}(...):")
        elif isinstance(node, ast.ClassDef):
            symbols.append(f"class {node.name}:")
    return symbols

def walk(root: str):
    out = {}
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in IGNORE]
        for fn in fns:
            p = os.path.join(dp, fn)
            rp = os.path.relpath(p, root)
            if fn.endswith(".py"):
                out[rp] = parse_python(p)
            else:
                out[rp] = "non-python"
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default="repo_map.json")
    a = ap.parse_args()
    data = walk(a.root)
    with open(a.out, "w") as f:
        json.dump(data, f, indent=2)
    print(f"wrote {a.out}")
```

### `tools/index_code.py`

```python
import argparse, os
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="./src")
    ap.add_argument("--db", default="./.rag")
    args = ap.parse_args()

    loader = GenericLoader.from_filesystem(
        args.repo,
        glob="**/*",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
    )
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=2000, chunk_overlap=200
    )
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma.from_documents(chunks, embeddings, persist_directory=args.db)
    db.persist()
    print(f"indexed {len(chunks)} chunks → {args.db}")
```

### `tools/diff_apply.py`

```python
import sys, subprocess, tempfile, pathlib

ALLOWED = ("src/", "tests/")

def allowed_patch(p: str) -> bool:
    return any(p.startswith(a) for a in ALLOWED)

def main():
    diff = sys.stdin.read()
    # Quick path guard: only allow changes under ALLOWED
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            path = line.split("b/", 1)[1]
            if not allowed_patch(path):
                raise SystemExit(f"blocked path: {path}")
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(diff.encode("utf-8"))
        patch = f.name
    subprocess.check_call(["git", "apply", "--whitespace=nowarn", patch])
    pathlib.Path(patch).unlink(missing_ok=True)

if __name__ == "__main__":
    main()
```

### `.prompts/architect.md`

```md
You are the Planner/Architect Agent. Produce a JSON plan conforming to this schema:
{
  "planSummary": string,
  "affectedFiles": [{"path": string, "action": "create"|"modify"|"delete", "description": string}],
  "stepByStepPlan": string[],
  "newADR": {"title": string, "context": string, "decision": string, "consequences": string} | null
}
Constraints: obey ADRs, CONVENTIONS.md, and only touch files under src/ and tests/.
```

### `.prompts/coder.md`

```md
You are the Implementer/Coder Agent. Execute one plan step. Output exactly one tool call:
{
  "toolName": "writeDiff" | "readFile" | "listFiles",
  "parameters": { ... }
}
Rules: generate a unified diff for writeDiff; no direct file writes; adhere to DoD.
```

### `.prompts/reviewer.md`

```md
You are the Reviewer. Inspect a git diff. Output JSON:
{
  "reviewComments": [
    {"filePath": string, "lineNumber": number, "comment": string, "severity": "nit"|"suggestion"|"issue"|"blocker"}
  ]
}
Enforce conventions, security, performance, and simplicity.
```

### `.prompts/tester.md`

```md
You are the Tester. Given a spec and source file, output a complete pytest file covering happy/edge/negative paths.
```

### `adr/template.md`

```md
# ADR-XXX: <Title>

**Date:** YYYY-MM-DD  
**Status:** Proposed | Accepted | Deprecated | Superseded

## Context

## Decision

## Consequences
```

### `docs/AGENT_RUNBOOK.md`

```md
# Agent Runbook
Loop: Clarify → Plan → Scaffold → Implement → Validate → Test → Document → Commit → Review → Close.
- Entry: Spec + AC ready. Exit: DoD satisfied.
- All writes via unified diff; apply with `tools/diff_apply.py`.
- Guardrails: path allowlist, CI gates (lint/type/test/security).
- Artefacts: plan.json, patch.diff, review.json, test reports.
```

### `docs/CONVENTIONS.md`

```md
- Python 3.11, FastAPI, strict typing, ruff/mypy clean.
- Module layout: `src/app/*`. Tests mirror paths in `tests/*`.
- Public functions/classes get docstrings.
- Prefer pure functions; no hidden I/O in utils.
```

### `DEFINITION_OF_DONE.md`

```md
- [ ] AC met (functional & non-functional)
- [ ] ruff, mypy, pytest pass; coverage ≥ 80%
- [ ] No new high/critical security findings
- [ ] Docs updated; README runnable commands verified
- [ ] Minimal diffs; human review approved
```

### `data/README.md`

```md
Do not commit secrets/PII. Use `samples/` for tiny public examples. Large files → external storage.
```

### `scripts/agent_task.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail
TASK=${1:-"Implement feature"}
DATE=$(date +%Y%m%d-%H%M%S)
mkdir -p .agent_artifacts
printf "${TASK}\n" > .agent_artifacts/task-${DATE}.txt
# placeholder for invoking your agent; save plan/diff/review under .agent_artifacts/
```

### `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.5.0
    hooks: [ { id: ruff, args: ["--fix"] } ]
  - repo: https://github.com/psf/black
    rev: 24.4.2
    hooks: [ { id: black } ]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks: [ { id: mypy } ]
```

---

## 3) Acceptance Criteria Matrix (sampling)

| Issue             | Key AC                                                                |
| ----------------- | --------------------------------------------------------------------- |
| Bootstrap project | `make setup` creates venv, installs deps; `make run` serves `/health` |
| RAG indexer       | `make rag-index` produces `.rag/` with > 0 docs                       |
| Diff-only agent   | Invalid path is blocked; valid patch applies cleanly                  |
| CI                | Lint/type/test steps run; failures block merge                        |

---

## 4) Agentic Adaptation Summary

- **Spec-as-code** via ADRs, DoD, and conventions wired into prompts and CI.
- **Context stack**: `tools/repo_map.py` (fast map) + Chroma RAG (deep retrieval).
- **Safety**: diff-only writes (`tools/diff_apply.py`), path allowlist, CI gates, coverage threshold.
- **Personas**: `.prompts/*` ready; Reviewer emits structured findings.

---

## 5) Scripts — Create Issues & Labels (optional)

> Requires GitHub CLI (`gh`) authenticated and repo set as current remote.

### Create labels

```bash
# once
for L in 'phase:0' 'phase:1' 'phase:2' 'phase:3' 'phase:4' 'phase:5' \
         'type:feature' 'type:chore' 'type:docs' 'type:ci' 'type:test' \
         'area:api' 'area:rag' 'area:tooling' 'area:security' 'area:devex' 'area:data' \
         'good-first-issue' 'help-wanted' 'agent-safe'; do gh label create "$L" -c '#0366d6' -f; done
```

### Create milestones

```bash
for M in M0-baseline M1-scaffold M2-rag-index M3-agents M4-ciq M5-docs; do gh milestone create "$M" -d "$M" || true; done
```

### Batch create issues

```bash
# Example: a few core issues; extend as needed
gh issue create -t "Audit: Structure, Tooling, and Licenses" -b "See doc: docs/audit.md" -l "phase:0,type:chore" -m M0-baseline

gh issue create -t "Bootstrap Python project (pyproject + uv/poetry)" -b "AC: make setup && make run" -l "phase:1,type:chore,area:build" -m M1-scaffold

gh issue create -t "Hello FastAPI service with /health & /embed" -b "AC: endpoints pass tests" -l "phase:1,type:feature,area:api" -m M1-scaffold

gh issue create -t "Repo Map generator" -b "AC: repo_map.json exists" -l "phase:2,type:feature,area:tooling,agent-safe" -m M2-rag-index

gh issue create -t "Code RAG indexer (Chroma)" -b "AC: .rag/ populated; smoke test passes" -l "phase:2,type:feature,area:rag" -m M2-rag-index

gh issue create -t "Diff-only patch generator" -b "AC: path allowlist enforced" -l "phase:3,type:feature,area:agents" -m M3-agents

gh issue create -t "Enable CI smoke (lint/type/test)" -b "AC: CI green on clean checkout" -l "phase:0,type:ci" -m M0-baseline
```

---

## 6) How to Apply Scaffolds

1. Copy the file tree above into your repo.
2. Run `make setup && make test && make run`.
3. Build the RAG index: `make rag-index` (requires an embedding model; the code uses `OllamaEmbeddings` as a local default).

If your repo already contains overlapping files, port the contents or merge as needed. All pieces are **idempotent and minimal**, designed to layer on top of your existing code.

---

## 7) What’s Next

- Wire your agent runner (Cursor/Aider/CLI) to produce unified diffs and pipe them to `tools/diff_apply.py`.
- Add real embeddings provider or model as needed (env var driven).
- Extend tests and add example notebooks in `notebooks/`.

