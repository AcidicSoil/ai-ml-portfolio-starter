# AI/ML Portfolio Starter

=======================

[![CI](https://github.com/AcidicSoil/ai-ml-portfolio-starter/actions/workflows/ci.yml/badge.svg)](https://github.com/AcidicSoil/ai-ml-portfolio-starter/actions/workflows/ci.yml)

FastAPI app + lightweight RAG tooling and an agentic workflow scaffold. Clean tests, pre-commit, and simple scripts help
you iterate quickly.

## Quickstart

- Create env and install dev deps: `make setup`
- Run the API locally: `make dev` (serves on `http://127.0.0.1:8000`)
- Lint, type-check, test: `make lint`, `make type`, `make test`

## API Endpoints

- `GET /health`: basic health check → `{ "status": "ok" }`
- `POST /embed` with `{ "text": "..." }`: returns vector dim and a short preview. Uses sentence-transformers if
  available, otherwise a deterministic fallback for tests.

## RAG Tools (Phase 2)

- Repo map: `make repo-map` → writes `repo_map.json` summarizing files and Python symbols.
- Code index: `make rag-index` → embeds Python files under `src/` into a local Chroma store at `./.rag`.
  - Prerequisites: Ollama running locally with the `nomic-embed-text` model. Python deps `langchain-community` and
    `langchain-text-splitters` are included in dev extras and installed by `make setup`.

## Project Structure

- `src/app`: FastAPI app (`main.py`), embedding util, retrieval helper.
- `tools/`: `repo_map.py` and `index_code.py` for mapping and indexing.
- `tests/`: API smoke tests; add retrieval tests in Phase 2.
- `.pre-commit-config.yaml`: ruff, mypy and formatting hooks.

## Development Notes

- If `rag-index` fails, ensure Ollama is running and required Python packages are installed. You can skip indexing and
  still run tests and the API.
- This README is UTF-8 encoded to avoid packaging readme parsing errors.
