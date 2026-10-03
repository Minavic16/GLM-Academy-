"""Domain entities of the frozen CDG v0.2 model.

Semantic distinction between entity types is preserved explicitly. A generic
graph node view (`GraphNode`) is provided for visualization/storage plumbing,
but the domain model never collapses entity types.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .enums import ClaimStatus, EntityType


@dataclass
class EntityBase:
    """Common lifecycle/provenance fields shared by all CDG entities."""

    id: str
    entity_type: Optional[EntityType] = None  # set in __post_init__ by subclass
    status: ClaimStatus = ClaimStatus.PROPOSED
    subject: Optional[str] = None  # versioned attribute, NOT encoded in id
    created_by_activity: Optional[str] = None
    created_at: Optional[str] = None  # ISO-8601
    cdg_version: Optional[str] = None
    supersedes: Optional[str] = None
    legacy_ids: list[str] = field(default_factory=list)
    label: str = ""
    definition: str = ""
    reviewed_by_activity: Optional[str] = None
    review_rationale: Optional[str] = None


@dataclass
class Subject(EntityBase):
    pass

    def __post_init__(self):
        self.entity_type = EntityType.SUBJECT


@dataclass
class CurriculumFramework(EntityBase):
    publisher: Optional[str] = None

    def __post_init__(self):
        self.entity_type = EntityType.CURRICULUM_FRAMEWORK


@dataclass
class CurriculumItem(EntityBase):
    framework_id: Optional[str] = None
    verbatim_text: str = ""

    def __post_init__(self):
        self.entity_type = EntityType.CURRICULUM_ITEM


@dataclass
class KnowledgeComponent(EntityBase):
    """An ability; no stem/options/format. Opaque id (no subject prefix)."""

    def __post_init__(self):
        self.entity_type = EntityType.KNOWLEDGE_COMPONENT


@dataclass
class TaskModel(EntityBase):
    """A family of tasks evidencing >=1 KC."""

    def __post_init__(self):
        self.entity_type = EntityType.TASK_MODEL


@dataclass
class Method(EntityBase):
    task_model_id: Optional[str] = None  # exactly one TaskModel

    def __post_init__(self):
        self.entity_type = EntityType.METHOD


@dataclass
class Item(EntityBase):
    task_model_id: Optional[str] = None  # exactly one TaskModel
    stem: str = ""
    options: list[str] = field(default_factory=list)
    key: Optional[str] = None

    def __post_init__(self):
        self.entity_type = EntityType.ITEM


@dataclass
class Misconception(EntityBase):
    def __post_init__(self):
        self.entity_type = EntityType.MISCONCEPTION


@dataclass
class GraphNode:
    """Internal generic projection used only by storage/visualization plumbing.

    It never replaces the typed domain entities above.
    """

    id: str
    entity_type: Optional[EntityType]
    label: str
    attributes: dict = field(default_factory=dict)
