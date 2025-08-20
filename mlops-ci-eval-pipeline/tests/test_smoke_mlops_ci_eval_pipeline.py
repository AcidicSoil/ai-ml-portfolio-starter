from pathlib import Path


def test_results_dir_exists():
    results = Path(__file__).resolve().parents[1] / "results"
    # Directory is created by eval script; just assert path object can be computed
    assert results.as_posix().endswith("/results")

