import pathlib
import sys


def test_clean_records():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from llm_datasets_toolkit.clean import clean_records  # type: ignore

    data = [{"text": "  Hello  "}, {"text": "hello"}, {"text": ""}]
    out = clean_records(data)
    assert out == [{"text": "Hello"}]

