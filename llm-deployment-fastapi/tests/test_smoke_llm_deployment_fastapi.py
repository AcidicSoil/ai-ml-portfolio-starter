import pathlib
import sys


def test_app_imports():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    import app  # type: ignore

    assert hasattr(app, "app"), "FastAPI app should be defined"

