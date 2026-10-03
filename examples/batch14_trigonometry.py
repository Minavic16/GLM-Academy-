"""Batch 014 — Trigonometry: ratios of acute angles."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch13_coordinate import build_graph_v13
from examples._batchkit import accept, ev

B_REVIEW = "act.batch14.review"
B_INTERP = "act.batch14.interpret"


def build_graph_v14() -> CDGStore:
    s = build_graph_v13()
    s.add_activity(Activity(id="act.batch14.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-04T02:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-04T02:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-04T03:00:00Z",
                            rationale="Human review of trigonometry batch."))
    if "SRC.OSX.CM.10.8" not in s.sources:
        s.add_source(Source(id="SRC.OSX.CM.10.8", title="Calculus: Early Transcendentals setup / Common Core geometry content",
                            identifier_or_url="legacy:SRC.OSX.CM.10.8", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="reference"))
    kc = KnowledgeComponent(id="kc.trig_ratios_acute",
                            label="Trigonometric ratios of acute angles",
                            definition="sin, cos, tan as opposite/hypotenuse, adjacent/hypotenuse, opposite/adjacent in right triangles.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.TRIG.RATIOS_ACUTE"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.trig_ratio_problems",
                   label="Solve right-triangle problems using trigonometric ratios",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.label_sides_match_ratio", label="Label opposite/adjacent/hypotenuse, match the ratio",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.trig_ratio", label="MCQ: trig ratio", task_model_id=tm.id,
              stem="In a right triangle, the side opposite angle A is 3 and the hypotenuse is 5. Find sin A.",
              options=["3/5", "4/5", "5/3", "3/4"], key="3/5",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-04T02:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm14.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets acute-angle ratios", ASSESS)
    add("cl.tm14.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req14.int", "kc.integer_arithmetic"),
                       ("cl.req14.alg", "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre14.alg_trig", RelationshipType.PREREQUISITE, "kc.algebraic_expressions", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via tm14's methods", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b14.t", "cl.tm14.target", "SRC.OSX.CM.10.8", "E0261",
                      "When you think about ratios, you should think about fractions.", True, B_INTERP))
    s.add_evidence(ev("ev.b14.m1", "cl.tm14.m1", "SRC.OSX.AT2E.7.2", "E0262",
                      "Sine sin t = opposite/hypotenuse.", True, B_INTERP))
    s.add_evidence(ev("ev.b14.r1", "cl.req14.int", "SRC.OSX.CM.10.8", "E0264",
                      "Right triangles with integer sides.", False, B_INTERP))
    s.add_evidence(ev("ev.b14.r2", "cl.req14.alg", "SRC.OSX.CM.10.8", "E0261",
                      "Ratios as fractions/algebra.", True, B_INTERP))
    s.add_evidence(ev("ev.b14.p1", "cl.pre14.alg_trig", "SRC.OSX.CM.10.8", "E0261",
                      "Ratio notation underpins trig definitions.", True, B_INTERP))
    return s
