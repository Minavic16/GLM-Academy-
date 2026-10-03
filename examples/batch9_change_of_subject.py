"""Batch 009 — Change of subject of a formula."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch8_indices_equations import build_graph_v8
from examples._batchkit import accept, ev

B_REVIEW = "act.batch9.review"
B_INTERP = "act.batch9.interpret"


def build_graph_v9() -> CDGStore:
    s = build_graph_v8()
    s.add_activity(Activity(id="act.batch9.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T16:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T16:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T17:00:00Z",
                            rationale="Human review of change-of-subject batch."))
    if "SRC.OSX.IA2E.3.3" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.3.3", title="Intermediate Algebra 2e, 3.3 Solving Equations",
                            identifier_or_url="legacy:SRC.OSX.IA2E.3.3", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.change_of_subject",
                            label="Change of subject of a formula/relation",
                            definition="Rearrange a formula so a specified variable is isolated.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.ALG.CHANGE_OF_SUBJECT"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.make_subject", label="Make a specified variable the subject",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.inverse_operations", label="Apply inverse operations until isolated",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    m2 = Method(id="m.collect_factor_subject", label="Collect like terms and factor the subject variable",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m2.reviewed_by_activity = B_REVIEW
    for e in (tm, m1, m2): s.add_entity(e)
    it = Item(id="it.mcq.subject", label="MCQ: change of subject",
              task_model_id=tm.id, stem="Make x the subject of y = 2x + 3",
              options=["x = (y - 3)/2", "x = (y + 3)/2", "x = 2y - 3", "x = y/2 - 3"],
              key="x = (y - 3)/2", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T16:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm9.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets change of subject", ASSESS)
    add("cl.tm9.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm9.m2", RelationshipType.HAS_METHOD, tm.id, m2.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, m, kc_id in [("cl.req9.inv_lin", m1, "kc.linear_equations_one_var"),
                          ("cl.req9.inv_alg", m1, "kc.algebraic_expressions"),
                          ("cl.req9.fact_alg", m2, "kc.algebraic_expressions"),
                          ("cl.req9.fact_int", m2, "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre9.lin_subject", RelationshipType.PREREQUISITE, "kc.linear_equations_one_var", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via every method of tm9", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b9.t", "cl.tm9.target", "SRC.WAEC.WASSCE.MATH.SYL", "E0084",
                      "Linear equations listed before 'Change of subject of a formula/relation'.", True, B_INTERP))
    s.add_evidence(ev("ev.b9.m1", "cl.tm9.m1", "SRC.OSX.IA2E.3.3", "E0083",
                      "Solve for y: y - 3 = -2(x + 1).", False, B_INTERP))
    s.add_evidence(ev("ev.b9.m2", "cl.tm9.m2", "SRC.OSX.IA2E.5.4", "E0089",
                      "Collect like terms.", False, B_INTERP))
    s.add_evidence(ev("ev.b9.r1", "cl.req9.inv_lin", "SRC.OSX.IA2E.3.3", "E0083",
                      "Rearrangement mirrors equation solving.", False, B_INTERP))
    s.add_evidence(ev("ev.b9.r2", "cl.req9.inv_alg", "SRC.OSX.IA2E.5.4", "E0089",
                      "Requires algebraic manipulation.", False, B_INTERP))
    s.add_evidence(ev("ev.b9.r3", "cl.req9.fact_alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Requires expanding/factoring.", False, B_INTERP))
    s.add_evidence(ev("ev.b9.r4", "cl.req9.fact_int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires signed-number handling.", False, B_INTERP))
    s.add_evidence(ev("ev.b9.p1", "cl.pre9.lin_subject", "SRC.WAEC.WASSCE.MATH.SYL", "E0084",
                      "Linear equations precede change of subject.", True, B_INTERP))
    return s
