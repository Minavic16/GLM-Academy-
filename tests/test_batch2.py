import json

from conftest import *

from examples.batch2_linear_equations import build_graph
from cdg.methods import evaluate_task_model
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def test_batch2_constructs_and_extends_slice():
    s = build_graph()
    tm_ids = {t.id for t in s.entities_of_type(EntityType.TASK_MODEL)}
    assert "tm.solve_linear_equations_one_var" in tm_ids
    assert len(s.entities_of_type(EntityType.METHOD)) == 9  # 7 + 2


def test_batch2_claims_satisfy_relationship_rules():
    s = build_graph()
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_linear_kc_graduated_via_owning_taskmodel():
    s = build_graph()
    kc = s.entities["kc.linear_equations_one_var"]
    assert kc.status == ClaimStatus.ACCEPTED
    assert s.targeting_task_models(kc.id), "KC must have a targeting TM"


def test_batch2_prerequisite_semantics():
    s = build_graph()
    prereqs = [c for c in s.claims.values()
               if c.predicate == RelationshipType.PREREQUISITE
               and c.object_id == "kc.linear_equations_one_var"]
    assert len(prereqs) == 2
    for c in prereqs:
        assert c.purpose == PrerequisitePurpose.EXECUTE
        assert c.scope == PrerequisiteScope.SPECIFIC_TASK_MODEL
        assert c.origin == ClaimOrigin.DERIVED
        assert c.scope_ref == "tm.solve_linear_equations_one_var"


def test_batch2_and_or_evaluation():
    # Both methods require algebraic expressions AND integer arithmetic:
    # each TM route needs BOTH (AND); either method is sufficient (OR).
    methods = [
        {"kc.algebraic_expressions", "kc.integer_arithmetic"},
        {"kc.algebraic_expressions", "kc.integer_arithmetic"},
    ]
    assert evaluate_task_model(methods, {"kc.algebraic_expressions"}) is False
    assert evaluate_task_model(methods, {"kc.algebraic_expressions", "kc.integer_arithmetic"}) is True


def test_batch2_store_validates():
    assert run_store_validation(build_graph()) == []


def test_batch2_serialization_round_trip():
    s = build_graph()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    assert len(parsed["evidence"]) == len(s.evidence)


def test_batch2_export_view():
    view = build_graph().export_view()
    pairs = {(e["predicate"], e["source"], e["target"]) for e in view["edges"]}
    assert ("targets", "tm.solve_linear_equations_one_var", "kc.linear_equations_one_var") in pairs
    assert ("requires", "m.isolate_variable", "kc.algebraic_expressions") in pairs
