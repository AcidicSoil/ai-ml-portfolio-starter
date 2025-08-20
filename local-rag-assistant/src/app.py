from fastapi import FastAPI
from pydantic import BaseModel

try:
    # Available after local import path is set or installation
    from rag.retriever import retrieve
except Exception:  # pragma: no cover - fallback if import not available yet
    def retrieve(query: str, k: int = 3):  # type: ignore
        return [f"stub-doc-{i} for: {query}" for i in range(k)]


class IngestRequest(BaseModel):
    paths: list[str]


class AskRequest(BaseModel):
    query: str
    top_k: int = 3


app = FastAPI(title="Local RAG Assistant")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ingest")
def ingest(req: IngestRequest) -> dict:
    # Placeholder: wire this to actual indexing later
    return {"ingested": len(req.paths)}


@app.post("/ask")
def ask(req: AskRequest) -> dict:
    docs = retrieve(req.query, k=req.top_k)
    return {"answers": docs}

