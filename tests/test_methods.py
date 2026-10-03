from conftest import *
from cdg.methods import evaluate_task_model, method_is_satisfied, derive_all_scope_execute_prerequisites


def test_and_within_method_or_across_methods():
    # TaskModel T: Method A requires KC1,KC2,KC3 OR Method B requires KC4,KC5
    methods = [{"KC1", "KC2", "KC3"}, {"KC4", "KC5"}]
    assert evaluate_task_model(methods, {"KC1", "KC2", "KC3"}) is True
    assert evaluate_task_model(methods, {"KC4", "KC5"}) is True
    assert evaluate_task_model(methods, {"KC1", "KC2", "KC4"}) is False  # no single method satisfied
    assert evaluate_task_model(methods, set()) is False


def test_method_is_satisfied_requires_all():
    assert method_is_satisfied({"KC1", "KC2"}, {"KC1", "KC2", "KC3"}) is True
    assert method_is_satisfied({"KC1", "KC4"}, {"KC1", "KC2"}) is False


def test_no_methods_is_unsatisfiable():
    assert evaluate_task_model([], {"KC1"}) is False


def test_all_scope_derivation_intersects_every_method():
    # One TaskModel targeting B with two methods; only KC_common is in both.
    methods = {"tm.x": [["A", "B_shared", "C"], ["B_shared", "D"]]}
    targets = {"B": {"tm.x"}}
    derived = derive_all_scope_execute_prerequisites("B", methods, targets)
    assert derived == {"B_shared"}


def test_all_scope_derivation_skips_self():
    methods = {"tm.x": [["A", "B"]]}
    targets = {"B": {"tm.x"}}
    derived = derive_all_scope_execute_prerequisites("B", methods, targets)
    assert "B" not in derived
    assert derived == {"A"}


def test_all_scope_derivation_requires_methods():
    methods = {}
    targets = {"B": {"tm.x"}}
    assert derive_all_scope_execute_prerequisites("B", methods, targets) == set()
