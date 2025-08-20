.PHONY: setup run dev lint type test rag-index repo-map

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -e .[dev] && pre-commit install

run:
	uvicorn src.app.main:app --reload --port 8000

dev: run

lint:
	ruff check src tests

type:
	mypy src

test:
	pytest

repo-map:
	python tools/repo_map.py --root . --out repo_map.json

rag-index:
	python tools/index_code.py --repo ./src --db ./.rag
