"""Dataset cleaning utilities (minimal).

Provide simple deduplication and whitespace normalization.
"""
from __future__ import annotations

from typing import Dict, Iterable, List


def clean_records(items: Iterable[Dict]) -> List[Dict]:
    """Return cleaned, deduplicated list of records by textual content."""
    seen = set()
    cleaned: List[Dict] = []
    for it in items:
        text = (it.get("text") or "").strip()
        key = text.lower()
        if not text or key in seen:
            continue
        seen.add(key)
        new = dict(it)
        new["text"] = text
        cleaned.append(new)
    return cleaned

