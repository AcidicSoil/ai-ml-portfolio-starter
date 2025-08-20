import pathlib
import sys


def test_import_and_triage():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from agent_playground_lite.triage import triage_items  # type: ignore

    out = triage_items([{"title": "A"}])
    assert isinstance(out, list) and out[0]["priority"] == "low"

