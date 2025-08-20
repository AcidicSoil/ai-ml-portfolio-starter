import chromadb

Client = chromadb.PersistentClient


def topk(query: str, k: int = 4, db_path: str = "./.rag") -> list[tuple[str, float]]:
    client = Client(path=db_path)
    col = client.get_or_create_collection("code")
    res = col.query(query_texts=[query], n_results=k)
    out = list(
        zip(res.get("documents", [[]])[0], res.get("distances", [[]])[0], strict=False)
    )
    return out
