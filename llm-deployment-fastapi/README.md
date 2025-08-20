# Dockerized LLM Inference API

**Repo:** `llm-deployment-fastapi` • **Last Updated:** 2025-08-19

## 🎯 Goal

Expose a streaming inference API with batching, timeouts, and simple auth.

## 🧱 Tech Stack

Python, FastAPI, Docker, uvicorn, Gunicorn

## 🔗 Upstream / Tools Used

fastapi, uvicorn, gunicorn, pydantic

## ✅ Success Metrics

- Throughput (req/sec)
- Latency p50/p95
- Container image size

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
llm-deployment-fastapi/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- Docker compose up
- Websocket streaming example
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
