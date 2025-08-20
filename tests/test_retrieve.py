import importlib
import sys
import types
from typing import Any, cast


def test_topk_with_stub(monkeypatch: Any) -> None:
    # Provide a minimal stub for the optional chromadb import used by app.retrieve
    chroma_stub = cast(Any, types.ModuleType("chromadb"))
    chroma_stub.PersistentClient = object
    sys.modules["chromadb"] = chroma_stub

    # Import (or reload) after injecting the stub so module import succeeds offline
    from app import retrieve as retrieve_module

    importlib.reload(retrieve_module)

    class FakeCollection:
        def query(
            self, query_texts: list[str], n_results: int
        ) -> dict[str, list[list[Any]]]:
            docs = [f"doc{i}" for i in range(5)]
            dists = [i * 0.1 for i in range(5)]
            return {"documents": [docs[:n_results]], "distances": [dists[:n_results]]}

    class FakeClient:
        def __init__(self, path: str) -> None:
            # path is ignored in the stub
            pass

        def get_or_create_collection(self, name: str) -> FakeCollection:
            return FakeCollection()

    monkeypatch.setattr(retrieve_module, "Client", FakeClient)

    out = retrieve_module.topk("what is this?", k=3, db_path="/tmp/does-not-matter")
    assert out == [("doc0", 0.0), ("doc1", 0.1), ("doc2", 0.2)]
