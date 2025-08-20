# Lightweight Agent Playground

**Repo:** `agent-playground-lite` • **Last Updated:** 2025-08-19

## 🎯 Goal

Experiment with task-specific agents that use tools (search/files) and deterministic routing.

## 🧱 Tech Stack

Python, DSPy (as a dependency), FastAPI

## 🔗 Upstream / Tools Used

dspy, pydantic

## ✅ Success Metrics

- Task success rate on a 50-task set
- Tool-call accuracy
- Reproducibility (fixed-seed runs)

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
agent-playground-lite/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- Single-file agent demo
- Tool registry JSON
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
