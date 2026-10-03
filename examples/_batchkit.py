"""Shared helpers for Mathematics CDG batch builders."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.enums import (
    AcceptanceBasis,
    ClaimStatus,
    EvidenceRole,
    EvidenceStance,
    ExcerptKind,
)
from cdg.evidence import EvidenceItem


def accept(claim: Claim, rationale: str, bases, review_activity: str) -> Claim:
    claim.status = ClaimStatus.UNDER_REVIEW
    claim.status = ClaimStatus.ACCEPTED
    claim.acceptance_bases = set(bases)
    claim.review_rationale = rationale + f" | REVIEW:{review_activity}"
    return claim


def ev(eid, cid, source, legacy_eid, excerpt, direct, interpret_activity, legacy=True):
    return EvidenceItem(
        id=eid, claim_id=cid, source_id=source,
        role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
        stance=EvidenceStance.SUPPORTS, locator="legacy excerpt",
        excerpt=excerpt,
        excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
        extracted_by_activity=interpret_activity,
        inherited_from_legacy=legacy, legacy_id=legacy_eid,
    )
