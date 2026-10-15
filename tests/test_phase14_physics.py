import json

from conftest import *

from examples.physics_completion_b import build_graph_v38
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v38_store_clean():
    s = build_graph_v38()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_phase14_physics_kcs_reviewed():
    s = build_graph_v38()
    for k in ("kc.friction", "kc.em_spectrum", "kc.energy_sources",
              "kc.fibre_optics", "kc.laser_basics", "kc.semiconductor_electronics"):
        assert s.entities[k].subject == "Physics", k
        assert s.entities[k].status == ClaimStatus.ACCEPTED, k
        assert s.targeting_task_models(k), k


def test_phase14_baselines_intact():
    s = build_graph_v38()
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Mathematics"]
    chem_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Chemistry"]
    assert len(math_kcs) == 39
    assert len(chem_kcs) == 12
    assert s.claims["cl.pre56.log_ph"].status == ClaimStatus.ACCEPTED
    assert s.entities["kc.median_ungrouped"].legacy_ids == ["MATH.STAT.MEDIAN"]


def test_phase14_understand_edges_asserted():
    s = build_graph_v38()
    for c in s.claims.values():
        if c.predicate == RelationshipType.PREREQUISITE and c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
            assert c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS, c.id


def test_no_bio_and_indicates_proposed():
    s = build_graph_v38()
    assert [e.id for e in s.entities.values() if (e.subject or "") == "Biology"] == []
    inds = [c for c in s.claims.values() if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED


def test_round_trip_and_export():
    s = build_graph_v38()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(s.export_view()["edges"]) == len(s.claims)
