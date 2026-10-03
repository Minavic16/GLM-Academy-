import json

from conftest import *

from examples.math_slice_v1 import build_slice
from cdg.methods import evaluate_task_model, derive_all_scope_execute_prerequisites
from cdg.serialization import dumps_store
from cdg.validation import (
    run_store_validation,
    validate_relationship_claim,
    validate_prerequisite_attributes,
)


def test_slice_constructs():
    s = build_slice()
    kcs = s.entities_of_type(EntityType.KNOWLEDGE_COMPONENT)
    tms = s.entities_of_type(EntityType.TASK_MODEL)
    methods = s.entities_of_type(EntityType.METHOD)
    assert len(kcs) == 8, len(kcs)
    assert len(tms) == 3, len(tms)
    assert len(methods) == 7, len(methods)
    assert len(s.entities_of_type(EntityType.ITEM)) == 2


def test_all_claims_satisfy_relationship_rules():
    s = build_slice()
    for c in s.claims.values():
        errs = validate_relationship_claim(c, s.entities)
        assert errs == [], (c.id, errs)


def test_prerequisite_semantics_validate():
    s = build_slice()
    prereqs = [c for c in s.claims.values() if c.predicate == RelationshipType.PREREQUISITE]
    assert prereqs, "slice must contain prerequisite claims"
    for c in prereqs:
        assert c.purpose is not None and c.scope is not None and c.origin is not None
        errs = validate_prerequisite_attributes(c, s.entities)
        assert errs == [], (c.id, errs)


def test_human_reviewed_acceptance_validates():
    s = build_slice()
    accepted = [c for c in s.claims.values() if c.status == ClaimStatus.ACCEPTED]
    assert accepted, "slice must contain human-accepted claims"
    for c in accepted:
        assert c.acceptance_bases, c.id
        assert "REVIEW:" in (c.review_rationale or ""), c.id


def test_method_and_or_evaluation_on_slice():
    s = build_slice()
    # TM2: roots via factorisation requires quadratic_by_factorisation, OR via formula, OR completing square
    tm2_methods = [
        {"kc.quadratic_by_factorisation"},
        {"kc.quadratic_formula"},
        {"kc.completing_the_square"},
    ]
    assert evaluate_task_model(tm2_methods, {"kc.quadratic_formula"}) is True
    assert evaluate_task_model(tm2_methods, {"kc.quadratic_by_factorisation", "kc.completing_the_square"}) is True
    assert evaluate_task_model(tm2_methods, set()) is False
    # TM1: BOTH methods require factorisation AND linear equations (AND structure)
    tm1_methods = [{"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"},
                   {"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"}]
    assert evaluate_task_model(tm1_methods, {"kc.factorisation_quadratic_trinomial"}) is False
    assert evaluate_task_model(tm1_methods, {"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"}) is True


def test_store_validates_clean():
    s = build_slice()
    errs = run_store_validation(s)
    assert errs == [], errs


def test_json_round_trip_preserves_slice():
    s = build_slice()
    blob = dumps_store(s)
    parsed = json.loads(blob)
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    # prerequisite metadata preserved
    prereq = [c for c in parsed["claims"] if c["predicate"] == "prerequisite"]
    assert prereq, "prerequisite claims must survive serialization"
    for c in prereq:
        assert c["purpose"] in ("EXECUTE", "UNDERSTAND")
        assert c["scope"] in ("ALL_RELEVANT_METHODS", "SPECIFIC_METHOD", "SPECIFIC_TASK_MODEL")
        assert c["origin"] in ("ASSERTED", "DERIVED")


def test_export_view_preserves_structure():
    s = build_slice()
    view = s.export_view()
    ids = {n["id"] for n in view["nodes"]}
    assert {"kc.quadratic_roots", "tm.find_quadratic_roots", "m.roots_via_formula"} <= ids
    edges = view["edges"]
    pred_pairs = {(e["predicate"], e["source"], e["target"]) for e in edges}
    assert ("targets", "tm.find_quadratic_roots", "kc.quadratic_roots") in pred_pairs
    assert ("requires", "m.roots_via_formula", "kc.quadratic_formula") in pred_pairs
    # Method AND/OR structure preserved structurally (requires edges not flattened)
    requires_edges = [e for e in edges if e["predicate"] == "requires"]
    assert len(requires_edges) == 11, len(requires_edges)


def test_derived_all_scope_consistency():
    """DERIVED ALL-scope EXECUTE prerequisites must equal the computed set."""
    s = build_slice()
    tm1_methods = [{"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"},
                   {"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"}]
    derived = derive_all_scope_execute_prerequisites(
        "kc.quadratic_by_factorisation",
        {"tm.solve_quadratic_by_factorisation": tm1_methods},
        {"kc.quadratic_by_factorisation": {"tm.solve_quadratic_by_factorisation"}},
    )
    assert derived == {"kc.factorisation_quadratic_trinomial", "kc.linear_equations_one_var"}
    # Asserted EXECUTE/ALL claim must not contradict the derived result
    asserted_all = {
        c.subject_id for c in s.claims.values()
        if c.predicate == RelationshipType.PREREQUISITE
        and c.purpose == PrerequisitePurpose.EXECUTE
        and c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS
        and c.origin == ClaimOrigin.ASSERTED
        and c.object_id == "kc.quadratic_by_factorisation"
    }
    assert asserted_all <= derived
