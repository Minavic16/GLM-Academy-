"""Batch 017 — Rate of change / applications of differentiation."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch16_calculus import build_graph_v16
from examples._batchkit import accept, ev

B_REVIEW = "act.batch17.review"
B_INTERP = "act.batch17.interpret"


def build_graph_v17() -> CDGStore:
    s = build_graph_v16()
    s.add_activity(Activity(id="act.batch17.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T00:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T00:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T01:00:00Z",
                            rationale="Human review of rate-of-change batch."))
    for sid, title in [("SRC.OSX.CALC1.3.4", "Calculus Volume 1, 3.4 Derivative as a Function")]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                                publisher="OpenStax", source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.rate_of_change", label="Rate of change of a function",
                            definition="Instantaneous rate of change as the derivative of a function.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.CAL.RATE_OF_CHANGE"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.compute_rate_of_change",
                   label="Compute the rate of change of a function at a point",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.derivative_at_point", label="Differentiate then evaluate",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.rate", label="MCQ: rate of change", task_model_id=tm.id,
              stem="Find dx/dt of s(t)=t^2+3t at t=2", options=["7", "4", "10", "3"], key="7",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T00:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm17.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets rate of change", ASSESS)
    add("cl.tm17.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.req17.diff", RelationshipType.REQUIRES, m1.id, "kc.differentiation_algebraic",
        ClaimType.DEPENDENCY, "rate_of_change requires differentiation", DEP)
    add("cl.req17.int", RelationshipType.REQUIRES, m1.id, "kc.integer_arithmetic",
        ClaimType.DEPENDENCY, "requires evaluating derivatives", DEP)
    add("cl.pre17.diff_roc", RelationshipType.PREREQUISITE, "kc.differentiation_algebraic", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE, all methods of tm17", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b17.t", "cl.tm17.target", "SRC.OSX.CALC1.3.4", "E0318",
                      "The instantaneous rate of change of f(x) at a is its derivative.", True, B_INTERP))
    s.add_evidence(ev("ev.b17.m1", "cl.tm17.m1", "SRC.OSX.CALC1.3.4", "E0319",
                      "Derivative at a point.", True, B_INTERP))
    s.add_evidence(ev("ev.b17.r1", "cl.req17.diff", "SRC.OSX.CALC1.3.4", "E0318",
                      "Differentiate first.", True, B_INTERP))
    s.add_evidence(ev("ev.b17.r2", "cl.req17.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires evaluating numeric expressions.", False, B_INTERP))
    s.add_evidence(ev("ev.b17.p1", "cl.pre17.diff_roc", "SRC.OSX.CALC1.3.4", "E0318",
                      "Rate of change requires differentiation skill.", True, B_INTERP))
    return s
