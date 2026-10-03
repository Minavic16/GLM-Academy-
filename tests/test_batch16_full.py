from conftest import *

from examples.batch16_calculus import build_graph_v16
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation


def test_v16_validate_clean_and_counts():
    s = build_graph_v16()
    assert run_store_validation(s) == []
    kcs = s.entities_of_type(EntityType.KNOWLEDGE_COMPONENT)
    tms = s.entities_of_type(EntityType.TASK_MODEL)
    methods = s.entities_of_type(EntityType.METHOD)
    assert len(kcs) == 22
    assert len(tms) == 22
    assert len(methods) == 35
    for k in kcs:
        assert s.targeting_task_models(k.id), k.id


def test_v16_domain_coverage_represented():
    s = build_graph_v16()
    ids = {e.id for e in s.entities.values() if e.entity_type == EntityType.KNOWLEDGE_COMPONENT}
    for expected in ["kc.mean_ungrouped_data", "kc.gradient", "kc.trig_ratios_acute",
                     "kc.differentiation_algebraic", "kc.percentage_concept",
                     "kc.triangle_angle_properties", "kc.function_concept"]:
        assert expected in ids


def test_v16_round_trip_and_view():
    import json
    s = build_graph_v16()
    p = json.loads(dumps_store(s))
    v = s.export_view()
    assert len(p["entities"]) == len(s.entities)
    assert len(v["edges"]) == len(s.claims)
