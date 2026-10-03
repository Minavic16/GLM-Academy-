"""Batch 005 — Quadratic formula and completing the square (owning TMs)."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, Method, TaskModel
from cdg.enums import (
    AcceptanceBasis,
    ActivityType,
    ClaimOrigin,
    ClaimStatus,
    ClaimType,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
    SourceType,
)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch4_factorisation import build_graph_v4
from examples._batchkit import accept, ev

B_REVIEW = "act.batch5.review"
B_INTERP = "act.batch5.interpret"


def build_graph_v5() -> CDGStore:
    s = build_graph_v4()
    s.add_activity(Activity(id="act.batch5.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T08:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T08:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T09:00:00Z",
                            rationale="Human review of quadratic-formula/cts batch."))
    if "SRC.OSX.IA2E.9.2" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.9.2",
                            title="Intermediate Algebra 2e, 9.2 Solve Quadratic Equations by Completing the Square",
                            identifier_or_url="legacy:SRC.OSX.IA2E.9.2",
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK, tier="primary"))

    tmF = TaskModel(id="tm.apply_quadratic_formula", label="Apply the quadratic formula",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmF.reviewed_by_activity = B_REVIEW
    mF = Method(id="m.substitute_formula", label="Identify a, b, c and substitute",
                task_model_id=tmF.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mF.reviewed_by_activity = B_REVIEW
    tmC = TaskModel(id="tm.complete_square", label="Complete the square",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmC.reviewed_by_activity = B_REVIEW
    mC1 = Method(id="m.cts_standard_form", label="Complete the square from standard form",
                 task_model_id=tmC.id, status=ClaimStatus.ACCEPTED,
                 created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mC1.reviewed_by_activity = B_REVIEW
    mC2 = Method(id="m.cts_then_roots", label="Complete the square then take square roots",
                 task_model_id=tmC.id, status=ClaimStatus.ACCEPTED,
                 created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mC2.reviewed_by_activity = B_REVIEW
    for e in (tmF, mF, tmC, mC1, mC2):
        s.add_entity(e)
    it = Item(id="it.mcq.completing_square", label="MCQ: complete the square",
              task_model_id=tmC.id, stem="Write x^2 + 6x + 5 in completed-square form",
              options=["(x+3)^2 - 4", "(x+6)^2 - 31", "(x+3)^2 + 5", "(x+5)^2 - 20"],
              key="(x+3)^2 - 4", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)

    for kc_id in ("kc.quadratic_formula", "kc.completing_the_square"):
        e = s.entities[kc_id]
        e.status = ClaimStatus.ACCEPTED
        e.reviewed_by_activity = B_REVIEW
        e.review_rationale = "Accepted via batch_005 TM + reviewed claims."

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T08:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tmQf.target", RelationshipType.TARGETS, tmF.id, "kc.quadratic_formula",
        ClaimType.ASSESSMENT_DESIGN, "targets the quadratic formula", ASSESS)
    add("cl.tmCts.target", RelationshipType.TARGETS, tmC.id, "kc.completing_the_square",
        ClaimType.ASSESSMENT_DESIGN, "targets completing the square", ASSESS)
    add("cl.tmQf.m1", RelationshipType.HAS_METHOD, tmF.id, mF.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    add("cl.tmCts.m1", RelationshipType.HAS_METHOD, tmC.id, mC1.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    add("cl.tmCts.m2", RelationshipType.HAS_METHOD, tmC.id, mC2.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    for cid, m, kc in [("cl.req.f_alg", mF, "kc.algebraic_expressions"),
                       ("cl.req.f_int", mF, "kc.integer_arithmetic"),
                       ("cl.req.c1_alg", mC1, "kc.algebraic_expressions"),
                       ("cl.req.c1_int", mC1, "kc.integer_arithmetic"),
                       ("cl.req.c2_alg", mC2, "kc.algebraic_expressions"),
                       ("cl.req.c2_int", mC2, "kc.integer_arithmetic")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc}", DEP)
    # Note: the UNDERSTAND prerequisite algebraic→quadratic_formula and
    # completing_the_square→quadratic_formula already exist from batch 001 with
    # legacy evidence; preserving them unchanged preserves history.

    s.add_evidence(ev("ev.b5.tF", "cl.tmQf.target", "SRC.NERDC.SSS2.MATH.2025", "E0129",
                      "NERDC SS1 already expects learners to 'derive the quadratic formula'.", True, B_INTERP))
    s.add_evidence(ev("ev.b5.tC", "cl.tmCts.target", "SRC.OSX.IA2E.9.2", "E0127",
                      "Square-root property section precedes completing the square.", False, B_INTERP))
    for cid, leg, src, exc in [
        ("cl.tmQf.m1", "E0131", "SRC.OSX.IA2E.9.3", "Evaluate b^2 - 4ab when a = 3 and b = -2."),
        ("cl.tmCts.m1", "E0126", "SRC.NERDC.SSS2.MATH.2025", "Factorization of algebraic expressions into perfect squares. 'Making...'"),
        ("cl.tmCts.m2", "E0126", "SRC.NERDC.SSS2.MATH.2025", "Making a perfect-square trinomial then square root."),
    ]:
        s.add_evidence(ev(f"ev.b5.m.{cid[-1]}.{cid}", cid, src, leg, exc, False, B_INTERP))
    s.add_evidence(ev("ev.b5.rF1", "cl.req.f_alg", "SRC.OSX.IA2E.9.3", "E0131",
                      "Requires substitution into the formula.", False, B_INTERP))
    s.add_evidence(ev("ev.b5.rF2", "cl.req.f_int", "SRC.OSX.IA2E.9.3", "E0131",
                      "Requires signed-number evaluation.", False, B_INTERP))
    s.add_evidence(ev("ev.b5.rC1", "cl.req.c1_alg", "SRC.NERDC.SSS2.MATH.2025", "E0126",
                      "Requires algebraic manipulation.", False, B_INTERP))
    s.add_evidence(ev("ev.b5.rC2", "cl.req.c1_int", "SRC.OSX.IA2E.9.2", "E0127",
                      "Requires signed-number arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b5.rC3", "cl.req.c2_alg", "SRC.NERDC.SSS2.MATH.2025", "E0126",
                      "Requires algebraic manipulation.", False, B_INTERP))
    s.add_evidence(ev("ev.b5.rC4", "cl.req.c2_int", "SRC.OSX.IA2E.9.2", "E0127",
                      "Requires signed-number arithmetic.", False, B_INTERP))
    return s
