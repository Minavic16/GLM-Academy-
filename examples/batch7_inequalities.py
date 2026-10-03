"""Batch 007 — Linear inequalities (analytical)."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch6_functions import build_graph_v6
from examples._batchkit import accept, ev

B_REVIEW = "act.batch7.review"
B_INTERP = "act.batch7.interpret"


def build_graph_v7() -> CDGStore:
    s = build_graph_v6()
    s.add_activity(Activity(id="act.batch7.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T12:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T12:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T13:00:00Z",
                            rationale="Human review of inequalities batch."))
    kc = KnowledgeComponent(id="kc.linear_inequalities_analytic",
                            label="Linear inequalities: analytical solution",
                            definition="Solve ax+b>c type inequalities analytically, flipping sense when multiplying by a negative.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.ALG.LINEAR_INEQUALITY_ANALYTIC"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.solve_linear_inequality",
                   label="Solve a linear inequality in one variable",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.balance_inverse", label="Apply inverse operations preserving/flipping sense",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    m2 = Method(id="m.test_graph", label="Represent on a number line",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m2.reviewed_by_activity = B_REVIEW
    for e in (tm, m1, m2): s.add_entity(e)
    it = Item(id="it.mcq.linear_ineq", label="MCQ: solve linear inequality",
              task_model_id=tm.id, stem="Solve 2x - 3 > 7",
              options=["x > 5", "x < 5", "x > 2", "x < 2"], key="x > 5",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T12:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm7.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets linear inequality solving", ASSESS)
    add("cl.tm7.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm7.m2", RelationshipType.HAS_METHOD, tm.id, m2.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, m, kc_id in [("cl.req7.bal_lin", m1, "kc.linear_equations_one_var"),
                          ("cl.req7.bal_alg", m1, "kc.algebraic_expressions"),
                          ("cl.req7.grph_lin", m2, "kc.linear_equations_one_var")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre7.lin_ineq", RelationshipType.PREREQUISITE, "kc.linear_equations_one_var", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via every method of tm7", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b7.t", "cl.tm7.target", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Linear equations precede linear inequalities.", True, B_INTERP))
    s.add_evidence(ev("ev.b7.m1", "cl.tm7.m1", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Analytical solution of linear inequalities.", True, B_INTERP))
    s.add_evidence(ev("ev.b7.m2", "cl.tm7.m2", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Representation on a number line implied.", False, B_INTERP))
    s.add_evidence(ev("ev.b7.r1", "cl.req7.bal_lin", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Builds on linear equation solving.", True, B_INTERP))
    s.add_evidence(ev("ev.b7.r2", "cl.req7.bal_alg", "SRC.OSX.IA2E.5.4", "E0089",
                      "Requires algebraic simplification.", False, B_INTERP))
    s.add_evidence(ev("ev.b7.r3", "cl.req7.grph_lin", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Graphical method relies on equation solving.", True, B_INTERP))
    s.add_evidence(ev("ev.b7.p1", "cl.pre7.lin_ineq", "SRC.WAEC.WASSCE.MATH.SYL", "E0168",
                      "Linear equations precede linear inequalities.", True, B_INTERP))
    return s
