import json

from conftest import *

from examples.math_stats_closure import build_graph_v36
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v36_store_clean():
    s = build_graph_v36()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_median_and_dispersion_kcs_reviewed():
    s = build_graph_v36()
    for k in ("kc.median_ungrouped", "kc.measures_of_dispersion"):
        assert s.entities[k].subject == "Mathematics"
        assert s.entities[k].status == ClaimStatus.ACCEPTED
        assert s.targeting_task_models(k), k


def test_dispersion_methods_require_means_and_indices():
    s = build_graph_v36()
    assert s.method_required_kcs("m.variance_sd") >= {
        "kc.mean_ungrouped_data", "kc.equations_in_indices"}
    assert s.method_required_kcs("m.range") >= {"kc.fraction_decimal_operations"}


def test_physics_chemistry_log_ph_intact():
    s = build_graph_v36()
    phys = [e for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Physics"]
    chem = [e for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Chemistry"]
    assert len(phys) == 19
    assert len(chem) == 12
    edge = [c for c in s.claims.values() if c.id == "cl.pre56.log_ph"]
    assert edge and edge[0].status == ClaimStatus.ACCEPTED


def test_no_bio_english_and_proposal_pairs_unchanged():
    s = build_graph_v36()
    assert [e.id for e in s.entities.values()
            if (e.subject or "") in ("Biology", "English")] == []
    inds = [c for c in s.claims.values() if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED


def test_round_trip_and_export():
    s = build_graph_v36()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(s.export_view()["edges"]) == len(s.claims)
