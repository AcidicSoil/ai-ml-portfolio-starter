# CI Pipeline for LLM Eval & Regression Tests

**Repo:** `mlops-ci-eval-pipeline` • **Last Updated:** 2025-08-19

## 🎯 Goal

Automate evals (quality, latency) on every PR and prevent regression before merge.

## 🧱 Tech Stack

GitHub Actions, Python, pytest, JSONL eval sets

## 🔗 Upstream / Tools Used

pytest, requests, matplotlib

## ✅ Success Metrics

- Eval jobs duration
- Pass/fail rate per PR
- Historical trend chart

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
mlops-ci-eval-pipeline/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- Status badges
- PR comments with metrics
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
