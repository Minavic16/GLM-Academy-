"""Frozen CDG v0.2 enumerations.

These enums encode the closed vocabularies of the frozen CDG v0.2 model.
New semantic values must NOT be added here without an owner-authorized spec change.
"""
from __future__ import annotations

from enum import Enum


class EntityType(str, Enum):
    SUBJECT = "Subject"
    CURRICULUM_FRAMEWORK = "CurriculumFramework"
    CURRICULUM_ITEM = "CurriculumItem"
    KNOWLEDGE_COMPONENT = "KnowledgeComponent"
    TASK_MODEL = "TaskModel"
    METHOD = "Method"
    ITEM = "Item"
    MISCONCEPTION = "Misconception"
    CLAIM = "Claim"
    EVIDENCE_ITEM = "EvidenceItem"
    SOURCE = "Source"
    AGENT = "Agent"
    ACTIVITY = "Activity"


class RelationshipType(str, Enum):
    IS_CHILD_OF = "isChildOf"
    MAPS_TO = "mapsTo"
    ALIGNS_TO = "alignsTo"
    BROADER = "broader"
    TARGETS = "targets"
    HAS_METHOD = "hasMethod"
    REQUIRES = "requires"
    PREREQUISITE = "prerequisite"
    PRECEDES = "precedes"
    RELATED_MISCONCEPTION = "relatedMisconception"
    INDICATES = "indicates"


class PrerequisitePurpose(str, Enum):
    EXECUTE = "EXECUTE"
    UNDERSTAND = "UNDERSTAND"


class PrerequisiteScope(str, Enum):
    ALL_RELEVANT_METHODS = "ALL_RELEVANT_METHODS"
    SPECIFIC_METHOD = "SPECIFIC_METHOD"
    SPECIFIC_TASK_MODEL = "SPECIFIC_TASK_MODEL"


class ClaimOrigin(str, Enum):
    ASSERTED = "ASSERTED"
    DERIVED = "DERIVED"


class MatchQualifier(str, Enum):
    EXACT = "EXACT"
    CLOSE = "CLOSE"
    BROAD = "BROAD"
    NARROW = "NARROW"


class AlignmentQualifier(str, Enum):
    EXPLICIT = "EXPLICIT"
    IMPLIED = "IMPLIED"
    REQUIRED_TO_EXECUTE = "REQUIRED_TO_EXECUTE"


class IndicatesPolarity(str, Enum):
    EVIDENCE_OF_MASTERY = "EVIDENCE_OF_MASTERY"
    EVIDENCE_OF_NON_MASTERY = "EVIDENCE_OF_NON_MASTERY"


class ClaimStatus(str, Enum):
    PROPOSED = "PROPOSED"
    UNDER_REVIEW = "UNDER_REVIEW"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    CONTESTED = "CONTESTED"
    DEPRECATED = "DEPRECATED"


class AcceptanceBasis(str, Enum):
    CURRICULUM = "CURRICULUM"
    MATHEMATICAL = "MATHEMATICAL"
    EXPERT = "EXPERT"
    EMPIRICAL = "EMPIRICAL"


class ClaimType(str, Enum):
    CURRICULUM = "CURRICULUM"
    CROSSWALK = "CROSSWALK"
    ALIGNMENT = "ALIGNMENT"
    DOMAIN = "DOMAIN"
    DEPENDENCY = "DEPENDENCY"
    ASSESSMENT_DESIGN = "ASSESSMENT_DESIGN"
    MISCONCEPTION = "MISCONCEPTION"
    NAVIGATION = "NAVIGATION"


class EvidenceRole(str, Enum):
    DIRECT = "DIRECT"
    INDIRECT = "INDIRECT"
    EMPIRICAL_LEARNER = "EMPIRICAL_LEARNER"
    AGENT_INFERENCE = "AGENT_INFERENCE"


class EvidenceStance(str, Enum):
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    NEUTRAL = "NEUTRAL"


class ExcerptKind(str, Enum):
    VERBATIM = "VERBATIM"
    PARAPHRASE = "PARAPHRASE"


class AgentKind(str, Enum):
    HUMAN = "HUMAN"
    AI_AGENT = "AI_AGENT"
    PIPELINE = "PIPELINE"


class ActivityType(str, Enum):
    EXTRACTION = "EXTRACTION"
    INTERPRETATION = "INTERPRETATION"
    REVIEW = "REVIEW"
    MIGRATION = "MIGRATION"
    AUTOMATED_CHECK = "AUTOMATED_CHECK"


class SourceType(str, Enum):
    SYLLABUS = "SYLLABUS"
    TEXTBOOK = "TEXTBOOK"
    DATASET = "DATASET"
    PAPER = "PAPER"
    LEGACY_DATASET = "LEGACY_DATASET"
    OTHER = "OTHER"


class MigrationDisposition(str, Enum):
    MAPPED = "MAPPED"
    SPLIT = "SPLIT"
    MERGED = "MERGED"
    CONVERTED_TO_TASKMODEL = "CONVERTED_TO_TASKMODEL"
    CONVERTED_TO_METHOD = "CONVERTED_TO_METHOD"
    RETIRED = "RETIRED"
    PENDING_REVIEW = "PENDING_REVIEW"
