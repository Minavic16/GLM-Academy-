"""Batch 013 — Coordinate geometry: gradient of a line segment."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch12_geometry import build_graph_v12
from examples._batchkit import accept, ev

B_REVIEW = "act.batch13.review"
B_INTERP = "act.batch13.interpret"


def build_graph_v13() -> CDGStore:
    s = build_graph_v12()
    s.add_activity(Activity(id="act.batch13.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-04T00:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-04T00:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-04T01:00:00Z",
                            rationale="Human review of coordinate-geometry batch."))
    if "SRC.OSX.IA2E.11.1" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.11.1", title="Intermediate Algebra 2e, 11.1 The Distance and Midpoint Formulas",
                            identifier_or_url="legacy:SRC.OSX.IA2E.11.1", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.gradient",
                            label="Gradient of a line segment",
                            definition="Compute the gradient m between two points; interpret slope.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.COORD.GRADIENT"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.compute_gradient", label="Compute the gradient of a line segment",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.gradient_from_two_points", label="Apply m=(y2-y1)/(x2-x1)",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    for e in (tm, m1): s.add_entity(e)
    it = Item(id="it.mcq.gradient", label="MCQ: gradient", task_model_id=tm.id,
              stem="Find the gradient of the line through (2,3) and (6,11)",
              options=["2", "8", "4", "1/2"], key="2",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-04T00:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm13.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets gradient", ASSESS)
    add("cl.tm13.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req13.alg", "kc.algebraic_expressions"),
                       ("cl.req13.int", "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre13.alg_grad", RelationshipType.PREREQUISITE, "kc.algebraic_expressions", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE, all methods of tm13", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b13.t", "cl.tm13.target", "SRC.WAEC.WASSCE.MATH.SYL", "E0247",
                      "The gradient, m, of the line joining the points (x1, y1) and (x2, y2).", True, B_INTERP))
    s.add_evidence(ev("ev.b13.m1", "cl.tm13.m1", "SRC.WAEC.WASSCE.MATH.SYL", "E0247",
                      "Gradient formula between two points.", True, B_INTERP))
    s.add_evidence(ev("ev.b13.r1", "cl.req13.alg", "SRC.OSX.IA2E.3.2", "E0248",
                      "Requires signed division.", False, B_INTERP))
    s.add_evidence(ev("ev.b13.r2", "cl.req13.int", "SRC.OSX.IA2E.3.2", "E0248",
                      "Requires integer arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b13.p1", "cl.pre13.alg_grad", "SRC.WAEC.WASSCE.MATH.SYL", "E0247",
                      "Requires algebraic evaluation of the formula.", True, B_INTERP))
    return s
