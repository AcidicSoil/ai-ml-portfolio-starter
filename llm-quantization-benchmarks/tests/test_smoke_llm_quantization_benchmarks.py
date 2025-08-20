import pathlib
import sys


def test_bench_stub():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from llm_quantization_benchmarks.bench import run_benchmark  # type: ignore

    res = run_benchmark("mistral-7b", "int4")
    assert "tokens_per_sec" in res and "mem_gb" in res and "quality_score" in res

