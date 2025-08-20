# Repository Guidelines

## Project Structure & Module Organization

This is a Python-first, multi-project repo. Each folder under the root (e.g., `local-rag-assistant/`, `llm-deployment-fastapi/`, `agent-playground-lite/`) is a self-contained module with:

- `requirements.txt` (module deps)
- `demo.py` (runnable example)
- `README.md` (module docs)

Recommended additions as you build features: `src/` for code, `tests/` for unit tests, `eval/` for experiments, `results/` for artifacts.

## Build, Test, and Development Commands

From a module directory:

- Create env: `python -m venv .venv && source .venv/bin/activate`  (Windows: `.venv\\Scripts\\activate`)
- Install deps: `pip install -r requirements.txt`
- Run demo: `python demo.py`
- Run tests (if present): `pytest -q`

Example: `cd llm-deployment-fastapi && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python demo.py`

## Coding Style & Naming Conventions

- Python 3.10+; 4-space indentation; UTF-8 files.
- Use type hints and docstrings for public functions.
- Naming: `snake_case` for functions/vars, `PascalCase` for classes, `SCREAMING_SNAKE_CASE` for constants.
- Module layout: place implementions under `src/<package>/` and keep `demo.py` minimal.
- Prefer small, pure functions; avoid side effects in module import scope.

## Testing Guidelines

- Framework: `pytest` (present in several modules’ `requirements.txt`).
- Structure: `tests/test_*.py`; mirror package structure under `tests/`.
- Conventions: Arrange–Act–Assert; use fixtures for I/O or network boundaries.
- Local run: `pytest -q` (add `-k PATTERN` to filter). Aim for meaningful coverage; add `pytest-cov` if measuring coverage.

## Commit & Pull Request Guidelines

- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`.
- Scope by module when helpful: `feat(local-rag-assistant): add hybrid retriever`.
- PRs: include a concise summary, linked issue, and before/after evidence (logs, metrics, or screenshots). Keep PRs small and focused.

## Security & Configuration Tips

- Never commit secrets; use `.env` files and add `.env.example` per module.
- Pin critical dependencies in `requirements.txt` and update with intent.
- For FastAPI services, expose an `app` in `src/app.py` and run with `uvicorn` locally (e.g., `uvicorn src.app:app --reload`).

  ### Documentation-First Routing (Always Apply)

    **Policy:** For user requests involving code examples, setup/configuration steps, or library/API docs, route via a documentation-focused MCP tool.

  - Preferred tools: `docfork`, `sourcebot`, `git-mcp` (set `owner/repo`), generic RAG
  - Fallbacks:
  - Detection cues: "example", "install", "configure", "setup", "API", "SDK", "how to", "usage", "params", "options".
  - Guardrails: Read-only unless explicitly elevated; no secrets exposure; respect repo permissions.

    **Example Invocation (conceptual):**
  - User: "Show me how to configure OAuth for Service X."
  - Agent: Selects `docfork` → extracts relevant guides → returns step-by-step with citations.
