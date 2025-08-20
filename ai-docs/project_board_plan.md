# AI/ML Portfolio Starter – Project Board & Scaffolding Plan

This plan adapts the **AI/ML Portfolio Starter** repo into a structured, agent‑friendly workflow following the **Agentic Engineering Playbook**【24†LLM Agent Codebase Playbook.md】.

---

## 📌 Project Board – Phases & Issues

### **Phase 0: Foundation & Repo Hygiene**

- **Issue 0.1 – Add Agentic Scaffolds**

  - Tasks: Add `.prompts/`, `adr/`, `DEFINITION_OF_DONE.md`, `CONTRIBUTING.md`, CI workflow.
  - AC: Repo passes lint, CI runs, ADR template in place.

- **Issue 0.2 – Environment Setup**

  - Tasks: Create `pyproject.toml` (Poetry), `requirements.txt`, `.devcontainer/` (Dockerfile + config).
  - AC: `poetry install` runs clean, devcontainer starts.

---

### **Phase 1: Core ML Portfolio Scaffolding**

- **Issue 1.1 – Data Module**

  - Tasks: Scaffold `src/data/`, add loaders for CSV/JSON, unit tests.
  - AC: `pytest tests/test_data.py` passes with sample data.

- **Issue 1.2 – Models Module**

  - Tasks: Scaffold `src/models/`, add baseline model class, placeholder configs.
  - AC: `pytest tests/test_models.py` passes with a dummy model.

- **Issue 1.3 – Training Scripts**

  - Tasks: Add `src/train.py`, minimal CLI (`argparse`/`typer`).
  - AC: `python src/train.py --help` runs.

- **Issue 1.4 – Evaluation Module**

  - Tasks: Add `src/eval.py`, placeholder metrics (accuracy, f1).
  - AC: `pytest tests/test_eval.py` passes.

---

### **Phase 2: Portfolio Apps**

- **Issue 2.1 – Streamlit/Dash App**

  - Tasks: Scaffold `apps/portfolio_app/` with Streamlit entrypoint.
  - AC: `streamlit run apps/portfolio_app/app.py` runs locally.

- **Issue 2.2 – API Service**

  - Tasks: Scaffold `apps/api/` with FastAPI boilerplate.
  - AC: `uvicorn apps.api.main:app --reload` starts server.

---

### **Phase 3: Agentic Enhancements**

- **Issue 3.1 – RAG Indexer**

  - Tasks: Add `tools/indexer.py` for code embedding + ChromaDB store.
  - AC: `python tools/indexer.py` runs and generates DB.

- **Issue 3.2 – Repo Map Generator**

  - Tasks: Add `tools/repo_map.py` for file + symbol map.
  - AC: `python tools/repo_map.py` outputs `repo_map.json`.

- **Issue 3.3 – Diff‑Only Workflow**

  - Tasks: Add `tools/guardrail.py` + enforce diff‑based agent changes.
  - AC: Guardrail blocks disallowed writes, CI validates patches.

---

### **Phase 4: Release & Docs**

- **Issue 4.1 – Documentation Scaffolding**

  - Tasks: Add `docs/`, README updates, usage examples, ADR log.
  - AC: `mkdocs serve` or `pdoc` runs.

- **Issue 4.2 – Deployment**

  - Tasks: Add container build (`Dockerfile`), GitHub Actions for deploy.
  - AC: `docker build .` succeeds.

---

## 📂 Missing Scaffolds to Generate

```
/adr/
  template.md
/.prompts/
  architect.md
  coder.md
  reviewer.md
/src/
  data/__init__.py
  models/__init__.py
  train.py
  eval.py
/tests/
  test_data.py
  test_models.py
  test_eval.py
/apps/
  portfolio_app/app.py
  api/main.py
/tools/
  repo_map.py
  indexer.py
  guardrail.py
/.github/workflows/ci.yml
/DEFINITION_OF_DONE.md
/CONTRIBUTING.md
/pyproject.toml
/devcontainer.json
```

Dependencies:

- **Runtime:** Python 3.11, Poetry
- **Core:** numpy, pandas, scikit-learn, torch, fastapi, streamlit
- **Dev:** pytest, pytest-cov, ruff, mypy
- **Agentic:** langchain, chromadb, pydantic

---

## ✅ Acceptance Criteria Examples

- Every scaffold runs (`pytest`, `streamlit run`, `uvicorn`).
- All ADRs + prompts present.
- CI pipeline enforces lint + tests.
- Repo map + RAG indexer generate artifacts.
- Agent modifications flow through diff workflow.

---

This board + scaffolding ensures the repo is runnable **today**, while embedding the **Agentic Engineering Playbook** principles: spec‑first, ADRs as guardrails, `.prompts/` for agent roles, RAG indexing, and diff‑only workflows.

