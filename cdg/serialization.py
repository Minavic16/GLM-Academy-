"""JSON serialization for round-tripping CDG records (storage-neutral)."""
from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from enum import Enum
from typing import Any


def _default(o: Any):
    if isinstance(o, Enum):
        return o.value
    if is_dataclass(o):
        return asdict(o)
    if isinstance(o, (set, frozenset)):
        return sorted(o)
    raise TypeError(f"not serializable: {type(o)}")


def to_json(obj: Any) -> str:
    return json.dumps(obj, default=_default, indent=2, sort_keys=True)


def dumps_store(store) -> str:
    return to_json(
        {
            "entities": list(store.entities.values()),
            "claims": list(store.claims.values()),
            "evidence": list(store.evidence.values()),
            "sources": list(store.sources.values()),
            "agents": list(store.agents.values()),
            "activities": list(store.activities.values()),
            "migrations": list(store.migrations.values()),
        }
    )
