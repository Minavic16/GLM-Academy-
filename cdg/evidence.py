"""Evidence items: immutable records of a Source bearing on one Claim."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .enums import EvidenceRole, EvidenceStance, ExcerptKind


@dataclass(frozen=True)
class EvidenceItem:
    id: str
    claim_id: str
    source_id: str
    role: EvidenceRole
    stance: EvidenceStance
    locator: str
    excerpt: str
    excerpt_kind: ExcerptKind
    extracted_by_activity: str
    quote_verified: Optional[str] = None  # id of verifying Activity
    inherited_from_legacy: bool = False
    legacy_id: Optional[str] = None
