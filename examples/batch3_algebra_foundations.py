"""Batch 003 — Algebra foundations (algebraic expressions + integer arithmetic).

Gives kc.algebraic_expressions and kc.integer_arithmetic their owning
TaskModels so both can graduate from PROPOSED via the normal lifecycle.
"""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
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
from examples.batch2_linear_equations import build_graph
from examples._batchkit import accept, ev

B_REVIEW = "act.batch3.review"
B_INTERP = "act.batch3.interpret"


def build_graph_v3() -> CDGStore:
    s = build_graph()
    s.add_activity(Activity(id="act.batch3.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T04:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T04:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T05:00:00Z",
                            rationale="Human review of algebra-foundations batch."))
    for sid, title, pub, styp in [
        ("SRC.OSX.IA2E.6.2", "Intermediate Algebra 2e, 6.2 Integer Exponents", "OpenStax", SourceType.TEXTBOOK),
        ("SRC.JAMB.UTME.MATH", "JAMB UTME Mathematics Syllabus", "JAMB", SourceType.SYLLABUS),
    ]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                                publisher=pub, source_type=styp, tier="primary"))

    tmA = TaskModel(id="tm.handle_algebraic_expressions",
                    label="Simplify and evaluate algebraic expressions",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmA.reviewed_by_activity = B_REVIEW
    mA1 = Method(id="m.collect_like_terms", label="Collect like terms and substitute",
                 task_model_id=tmA.id, status=ClaimStatus.ACCEPTED,
                 created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mA1.reviewed_by_activity = B_REVIEW
    mA2 = Method(id="m.expand_simplify", label="Expand then simplify",
                 task_model_id=tmA.id, status=ClaimStatus.ACCEPTED,
                 created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mA2.reviewed_by_activity = B_REVIEW
    s.add_entity(tmA); s.add_entity(mA1); s.add_entity(mA2)

    tmB = TaskModel(id="tm.signed_number_arithmetic", label="Perform signed-number arithmetic",
                    status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tmB.reviewed_by_activity = B_REVIEW
    mB1 = Method(id="m.sign_rules", label="Apply sign rules for operations",
                 task_model_id=tmB.id, status=ClaimStatus.ACCEPTED,
                 created_by_activity=B_INTERP, cdg_version="v0.2.0")
    mB1.reviewed_by_activity = B_REVIEW
    s.add_entity(tmB); s.add_entity(mB1)

    it = Item(id="it.mcq.alg_simplify", label="MCQ: simplify algebraic expression",
              task_model_id=tmA.id, stem="Simplify 8a^2 + 12a + 1 + 3a^2 - 5a + 4",
              options=["11a^2 + 7a + 1", "11a^2 + 17a + 1", "5a^2 + 7a + 1", "11a^2 + 7a + 5"],
              key="11a^2 + 7a + 1", status=ClaimStatus.ACCEPTED,
              created_by_activity=B_INTERP)
    s.add_entity(it)

    # graduate the two foundational KCs
    for kc_id, review in [("kc.algebraic_expressions", B_REVIEW), ("kc.integer_arithmetic", B_REVIEW)]:
        e = s.entities[kc_id]
        e.status = ClaimStatus.ACCEPTED
        e.reviewed_by_activity = review
        e.review_rationale = "Accepted via batch_003 TaskModel + reviewed claims."

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    mB1_req = Claim(id="cl.req.signrules", predicate=RelationshipType.REQUIRES,
                    subject_id=mB1.id, object_id="kc.integer_arithmetic",
                    claim_type=ClaimType.DEPENDENCY, created_by_activity=B_INTERP)
    s.add_claim(accept(mB1_req, "sign rules exercise integer arithmetic", DEP, B_REVIEW))

    s.add_claim(accept(Claim(id="cl.tmA.target", predicate=RelationshipType.TARGETS,
              subject_id=tmA.id, object_id="kc.algebraic_expressions",
              claim_type=ClaimType.ASSESSMENT_DESIGN, created_by_activity=B_INTERP),
              "targets algebraic expressions", ASSESS, B_REVIEW))
    s.add_claim(accept(Claim(id="cl.tmB.target", predicate=RelationshipType.TARGETS,
              subject_id=tmB.id, object_id="kc.integer_arithmetic",
              claim_type=ClaimType.ASSESSMENT_DESIGN, created_by_activity=B_INTERP),
              "targets integer arithmetic", ASSESS, B_REVIEW))
    for cid, tm, m in [("cl.tmA.m1", tmA, mA1), ("cl.tmA.m2", tmA, mA2), ("cl.tmB.m1", tmB, mB1)]:
        s.add_claim(accept(Claim(id=cid, predicate=RelationshipType.HAS_METHOD,
                                 subject_id=tm.id, object_id=m.id,
                                 claim_type=ClaimType.ASSESSMENT_DESIGN, created_by_activity=B_INTERP),
                           "method ownership", ASSESS, B_REVIEW))
    for cid, m, kc in [("cl.req.collect_int", mA1, "kc.integer_arithmetic"),
                       ("cl.req.expand_int", mA2, "kc.integer_arithmetic")]:
        s.add_claim(accept(Claim(id=cid, predicate=RelationshipType.REQUIRES,
                                 subject_id=m.id, object_id=kc,
                                 claim_type=ClaimType.DEPENDENCY, created_by_activity=B_INTERP),
                           f"{m.id} needs {kc}", DEP, B_REVIEW))
    # tmB method requires the target KC it exercises (permitted: target inclusion rule).

    c = Claim(id="cl.pre.int_alg", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.integer_arithmetic", object_id="kc.algebraic_expressions",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref=tmA.id,
              origin=ClaimOrigin.DERIVED, created_by_activity=B_INTERP)
    s.add_claim(accept(c, "DERIVED: both tmA methods require integer arithmetic.", DEP, B_REVIEW))

    s.add_evidence(ev("ev.b3.tA", "cl.tmA.target", "SRC.OSX.IA2E.5.4", "E0089",
                      "Combine like terms.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.tB", "cl.tmB.target", "SRC.OSX.IA2E.6.2", "E0099",
                      "Simplify: -9(6); -9(-6).", False, B_INTERP))
    s.add_evidence(ev("ev.b3.r1", "cl.req.collect_int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Signed-number arithmetic inside simplification.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.r2", "cl.req.expand_int", "SRC.OSX.IA2E.5.4", "E0100",
                      "Find the product: (3y + 4)(2y + 5).", False, B_INTERP))
    s.add_evidence(ev("ev.b3.m1", "cl.tmA.m1", "SRC.OSX.IA2E.5.4", "E0089",
                      "Combine like terms.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.m2", "cl.tmA.m2", "SRC.OSX.IA2E.5.4", "E0100",
                      "Expand then simplify.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.m3", "cl.tmB.m1", "SRC.OSX.IA2E.6.2", "E0099",
                      "Sign rules for products.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.p1", "cl.pre.int_alg", "SRC.OSX.IA2E.6.2", "E0099",
                      "Requires signed-number arithmetic.", False, B_INTERP))
    s.add_evidence(ev("ev.b3.r3", "cl.req.signrules", "SRC.OSX.IA2E.6.2", "E0099",
                      "Sign rules exercise integer arithmetic.", False, B_INTERP))
    return s
