# ADR-001: Place RAG indexer deps in dev extras

## Context

The repository includes RAG tooling (`tools/index_code.py`) that uses `langchain-community` and `langchain-text-splitters` to build a local Chroma index from the codebase. These packages are only needed for local indexing and are not required to run the FastAPI app or tests.

Pre-commit runs `mypy` against staged files and will fail if these modules are missing when RAG tooling is modified. We already pinned them for the mypy hook via `additional_dependencies`, but local `make setup` should also install them so that `make rag-index` works out of the box.

## Decision

Add `langchain-community` and `langchain-text-splitters` to the `dev` optional dependency group in `pyproject.toml`. Keep runtime `dependencies` unchanged to avoid increasing the production install surface area.

## Consequences

- Pros: `make setup` (which installs `.[dev]`) provides everything required to run `make rag-index`; pre-commit mypy resolution matches local installs.
- Cons: Slightly larger dev install footprint; no impact on runtime dependencies.
- Risk: If langchain package APIs change, dev installs could break indexing. Mitigation: pin compatible major/minor versions and bump as needed.
