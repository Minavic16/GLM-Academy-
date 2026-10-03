from conftest import *


def base_prereq(**kw) -> Claim:
    defaults = dict(
        id="cl.pr", predicate=RelationshipType.PREREQUISITE, subject_id="kc.place_value",
        object_id="kc.base_numerals", claim_type=ClaimType.DEPENDENCY,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED, created_by_activity="act.extract",
    )
    defaults.update(kw)
    return Claim(**defaults)


def test_valid_asserted_all_scope_prerequisite():
    s = make_store()
    assert validate_relationship_claim(base_prereq(), s.entities) == []


def test_prerequisite_missing_purpose_rejected():
    s = make_store()
    c = base_prereq(purpose=None)
    errs = validate_relationship_claim(c, s.entities)
    assert any("purpose" in e for e in errs)


def test_prerequisite_missing_scope_rejected():
    s = make_store()
    c = base_prereq(scope=None)
    errs = validate_relationship_claim(c, s.entities)
    assert any("scope" in e for e in errs)


def test_prerequisite_missing_origin_rejected():
    s = make_store()
    c = base_prereq(origin=None)
    errs = validate_relationship_claim(c, s.entities)
    assert any("origin" in e for e in errs)


def test_prerequisite_self_loop_rejected():
    s = make_store()
    c = base_prereq(object_id="kc.place_value")
    errs = validate_relationship_claim(c, s.entities)
    assert any("self-loop" in e for e in errs)


def test_prerequisite_domain_range_rejected():
    s = make_store()
    c = base_prereq(subject_id="tm.1")  # TaskModel is not a KC
    errs = validate_relationship_claim(c, s.entities)
    assert any("domain must be KnowledgeComponent" in e for e in errs)


def test_specific_method_scope_requires_derived_origin():
    s = make_store()
    c = base_prereq(scope=PrerequisiteScope.SPECIFIC_METHOD, scope_ref="m.1", origin=ClaimOrigin.ASSERTED)
    errs = validate_relationship_claim(c, s.entities)
    assert any("DERIVED" in e for e in errs)


def test_specific_task_model_scope_derives():
    s = make_store()
    c = base_prereq(scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.1", origin=ClaimOrigin.DERIVED)
    assert validate_relationship_claim(c, s.entities) == []


def test_understand_must_be_asserted():
    s = make_store()
    c = base_prereq(purpose=PrerequisitePurpose.UNDERSTAND, origin=ClaimOrigin.DERIVED)
    errs = validate_relationship_claim(c, s.entities)
    assert any("UNDERSTAND prerequisite must be ASSERTED" in e for e in errs)


def test_understand_allows_only_all_or_taskmodel_scope():
    s = make_store()
    c = base_prereq(purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.SPECIFIC_METHOD,
                    scope_ref="m.1", origin=ClaimOrigin.ASSERTED)
    errs = validate_relationship_claim(c, s.entities)
    assert any("UNDERSTAND permits only" in e for e in errs)
