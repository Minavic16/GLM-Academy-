from conftest import *

from examples.closure_fixes import build_graph_v35
from cdg.validation import run_store_validation, validate_relationship_claim


def test_closure_store_clean():
    s = build_graph_v35()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_log_and_ph_present_and_reviewed():
    s = build_graph_v35()
    for k in ("kc.logarithms", "kc.ph_scale"):
        assert s.entities[k].status == ClaimStatus.ACCEPTED
        assert s.targeting_task_models(k), k
    assert s.entities["kc.logarithms"].subject == "Mathematics"
    assert s.entities["kc.ph_scale"].subject == "Chemistry"


def test_ph_dependency_unblocked():
    s = build_graph_v35()
    e = [c for c in s.claims.values() if c.id == "cl.pre56.log_ph"]
    assert len(e) == 1 and e[0].origin == ClaimOrigin.DERIVED
    assert e[0].status == ClaimStatus.ACCEPTED
