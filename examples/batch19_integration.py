"""Batch 019 — Elementary algebraic integration."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch18_maxima_minima import build_graph_v18
from examples._batchkit import accept, ev

B_REVIEW = "act.batch19.review"
B_INTERP = "act.batch19.interpret"


def build_graph_v19() -> CDGStore:
    s = build_graph_v18()
    s.add_activity(Activity(id="act.batch19.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T04:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T04:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T05:00:00Z",
                            rationale="Human review of integration batch."))
    kc = KnowledgeComponent(id="kc.integration_algebraic",
                            label="Elementary integration of algebraic functions",
                            definition="Find antiderivatives of polynomials using the reverse power rule.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.CAL.INTEGRATION_ALGEBRAIC"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.integrate_polynomial",
                   label="Integrate a polynomial term-by-term",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.reverse_power_rule", label="Apply the power rule in reverse and add the constant",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.integral", label="MCQ: integral", task_model_id=tm.id,
              stem="Integrate 3x^2", options=["x^3 + C", "3x^3 + C", "x^2 + C", "6x + C"],
              key="x^3 + C", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T04:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm19.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets elementary integration", ASSESS)
    add("cl.tm19.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req19.alg", "kc.algebraic_expressions"),
                       ("cl.req19.fn", "kc.function_concept")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre19.diff_int", RelationshipType.PREREQUISITE, "kc.differentiation_algebraic", kc.id,
        ClaimType.DEPENDENCY, "UNDERSTAND, asserted", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    s.add_evidence(ev("ev.b19.t", "cl.tm19.target", "SRC.OSX.CALC1.4.10", "E0325",
                      "A function F is an antiderivative of f.", True, B_INTERP))
    s.add_evidence(ev("ev.b19.m1", "cl.tm19.m1", "SRC.OSX.CALC1.4.10", "E0326",
                      "Power rule of differentiation reversed.", True, B_INTERP))
    s.add_evidence(ev("ev.b19.r1", "cl.req19.alg", "SRC.OSX.CALC1.4.10", "E0325",
                      "Requires algebraic terms.", True, B_INTERP))
    s.add_evidence(ev("ev.b19.r2", "cl.req19.fn", "SRC.OSX.CALC1.3.1", "E0309",
                      "Requires function notation.", True, B_INTERP))
    s.add_evidence(ev("ev.b19.p1", "cl.pre19.diff_int", "SRC.OSX.CALC1.4.10", "E0325",
                      "Antiderivative definitionally linked to differentiation.", True, B_INTERP))
    return s
