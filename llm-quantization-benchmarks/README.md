# Quantization Benchmarks for Local LLMs

**Repo:** `llm-quantization-benchmarks` • **Last Updated:** 2025-08-19

## 🎯 Goal

Compare FP16 vs. INT8/INT4 (GGUF/GPTQ/AWQ) on latency, memory, and quality across hardware.

## 🧱 Tech Stack

Python, llama.cpp, AutoGPTQ, AWQ, GGUF

## 🔗 Upstream / Tools Used

llama.cpp, auto-gptq, awq, gguf

## ✅ Success Metrics

- Tokens/sec (prompt + generation)
- Peak memory usage
- Accuracy on small QA set / MT-Bench-lite score (proxy)

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
llm-quantization-benchmarks/
  ├─ src/
  ├─ demo.py
  ├─ eval/
  ├─ results/
  ├─ tests/
  ├─ requirements.txt
  └─ README.md
```

## 📸 Demos

- Scripts to run batch benches
- Markdown tables & plots
-

## 🗺️ Roadmap

- [ ] Define baseline & target metrics
- [ ] Implement MVP
- [ ] Add CI checks
- [ ] Document limitations & next steps

## ⚖️ License

MIT (adjust as needed). Respect upstream licenses.
