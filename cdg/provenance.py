"""Provenance and source records: Agent, Activity, Source."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .enums import ActivityType, AgentKind, SourceType


@dataclass
class Agent:
    id: str
    kind: AgentKind
    name: str
    model_or_version: Optional[str] = None  # mandatory for AI_AGENT (enforced in validation)


@dataclass
class Activity:
    id: str
    type: ActivityType
    agent_id: str
    time: str  # ISO-8601
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)
    rationale: Optional[str] = None
    rule_applied: Optional[str] = None


@dataclass
class Source:
    id: str
    title: str
    identifier_or_url: str
    publisher: Optional[str]
    source_type: SourceType
    tier: Optional[str] = None
    edition_or_version: Optional[str] = None
    retrieved_at: Optional[str] = None
    content_hash: Optional[str] = None
