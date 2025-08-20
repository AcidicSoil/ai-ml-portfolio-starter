# Local RAG Assistant (Docs → Answers)

**Repo:** `local-rag-assistant` • **Last Updated:** 2025-08-19

## 🎯 Goal

Build a retrieval-augmented assistant over local docs (PDF/Markdown) with streaming answers.

## 🧱 Tech Stack

Python, FastAPI, Chroma/FAISS, Sentence-Transformers, uvicorn

## 🔗 Upstream / Tools Used

chromadb, faiss-cpu, sentence-transformers, pydantic

## ✅ Success Metrics

- Top-k retrieval precision@k
- Latency p50/p95
- Qualitative answer correctness on 30 curated questions

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
local-rag-assistant/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- Web UI (simple HTML)
- Curl examples
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
