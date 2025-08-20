"""Lightweight retrieval stubs.

Replace with a real vector index (e.g., Chroma/FAISS + Sentence-Transformers).
"""
from typing import List


def index_documents(paths: List[str]) -> int:
    """Index documents from the provided file paths (stub)."""
    return len(paths)


def retrieve(query: str, k: int = 3) -> List[str]:
    """Return top-k dummy matches for a query (stub)."""
    return [f"doc-{i}: about {query}" for i in range(k)]

