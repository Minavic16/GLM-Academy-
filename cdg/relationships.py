"""Relationship domain/range table and qualifier requirements (frozen vocabulary)."""
from __future__ import annotations

from .enums import EntityType, RelationshipType

# Explicit domain/range per frozen relation. precedes and indicates are
# validated specially because they allow two ranges.
RELATIONSHIP_DOMAIN_RANGE: dict[RelationshipType, tuple[EntityType, frozenset[EntityType]]] = {
    RelationshipType.IS_CHILD_OF: (EntityType.CURRICULUM_ITEM, frozenset({EntityType.CURRICULUM_ITEM})),
    RelationshipType.MAPS_TO: (EntityType.CURRICULUM_ITEM, frozenset({EntityType.CURRICULUM_ITEM})),
    RelationshipType.ALIGNS_TO: (EntityType.KNOWLEDGE_COMPONENT, frozenset({EntityType.CURRICULUM_ITEM})),
    RelationshipType.BROADER: (EntityType.KNOWLEDGE_COMPONENT, frozenset({EntityType.KNOWLEDGE_COMPONENT})),
    RelationshipType.TARGETS: (EntityType.TASK_MODEL, frozenset({EntityType.KNOWLEDGE_COMPONENT})),
    RelationshipType.HAS_METHOD: (EntityType.TASK_MODEL, frozenset({EntityType.METHOD})),
    RelationshipType.REQUIRES: (EntityType.METHOD, frozenset({EntityType.KNOWLEDGE_COMPONENT})),
    RelationshipType.PREREQUISITE: (EntityType.KNOWLEDGE_COMPONENT, frozenset({EntityType.KNOWLEDGE_COMPONENT})),
    RelationshipType.PRECEDES: (EntityType.KNOWLEDGE_COMPONENT, frozenset({EntityType.KNOWLEDGE_COMPONENT, EntityType.CURRICULUM_ITEM})),
    RelationshipType.RELATED_MISCONCEPTION: (EntityType.MISCONCEPTION, frozenset({EntityType.KNOWLEDGE_COMPONENT})),
    RelationshipType.INDICATES: (EntityType.ITEM, frozenset({EntityType.MISCONCEPTION, EntityType.KNOWLEDGE_COMPONENT})),
}

# Qualifiers required on every claim of the given predicate.
REQUIRED_QUALIFIERS: dict[RelationshipType, tuple[str, ...]] = {
    RelationshipType.MAPS_TO: ("match",),
    RelationshipType.ALIGNS_TO: ("alignment",),
    RelationshipType.PREREQUISITE: ("purpose", "scope", "origin"),
    RelationshipType.INDICATES: ("response_pattern",),
}

# Predicates whose endpoints must never be the same entity.
NO_SELF_LOOP: frozenset[RelationshipType] = frozenset(
    {
        RelationshipType.PREREQUISITE,
        RelationshipType.BROADER,
        RelationshipType.PRECEDES,
        RelationshipType.IS_CHILD_OF,
    }
)

# Predicates that are soft navigation aids and must never feed diagnostics.
NAVIGATION_ONLY: frozenset[RelationshipType] = frozenset({RelationshipType.PRECEDES})
