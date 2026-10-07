"""Batch 018 — Maxima and minima / applications of differentiation."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch17_rate_of_change import build_graph_v17
from examples._batchkit import accept, ev

B_REVIEW = "act.batch18.review"
B_INTERP = "act.batch18.interpret"


def build_graph_v18() -> CDGStore:
    s = build_graph_v17()
    s.add_activity(Activity(id="act.batch18.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T02:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T02:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T03:00:00Z",
                            rationale="Human review of maxima/minima batch."))
    if "SRC.OSX.CALC1.4.3" not in s.sources:
        s.add_source(Source(id="SRC.OSX.CALC1.4.3", title="Calculus Volume 1, 4.3 Maxima and Minima",
                            identifier_or_url="legacy:SRC.OSX.CALC1.4.3", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.maxima_minima", label="Maxima and minima of a function",
                            definition="Locate and classify local maximum/minimum points via derivatives.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.CAL.MAXIMA_MINIMA"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.find_maxima_minima", label="Find local maxima and minima",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.first_derivative", label="Differentiate, solve f'(x)=0, classify by sign change",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.extremum", label="MCQ: local maximum", task_model_id=tm.id,
              stem="Find the local maximum of f(x)=-x^2+4x", options=["f(2)=4", "f(0)=0", "f(4)=0", "f(-2)=-12"],
              key="f(2)=4", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T02:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm18.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets maxima/minima", ASSESS)
    add("cl.tm18.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req18.diff", "kc.differentiation_algebraic"),
                       ("cl.req18.roots", "kc.quadratic_roots")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre18.diff_mm", RelationshipType.PREREQUISITE, "kc.differentiation_algebraic", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm18", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre18.roots_mm", RelationshipType.PREREQUISITE, "kc.quadratic_roots", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm18", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b18.t", "cl.tm18.target", "SRC.OSX.CALC1.4.3", "E0321",
                      "If f has a local extremum at c and f is differentiable.", True, B_INTERP))
    s.add_evidence(ev("ev.b18.m1", "cl.tm18.m1", "SRC.OSX.CALC1.4.3", "E0321",
                      "First-derivative test.", True, B_INTERP))
    s.add_evidence(ev("ev.b18.r1", "cl.req18.diff", "SRC.JAMB.UTME.MATH", "E0322",
                      "Application to maxima and minima.", True, B_INTERP))
    s.add_evidence(ev("ev.b18.r2", "cl.req18.roots", "SRC.NERDC.SSS1.MATH.2025", "E0134",
                      "Solving f'(x)=0 uses quadratic roots.", True, B_INTERP))
    s.add_evidence(ev("ev.b18.p1", "cl.pre18.diff_mm", "SRC.OSX.CALC1.4.3", "E0321",
                      "Requires differentiation.", True, B_INTERP))
    s.add_evidence(ev("ev.b18.p2", "cl.pre18.roots_mm", "SRC.NERDC.SSS1.MATH.2025", "E0134",
                      "Requires Obtain roots from quadratic equations.", True, B_INTERP))
    return s
