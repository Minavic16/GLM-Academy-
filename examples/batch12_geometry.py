"""Batch 012 — Euclidean geometry: lines/angles and triangle angle properties."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity
from cdg.store import CDGStore
from examples.batch11_number import build_graph_v11
from examples._batchkit import accept, ev

B_REVIEW = "act.batch12.review"
B_INTERP = "act.batch12.interpret"


def build_graph_v12() -> CDGStore:
    s = build_graph_v11()
    s.add_activity(Activity(id="act.batch12.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T22:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T22:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T23:00:00Z",
                            rationale="Human review of geometry batch."))
    for kid, label, definition, legacy in [
        ("kc.parallel_line_angles", "Angles formed by parallel lines and a transversal",
         "Corresponding, alternate and co-interior angle facts.", "MATH.GEO.PARALLEL_LINE_ANGLES"),
        ("kc.triangle_angle_properties", "Triangle angle properties",
         "Angle sum of a triangle; exterior angle equals sum of interior opposites.", "MATH.GEO.TRIANGLE_PROPERTIES"),
    ]:
        k = KnowledgeComponent(id=kid, label=label, definition=definition, subject="Mathematics",
                               status=ClaimStatus.ACCEPTED, legacy_ids=[legacy],
                               created_by_activity=B_INTERP, cdg_version="v0.2.0")
        k.reviewed_by_activity = B_REVIEW
        s.add_entity(k)
    tmP = TaskModel(id="tm.identify_parallel_line_angles",
                    label="Identify/apply parallel-line angle relations",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmP.reviewed_by_activity = B_REVIEW
    mP = Method(id="m.corresponding_alternate", label="Apply corresponding/alternate angle theorems",
                task_model_id=tmP.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mP.reviewed_by_activity = B_REVIEW
    tmT = TaskModel(id="tm.triangle_angle_problems",
                    label="Solve triangle angle problems",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmT.reviewed_by_activity = B_REVIEW
    mT1 = Method(id="m.triangle_angle_sum", label="Use the triangle angle sum",
                 task_model_id=tmT.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mT1.reviewed_by_activity = B_REVIEW
    mT2 = Method(id="m.exterior_angle", label="Use the exterior-angle property",
                 task_model_id=tmT.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mT2.reviewed_by_activity = B_REVIEW
    for e in (tmP, mP, tmT, mT1, mT2): s.add_entity(e)
    it = Item(id="it.mcq.triangle_angle", label="MCQ: triangle angle problem",
              task_model_id=tmT.id, stem="Two angles of a triangle are 50° and 60°. Find the third.",
              options=["70°", "60°", "50°", "110°"], key="70°",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T22:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm12P.target", RelationshipType.TARGETS, tmP.id, "kc.parallel_line_angles",
        ClaimType.ASSESSMENT_DESIGN, "targets parallel-line angles", ASSESS)
    add("cl.tm12T.target", RelationshipType.TARGETS, tmT.id, "kc.triangle_angle_properties",
        ClaimType.ASSESSMENT_DESIGN, "targets triangle angle properties", ASSESS)
    add("cl.tm12P.m1", RelationshipType.HAS_METHOD, tmP.id, mP.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm12T.m1", RelationshipType.HAS_METHOD, tmT.id, mT1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm12T.m2", RelationshipType.HAS_METHOD, tmT.id, mT2.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.req12P.int", RelationshipType.REQUIRES, mP.id, "kc.integer_arithmetic",
        ClaimType.DEPENDENCY, "angle arithmetic", DEP)
    add("cl.req12T1.parallel", RelationshipType.REQUIRES, mT1.id, "kc.parallel_line_angles",
        ClaimType.DEPENDENCY, "triangle sum builds on parallel-line facts", DEP)
    add("cl.req12T2.parallel", RelationshipType.REQUIRES, mT2.id, "kc.parallel_line_angles",
        ClaimType.DEPENDENCY, "exterior-angle property builds on parallel-line facts", DEP)
    add("cl.req12T1.int", RelationshipType.REQUIRES, mT1.id, "kc.integer_arithmetic",
        ClaimType.DEPENDENCY, "angle arithmetic", DEP)
    add("cl.pre12.parallel_triangle", RelationshipType.PREREQUISITE, "kc.parallel_line_angles",
        "kc.triangle_angle_properties", ClaimType.DEPENDENCY, "EXECUTE, whole TM", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tmT.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre12_u.parallel_triangle", RelationshipType.PREREQUISITE, "kc.parallel_line_angles",
        "kc.triangle_angle_properties", ClaimType.DEPENDENCY, "UNDERSTAND, asserted", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    s.add_evidence(ev("ev.b12.tP", "cl.tm12P.target", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Proofs of Some Basic Theorems", True, B_INTERP))
    s.add_evidence(ev("ev.b12.tT", "cl.tm12T.target", "SRC.WAEC.WASSCE.MATH.SYL", "E0230",
                      "Triangle angle sum precedes polygon angle sum.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.mP", "cl.tm12P.m1", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Parallel-line angle theorems.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.mT1", "cl.tm12T.m1", "SRC.WAEC.WASSCE.MATH.SYL", "E0230",
                      "Sum of angles of a triangle.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.mT2", "cl.tm12T.m2", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Exterior angle theorem.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.r1", "cl.req12P.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires integer angle arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b12.r2", "cl.req12T1.parallel", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Builds on parallel-line theorems.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.r3", "cl.req12T2.parallel", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Exterior-angle fact from parallel lines.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.r4", "cl.req12T1.int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires integer arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b12.p1", "cl.pre12.parallel_triangle", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "Parallel-line facts required.", True, B_INTERP))
    s.add_evidence(ev("ev.b12.p2", "cl.pre12_u.parallel_triangle", "SRC.NERDC.SSS2.MATH.2025", "E0227",
                      "UNDERSTAND chain from legacy edge E0227.", True, B_INTERP))
    return s
