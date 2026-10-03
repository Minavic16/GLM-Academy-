"""In-memory CDG store: typed records + graph projection + invariant helpers."""
from __future__ import annotations

from typing import Dict, List, Optional, Set

from .claims import Claim
from .entities import EntityBase
from .enums import ClaimStatus, EntityType, RelationshipType
from .evidence import EvidenceItem
from .migration import MigrationRecord
from .provenance import Activity, Agent, Source


class CDGStore:
    def __init__(self) -> None:
        self.entities: Dict[str, EntityBase] = {}
        self.claims: Dict[str, Claim] = {}
        self.evidence: Dict[str, EvidenceItem] = {}
        self.sources: Dict[str, Source] = {}
        self.agents: Dict[str, Agent] = {}
        self.activities: Dict[str, Activity] = {}
        self.migrations: Dict[str, MigrationRecord] = {}

    # ---------- typed add/get ----------
    def add_entity(self, e: EntityBase) -> None:
        self.entities[e.id] = e

    def add_claim(self, c: Claim) -> None:
        self.claims[c.id] = c

    def add_evidence(self, ev: EvidenceItem) -> None:
        self.evidence[ev.id] = ev

    def add_source(self, s: Source) -> None:
        self.sources[s.id] = s

    def add_agent(self, a: Agent) -> None:
        self.agents[a.id] = a

    def add_activity(self, a: Activity) -> None:
        self.activities[a.id] = a

    def add_migration(self, m: MigrationRecord) -> None:
        self.migrations[m.id] = m

    def claims_by_predicate(self, p: RelationshipType) -> List[Claim]:
        return [c for c in self.claims.values() if c.predicate == p]

    def entities_of_type(self, t: EntityType) -> List[EntityBase]:
        return [e for e in self.entities.values() if e.entity_type == t]

    # ---------- diagnostic boundary ----------
    def diagnostic_prerequisite_claims(self) -> List[Claim]:
        """Only EXECUTE/UNDERSTAND prerequisite claims may inform diagnosis.

        `precedes` is navigation-only and is never consumed here.
        """
        out = []
        for c in self.claims.values():
            if c.predicate != RelationshipType.PREREQUISITE:
                continue
            if c.origin is None or c.purpose is None:
                continue
            out.append(c)
        return out

    def vector_similarity_candidates(self, kc_ids: Set[str]) -> Set[str]:
        """Placeholder seam: similarity tools may PROPOSE candidates only.
        They never create authoritative relationships. This returns ids marked
        as candidates; authoritative edges require Claims with the normal
        status lifecycle."""
        return set(kc_ids)

    # ---------- structural helpers ----------
    def targeting_task_models(self, kc_id: str) -> Set[str]:
        return {
            c.subject_id
            for c in self.claims.values()
            if c.predicate == RelationshipType.TARGETS and c.object_id == kc_id
        }

    def method_required_kcs(self, method_id: str) -> Set[str]:
        return {
            c.object_id
            for c in self.claims.values()
            if c.predicate == RelationshipType.REQUIRES and c.subject_id == method_id
        }

    def target_kcs_of_task_model(self, tm_id: str) -> Set[str]:
        return {
            c.object_id
            for c in self.claims.values()
            if c.predicate == RelationshipType.TARGETS and c.subject_id == tm_id
        }

    # ---------- visualization projection ----------
    def export_view(self) -> dict:
        """Generic projection for future visualization. Consumes the domain
        model; is never the source of truth."""
        nodes = [
            {
                "id": e.id,
                "type": e.entity_type.value,
                "label": e.label,
                "status": e.status.value,
            }
            for e in self.entities.values()
        ]
        edges = [
            {
                "id": c.id,
                "predicate": c.predicate.value if c.predicate else None,
                "source": c.subject_id,
                "target": c.object_id,
                "status": c.status.value,
                "qualifiers": c.qualifiers,
            }
            for c in self.claims.values()
        ]
        return {"nodes": nodes, "edges": edges}
