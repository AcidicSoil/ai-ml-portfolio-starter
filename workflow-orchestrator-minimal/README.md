# Deterministic Workflow Orchestrator (Minimal)

**Repo:** `workflow-orchestrator-minimal` • **Last Updated:** 2025-08-19

## 🎯 Goal

Show a state-machine approach to multi-step reasoning with strict validation.

## 🧱 Tech Stack

Python, Pydantic, Typer, Unit tests

## 🔗 Upstream / Tools Used

pydantic, typer, pytest

## ✅ Success Metrics

- Branch coverage in tests
- Error handling rate (invalid state transitions)
-

## 🚀 Quickstart

```bash
# 1) Create and activate env
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install
pip install -r requirements.txt

# 3) Run demo
python demo.py
```

## 📊 Evaluation

- Scripts in `eval/` reproduce metrics.
- Results saved to `results/` as CSV/JSON, summarized in README tables.

## 🧪 Tests

```bash
pytest -q
```

## 📦 Structure

```text
workflow-orchestrator-minimal/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- CLI workflow demo
- State-diagram in docs
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
