"""Quantization benchmark stubs.

Replace with actual integration to llama.cpp / GPTQ / AWQ as needed.
"""
from __future__ import annotations

import random
from typing import Dict


def run_benchmark(model: str, quant: str) -> Dict[str, float | str]:
    """Return dummy metrics for a model/quantization pair."""
    tokens_per_sec = random.uniform(10.0, 60.0)
    mem_gb = random.uniform(3.0, 12.0)
    quality = random.uniform(0.5, 0.9)
    return {
        "model": model,
        "quant": quant,
        "tokens_per_sec": round(tokens_per_sec, 2),
        "mem_gb": round(mem_gb, 2),
        "quality_score": round(quality, 3),
    }

