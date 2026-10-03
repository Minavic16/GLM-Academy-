from conftest import *


def claim(c: Claim) -> None:  # helper no-op
    pass


def add_targets_and_methods(store: CDGStore):
    store.add_claim(Claim(
        id="cl.t1", predicate=RelationshipType.TARGETS, subject_id="tm.1", object_id="kc.base_numerals",
        claim_type=ClaimType.ASSESSMENT_DESIGN, status=ClaimStatus.PROPOSED,
        created_by_activity="act.extract",
    ))
    store.add_claim(Claim(
        id="cl.hm1", predicate=RelationshipType.HAS_METHOD, subject_id="tm.1", object_id="m.1",
        claim_type=ClaimType.ASSESSMENT_DESIGN, status=ClaimStatus.PROPOSED,
        created_by_activity="act.extract",
    ))
    store.add_claim(Claim(
        id="cl.req1", predicate=RelationshipType.REQUIRES, subject_id="m.1", object_id="kc.place_value",
        claim_type=ClaimType.DEPENDENCY, status=ClaimStatus.PROPOSED,
        created_by_activity="act.extract",
    ))


def test_valid_structure_has_no_method_errors():
    s = make_store()
    add_targets_and_methods(s)
    errs = validate_method_structure(s)
    assert errs == [], errs


def test_method_without_taskmodel_rejected():
    s = make_store()
    add_targets_and_methods(s)
    s.add_entity(Method(id="m.orphan", label="orphan method", task_model_id=None))
    errs = validate_method_structure(s)
    assert any("m.orphan" in e and "exactly one TaskModel" in e for e in errs)


def test_method_needs_at_least_one_requires():
    s = make_store()
    add_targets_and_methods(s)
    s.add_entity(Method(id="m.2", label="empty", task_model_id="tm.1"))
    s.add_claim(Claim(id="cl.hm2", predicate=RelationshipType.HAS_METHOD, subject_id="tm.1",
                      object_id="m.2", claim_type=ClaimType.ASSESSMENT_DESIGN, created_by_activity="act.extract"))
    errs = validate_method_structure(s)
    assert any("m.2" in e and "at least one KC" in e for e in errs)


def test_item_has_no_targets_or_requires():
    s = make_store()
    add_targets_and_methods(s)
    s.add_claim(Claim(id="cl.bad", predicate=RelationshipType.TARGETS, subject_id="it.1",
                      object_id="kc.place_value", claim_type=ClaimType.ASSESSMENT_DESIGN,
                      created_by_activity="act.extract"))
    errs = validate_method_structure(s)
    assert any("Item may not originate" in e for e in errs)


def test_taskmodel_requires_target_and_method():
    s = make_store()
    s.add_entity(TaskModel(id="tm.2", label="bare"))
    errs = validate_method_structure(s)
    assert any("tm.2" in e and "target at least one KC" in e for e in errs)
    assert any("tm.2" in e and "at least one Method" in e for e in errs)


def test_kc_cannot_leave_proposed_without_taskmodel():
    s = make_store()
    kc = s.entities["kc.place_value"]
    kc.status = ClaimStatus.UNDER_REVIEW
    errs = validate_kc_lifecycle(s)
    assert any("kc.place_value" in e for e in errs)


def test_misconception_has_related_kc():
    s = make_store()
    # a Misconception with no relatedMisconception claim is flagged by relation
    # contracts (enforced at relationship-creation time); here we check the
    # domain/range rule instead.
    c = Claim(id="cl.rm", predicate=RelationshipType.RELATED_MISCONCEPTION, subject_id="mis.1",
              object_id="kc.place_value", claim_type=ClaimType.MISCONCEPTION, created_by_activity="act.extract")
    assert validate_relationship_claim(c, s.entities) == []
