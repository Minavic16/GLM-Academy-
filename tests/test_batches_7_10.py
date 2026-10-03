import json

from conftest import *

from examples.batch10_simultaneous_lq import build_graph_v10
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v10_graph_clean():
    s = build_graph_v10()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_v10_counts_and_coverage_progress():
    s = build_graph_v10()
    kcs = s.entities_of_type(EntityType.KNOWLEDGE_COMPONENT)
    methods = s.entities_of_type(EntityType.METHOD)
    tms = s.entities_of_type(EntityType.TASK_MODEL)
    assert len(kcs) == 14, len(kcs)
    assert len(tms) == 14, len(tms)
    assert len(methods) >= 23
    # every accepted KC has a targeting TaskModel
    for k in kcs:
        if k.status == ClaimStatus.ACCEPTED:
            assert s.targeting_task_models(k.id), k.id


def test_v10_serialization_round_trip_and_export():
    s = build_graph_v10()
    parsed = json.loads(dumps_store(s))
    view = s.export_view()
    assert len(parsed["entities"]) == len(s.entities)
    assert len(view["edges"]) == len(s.claims)
