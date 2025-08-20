import pathlib
import sys


def test_train_stub():
    sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / "src"))
    from llm_finetune_supportbot.train_lora import train_lora  # type: ignore

    metrics = train_lora("/tmp/dataset.jsonl", "/tmp/out")
    assert "train_loss" in metrics and "eval_accuracy" in metrics

