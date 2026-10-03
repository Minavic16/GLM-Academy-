"""Batch 016 — Calculus: differentiation of explicit algebraic functions."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch15_statistics import build_graph_v15
from examples._batchkit import accept, ev

B_REVIEW = "act.batch16.review"
B_INTERP = "act.batch16.interpret"


def build_graph_v16() -> CDGStore:
    s = build_graph_v15()
    s.add_activity(Activity(id="act.batch16.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-04T06:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-04T06:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-04T07:00:00Z",
                            rationale="Human review of differentiation batch."))
    if "SRC.OSX.CALC1.4.10" not in s.sources:
        s.add_source(Source(id="SRC.OSX.CALC1.4.10", title="Calculus Volume 1, 4.10 The Derivative of a Function",
                            identifier_or_url="legacy:SRC.OSX.CALC1.4.10", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.differentiation_algebraic",
                            label="Differentiation of explicit algebraic functions",
                            definition="Apply differentiation rules (power rule et al.) to algebraic functions.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.CAL.DIFF_ALGEBRAIC"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.differentiate_explicit",
                   label="Differentiate an explicit algebraic function",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.power_rule", label="Apply the power rule to each term",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.diff", label="MCQ: differentiate", task_model_id=tm.id,
              stem="Differentiate f(x) = 3x^4 - 2x",
              options=["12x^3 - 2", "3x^3 - 2", "12x^4 - 2", "4x^3 - 2"], key="12x^3 - 2",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-04T06:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm16.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets algebraic differentiation", ASSESS)
    add("cl.tm16.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req16.fn", "kc.function_concept"),
                       ("cl.req16.alg", "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre16.alg_diff", RelationshipType.PREREQUISITE, "kc.algebraic_expressions", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm16 methods", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre16.fn_diff", RelationshipType.PREREQUISITE, "kc.function_concept", kc.id,
        ClaimType.DEPENDENCY, "UNDERSTAND, asserted", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    s.add_evidence(ev("ev.b16.t", "cl.tm16.target", "SRC.OSX.CALC1.4.10", "E0308",
                      "Power rule used directly: 'Knowing the power rule of differentiating...'", True, B_INTERP))
    s.add_evidence(ev("ev.b16.m1", "cl.tm16.m1", "SRC.OSX.CALC1.4.10", "E0312",
                      "Power rule applied to x^n.", True, B_INTERP))
    s.add_evidence(ev("ev.b16.r1", "cl.req16.fn", "SRC.OSX.CALC1.3.1", "E0309",
                      "Derivative defined for a function f at a point a.", True, B_INTERP))
    s.add_evidence(ev("ev.b16.r2", "cl.req16.alg", "SRC.OSX.CALC1.4.10", "E0308",
                      "Requires algebraic function terms.", True, B_INTERP))
    s.add_evidence(ev("ev.b16.p1", "cl.pre16.alg_diff", "SRC.OSX.CALC1.4.10", "E0312",
                      "Algebraic expressions are manipulated term-wise.", True, B_INTERP))
    s.add_evidence(ev("ev.b16.p2", "cl.pre16.fn_diff", "SRC.OSX.CALC1.3.1", "E0310",
                      "Derivative definition precedes derivative rules.", True, B_INTERP))
    return s
