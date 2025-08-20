"""Minimal triage agent stub.

Provides a small CLI to tag incoming items with a default priority.
"""
from typing import List, Dict


def triage_items(items: List[Dict]) -> List[Dict]:
    """Assign a low priority to each item (stub)."""
    out = []
    for it in items:
        new = dict(it)
        new.setdefault("priority", "low")
        out.append(new)
    return out


if __name__ == "__main__":
    sample = [{"title": "Example ticket"}]
    print(triage_items(sample))

