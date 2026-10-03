"""Batch 002 — Linear equations in one variable.

Smallest coherent batch after math_slice_v1: give kc.linear_equations_one_var
the owning TaskModel/Methods that allow it to graduate from PROPOSED, and
attach its prerequisite claims + evidence per the same contracts used by
batch 001.

Everything here is proposed by the agent pipeline and marked for human
review; acceptance is explicit through the same lifecycle helper semantics.
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
    EvidenceRole,
    EvidenceStance,
    ExcerptKind,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity
from cdg.store import CDGStore
from examples.math_slice_v1 import build_slice

BATCH = "batch_002"


def _accept_batch2(claim: Claim, rationale: str, bases) -> Claim:
    claim.status = ClaimStatus.UNDER_REVIEW
    claim.status = ClaimStatus.ACCEPTED
    claim.acceptance_bases = set(bases)
    claim.review_rationale = rationale + " | REVIEW:act.batch2.review"
    return claim


def build_graph() -> CDGStore:
    s = build_slice()

    s.add_activity(Activity(id="act.batch2.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-03T02:00:00Z"))
    s.add_activity(Activity(id="act.batch2.interpret", type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T02:10:00Z"))
    s.add_activity(Activity(id="act.batch2.review", type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T03:00:00Z",
                            rationale="Human review of linear-equations batch."))

    # new supporting KC
    kc_int = KnowledgeComponent(
        id="kc.integer_arithmetic", label="Signed-number (integer) arithmetic",
        definition="Performing +, -, x, / with positive and negative integers.",
        subject="Mathematics", status=ClaimStatus.PROPOSED,
        legacy_ids=["MATH.FND.INTEGER_ARITHMETIC"],
        created_by_activity="act.batch2.interpret", cdg_version="v0.2.0",
    )
    s.add_entity(kc_int)

    tm4 = TaskModel(id="tm.solve_linear_equations_one_var",
                    label="Solve linear equations in one variable",
                    status=ClaimStatus.ACCEPTED, created_by_activity="act.batch2.interpret",
                    cdg_version="v0.2.0")
    tm4.reviewed_by_activity = "act.batch2.review"
    s.add_entity(tm4)

    m_inv = Method(id="m.isolate_variable", label="Isolate the variable via inverse operations",
                   task_model_id=tm4.id, status=ClaimStatus.ACCEPTED,
                   created_by_activity="act.batch2.interpret", cdg_version="v0.2.0")
    m_inv.reviewed_by_activity = "act.batch2.review"
    m_exp = Method(id="m.expand_collect", label="Expand brackets, collect like terms, then isolate",
                   task_model_id=tm4.id, status=ClaimStatus.ACCEPTED,
                   created_by_activity="act.batch2.interpret", cdg_version="v0.2.0")
    m_exp.reviewed_by_activity = "act.batch2.review"
    s.add_entity(m_inv); s.add_entity(m_exp)

    it3 = Item(id="it.mcq.linear_one_var", label="MCQ: solve linear equation",
               task_model_id=tm4.id, stem="Solve 5y - 3 = 0",
               options=["y = 3/5", "y = -3/5", "y = 5/3", "y = 3"], key="y = 3/5",
               status=ClaimStatus.ACCEPTED, created_by_activity="act.batch2.interpret")
    s.add_entity(it3)

    # graduate linear-equations KC from PROPOSED
    kc_lin = s.entities["kc.linear_equations_one_var"]
    kc_lin.status = ClaimStatus.ACCEPTED
    kc_lin.reviewed_by_activity = "act.batch2.review"
    kc_lin.review_rationale = "Accepted via batch_002 TM + reviewed claims."

    def claim(cid, pred, subj, obj, ctype, bases, purpose=None, scope=None,
              scope_ref=None, origin=None, qualifiers=None, rationale=""):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, purpose=purpose, scope=scope, scope_ref=scope_ref,
                  origin=origin, qualifiers=qualifiers or {},
                  created_by_activity="act.batch2.interpret",
                  created_at="2026-10-03T02:10:00Z", cdg_version="v0.2.0")
        c.status = ClaimStatus.PROPOSED
        c = _accept_batch2(c, rationale, bases)
        s.add_claim(c)
        return c

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    claim("cl.tm4.target", RelationshipType.TARGETS, tm4.id, "kc.linear_equations_one_var",
          ClaimType.ASSESSMENT_DESIGN, ASSESS, rationale="TM4 targets linear equations in one variable.")
    claim("cl.tm4.m1", RelationshipType.HAS_METHOD, tm4.id, m_inv.id,
          ClaimType.ASSESSMENT_DESIGN, ASSESS, rationale="Method ownership.")
    claim("cl.tm4.m2", RelationshipType.HAS_METHOD, tm4.id, m_exp.id,
          ClaimType.ASSESSMENT_DESIGN, ASSESS, rationale="Method ownership.")
    for cid, m, kc in [
        ("cl.req.inv_alg", m_inv, "kc.algebraic_expressions"),
        ("cl.req.inv_int", m_inv, "kc.integer_arithmetic"),
        ("cl.req.exp_alg", m_exp, "kc.algebraic_expressions"),
        ("cl.req.exp_int", m_exp, "kc.integer_arithmetic"),
    ]:
        claim(cid, RelationshipType.REQUIRES, m.id, kc, ClaimType.DEPENDENCY, DEP,
              rationale=f"{m.id} requires {kc}.")

    claim("cl.pre.alg_linear", RelationshipType.PREREQUISITE, "kc.algebraic_expressions",
          "kc.linear_equations_one_var", ClaimType.DEPENDENCY, DEP,
          purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
          scope_ref=tm4.id, origin=ClaimOrigin.DERIVED,
          rationale="DERIVED: every method of tm4 requires algebraic expressions.")
    claim("cl.pre.int_linear", RelationshipType.PREREQUISITE, "kc.integer_arithmetic",
          "kc.linear_equations_one_var", ClaimType.DEPENDENCY, DEP,
          purpose=PrerequisitePurpose.EXECUTE, scope=PrerequisiteScope.SPECIFIC_TASK_MODEL,
          scope_ref=tm4.id, origin=ClaimOrigin.DERIVED,
          rationale="DERIVED: every method of tm4 requires integer arithmetic.")

    def ev(eid, cid, source, legacy, excerpt, direct):
        s.add_evidence(EvidenceItem(
            id=eid, claim_id=cid, source_id=source,
            role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
            stance=EvidenceStance.SUPPORTS, locator="legacy excerpt", excerpt=excerpt,
            excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
            extracted_by_activity="act.batch2.interpret", inherited_from_legacy=True,
            legacy_id=legacy))

    ev("ev.b2.t", "cl.tm4.target", "SRC.WAEC.WASSCE.MATH.SYL", "E0084",
       "Linear equations listed before 'Change of subject of a formula/relation'.", True)
    ev("ev.b2.m1", "cl.tm4.m1", "SRC.OSX.IA2E.6.5", "E0124", "Solve: 5y - 3 = 0.", False)
    ev("ev.b2.m2", "cl.tm4.m2", "SRC.OSX.IA2E.5.4", "E0089",
       "Combine like terms: 8a^2 + 12a + 1 + 3a^2 - 5a + 4.", False)
    ev("ev.b2.r1", "cl.req.inv_alg", "SRC.OSX.IA2E.5.4", "E0089",
       "Combine like terms.", False)
    ev("ev.b2.r2", "cl.req.inv_int", "SRC.OSX.IA2E.6.5", "E0124", "Solve: 5y - 3 = 0.", False)
    ev("ev.b2.r3", "cl.req.exp_alg", "SRC.OSX.IA2E.5.4", "E0089", "Combine like terms.", False)
    ev("ev.b2.r4", "cl.req.exp_int", "SRC.OSX.IA2E.6.5", "E0124", "Solve: 5y - 3 = 0.", False)
    ev("ev.b2.p1", "cl.pre.alg_linear", "SRC.OSX.IA2E.5.4", "E0089",
       "Combining like terms precedes equation solving.", False)
    ev("ev.b2.p2", "cl.pre.int_linear", "SRC.OSX.IA2E.6.5", "E0124",
       "Solving linear equations requires integer arithmetic.", False)

    return s


if __name__ == "__main__":
    pass
