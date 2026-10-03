"""Batch 006 — Function concept and notation."""
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
from examples.batch5_quadratic_tools import build_graph_v5
from examples._batchkit import accept, ev

B_REVIEW = "act.batch6.review"
B_INTERP = "act.batch6.interpret"


def build_graph_v6() -> CDGStore:
    s = build_graph_v5()
    s.add_activity(Activity(id="act.batch6.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T10:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T10:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T11:00:00Z",
                            rationale="Human review of function-concept batch."))
    for sid, title in [("SRC.OSX.CALC1.2.2", "Calculus Volume 1, 2.2 Limits: A Numerical and Graphical Approach"),
                       ("SRC.OSX.CALC1.3.1", "Calculus Volume 1, 3.1 Defining the Derivative")]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                                publisher="OpenStax", source_type=SourceType.TEXTBOOK, tier="primary"))

    tm = TaskModel(id="tm.evaluate_and_represent_function",
                   label="Evaluate and represent functions",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.evaluate_substitution", label="Evaluate f(x) by substitution",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    m2 = Method(id="m.table_of_values", label="Represent via table of values",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m2.reviewed_by_activity = B_REVIEW
    for e in (tm, m1, m2):
        s.add_entity(e)
    it = Item(id="it.mcq.function_eval", label="MCQ: evaluate f(x)=x^2-3x",
              task_model_id=tm.id, stem="If f(x)=x^2-3x, find f(2)",
              options=["-2", "10", "2", "-10"], key="-2",
              status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)

    from cdg.entities import KnowledgeComponent
    if "kc.function_concept" not in s.entities:
        kc = KnowledgeComponent(id="kc.function_concept", label="Function concept and notation",
                                definition="A function assigns each input exactly one output; f(x) notation.",
                                subject="Mathematics", status=ClaimStatus.PROPOSED,
                                legacy_ids=["MATH.FND.FUNCTION_CONCEPT"],
                                created_by_activity=B_INTERP, cdg_version="v0.2.0")
        s.add_entity(kc)
    kc = s.entities["kc.function_concept"]
    kc.status = ClaimStatus.ACCEPTED
    kc.reviewed_by_activity = B_REVIEW
    kc.review_rationale = "Accepted via batch_006 TM + reviewed claims."

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T10:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tmFn.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets function concept", ASSESS)
    add("cl.tmFn.m1", RelationshipType.HAS_METHOD, tm.id, m1.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    add("cl.tmFn.m2", RelationshipType.HAS_METHOD, tm.id, m2.id,
        ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    for cid, m, kc_id in [("cl.req.fn1_alg", m1, "kc.algebraic_expressions"),
                          ("cl.req.fn1_int", m1, "kc.integer_arithmetic"),
                          ("cl.req.fn2_alg", m2, "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre.alg_fn", RelationshipType.PREREQUISITE, "kc.algebraic_expressions", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE via all methods of tmFn", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
        scope_ref=tm.id, origin=ClaimOrigin.DERIVED)

    s.add_evidence(ev("ev.b6.t", "cl.tmFn.target", "SRC.JAMB.UTME.MATH", "E0298",
                      "Function notation and 'limit of a function' in JAMB syllabus.", False, B_INTERP))
    s.add_evidence(ev("ev.b6.m1", "cl.tmFn.m1", "SRC.OSX.CALC1.3.1", "E0309",
                      "Derivative defined for a function f at a point a (function evaluation prerequisite).", False, B_INTERP))
    s.add_evidence(ev("ev.b6.m2", "cl.tmFn.m2", "SRC.WAEC.WASSCE.MATH.SYL", "E0156",
                      "'table of values'", False, B_INTERP))
    s.add_evidence(ev("ev.b6.r1", "cl.req.fn1_alg", "SRC.OSX.IA2E.5.4", "E0089",
                      "Substitution into algebraic expressions.", False, B_INTERP))
    s.add_evidence(ev("ev.b6.r2", "cl.req.fn1_int", "SRC.OSX.IA2E.6.2", "E0099",
                      "Integer arithmetic inside evaluation.", False, B_INTERP))
    s.add_evidence(ev("ev.b6.r3", "cl.req.fn2_alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Polynomial evaluation for table of values.", False, B_INTERP))
    s.add_evidence(ev("ev.b6.p1", "cl.pre.alg_fn", "SRC.OSX.CALC1.2.2", "E0297",
                      "Function skills rest on algebraic evaluation.", False, B_INTERP))
    return s
