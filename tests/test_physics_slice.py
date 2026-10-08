import json
from conftest import *

from examples.physics_slice import build_graph_v30
from cdg.validation import run_store_validation, validate_relationship_claim
from cdg.serialization import dumps_store


def test_physics_kcs_have_subject_and_status():
    s = build_graph_v30()
    kcs = [e for e in s.entities.values() if e.entity_type == EntityType.KNOWLEDGE_COMPONENT]
    phys = [k for k in kcs if k.subject == "Physics"]
    assert len(phys) == 8
    accepted = [k for k in phys if k.status == ClaimStatus.ACCEPTED]
    for k in accepted:
        assert s.targeting_task_models(k.id), k.id


def test_math_to_physics_cross_edges():
    s = build_graph_v30()
    xs = [c for c in s.claims.values()
          if c.predicate == RelationshipType.PREREQUISITE
          and c.subject_id in {e.id for e in s.entities.values() if e.subject == "Mathematics"}
          and c.object_id in {e.id for e in s.entities.values() if e.subject == "Physics"}]
    assert len(xs) == 4
    for c in xs:
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_store_clean_with_physics():
    assert run_store_validation(build_graph_v30()) == []


def test_physics_evidence_resolves():
    s = build_graph_v30()
    for e in s.evidence.values():
        assert e.source_id in s.sources, e.id
        assert e.claim_id in s.claims, e.id


def test_backward_compat_math_counts():
    s = build_graph_v30()
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Mathematics"]
    assert len(math_kcs) == 36


def test_no_chemistry_biology_english_entities():
    s = build_graph_v30()
    subs = {e.subject for e in s.entities.values() if e.subject}
    assert subs <= {"Mathematics", "Physics"}, subs


def test_physics_review_lifecycle():
    s = build_graph_v30()
    for c in s.claims.values():
        if c.subject_id.startswith("cl.p.") or c.id.startswith("cl.p.") or c.id.startswith("cl.xs."):
            assert "REVIEW:" in (c.review_rationale or ""), c.id
            assert c.acceptance_bases, c.id
