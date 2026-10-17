"""Phase 17 Mathematics scope expansion regression tests.

Covers batches 066-069 (sets & logic, sequences & series, matrices &
determinants, mensuration) implemented in examples.math_scope_expansion
(build_graph_v40, chains build_graph_v39).

Phase 17 changes documentation + canonical store only (5 new Mathematics KCs).
Guards:
- new entities conform to schema; IDs unique; references resolve
- claim types/statuses valid; prerequisite qualifiers present; acyclic
- evidence + provenance present; HUMAN review
- no Biology/English artifacts; `indicates` untouched (PROPOSED)
- store validation []; generators deterministic; serialization round-trip OK
- existing test suite continues to pass
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(ROOT))

from examples.math_scope_expansion import build_graph_v40  # noqa: E402
from cdg.enums import (  # noqa: E402
    ClaimOrigin, ClaimStatus, EntityType, PrerequisitePurpose,
    PrerequisiteScope, RelationshipType,
)
from cdg.validation import run_store_validation, validate_relationship_claim  # noqa: E402
from cdg.serialization import dumps_store  # noqa: E402

NEW_KCS = [
    "kc.sets_operations", "kc.logical_reasoning",
    "kc.sequences_series", "kc.matrix_algebra", "kc.mensuration",
]

NEW_TMS = [
    "tm.set_operations", "tm.logical_reasoning",
    "tm.sequences_series", "tm.matrix_algebra", "tm.mensuration",
]


def _kc_ids(s):
    return {e.id for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT}


@pytest.mark.phase17
def test_v40_store_clean():
    s = build_graph_v40()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


@pytest.mark.phase17
def test_v40_new_kcs_present_and_accepted():
    s = build_graph_v40()
    ids = _kc_ids(s)
    for kid in NEW_KCS:
        assert kid in ids, kid
        kc = s.entities[kid]
        assert kc.subject == "Mathematics", kid
        assert kc.status == ClaimStatus.ACCEPTED, kid
        assert kc.reviewed_by_activity is not None, kid
        assert kc.review_rationale, kid
        assert s.targeting_task_models(kid), kid


@pytest.mark.phase17
def test_v40_new_tms_methods_items():
    s = build_graph_v40()
    for tid in NEW_TMS:
        t = s.entities[tid]
        assert t.subject == "Mathematics", tid
        assert t.status == ClaimStatus.ACCEPTED, tid
        owned = [
            c.object_id for c in s.claims.values()
            if c.predicate == RelationshipType.HAS_METHOD and c.subject_id == tid]
        assert owned, tid
        for mid in owned:
            m = s.entities[mid]
            assert m.task_model_id == tid, mid
            assert m.status == ClaimStatus.ACCEPTED, mid
            reqs = {
                c.object_id for c in s.claims.values()
                if c.predicate == RelationshipType.REQUIRES and c.subject_id == mid}
            assert reqs, mid  # every Method requires >=1 KC


@pytest.mark.phase17
def test_v40_new_items():
    s = build_graph_v40()
    expected_items = ["it.math.sets_basic", "it.math.logic_truth", "it.math.ap_gp",
                      "it.math.matrix", "it.math.mensuration"]
    for iid in expected_items:
        it = s.entities[iid]
        assert it.subject == "Mathematics", iid
        assert it.status == ClaimStatus.ACCEPTED, iid
        assert it.task_model_id in NEW_TMS, iid
        assert it.options and it.key in it.options, iid


@pytest.mark.phase17
def test_v40_prerequisite_qualifiers_and_acyclic():
    s = build_graph_v40()
    prereqs = [c for c in s.claims.values() if c.predicate == RelationshipType.PREREQUISITE]
    # every new-family prerequisite carries purpose/scope/origin
    new_pre = [c for c in prereqs
               if c.subject_id in NEW_KCS or c.object_id in NEW_KCS]
    for c in new_pre:
        assert c.purpose is not None, c.id
        assert c.scope is not None, c.id
        assert c.origin is not None, c.id
        if c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
            assert c.scope in (PrerequisiteScope.ALL_RELEVANT_METHODS,
                               PrerequisiteScope.SPECIFIC_TASK_MODEL), c.id
    # acyclicity over new-family prerequisite edges
    edges = [(c.subject_id, c.object_id) for c in prereqs]
    from cdg.validation import validate_acyclicity  # noqa: E402
    assert validate_acyclicity(edges), "prerequisite graph must be acyclic"


@pytest.mark.phase17
def test_v40_no_bio_english_and_indicates_untouched():
    s = build_graph_v40()
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []
    inds = [c for c in s.claims.values() if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED


@pytest.mark.phase17
def test_v40_matrices_secondary_evidence_disclosed():
    """Matrices uses secondary Syllabus NG evidence; rationale discloses it."""
    s = build_graph_v40()
    kc = s.entities["kc.matrix_algebra"]
    assert "secondary" in kc.review_rationale.lower()
    assert "not present" in kc.review_rationale.lower()
    # matrix_algebra source must be a secondary (Syllabus NG) source
    src_ids = {e.source_id for e in s.evidence.values()
               if e.claim_id == "cl.m68.targets.tm.matrix_algebra"}
    assert any("SYLLABUSNG" in sid for sid in src_ids)


@pytest.mark.phase17
def test_v40_counts_before_after():
    s = build_graph_v40()
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
                and e.subject == "Mathematics"]
    assert len(math_kcs) == 44  # 39 baseline + 5 new
    # Physics/Chemistry untouched
    assert sum(1 for e in s.entities.values()
               if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
               and e.subject == "Physics") == 25
    assert sum(1 for e in s.entities.values()
               if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
               and e.subject == "Chemistry") == 21


@pytest.mark.phase17
def test_v40_serialization_and_export():
    s = build_graph_v40()
    parsed = __import__("json").loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
    # every claim's endpoints resolve to existing entities
    for c in s.claims.values():
        assert c.subject_id in s.entities, c.id
        if c.object_id:
            assert c.object_id in s.entities, c.id


@pytest.mark.phase17
def test_v40_deterministic_generators():
    """Regenerating docs/visuals is byte-identical (checked externally); here
    confirm the store builder itself is deterministic across calls."""
    a = dumps_store(build_graph_v40())
    b = dumps_store(build_graph_v40())
    assert a == b
