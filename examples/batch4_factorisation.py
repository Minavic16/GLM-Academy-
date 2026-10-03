"""Batch 004 — Factorisation of quadratic trinomials."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (
    AcceptanceBasis,
    ActivityType,
    ClaimOrigin,
    ClaimStatus,
    ClaimType,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
)
from cdg.provenance import Activity
from cdg.store import CDGStore
from examples.batch3_algebra_foundations import build_graph_v3
from examples._batchkit import accept, ev

B_REVIEW = "act.batch4.review"
B_INTERP = "act.batch4.interpret"


def build_graph_v4() -> CDGStore:
    s = build_graph_v3()
    s.add_activity(Activity(id="act.batch4.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T06:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T06:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T07:00:00Z",
                            rationale="Human review of factorisation batch."))

    tm = TaskModel(id="tm.factorise_quadratic_trinomial",
                   label="Factorise quadratic trinomials",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.factorise_unit_leading", label="Trinomial with unit leading coefficient",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    m2 = Method(id="m.factorise_by_grouping", label="Grouping for non-unit leading coefficient",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m2.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1); s.add_entity(m2)
    it = Item(id="it.mcq.factorise", label="MCQ: factorise x^2+7x+12", task_model_id=tm.id,
              stem="Factorise x^2 + 7x + 12", options=["(x+3)(x+4)", "(x+2)(x+6)", "(x-3)(x-4)", "(x+1)(x+12)"],
              key="(x+3)(x+4)", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)

    kc = s.entities["kc.factorisation_quadratic_trinomial"]
    kc.status = ClaimStatus.ACCEPTED
    kc.reviewed_by_activity = B_REVIEW
    kc.review_rationale = "Accepted via batch_004 TM + reviewed claims."

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T06:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tmF.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets factorisation of trinomials", ASSESS)
    add("cl.tmF.m1", RelationshipType.HAS_METHOD, tm.id, m1.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    add("cl.tmF.m2", RelationshipType.HAS_METHOD, tm.id, m2.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    for cid, m, kc_id in [("cl.req.unit_alg", m1, "kc.algebraic_expressions"),
                          ("cl.req.unit_int", m1, "kc.integer_arithmetic"),
                          ("cl.req.grp_alg", m2, "kc.algebraic_expressions"),
                          ("cl.req.grp_int", m2, "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre.alg_fact", RelationshipType.PREREQUISITE, "kc.algebraic_expressions", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE, all-methods derived", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre.int_fact", RelationshipType.PREREQUISITE, "kc.integer_arithmetic", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE, all-methods derived", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)

    s.add_evidence(ev("ev.b4.t", "cl.tmF.target", "SRC.NERDC.SSS1.MATH.2025", "E0119",
                      "Factorization of quadratic expressions.", True, B_INTERP))
    s.add_evidence(ev("ev.b4.m1", "cl.tmF.m1", "SRC.OSX.IA2E.6.5", "E0120",
                      "Factor completely ...; objective 'Solve quadratic equations by factoring'.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.m2", "cl.tmF.m2", "SRC.OSX.IA2E.6.5", "E0112",
                      "Factor completely: n^3 - 9n^2 - 22n.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.r1", "cl.req.unit_alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Find the product: (3y + 4)(2y + 5).", False, B_INTERP))
    s.add_evidence(ev("ev.b4.r2", "cl.req.unit_int", "SRC.OSX.IA2E.6.2", "E0098",
                      "Find all the factors of 72.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.r3", "cl.req.grp_alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Polynomial products.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.r4", "cl.req.grp_int", "SRC.OSX.IA2E.6.2", "E0098",
                      "Factors/multiples.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.p1", "cl.pre.alg_fact", "SRC.OSX.IA2E.5.4", "E0100",
                      "Requires algebraic manipulation prior to factorisation.", False, B_INTERP))
    s.add_evidence(ev("ev.b4.p2", "cl.pre.int_fact", "SRC.OSX.IA2E.6.2", "E0098",
                      "Requires integer arithmetic.", False, B_INTERP))
    return s
