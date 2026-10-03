from conftest import *


def accepted_claim_kwargs():
    return dict(
        claim_type=ClaimType.DEPENDENCY,
        created_by_activity="act.review",
    )


def test_proposed_to_under_review_ok():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              claim_type=ClaimType.DEPENDENCY, created_by_activity="act.extract")
    errs = validate_status_transition(c, ClaimStatus.UNDER_REVIEW, {EvidenceRole.DIRECT}, review_is_human=True)
    assert errs == []


def test_illegal_transition_rejected():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              claim_type=ClaimType.DEPENDENCY, created_by_activity="act.extract")
    errs = validate_status_transition(c, ClaimStatus.ACCEPTED, {EvidenceRole.DIRECT}, review_is_human=True)
    assert any("illegal transition" in e for e in errs)


def test_accepted_requires_admissible_basis():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              status=ClaimStatus.UNDER_REVIEW, claim_type=ClaimType.DEPENDENCY,
              acceptance_bases={AcceptanceBasis.CURRICULUM},  # not admissible for DEPENDENCY
              created_by_activity="act.extract")
    errs = validate_status_transition(c, ClaimStatus.ACCEPTED, {EvidenceRole.DIRECT}, review_is_human=True)
    assert any("admissible acceptance basis" in e for e in errs)


def test_accepted_requires_human_review():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              status=ClaimStatus.UNDER_REVIEW, claim_type=ClaimType.DEPENDENCY,
              acceptance_bases={AcceptanceBasis.EXPERT}, created_by_activity="act.extract")
    errs = validate_status_transition(c, ClaimStatus.ACCEPTED, {EvidenceRole.DIRECT}, review_is_human=False)
    assert any("HUMAN review" in e for e in errs)


def test_accepted_rejected_with_only_agent_inference():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              status=ClaimStatus.UNDER_REVIEW, claim_type=ClaimType.DEPENDENCY,
              acceptance_bases={AcceptanceBasis.EXPERT}, created_by_activity="act.extract")
    errs = validate_status_transition(c, ClaimStatus.ACCEPTED, {EvidenceRole.AGENT_INFERENCE}, review_is_human=True)
    assert any("AGENT_INFERENCE" in e for e in errs)


def test_agent_proposal_must_be_proposed():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              status=ClaimStatus.UNDER_REVIEW, claim_type=ClaimType.DEPENDENCY,
              created_by_activity="act.extract")
    errs = validate_agent_proposal(AgentKind.AI_AGENT, c)
    assert any("PROPOSED" in e for e in errs)


def test_agent_proposal_ok_when_proposed():
    c = Claim(id="c1", predicate=None, subject_id="x", object_id=None,
              status=ClaimStatus.PROPOSED, claim_type=ClaimType.DEPENDENCY,
              created_by_activity="act.extract")
    assert validate_agent_proposal(AgentKind.AI_AGENT, c) == []


def test_precedes_never_diagnostic():
    s = make_store()
    s.add_claim(Claim(id="cp", predicate=RelationshipType.PRECEDES, subject_id="kc.place_value",
                      object_id="kc.base_numerals", claim_type=ClaimType.NAVIGATION,
                      origin=ClaimOrigin.ASSERTED, purpose=PrerequisitePurpose.EXECUTE,
                      created_by_activity="act.extract"))
    s.add_claim(Claim(id="cpr", predicate=RelationshipType.PREREQUISITE, subject_id="kc.place_value",
                      object_id="kc.base_numerals", claim_type=ClaimType.DEPENDENCY,
                      purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
                      origin=ClaimOrigin.ASSERTED, created_by_activity="act.extract"))
    diag = {c.id for c in s.diagnostic_prerequisite_claims()}
    assert diag == {"cpr"}  # precedes excluded even if it carries purpose/origin fields
