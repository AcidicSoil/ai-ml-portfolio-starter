import pathlib
import sys


def test_rag_imports():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    import app as rag_app  # type: ignore
    from rag.retriever import retrieve  # type: ignore

    assert hasattr(rag_app, "app")
    out = retrieve("test", k=2)
    assert isinstance(out, list) and len(out) == 2

