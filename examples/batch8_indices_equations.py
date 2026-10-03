"""Batch 008 — Equations in indices."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch7_inequalities import build_graph_v7
from examples._batchkit import accept, ev

B_REVIEW = "act.batch8.review"
B_INTERP = "act.batch8.interpret"


def build_graph_v8() -> CDGStore:
    s = build_graph_v7()
    s.add_activity(Activity(id="act.batch8.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T14:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T14:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T15:00:00Z",
                            rationale="Human review of index-equations batch."))
    if "SRC.OSX.IA2E.10.3" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.10.3", title="Intermediate Algebra 2e, 10.3 Exponential Functions",
                            identifier_or_url="legacy:SRC.OSX.IA2E.10.3", publisher="OpenStax",
                            source_type=SourceType.TEXTBOOK, tier="primary"))
    kc = KnowledgeComponent(id="kc.equations_in_indices",
                            label="Equations involving indices",
                            definition="Solve equations with unknowns in exponents by equating bases/indices.",
                            subject="Mathematics", status=ClaimStatus.ACCEPTED,
                            legacy_ids=["MATH.NUM.EQUATIONS_IN_INDICES"],
                            created_by_activity=B_INTERP, cdg_version="v0.2.0")
    kc.reviewed_by_activity = B_REVIEW
    s.add_entity(kc)
    tm = TaskModel(id="tm.solve_index_equation", label="Solve an equation involving indices",
                   status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
    tm.reviewed_by_activity = B_REVIEW
    m1 = Method(id="m.match_bases", label="Express both sides with the same base, then equate indices",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m1.reviewed_by_activity = B_REVIEW
    m2 = Method(id="m.logs", label="Take logarithms of both sides",
                task_model_id=tm.id, status=ClaimStatus.ACCEPTED,
                created_by_activity=B_INTERP, cdg_version="v0.2.0")
    m2.reviewed_by_activity = B_REVIEW
    for e in (tm, m1, m2): s.add_entity(e)
    it = Item(id="it.mcq.index_eq", label="MCQ: index equation",
              task_model_id=tm.id, stem="Solve 2^x = 16", options=["x = 4", "x = 8", "x = 2", "x = 16"],
              key="x = 4", status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP)
    s.add_entity(it)
    ASSESS = (AcceptanceBasis.EXPERT,); DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def add(cid, pred, subj, obj, ctype, rationale, bases, **kw):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=B_INTERP,
                  created_at="2026-10-03T14:10:00Z", cdg_version="v0.2.0", **kw)
        s.add_claim(accept(c, rationale, bases, B_REVIEW))

    add("cl.tm8.target", RelationshipType.TARGETS, tm.id, kc.id,
        ClaimType.ASSESSMENT_DESIGN, "targets equations in indices", ASSESS)
    add("cl.tm8.m1", RelationshipType.HAS_METHOD, tm.id, m1.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    add("cl.tm8.m2", RelationshipType.HAS_METHOD, tm.id, m2.id, ClaimType.ASSESSMENT_DESIGN, "ownership", ASSESS)
    for cid, m, kc_id in [("cl.req8.match_lin", m1, "kc.linear_equations_one_var"),
                          ("cl.req8.match_alg", m1, "kc.algebraic_expressions"),
                          ("cl.req8.logs_alg", m2, "kc.algebraic_expressions")]:
        add(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY,
            f"{m.id} requires {kc_id}", DEP)
    add("cl.pre8.lin_idx", RelationshipType.PREREQUISITE, "kc.linear_equations_one_var", kc.id,
        ClaimType.DEPENDENCY, "EXECUTE for match-bases method", DEP,
        purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_METHOD,
        scope_ref=m1.id, origin=ClaimOrigin.DERIVED)
    s.add_evidence(ev("ev.b8.t", "cl.tm8.target", "SRC.OSX.IA2E.10.3", "E0043",
                      "Solve: 2^4 = 3x - 5.", False, B_INTERP))
    s.add_evidence(ev("ev.b8.m1", "cl.tm8.m1", "SRC.OSX.IA2E.10.3", "E0043", "Equating indices.", False, B_INTERP))
    s.add_evidence(ev("ev.b8.m2", "cl.tm8.m2", "SRC.OSX.IA2E.10.3", "E0043", "Logarithm route.", False, B_INTERP))
    s.add_evidence(ev("ev.b8.r1", "cl.req8.match_lin", "SRC.OSX.IA2E.10.3", "E0043",
                      "Reduces to a linear equation.", False, B_INTERP))
    s.add_evidence(ev("ev.b8.r2", "cl.req8.match_alg", "SRC.OSX.IA2E.10.3", "E0043",
                      "Requires exponent laws (algebraic manipulation).", False, B_INTERP))
    s.add_evidence(ev("ev.b8.r3", "cl.req8.logs_alg", "SRC.OSX.IA2E.10.3", "E0043",
                      "Log laws and algebraic manipulation.", False, B_INTERP))
    s.add_evidence(ev("ev.b8.p1", "cl.pre8.lin_idx", "SRC.OSX.IA2E.10.3", "E0043",
                      "Reduces to linear equation after equating indices.", False, B_INTERP))
    return s
