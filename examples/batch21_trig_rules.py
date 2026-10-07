"""Batch 021 — Sine rule and cosine rule (non-right triangles)."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch20_probability import build_graph_v20
from examples._batchkit import accept, ev

B_REVIEW = "act.batch21.review"
B_INTERP = "act.batch21.interpret"


def build_graph_v21() -> CDGStore:
    s = build_graph_v20()
    s.add_activity(Activity(id="act.batch21.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T08:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T08:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T09:00:00Z",
                            rationale="Human review of sine/cosine rule batch."))
    for sid, title in [("SRC.OSX.AT2E.10.1", "Algebra and Trigonometry 2e, 10.1 The Law of Sines"),
                       ("SRC.OSX.AT2E.10.2", "Algebra and Trigonometry 2e, 10.2 The Law of Cosines")]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                                publisher="OpenStax", source_type=SourceType.TEXTBOOK, tier="primary"))
    kcS = KnowledgeComponent(id="kc.sine_rule", label="Sine rule for oblique triangles",
                             definition="a/sin A = b/sin B = c/sin C.",
                             subject="Mathematics", status=ClaimStatus.ACCEPTED,
                             legacy_ids=["MATH.TRIG.SINE_RULE"], created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kcS.reviewed_by_activity = B_REVIEW
    kcC = KnowledgeComponent(id="kc.cosine_rule", label="Cosine rule for oblique triangles",
                             definition="c^2 = a^2 + b^2 - 2ab cos C.",
                             subject="Mathematics", status=ClaimStatus.ACCEPTED,
                             legacy_ids=["MATH.TRIG.COSINE_RULE"], created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kcC.reviewed_by_activity = B_REVIEW
    s.add_entity(kcS); s.add_entity(kcC)
    tm = TaskModel(id="tm.solve_oblique_triangle",
                   label="Solve a non-right triangle",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    mS = Method(id="m.sine_rule", label="Apply the sine rule",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mS.reviewed_by_activity = B_REVIEW
    mC = Method(id="m.cosine_rule", label="Apply the cosine rule",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    mC.reviewed_by_activity = B_REVIEW
    for e in (tm, mS, mC): s.add_entity(e)
    it = Item(id="it.mcq.sine_rule", label="MCQ: sine rule", task_model_id=tm.id,
              stem="In triangle ABC, a=5, A=30°, b=7. Find B (sine rule).", 
              options=["about 44.4°", "about 60°", "about 30°", "about 90°"], key="about 44.4°",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-07T08:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm21.targetS", RelationshipType.TARGETS, tm.id, kcS.id,
        ClaimType.ASSESSMENT_DESIGN, "targets sine rule", ASSESS)
    add("cl.tm21.targetC", RelationshipType.TARGETS, tm.id, kcC.id,
        ClaimType.ASSESSMENT_DESIGN, "targets cosine rule", ASSESS)
    add("cl.tm21.mS", RelationshipType.HAS_METHOD, tm.id, mS.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm21.mC", RelationshipType.HAS_METHOD, tm.id, mC.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, m, kc_id in [("cl.req21S.trig", mS, "kc.trig_ratios_acute"),
                          ("cl.req21S.alg", mS, "kc.algebraic_expressions"),
                          ("cl.req21C.trig", mC, "kc.trig_ratios_acute"),
                          ("cl.req21C.alg", mC, "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre21.trig_sine", RelationshipType.PREREQUISITE, "kc.trig_ratios_acute", kcS.id,
        ClaimType.DEPENDENCY, "UNDERSTAND, asserted", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    add("cl.pre21.trig_cosine", RelationshipType.PREREQUISITE, "kc.trig_ratios_acute", kcC.id,
        ClaimType.DEPENDENCY, "UNDERSTAND, asserted", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    s.add_evidence(ev("ev.b21.tS", "cl.tm21.targetS", "SRC.OSX.AT2E.10.1", "E0283",
                      "Law of Sines applied to oblique triangles.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.tC", "cl.tm21.targetC", "SRC.OSX.AT2E.10.2", "E0286",
                      "Using the side as one leg of a right triangle.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.mS", "cl.tm21.mS", "SRC.OSX.AT2E.10.1", "E0285",
                      "Law of Sines applied to oblique triangles.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.mC", "cl.tm21.mC", "SRC.OSX.AT2E.10.2", "E0290",
                      "Law of Cosines statement.", False, B_INTERP))
    s.add_evidence(ev("ev.b21.r1", "cl.req21S.trig", "SRC.OSX.AT2E.10.1", "E0283",
                      "Requires right-triangle trig ratios.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.r2", "cl.req21S.alg", "SRC.OSX.IA2E.5.4", "E0089",
                      "Requires solving proportions.", False, B_INTERP))
    s.add_evidence(ev("ev.b21.r3", "cl.req21C.trig", "SRC.OSX.AT2E.10.2", "E0286",
                      "Requires right-triangle trig ratios.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.r4", "cl.req21C.alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Requires expanding and simplifying.", False, B_INTERP))
    s.add_evidence(ev("ev.b21.p1", "cl.pre21.trig_sine", "SRC.OSX.AT2E.10.1", "E0283",
                      "Builds on sine/cosine/tangent ratios.", True, B_INTERP))
    s.add_evidence(ev("ev.b21.p2", "cl.pre21.trig_cosine", "SRC.OSX.AT2E.10.2", "E0286",
                      "Builds on right-triangle trig.", True, B_INTERP))
    return s
