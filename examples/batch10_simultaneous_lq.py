"""Batch 010 — Simultaneous linear-quadratic equations (substitution method)."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch9_change_of_subject import build_graph_v9
from examples._batchkit import accept, ev

B_REVIEW = "act.batch10.review"
B_INTERP = "act.batch10.interpret"


def build_graph_v10() -> CDGStore:
    s = build_graph_v9()
    s.add_activity(Activity(id="act.batch10.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T18:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T18:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T19:00:00Z",
                            rationale="Human review of simultaneous linear-quadratic batch."))
    if "SRC.OSX.IA2E.11.5" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.11.5", title="Intermediate Algebra 2e, 11.5 Systems of Nonlinear Equations",
                            identifier_or_url="legacy:SRC.OSX.IA2E.11.5", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.simultaneous_linear_quadratic",
                            label="Simultaneous equations: one linear, one quadratic",
                            definition="Solve a system with a linear and a quadratic equation.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.ALG.SIMULTANEOUS_LINEAR_QUADRATIC"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.solve_linear_quadratic_system",
                   label="Solve a system with one linear and one quadratic equation",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.substitute_linear_into_quadratic",
                label="Rearrange the linear equation, substitute into the quadratic",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    s.add_entity(tm); s.add_entity(m1)
    it = Item(id="it.mcq.linquad", label="MCQ: linear-quadratic system",
              task_model_id=tm.id, stem="Solve y = x + 1 and y = x^2 - 3",
              options=["(2,3) and (-1,0)", "(3,-2) and (0,-1)", "(1,2) only", "(4,5) and (-2,-1)"],
              key="(2,3) and (-1,0)", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T18:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm10.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets linear-quadratic systems", ASSESS)
    add("cl.tm10.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, kc_id in [("cl.req10.sub_change", "kc.change_of_subject"),
                       ("cl.req10.sub_simlin", "kc.simultaneous_linear_equations"),
                       ("cl.req10.sub_quad", "kc.quadratic_roots")]:
        add(cid, RelationshipType.REQUIRES, m1.id, kc_id, ClaimType.DEPENDENCY,
            f"{m1.id} requires {kc_id}", DEP)
    add("cl.pre10.simlin_lq", RelationshipType.PREREQUISITE, "kc.simultaneous_linear_equations", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via every method of tm10", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    add("cl.pre10.roots_lq", RelationshipType.PREREQUISITE, "kc.quadratic_roots", kc.id,
        ClaimType.DEPENDENCY, "UNDERSTAND prerequisite (asserted)", DEP,
        purpose=PrerequisitePurpose.UNDERSTAND, scope=PrerequisiteScope.ALL_RELEVANT_METHODS,
        origin=ClaimOrigin.ASSERTED)
    s.add_evidence(ev("ev.b10.t", "cl.tm10.target", "SRC.OSX.IA2E.11.5", "E0153",
                      "Solve linear systems by graphing, substitution and elimination.", False, B_INTERP))
    s.add_evidence(ev("ev.b10.m1", "cl.tm10.m1", "SRC.OSX.IA2E.11.5", "E0153",
                      "Substitution method.", False, B_INTERP))
    s.add_evidence(ev("ev.b10.r1", "cl.req10.sub_change", "SRC.WAEC.WASSCE.MATH.SYL", "E0084",
                      "Requires change of subject.", True, B_INTERP))
    s.add_evidence(ev("ev.b10.r2", "cl.req10.sub_simlin", "SRC.OSX.IA2E.11.5", "E0153",
                      "Requires simultaneous-equation methods.", False, B_INTERP))
    s.add_evidence(ev("ev.b10.r3", "cl.req10.sub_quad", "SRC.NERDC.SSS1.MATH.2025", "E0134",
                      "Requires obtaining roots of quadratics.", True, B_INTERP))
    s.add_evidence(ev("ev.b10.p1", "cl.pre10.simlin_lq", "SRC.OSX.IA2E.11.5", "E0153",
                      "Builds on simultaneous-equation solving.", False, B_INTERP))
    s.add_evidence(ev("ev.b10.p2", "cl.pre10.roots_lq", "SRC.NERDC.SSS1.MATH.2025", "E0134",
                      "Quadratic roots underpin the final solution.", True, B_INTERP))
    return s
