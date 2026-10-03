"""Claims: every domain-relationship instance is reified as exactly one Claim."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .enums import (
    AcceptanceBasis,
    ClaimOrigin,
    ClaimStatus,
    ClaimType,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
)


@dataclass
class Claim:
    id: str
    predicate: Optional[RelationshipType]  # None for entity-level claims
    subject_id: str  # source entity id
    object_id: Optional[str]  # target entity id
    claim_type: ClaimType
    status: ClaimStatus = ClaimStatus.PROPOSED
    acceptance_bases: set[AcceptanceBasis] = field(default_factory=set)
    confidence: Optional[str] = None
    supersedes: Optional[str] = None
    legacy_ids: list[str] = field(default_factory=list)
    created_by_activity: Optional[str] = None
    created_at: Optional[str] = None
    cdg_version: Optional[str] = None
    qualifiers: dict = field(default_factory=dict)

    # Prerequisite-specific semantic attributes (required when
    # predicate == PREREQUISITE; stored in qualifiers mirror too).
    purpose: Optional[PrerequisitePurpose] = None
    scope: Optional[PrerequisiteScope] = None
    scope_ref: Optional[str] = None  # method/taskmodel id when scope is specific
    origin: Optional[ClaimOrigin] = None

    # Set by review Activities when transitioning out of PROPOSED.
    review_rationale: Optional[str] = None
