from fastapi import FastAPI
from pydantic import BaseModel


class GenerateRequest(BaseModel):
    """Request body for text generation."""
    prompt: str
    max_tokens: int = 128


app = FastAPI(title="LLM Inference API")


@app.get("/health")
def health() -> dict:
    """Basic liveness check."""
    return {"status": "ok"}


@app.post("/generate")
def generate(req: GenerateRequest) -> dict:
    """Stub generation endpoint. Replace with real model call."""
    preview = req.prompt[:50]
    return {"text": f"stub: {preview}", "max_tokens": req.max_tokens}

