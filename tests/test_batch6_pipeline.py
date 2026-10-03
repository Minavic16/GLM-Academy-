from conftest import *

from examples.batch5_quadratic_tools import build_graph_v5
from examples.batch6_functions import build_graph_v6
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v6_store_validates_clean():
    assert run_store_validation(build_graph_v6()) == []


def test_v6_all_claim_predicates_valid():
    s = build_graph_v6()
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_v6_all_kcs_either_accepted_or_explicitly_proposed():
    s = build_graph_v6()
    kcs = s.entities_of_type(EntityType.KNOWLEDGE_COMPONENT)
    assert kcs
    for k in kcs:
        assert k.status in (ClaimStatus.ACCEPTED, ClaimStatus.PROPOSED)


def test_v6_no_agent_only_acceptance():
    s = build_graph_v6()
    for c in s.claims.values():
        if c.status == ClaimStatus.ACCEPTED:
            assert "REVIEW:" in (c.review_rationale or ""), c.id


def test_v6_serialization_not_lossy():
    s = build_graph_v6()
    import json
    p = json.loads(dumps_store(s))
    assert len(p["claims"]) == len(s.claims)
    assert len(p["entities"]) == len(s.entities)


def test_v6_export_view_deterministic_counts():
    v = build_graph_v6().export_view()
    assert len(v["edges"]) == len(build_graph_v6().claims)
