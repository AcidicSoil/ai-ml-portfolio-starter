from typing import cast

try:
    from sentence_transformers import SentenceTransformer

    _MODEL = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:  # pragma: no cover
    _MODEL = None


def embed_text(text: str) -> list[float]:
    if _MODEL is None:
        # Fallback deterministic mock for offline tests
        return [float((i * 31 + len(text)) % 97) / 97.0 for i in range(384)]
    emb = _MODEL.encode([text], normalize_embeddings=True)[0]
    return cast(list[float], emb.tolist())
