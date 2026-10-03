"""Status lifecycle and admissible acceptance bases (adopted contract)."""
from __future__ import annotations

from .enums import AcceptanceBasis, ClaimStatus, ClaimType

# PROPOSED → UNDER_REVIEW → ACCEPTED | REJECTED | CONTESTED
# CONTESTED → UNDER_REVIEW
# ACCEPTED → DEPRECATED   (only via a superseding record)
ALLOWED_TRANSITIONS: dict[ClaimStatus, frozenset[ClaimStatus]] = {
    ClaimStatus.PROPOSED: frozenset({ClaimStatus.UNDER_REVIEW}),
    ClaimStatus.UNDER_REVIEW: frozenset(
        {ClaimStatus.ACCEPTED, ClaimStatus.REJECTED, ClaimStatus.CONTESTED}
    ),
    ClaimStatus.CONTESTED: frozenset({ClaimStatus.UNDER_REVIEW}),
    ClaimStatus.ACCEPTED: frozenset({ClaimStatus.DEPRECATED}),
    ClaimStatus.REJECTED: frozenset(),
    ClaimStatus.DEPRECATED: frozenset(),
}

ADMISSIBLE_ACCEPTANCE_BASES: dict[ClaimType, frozenset[AcceptanceBasis]] = {
    ClaimType.CURRICULUM: frozenset({AcceptanceBasis.CURRICULUM}),
    ClaimType.CROSSWALK: frozenset({AcceptanceBasis.EXPERT}),
    ClaimType.ALIGNMENT: frozenset({AcceptanceBasis.EXPERT}),
    ClaimType.DOMAIN: frozenset({AcceptanceBasis.MATHEMATICAL, AcceptanceBasis.EXPERT}),
    ClaimType.DEPENDENCY: frozenset({AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL}),
    ClaimType.ASSESSMENT_DESIGN: frozenset({AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL}),
    ClaimType.MISCONCEPTION: frozenset({AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL}),
    ClaimType.NAVIGATION: frozenset(
        {
            AcceptanceBasis.CURRICULUM,
            AcceptanceBasis.MATHEMATICAL,
            AcceptanceBasis.EXPERT,
            AcceptanceBasis.EMPIRICAL,
        }
    ),
}


def transition_allowed(old: ClaimStatus, new: ClaimStatus) -> bool:
    return new in ALLOWED_TRANSITIONS.get(old, frozenset())
