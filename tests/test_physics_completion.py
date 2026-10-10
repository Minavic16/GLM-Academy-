import json

from conftest import *

from examples.physics_wave3 import build_graph_v32
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim, validate_acyclicity


def test_v32_store_clean_and_all_claims_valid():
    s = build_graph_v32()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_physics_subject_identity_complete():
    s = build_graph_v32()
    for e in s.entities.values():
        if e.id.startswith(("kc.", "tm.", "m.", "it.physics")) and e.entity_type in (
                EntityType.KNOWLEDGE_COMPONENT, EntityType.TASK_MODEL,
                EntityType.METHOD, EntityType.ITEM) and "physics" in (
                e.id + e.label).lower().replace(" ", "") or e.id in (
                "kc.scalar_vector_quantities", "kc.work_energy_power",
                "kc.linear_momentum", "kc.gravitation", "kc.pressure_fluids",
                "kc.heat_temperature", "kc.wave_phenomena", "kc.geometrical_optics",
                "kc.electric_circuits", "kc.electromagnetism", "kc.atomic_nuclear_physics"):
            assert e.subject == "Physics", e.id


def test_no_chem_bio_english_entities():
    s = build_graph_v32()
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Chemistry", "Biology", "English")]
    assert bad == []


def test_math_baseline_unchanged():
    s = build_graph_v32()
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
                and e.subject == "Mathematics"]
    assert len(math_kcs) == 36


def test_coverage_matrix_rows_resolve():
    s = build_graph_v32()
    required_kcs = ["kc.scalar_vector_quantities", "kc.work_energy_power",
                    "kc.linear_momentum", "kc.gravitation", "kc.pressure_fluids",
                    "kc.heat_temperature", "kc.wave_phenomena", "kc.geometrical_optics",
                    "kc.electric_circuits", "kc.electromagnetism",
                    "kc.atomic_nuclear_physics", "kc.practical_measurement",
                    "kc.measurement_errors_precision"]
    for k in required_kcs:
        assert k in s.entities, k
        assert s.entities[k].status == ClaimStatus.ACCEPTED
        assert s.targeting_task_models(k), k


def test_no_covered_without_evidence():
    s = build_graph_v32()
    ev_by_claim = {}
    for e in s.evidence.values():
        ev_by_claim.setdefault(e.claim_id, []).append(e)
        assert e.source_id in s.sources, e.id
    for c in s.claims.values():
        if c.status == ClaimStatus.ACCEPTED and c.predicate in (
                RelationshipType.TARGETS, RelationshipType.REQUIRES,
                RelationshipType.PREREQUISITE):
            assert c.id in ev_by_claim or "REVIEW:" in (c.review_rationale or ""), c.id


def test_proposed_not_counted_as_coverage():
    s = build_graph_v32()
    proposed = [c for c in s.claims.values() if c.status == ClaimStatus.PROPOSED]
    assert proposed, "the 2 PROPOSED claims must still exist"
    for c in proposed:
        assert c.id in ("cl.mis.factsign", "cl.it.indicates"), c.id


def test_no_all_scope_execute_cycles():
    s = build_graph_v32()
    edges = [(c.subject_id, c.object_id) for c in s.claims.values()
             if c.predicate == RelationshipType.PREREQUISITE
             and c.purpose == PrerequisitePurpose.EXECUTE
             and c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS]
    assert validate_acyclicity(edges)


def test_cross_subject_edges_bounded_and_derived():
    s = build_graph_v32()
    xs = [c for c in s.claims.values()
          if c.predicate == RelationshipType.PREREQUISITE
          and s.entities[c.subject_id].subject == "Mathematics"
          and s.entities[c.object_id].subject == "Physics"]
    assert 4 <= len(xs) <= 30, len(xs)
    for c in xs:
        if c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
        else:
            assert c.origin == ClaimOrigin.DERIVED, c.id
        assert c.status == ClaimStatus.ACCEPTED


def test_serialization_round_trip_and_export():
    s = build_graph_v32()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
    assert len(view["nodes"]) == len(s.entities)
