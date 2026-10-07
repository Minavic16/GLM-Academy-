from conftest import *

from examples.wave2_batches import build_graph_v29
from cdg.validation import run_store_validation, validate_relationship_claim


def test_v29_store_clean():
    s = build_graph_v29()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_v29_method_and_or_and_ids():
    s = build_graph_v29()
    ids = [e.id for e in s.entities.values()]
    assert len(ids) == len(set(ids))
    cids = [c.id for c in s.claims.values()]
    assert len(cids) == len(set(cids))
    for c in s.claims.values():
        if c.status == ClaimStatus.ACCEPTED:
            assert "REVIEW:" in (c.review_rationale or "")
            assert c.acceptance_bases, c.id
