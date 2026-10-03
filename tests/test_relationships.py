from conftest import *


def test_indicates_requires_response_pattern():
    s = make_store()
    c = Claim(id="ci1", predicate=RelationshipType.INDICATES, subject_id="it.1", object_id="mis.1",
              claim_type=ClaimType.ASSESSMENT_DESIGN, qualifiers={}, created_by_activity="act.extract")
    errs = validate_relationship_claim(c, s.entities)
    assert any("response_pattern" in e for e in errs)


def test_indicates_domain_is_not_broadened():
    # `indicates` must keep its narrow contract: Item -> Misconception|KC only.
    s = make_store()
    bad = Claim(id="ci.bad", predicate=RelationshipType.INDICATES, subject_id="tm.1",
                object_id="mis.1", claim_type=ClaimType.ASSESSMENT_DESIGN,
                qualifiers={"response_pattern": "p"}, created_by_activity="act.extract")
    errs = validate_relationship_claim(bad, s.entities)
    assert any("domain must be Item" in e for e in errs)
    bad2 = Claim(id="ci.bad2", predicate=RelationshipType.INDICATES, subject_id="it.1",
                 object_id="tm.1", claim_type=ClaimType.ASSESSMENT_DESIGN,
                 qualifiers={"response_pattern": "p"}, created_by_activity="act.extract")
    errs = validate_relationship_claim(bad2, s.entities)
    assert any("range" in e for e in errs)


def test_indicates_to_kc_requires_polarity():
    s = make_store()
    c = Claim(id="ci2", predicate=RelationshipType.INDICATES, subject_id="it.1", object_id="kc.place_value",
              claim_type=ClaimType.ASSESSMENT_DESIGN, qualifiers={"response_pattern": "selects 10011"},
              created_by_activity="act.extract")
    errs = validate_relationship_claim(c, s.entities)
    assert any("polarity" in e for e in errs)


def test_indicates_to_kc_ok_with_polarity():
    s = make_store()
    c = Claim(id="ci3", predicate=RelationshipType.INDICATES, subject_id="it.1", object_id="kc.place_value",
              claim_type=ClaimType.ASSESSMENT_DESIGN,
              qualifiers={"response_pattern": "selects 11001", "polarity": "EVIDENCE_OF_MASTERY"},
              created_by_activity="act.extract")
    assert validate_relationship_claim(c, s.entities) == []


def test_maps_to_requires_different_frameworks():
    s = make_store()
    s.add_entity(CurriculumFramework(id="fw.x", label="X"))
    a = CurriculumItem(id="ci.a", framework_id="fw.jamb.maths", label="a")
    b = CurriculumItem(id="ci.b", framework_id="fw.x", label="b")
    s.add_entity(a); s.add_entity(b)
    good = Claim(id="cm1", predicate=RelationshipType.MAPS_TO, subject_id="ci.a", object_id="ci.b",
                 claim_type=ClaimType.CROSSWALK, qualifiers={"match": "EXACT"}, created_by_activity="act.extract")
    assert validate_relationship_claim(good, s.entities) == []
    bad = Claim(id="cm2", predicate=RelationshipType.MAPS_TO, subject_id="ci.a", object_id="ci.1",
                claim_type=ClaimType.CROSSWALK, qualifiers={"match": "EXACT"}, created_by_activity="act.extract")
    errs = validate_relationship_claim(bad, s.entities)
    assert any("different frameworks" in e for e in errs)


def test_broader_no_self_loop():
    s = make_store()
    c = Claim(id="cb1", predicate=RelationshipType.BROADER, subject_id="kc.place_value",
              object_id="kc.place_value", claim_type=ClaimType.DOMAIN, created_by_activity="act.extract")
    errs = validate_relationship_claim(c, s.entities)
    assert any("self-loop" in e for e in errs)


def test_ischildof_same_framework_and_single_parent():
    s = make_store()
    parent = CurriculumItem(id="ci.parent", framework_id="fw.jamb.maths", label="p")
    child = CurriculumItem(id="ci.child", framework_id="fw.jamb.maths", label="c")
    s.add_entity(parent); s.add_entity(child)
    c1 = Claim(id="cc1", predicate=RelationshipType.IS_CHILD_OF, subject_id="ci.child", object_id="ci.parent",
               claim_type=ClaimType.CURRICULUM, qualifiers={}, created_by_activity="act.extract")
    s.add_claim(c1)
    assert validate_ischildof_tree(s, None) == []
    c2 = Claim(id="cc2", predicate=RelationshipType.IS_CHILD_OF, subject_id="ci.child", object_id="ci.1",
               claim_type=ClaimType.CURRICULUM, created_by_activity="act.extract")
    s.add_claim(c2)
    errs = validate_ischildof_tree(s, None)
    assert any("more than one parent" in e for e in errs)


def test_evaluate_exported_view_has_no_learners():
    s = make_store()
    view = s.export_view()
    blob = str(view).lower()
    assert "learner" not in blob and "student" not in blob
