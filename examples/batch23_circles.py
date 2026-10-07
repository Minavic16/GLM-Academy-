"""Batch 023 — Foundational circle angle theorems."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity
from cdg.store import CDGStore
from examples.batch22_equation_of_line import build_graph_v22
from examples._batchkit import accept, ev

B_REVIEW = "act.batch23.review"
B_INTERP = "act.batch23.interpret"


def build_graph_v23() -> CDGStore:
    s = build_graph_v22()
    s.add_activity(Activity(id="act.batch23.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T12:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T12:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T13:00:00Z",
                            rationale="Human review of circle-geometry batch."))
    kc = KnowledgeComponent(id="kc.circle_angle_theorems",
                            label="Basic circle angle theorems",
                            definition="Angles in same segment, angle at centre is twice angle at circumference, angle in semicircle.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.GEO.CIRCLE_ANGLE_THEOREMS"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.circle_angle_problems", label="Solve circle angle problems using theorems",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.centre_vs_circumference", label="Apply angle-at-centre = twice angle-at-circumference",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.circle", label="MCQ: circle angle", task_model_id=tm.id,
              stem="Angle at centre subtended by arc is 140°. Angle at circumference on same arc?",
              options=["70°", "140°", "40°", "280°"], key="70°",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T12:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm23.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets circle angle theorems", ASSESS)
    add("cl.tm23.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req23.tri", "kc.triangle_angle_properties"),
                       ("cl.req23.int", "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre23.tri_circle", RelationshipType.PREREQUISITE, "kc.triangle_angle_properties", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm23", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b23.t", "cl.tm23.target", "SRC.NERDC.SSS2.MATH.2025", "E0233",
                      "Circle theorems; proofs based on the knowledge of these theorems.", True, B_INTERP))
    s.add_evidence(ev("ev.b23.m1", "cl.tm23.m1", "SRC.NERDC.SSS2.MATH.2025", "E0233",
                      "Angles in a segment theorems.", True, B_INTERP))
    s.add_evidence(ev("ev.b23.r1", "cl.req23.tri", "SRC.NERDC.SSS2.MATH.2025", "E0233",
                      "Requires triangle angle facts.", True, B_INTERP))
    s.add_evidence(ev("ev.b23.r2", "cl.req23.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires angle arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b23.p1", "cl.pre23.tri_circle", "SRC.NERDC.SSS2.MATH.2025", "E0233",
                      "Circle theorems require triangle angle properties.", True, B_INTERP))
    return s
