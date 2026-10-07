from conftest import *

from examples.batch23_circles import build_graph_v23
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v23_clean():
    s = build_graph_v23()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == []


def test_v23_domain_sequencing():
    s = build_graph_v23()
    ids = {e.id for e in s.entities.values() if e.entity_type == EntityType.KNOWLEDGE_COMPONENT}
    for k in ["kc.rate_of_change", "kc.maxima_minima", "kc.integration_algebraic",
              "kc.theoretical_probability", "kc.sine_rule", "kc.cosine_rule",
              "kc.equation_of_line", "kc.circle_angle_theorems"]:
        assert k in ids
