from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from .embeddings import embed_text

app = FastAPI(title="AI/ML Starter")


class EmbedIn(BaseModel):  # type: ignore[misc]
    text: str


@app.get("/health")  # type: ignore[misc]
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/embed")  # type: ignore[misc]
def embed(body: EmbedIn) -> dict[str, Any]:
    vec = embed_text(body.text)
    return {"dim": len(vec), "vector": vec[:8]}  # preview first 8 dims
