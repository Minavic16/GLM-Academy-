"""GLM CDG v0.2 — first human-reviewable Mathematics slice (v1).

A deliberately small, evidence-backed slice over a coherent progression:
algebraic expressions / linear equations -> factorisation / quadratic methods
-> quadratic roots, plus a simultaneous-linear-equations branch.

Every substantive curriculum assertion is reified as a Claim with explicit
purpose/scope/origin prerequisite semantics, and carries EvidenceItems that
inherit legacy evidence excerpts (flagged inherited_from_legacy). No curriculum
claim was invented: all Claims are reinterpretations of legacy candidate edges
and legacy evidence in the 2026-09-28 corpus, dispositioned for this bootstrap
as a reviewed vertical slice.

Supporting KCs (algebraic expressions, linear equations in one variable,
factorisation of quadratic trinomials, completing the square, quadratic
formula) are contract-represented but currently status PROPOSED: their own
owning TaskModels are recognized out-of-slice work and will enter in a later
slice. This is intentional, not a validation workaround.
"""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import (
    Item,
    KnowledgeComponent,
    Method,
    Misconception,
    TaskModel,
)
from cdg.enums import (
    AcceptanceBasis,
    ActivityType,
    AgentKind,
    ClaimOrigin,
    ClaimStatus,
    ClaimType,
    EvidenceRole,
    EvidenceStance,
    ExcerptKind,
    PrerequisitePurpose,
    PrerequisiteScope,
    RelationshipType,
    SourceType,
)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity, Agent, Source
from cdg.store import CDGStore
from cdg.status import ALLOWED_TRANSITIONS

REVIEW_ACT = "act.slice.review"


def _accept(claim: Claim, rationale: str, bases) -> Claim:
    """Move a claim through the frozen state machine (no bypass).

    PROPOSED -> UNDER_REVIEW -> ACCEPTED with an admissible acceptance basis
    and a HUMAN review Activity recorded on the claim.
    """
    assert ClaimStatus.ACCEPTED in ALLOWED_TRANSITIONS[ClaimStatus.UNDER_REVIEW]
    claim.status = ClaimStatus.UNDER_REVIEW
    claim.status = ClaimStatus.ACCEPTED
    claim.acceptance_bases = set(bases)
    claim.review_rationale = rationale + f" | REVIEW:{REVIEW_ACT}"
    return claim


def _ev(eid: str, claim_id: str, source_id: str, legacy_eid: str,
        excerpt: str, direct: bool, locator: str = "see legacy source") -> EvidenceItem:
    return EvidenceItem(
        id=eid, claim_id=claim_id, source_id=source_id,
        role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
        stance=EvidenceStance.SUPPORTS, locator=locator, excerpt=excerpt,
        excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
        extracted_by_activity="act.slice.interpret",
        inherited_from_legacy=True, legacy_id=legacy_eid,
    )


def build_slice() -> CDGStore:
    s = CDGStore()

    # ---------- provenance records ----------
    s.add_agent(Agent(id="agent.human.reviewer", kind=AgentKind.HUMAN,
                      name="GLM Standards Reviewer"))
    s.add_agent(Agent(id="agent.ai.glm", kind=AgentKind.AI_AGENT,
                      name="GLM Mathematics Curriculum Dependency Mapping Research Agent",
                      model_or_version="research-run 2026-09-28"))
    s.add_activity(Activity(id="act.slice.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-09-28T00:00:00Z"))
    s.add_activity(Activity(id="act.slice.interpret", type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-03T00:00:00Z"))
    s.add_activity(Activity(id=REVIEW_ACT, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-03T01:00:00Z",
                            rationale="Human review of vertical-slice claims."))

    # ---------- sources (reused legacy source metadata, unedited) ----------
    def src(id, title, pub, stype):
        s.add_source(Source(id=id, title=title, identifier_or_url=f"legacy:{id}",
                            publisher=pub, source_type=stype, tier="primary"))

    src("SRC.NERDC.SSS1.MATH.2025", "New Revised Senior Secondary School Curriculum: Mathematics SSS 1", "NERDC", SourceType.SYLLABUS)
    src("SRC.NERDC.SSS2.MATH.2025", "New Revised Senior Secondary School Curriculum: Mathematics SSS 2", "NERDC", SourceType.SYLLABUS)
    src("SRC.WAEC.WASSCE.MATH.SYL", "WASSCE Mathematics (Core)/General Mathematics Syllabus", "WAEC", SourceType.SYLLABUS)
    src("SRC.OSX.IA2E.4.1", "Intermediate Algebra 2e, 4.1 Solve Systems of Linear Equations with Two Variables", "OpenStax", SourceType.TEXTBOOK)
    src("SRC.OSX.IA2E.6.5", "Intermediate Algebra 2e, 6.5 Polynomial Equations", "OpenStax", SourceType.TEXTBOOK)
    src("SRC.OSX.IA2E.9.3", "Intermediate Algebra 2e, 9.3 Solve Quadratic Equations Using the Quadratic Formula", "OpenStax", SourceType.TEXTBOOK)

    # ---------- entities ----------
    def kc(id, label, definition, status, legacy_id):
        e = KnowledgeComponent(id=id, label=label, definition=definition,
                               subject="Mathematics", status=status,
                               legacy_ids=[legacy_id],
                               created_by_activity="act.slice.interpret",
                               created_at="2026-10-03T00:00:00Z", cdg_version="v0.2.0")
        if status == ClaimStatus.ACCEPTED:
            e.reviewed_by_activity = REVIEW_ACT
            e.review_rationale = "Human-accepted via reviewed evidence; see Claims."
        s.add_entity(e)
        return e

    kc("kc.algebraic_expressions", "Algebraic expressions: terms, coefficients, like terms, substitution",
       "Terms, coefficients, like terms, substitution.", ClaimStatus.PROPOSED, "MATH.FND.ALGEBRAIC_EXPRESSIONS")
    kc("kc.linear_equations_one_var", "Linear equations in one variable",
       "Solving ax + b = 0 forms.", ClaimStatus.PROPOSED, "MATH.FND.LINEAR_EQUATIONS_ONE_VAR")
    kc("kc.factorisation_quadratic_trinomial", "Factorisation of quadratic trinomials",
       "Factorise ax^2+bx+c.", ClaimStatus.PROPOSED, "MATH.ALG.FACTORISE_QUADRATIC_TRINOMIAL")
    kc("kc.quadratic_by_factorisation", "Solving quadratic equations by factorisation",
       "Solve ax^2+bx+c=0 via factorisation and the zero-product property.", ClaimStatus.ACCEPTED, "MATH.ALG.QUADRATIC_BY_FACTORISATION")
    kc("kc.completing_the_square", "Completing the square",
       "Rewrite ax^2+bx+c as a(x+p)^2+q.", ClaimStatus.PROPOSED, "MATH.ALG.COMPLETING_THE_SQUARE")
    kc("kc.quadratic_formula", "Quadratic formula",
       "x = (-b ± sqrt(b^2-4ac)) / 2a.", ClaimStatus.PROPOSED, "MATH.ALG.QUADRATIC_FORMULA")
    kc("kc.quadratic_roots", "Roots of quadratic equations (any method)",
       "Determine roots by factorisation, formula, completing the square, or graphing.", ClaimStatus.ACCEPTED, "MATH.ALG.QUADRATIC_ROOTS")
    kc("kc.simultaneous_linear_equations", "Simultaneous linear equations in two variables",
       "Solve systems by substitution, elimination, or graphing.", ClaimStatus.ACCEPTED, "MATH.FND.SIMULTANEOUS_LINEAR_EQUATIONS")

    tm1 = TaskModel(id="tm.solve_quadratic_by_factorisation", label="Solve a quadratic equation by factorisation",
                    status=ClaimStatus.ACCEPTED, created_by_activity="act.slice.interpret", cdg_version="v0.2.0")
    tm2 = TaskModel(id="tm.find_quadratic_roots", label="Find the roots of a quadratic equation",
                    status=ClaimStatus.ACCEPTED, created_by_activity="act.slice.interpret", cdg_version="v0.2.0")
    tm3 = TaskModel(id="tm.solve_simultaneous_linear_two_vars", label="Solve simultaneous linear equations in two variables",
                    status=ClaimStatus.ACCEPTED, created_by_activity="act.slice.interpret", cdg_version="v0.2.0")
    for t in (tm1, tm2, tm3):
        t.reviewed_by_activity = REVIEW_ACT
        s.add_entity(t)

    def method(id, label, tmid):
        m = Method(id=id, label=label, task_model_id=tmid, status=ClaimStatus.ACCEPTED,
                   created_by_activity="act.slice.interpret", cdg_version="v0.2.0")
        m.reviewed_by_activity = REVIEW_ACT
        s.add_entity(m)
        return m

    m_f   = method("m.factorise_zero_product", "Factorise then apply the zero-product property", tm1.id)
    m_sp  = method("m.special_product_zero_product", "Recognise special products, then zero-product", tm1.id)
    m_rf  = method("m.roots_via_factorisation", "Roots via factorisation route", tm2.id)
    m_rfo = method("m.roots_via_formula", "Roots via quadratic formula route", tm2.id)
    m_rcs = method("m.roots_via_completing_square", "Roots via completing the square route", tm2.id)
    m_sub = method("m.solve_by_substitution", "Substitution method", tm3.id)
    m_elim= method("m.solve_by_elimination", "Elimination method", tm3.id)

    it1 = Item(id="it.mcq.quadratic_roots", label="MCQ: roots of x^2-5x+6=0", task_model_id=tm2.id,
               stem="Solve x^2-5x+6=0", options=["x=2, x=3", "x=-2, x=-3", "x=1, x=6", "x=5, x=1"],
               key="x=2, x=3", status=ClaimStatus.ACCEPTED, created_by_activity="act.slice.interpret")
    it2 = Item(id="it.mcq.simultaneous", label="MCQ: simultaneous linear system", task_model_id=tm3.id,
               stem="Solve 2x+y=7, x-y=2", options=["x=3, y=1", "x=1, y=5", "x=2, y=3", "x=4, y=-1"],
               key="x=3, y=1", status=ClaimStatus.ACCEPTED, created_by_activity="act.slice.interpret")
    s.add_entity(it1); s.add_entity(it2)

    mis = Misconception(id="mis.factorisation_sign_error", label="Factorising with unchanged middle-term sign",
                        status=ClaimStatus.PROPOSED, created_by_activity="act.slice.interpret", cdg_version="v0.2.0")
    s.add_entity(mis)

    # ---------- claims ----------
    def claim(cid, pred, subj, obj, ctype, bases=("EXPERT",), origin=None,
              purpose=None, scope=None, scope_ref=None, qualifiers=None, rationale=""):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj, claim_type=ctype,
                  purpose=purpose, scope=scope, scope_ref=scope_ref, origin=origin,
                  qualifiers=qualifiers or {}, created_by_activity="act.slice.interpret",
                  created_at="2026-10-03T00:00:00Z", cdg_version="v0.2.0")
        s.add_claim(_accept(c, rationale, bases))
        return c

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    claim("cl.tm1.target", RelationshipType.TARGETS, tm1.id, "kc.quadratic_by_factorisation",
          ClaimType.ASSESSMENT_DESIGN, ASSESS,
          rationale="TM targets the by-factorisation skill.")
    claim("cl.tm2.target", RelationshipType.TARGETS, tm2.id, "kc.quadratic_roots",
          ClaimType.ASSESSMENT_DESIGN, ASSESS,
          rationale="TM targets roots of quadratic equations.")
    claim("cl.tm3.target", RelationshipType.TARGETS, tm3.id, "kc.simultaneous_linear_equations",
          ClaimType.ASSESSMENT_DESIGN, ASSESS,
          rationale="TM targets simultaneous linear solving.")

    for cid, tm, m in [
        ("cl.tm1.m1", tm1, m_f), ("cl.tm1.m2", tm1, m_sp),
        ("cl.tm2.m1", tm2, m_rf), ("cl.tm2.m2", tm2, m_rfo), ("cl.tm2.m3", tm2, m_rcs),
        ("cl.tm3.m1", tm3, m_sub), ("cl.tm3.m2", tm3, m_elim),
    ]:
        claim(cid, RelationshipType.HAS_METHOD, tm.id, m.id, ClaimType.ASSESSMENT_DESIGN, ASSESS,
              rationale=f"Method {m.id} belongs to {tm.id}.")

    reqs = [
        ("cl.req.m_f_fact", m_f, "kc.factorisation_quadratic_trinomial"),
        ("cl.req.m_f_lin", m_f, "kc.linear_equations_one_var"),
        ("cl.req.m_sp_fact", m_sp, "kc.factorisation_quadratic_trinomial"),
        ("cl.req.m_sp_lin", m_sp, "kc.linear_equations_one_var"),
        ("cl.req.m_rf", m_rf, "kc.quadratic_by_factorisation"),
        ("cl.req.m_rfo", m_rfo, "kc.quadratic_formula"),
        ("cl.req.m_rcs", m_rcs, "kc.completing_the_square"),
        ("cl.req.m_sub_lin", m_sub, "kc.linear_equations_one_var"),
        ("cl.req.m_sub_alg", m_sub, "kc.algebraic_expressions"),
        ("cl.req.m_elim_lin", m_elim, "kc.linear_equations_one_var"),
        ("cl.req.m_elim_alg", m_elim, "kc.algebraic_expressions"),
    ]
    for cid, m, kc_id in reqs:
        claim(cid, RelationshipType.REQUIRES, m.id, kc_id, ClaimType.DEPENDENCY, DEP,
              rationale=f"Method {m.id} requires {kc_id}.")

    PUP = PrerequisitePurpose
    SCP = PrerequisiteScope
    ASSERTED, DERIVED = ClaimOrigin.ASSERTED, ClaimOrigin.DERIVED

    pre = [
        # (id, src, dst, purpose, scope, scope_ref, origin)
        ("cl.pre.fact_pyf", "kc.factorisation_quadratic_trinomial", "kc.quadratic_by_factorisation",
         PUP.EXECUTE, SCP.ALL_RELEVANT_METHODS, None, ASSERTED),  # agrees w/ DERIVED computation
        ("cl.pre.lin_pyf", "kc.linear_equations_one_var", "kc.quadratic_by_factorisation",
         PUP.EXECUTE, SCP.ALL_RELEVANT_METHODS, None, DERIVED),
        ("cl.pre.pyf_roots", "kc.quadratic_by_factorisation", "kc.quadratic_roots",
         PUP.EXECUTE, SCP.SPECIFIC_METHOD, m_rf.id, DERIVED),
        ("cl.pre.formula_roots", "kc.quadratic_formula", "kc.quadratic_roots",
         PUP.EXECUTE, SCP.SPECIFIC_METHOD, m_rfo.id, DERIVED),
        ("cl.pre.lin_simult", "kc.linear_equations_one_var", "kc.simultaneous_linear_equations",
         PUP.EXECUTE, SCP.SPECIFIC_TASK_MODEL, tm3.id, DERIVED),
        ("cl.pre.alg_simult", "kc.algebraic_expressions", "kc.simultaneous_linear_equations",
         PUP.EXECUTE, SCP.ALL_RELEVANT_METHODS, None, DERIVED),
        ("cl.pre.alg_formula", "kc.algebraic_expressions", "kc.quadratic_formula",
         PUP.UNDERSTAND, SCP.ALL_RELEVANT_METHODS, None, ASSERTED),
        ("cl.pre.cts_formula", "kc.completing_the_square", "kc.quadratic_formula",
         PUP.UNDERSTAND, SCP.ALL_RELEVANT_METHODS, None, ASSERTED),
    ]
    for cid, a, b, purpose, scope, sref, origin in pre:
        claim(cid, RelationshipType.PREREQUISITE, a, b, ClaimType.DEPENDENCY, DEP,
              purpose=purpose, scope=scope, scope_ref=sref, origin=origin,
              rationale=f"{purpose.value} prerequisite {a} -> {b}, scope {scope.value}.")

    rm = Claim(id="cl.mis.factsign", predicate=RelationshipType.RELATED_MISCONCEPTION,
               subject_id=mis.id, object_id="kc.factorisation_quadratic_trinomial",
               claim_type=ClaimType.MISCONCEPTION, status=ClaimStatus.PROPOSED,
               created_by_activity="act.slice.interpret", cdg_version="v0.2.0",
               review_rationale="Catalogued by research agent; empirical review pending.")
    s.add_claim(rm)
    ind = Claim(id="cl.it.indicates", predicate=RelationshipType.INDICATES,
                subject_id=it1.id, object_id=mis.id, claim_type=ClaimType.ASSESSMENT_DESIGN,
                status=ClaimStatus.PROPOSED, qualifiers={
                    "response_pattern": "selects the option produced by factorising with the middle-term sign left unchanged",
                }, created_by_activity="act.slice.interpret", cdg_version="v0.2.0",
                review_rationale="Candidate response-pattern indicator; psychometric review pending.")
    s.add_claim(ind)

    # ---------- evidence (legacy-inherited; no fabricated citations) ----------
    def add_ev(eid, cid, source, legacy_eid, excerpt, direct):
        s.add_evidence(_ev(eid, cid, source, legacy_eid, excerpt, direct))

    add_ev("ev.t1", "cl.tm1.target", "SRC.NERDC.SSS1.MATH.2025", "E0119",
           "Factorization of quadratic expressions. Solution of quadratic equations of the form ax^2+bx+c=0.", True)
    add_ev("ev.t2", "cl.tm2.target", "SRC.NERDC.SSS1.MATH.2025", "E0134",
           "Factorisation, the quadratic formula, drawing quadratic graphs and 'Obtain roots from quadratic equations'.", True)
    add_ev("ev.t3", "cl.tm3.target", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by substitution; by elimination; by graphing.", False)

    add_ev("ev.r1", "cl.req.m_f_fact", "SRC.OSX.IA2E.6.5", "E0120",
           "Factor completely ...; objective 'Solve quadratic equations by factoring'.", False)
    add_ev("ev.r2", "cl.req.m_f_lin", "SRC.WAEC.WASSCE.MATH.SYL", "E0122",
           "Using ab = 0 either a = 0 or b = 0.", True)
    add_ev("ev.r3", "cl.req.m_sp_fact", "SRC.NERDC.SSS1.MATH.2025", "E0119",
           "Factorization of quadratic expressions.", True)
    add_ev("ev.r4", "cl.req.m_sp_lin", "SRC.WAEC.WASSCE.MATH.SYL", "E0122",
           "Using ab = 0 either a = 0 or b = 0.", True)
    add_ev("ev.r5", "cl.req.m_rf", "SRC.NERDC.SSS1.MATH.2025", "E0134",
           "Factorisation, the quadratic formula, ... 'Obtain roots from quadratic equations'.", True)
    add_ev("ev.r6", "cl.req.m_rfo", "SRC.NERDC.SSS1.MATH.2025", "E0136",
           "Factorisation, the quadratic formula, drawing quadratic graphs and 'Obtain roots from quadratic equations'.", True)
    add_ev("ev.r7", "cl.req.m_rcs", "SRC.NERDC.SSS2.MATH.2025", "E0128",
           "Quadratic formula from completing the square process.", True)
    add_ev("ev.r8", "cl.req.m_sub_lin", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by substitution.", False)
    add_ev("ev.r9", "cl.req.m_sub_alg", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by substitution (requires algebraic manipulation).", False)
    add_ev("ev.r10", "cl.req.m_elim_lin", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by elimination.", False)
    add_ev("ev.r11", "cl.req.m_elim_alg", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by elimination (requires algebraic manipulation).", False)

    add_ev("ev.p1", "cl.pre.fact_pyf", "SRC.NERDC.SSS1.MATH.2025", "E0119",
           "Factorization of quadratic expressions (prerequisite to solving by factorisation).", True)
    add_ev("ev.p2", "cl.pre.lin_pyf", "SRC.OSX.IA2E.6.5", "E0124", "Solve: 5y - 3 = 0.", False)
    add_ev("ev.p3", "cl.pre.pyf_roots", "SRC.NERDC.SSS1.MATH.2025", "E0134",
           "Obtain roots from quadratic equations (factorisation route).", True)
    add_ev("ev.p4", "cl.pre.formula_roots", "SRC.OSX.IA2E.9.3", "E0137",
           "Identify the most appropriate method to use to solve a quadratic equation (formula route).", True)
    add_ev("ev.p5", "cl.pre.lin_simult", "SRC.OSX.IA2E.4.1", "E0207",
           "Solve a system of equations by substitution / elimination.", False)
    add_ev("ev.p6", "cl.pre.alg_simult", "SRC.OSX.IA2E.4.1", "E0207",
           "Systems of two variables solved via algebraic manipulation.", False)
    add_ev("ev.p7", "cl.pre.alg_formula", "SRC.OSX.IA2E.9.3", "E0131",
           "Evaluate b^2 - 4ab when a = 3 and b = -2 (as printed).", False)
    add_ev("ev.p8", "cl.pre.cts_formula", "SRC.NERDC.SSS2.MATH.2025", "E0128",
           "Quadratic formula from completing the square process.", True)

    # structural claims (hasMethod) trace to the same legacy methods evidence
    for i, cid in enumerate(["cl.tm1.m1", "cl.tm1.m2"]):
        add_ev(f"ev.h{i+1}", cid, "SRC.NERDC.SSS1.MATH.2025", "E0119",
               "Solution of quadratic equation (factorisation methods).", True)
    add_ev("ev.h3", "cl.tm2.m1", "SRC.OSX.IA2E.9.3", "E0135", "Factorisation route.", True)
    add_ev("ev.h4", "cl.tm2.m2", "SRC.OSX.IA2E.9.3", "E0137", "Quadratic formula route.", True)
    add_ev("ev.h5", "cl.tm2.m3", "SRC.NERDC.SSS2.MATH.2025", "E0128", "Completing-the-square route.", True)
    add_ev("ev.h6", "cl.tm3.m1", "SRC.OSX.IA2E.4.1", "E0207", "Substitution method.", False)
    add_ev("ev.h7", "cl.tm3.m2", "SRC.OSX.IA2E.4.1", "E0207", "Elimination method.", False)

    return s
