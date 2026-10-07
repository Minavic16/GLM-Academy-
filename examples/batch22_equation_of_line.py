"""Batch 022 — Equation of a straight line."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch21_trig_rules import build_graph_v21
from examples._batchkit import accept, ev

B_REVIEW = "act.batch22.review"
B_INTERP = "act.batch22.interpret"


def build_graph_v22() -> CDGStore:
    s = build_graph_v21()
    s.add_activity(Activity(id="act.batch22.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T10:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T10:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T11:00:00Z",
                            rationale="Human review of straight-line-equation batch."))
    kc = KnowledgeComponent(id="kc.equation_of_line",
                            label="Equation of a straight line (all forms)",
                            definition="Find/interpret straight-line equations, e.g. y=mx+c, point-gradient form.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.COORD.EQUATION_OF_LINE"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.find_line_equation", label="Find the equation of a straight line",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.point_gradient", label="Use y - y1 = m(x - x1) then rearrange",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.line_eq", label="MCQ: line equation", task_model_id=tm.id,
              stem="Line with gradient 2 through (1,3): equation?",
              options=["y = 2x + 1", "y = 2x + 3", "y = x + 2", "y = 3x + 2"],
              key="y = 2x + 1", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T10:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm22.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets equation of a line", ASSESS)
    add("cl.tm22.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req22.grad", "kc.gradient"),
                       ("cl.req22.subject", "kc.change_of_subject"),
                       ("cl.req22.alg", "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre22.grad_eq", RelationshipType.PREREQUISITE, "kc.gradient", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm22", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre22.subject_eq", RelationshipType.PREREQUISITE, "kc.change_of_subject", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm22", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b22.t", "cl.tm22.target", "SRC.OSX.IA2E.3.3", "E0254",
                      "Find an equation of the line given the slope and a point.", False, B_INTERP))
    s.add_evidence(ev("ev.b22.m1", "cl.tm22.m1", "SRC.OSX.IA2E.3.3", "E0254",
                      "Point-gradient form.", False, B_INTERP))
    s.add_evidence(ev("ev.b22.r1", "cl.req22.grad", "SRC.WAEC.WASSCE.MATH.SYL", "E0247",
                      "Requires the gradient.", True, B_INTERP))
    s.add_evidence(ev("ev.b22.r2", "cl.req22.subject", "SRC.WAEC.WASSCE.MATH.SYL", "E0084",
                      "Requires rearranging the equation.", True, B_INTERP))
    s.add_evidence(ev("ev.b22.r3", "cl.req22.alg", "SRC.OSX.IA2E.5.4", "E0089",
                      "Requires algebraic simplification.", False, B_INTERP))
    s.add_evidence(ev("ev.b22.p1", "cl.pre22.grad_eq", "SRC.WAEC.WASSCE.MATH.SYL", "E0254",
                      "Needs gradient as a prerequisite.", False, B_INTERP))
    s.add_evidence(ev("ev.b22.p2", "cl.pre22.subject_eq", "SRC.WAEC.WASSCE.MATH.SYL", "E0255",
                      "Needs change of subject.", True, B_INTERP))
    return s
