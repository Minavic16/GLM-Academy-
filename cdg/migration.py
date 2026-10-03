"""Legacy migration metadata contract (no full dataset migration in this phase)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .enums import MigrationDisposition


@dataclass
class MigrationRecord:
    """Every migrated legacy item must be traceable through this record."""

    id: str
    legacy_ids: list[str]
    disposition: MigrationDisposition
    migration_activity_id: str  # Activity of type MIGRATION
    mapping_rule: str
    target_cdg_version: str
    new_record_ids: list[str] = field(default_factory=list)
    notes: Optional[str] = None
