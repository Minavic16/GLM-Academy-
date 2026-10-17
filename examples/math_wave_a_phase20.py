"""Phase 20 Mathematics implementation wave (owner-authorized, batches 070-079).

Implements the ten authorized topics as canonical CDG records, controlled by
the official JAMB UTME Mathematics E-syllabus (SRC.JAMB.UTME.MATH.2025 —
IBASS static asset; SHA-256 aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f;
locators "JAMB Math p.N" = extracted-text page N of that exact revision):

- 070 Number bases            I.1(a-b)  (JAMB Math p.2)
- 071 Modular arithmetic      I.1(c)    (JAMB Math p.2)
- 072 Laws of indices         I.3(a)    (JAMB Math p.2)
- 073 Surds                   I.3(h)    (JAMB Math p.2)
- 074 Approximation & errors  I.2(b-d)  (JAMB Math p.2)
- 075 Standard form           I.3(c)    (JAMB Math p.2)
- 076 Log change of base      I.3(e-f)  (JAMB Math p.2; extends b055 TM)
- 077 Financial mathematics   I.2(e,f,h)(JAMB Math p.2)
- 078 Change of subject depth II.1(a)   (JAMB Math p.2; extends b009 TM)
- 079 Factorisation extensions II.1(c)  (JAMB Math p.2 content; p.3 objective iv)

Provenance discipline (Phase 18/19 rules preserved):
- All new/modified claims are Phase 20 records; no historical claim, evidence
  or review rationale is rewritten or backdated. The matrices family keeps its
  secondary (Syllabus NG) implementation evidence (b068, untouched). The
  existing change-of-subject (b009), index-equation (b008) and logarithms
  (b055) records remain as accepted; Phase 20 only ADDS methods/claims.
- The ten topics are official JAMB requirements; the JAMB source record is
  registered in the canonical store for the first time here as the controlling
  evidence for the new claims.
- Disclosed boundaries (see PHASE20_REPORT.md): modular division/inverses
  beyond the UTME treatment are not implemented; absolute/relative error and
  bounds are not JAMB I.2 requirements and are not implemented; compound
  interest, depreciation and discount are not in JAMB I.2 and are not
  implemented; cubic factorisation, factor/remainder theorems and polynomial
  division remain open (M-23).

Chains build_graph_v40. No schema change; 13 entity types preserved; no
Biology/English artifacts; `indicates` untouched (PROPOSED). All new claims
ACCEPTED with HUMAN review; prerequisite claims carry purpose/scope/origin
qualifiers per the frozen CDG v0.2 contract.
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
    SourceType,
)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples._batchkit import accept
from examples.math_scope_expansion import build_graph_v40

SUBJ = "Mathematics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-17T10:10:00Z"
E = PrerequisitePurpose.EXECUTE
U = PrerequisitePurpose.UNDERSTAND
P_ALL = PrerequisiteScope.ALL_RELEVANT_METHODS
P_M = PrerequisiteScope.SPECIFIC_METHOD
P_TM = PrerequisiteScope.SPECIFIC_TASK_MODEL
JAMB = "SRC.JAMB.UTME.MATH.2025"


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.m{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-17T10:00:00Z"))
    interp = f"act.m{nn}.interpret"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-17T10:10:00Z"))
    rev = f"act.m{nn}.review"
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-17T11:00:00Z",
                            rationale=note))
    return interp, rev


def _src_jamb(s):
    """Register the official JAMB Mathematics E-syllabus PDF (Phase 18 asset)."""
    if JAMB not in s.sources:
        s.add_source(Source(
            id=JAMB,
            title="UTME Syllabus — Mathematics (JAMB IBASS e-syllabus PDF)",
            identifier_or_url=("https://ibass.jamb.gov.ng/static/media/"
                               "Mathematics.c0621f4b8b674e75fd05.pdf"),
            publisher="JAMB (Joint Admissions and Matriculation Board)",
            source_type=SourceType.SYLLABUS, tier="primary",
            edition_or_version=("IBASS e-syllabus PDF; no cycle year printed; "
                                "PDF metadata 2025-07-31"),
            retrieved_at="2026-10-17",
            content_hash=("sha256:aff7a7c2cc46036902dda38db1d1567d10982de709305"
                          "cfbfc90dc437329754f")))


def _kc(s, interp, rev, kid, label, definition, note_suffix=""):
    k = KnowledgeComponent(id=kid, label=label, definition=definition, subject=SUBJ,
                           status=ClaimStatus.ACCEPTED,
                           created_by_activity=interp, cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = ("Accepted in Phase 20 via human review."
                          " Controlling evidence: official JAMB UTME Mathematics "
                          "E-syllabus (SRC.JAMB.UTME.MATH.2025)." + note_suffix)
    s.add_entity(k)
    return k


def _tm(s, interp, rev, tid, label):
    t = TaskModel(id=tid, label=label, subject=SUBJ,
                  status=ClaimStatus.ACCEPTED,
                  created_by_activity=interp, cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    return t


def _method(s, interp, rev, mid, tmid, label):
    m = Method(id=mid, label=label, task_model_id=tmid, subject=SUBJ,
               status=ClaimStatus.ACCEPTED,
               created_by_activity=interp, cdg_version="v0.2.0")
    m.reviewed_by_activity = rev
    s.add_entity(m)
    return m


def _item(s, interp, rev, iid, tm_id, stem, options, key):
    it = Item(id=iid, stem=stem, options=options, key=key, task_model_id=tm_id,
              subject=SUBJ, status=ClaimStatus.ACCEPTED,
              created_by_activity=interp, cdg_version="v0.2.0")
    it.reviewed_by_activity = rev
    s.add_entity(it)
    return it


def _claim(s, interp, rev, cid, pred, subj, obj, ctype, rationale, bases,
           purpose=None, scope=None, origin=None, scope_ref=None):
    c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
              claim_type=ctype,
              purpose=purpose, scope=scope, origin=origin, scope_ref=scope_ref,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, rationale, bases, rev))


def _ev(s, interp, eid, claim_id, locator, text):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=claim_id, source_id=JAMB,
        role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS,
        locator=locator, excerpt=text, excerpt_kind=ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def _pfx(nn):
    return f"cl.m{nn}"


def _targets(s, interp, rev, nn, tm_id, kc_id, rat):
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.{tm_id}",
           RelationshipType.TARGETS, tm_id, kc_id,
           ClaimType.ASSESSMENT_DESIGN, rat, ASSESS)


def _m_claims(s, interp, rev, nn, tm_id, mid, mlab, req_ids):
    m = _method(s, interp, rev, mid, tm_id, mlab)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.{tm_id}.{mid}",
           RelationshipType.HAS_METHOD, tm_id, mid,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    for r in req_ids:
        _claim(s, interp, rev, f"{_pfx(nn)}.req.{mid}.{r}",
               RelationshipType.REQUIRES, mid, r,
               ClaimType.DEPENDENCY, f"{mid} requires {r}", DEP)
    return m


def _pre(s, interp, rev, cid, prereq_kc, dependent_kc, purpose, scope,
         scope_ref, origin, rationale):
    _claim(s, interp, rev, cid, RelationshipType.PREREQUISITE,
           prereq_kc, dependent_kc, ClaimType.DEPENDENCY, rationale, DEP,
           purpose=purpose, scope=scope, scope_ref=scope_ref, origin=origin)


def build_graph_v41() -> CDGStore:
    s = build_graph_v40()

    # Official controlling source for this wave (first canonical registration).
    _src_jamb(s)

    # =====================================================================
    # Batch 070 — Number bases (JAMB I.1 a-b; objectives i-ii; JAMB Math p.2)
    # =====================================================================
    nn = "70"
    interp, rev = _base(s, nn, "Human review of number bases batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.number_bases",
             "Number bases: conversion and operations (bases 2 to 10)",
             "Convert numbers from one base to another, including fractional "
             "parts; perform the four basic operations (+, -, x, division) in "
             "bases 2 to 10.",
             " JAMB locator: I.1(a-b), JAMB Math p.2.")
    t = _tm(s, interp, rev, "tm.number_base_problems",
            "Convert and operate in number bases")
    _targets(s, interp, rev, nn, t.id, kc.id, "targets number bases capability")
    _m_claims(s, interp, rev, nn, t.id, "m.convert_number_base",
              "Convert between bases by place-value expansion and repeated "
              "division, including fractional parts",
              ["kc.number_bases", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.base_arithmetic",
              "Perform addition, subtraction, multiplication and division in "
              "bases 2 to 10",
              ["kc.number_bases", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m70.pre.kc.number_bases",
         "kc.integer_arithmetic", "kc.number_bases", E, P_TM,
         "tm.number_base_problems", ClaimOrigin.DERIVED,
         "EXECUTE: both methods require integer arithmetic "
         "(all-methods derived).")
    _item(s, interp, rev, "it.math.number_base_convert", t.id,
          "Convert 121 (base 3) to base 10.",
          ["16", "15", "13", "12"], "16")
    _item(s, interp, rev, "it.math.number_base_add", t.id,
          "Evaluate 1101 + 111 in base 2, leaving the answer in base 2.",
          ["10100", "10010", "10110", "11000"], "10100")
    _ev(s, interp, "ev.m70.target", f"{_pfx(nn)}.targets.tm.number_base_problems",
        "JAMB Math p.2 (I.1a-b; objectives i-ii)",
        "Number bases: operations in different number bases from 2 to 10; "
        "conversion from one base to another including fractional parts.")
    _ev(s, interp, "ev.m70.conv", f"{_pfx(nn)}.req.m.convert_number_base.kc.number_bases",
        "JAMB Math p.2 (I.1b; objective ii)",
        "Convert one base to another, including fractional parts (I.1b).")
    _ev(s, interp, "ev.m70.ops", f"{_pfx(nn)}.req.m.base_arithmetic.kc.number_bases",
        "JAMB Math p.2 (I.1a; objective i)",
        "Perform four basic operations (x, +, -, division) in different number "
        "bases from 2 to 10 (I.1a).")
    _ev(s, interp, "ev.m70.pre", "cl.m70.pre.kc.number_bases",
        "JAMB Math p.2 (I.1a-b) — pedagogical inference",
        "Base conversion and base arithmetic exercise integer operations.")

    # =====================================================================
    # Batch 071 — Modular arithmetic (JAMB I.1 c; objective iii; p.2)
    # =====================================================================
    nn = "71"
    interp, rev = _base(s, nn, "Human review of modular arithmetic batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.modular_arithmetic",
             "Modular arithmetic: residues and operations",
             "Express numbers in modulo notation and find residues; perform "
             "addition, subtraction and multiplication in modulo arithmetic.",
             " JAMB locator: I.1(c), JAMB Math p.2.")
    t = _tm(s, interp, rev, "tm.modular_arithmetic_problems",
            "Perform calculations in modular arithmetic")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets modular arithmetic capability")
    _m_claims(s, interp, rev, nn, t.id, "m.mod_notation_residue",
              "Express congruences in modulo notation and find residues",
              ["kc.modular_arithmetic", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.mod_operations",
              "Add, subtract and multiply in modulo arithmetic",
              ["kc.modular_arithmetic", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m71.pre.kc.modular_arithmetic",
         "kc.integer_arithmetic", "kc.modular_arithmetic", E, P_TM,
         "tm.modular_arithmetic_problems", ClaimOrigin.DERIVED,
         "EXECUTE: residue and modulo operations build on integer division "
         "with remainders (all-methods derived).")
    _item(s, interp, rev, "it.math.modular", t.id,
          "Find the value of (17 x 14) mod 5.",
          ["3", "2", "1", "4"], "3")
    _ev(s, interp, "ev.m71.target", f"{_pfx(nn)}.targets.tm.modular_arithmetic_problems",
        "JAMB Math p.2 (I.1c; objective iii)",
        "Modular arithmetic (I.1c): perform operations in modulo arithmetic.")
    _ev(s, interp, "ev.m71.res", f"{_pfx(nn)}.req.m.mod_notation_residue.kc.modular_arithmetic",
        "JAMB Math p.2 (I.1c)",
        "Modular arithmetic (I.1c): residues of numbers in a given modulus.")
    _ev(s, interp, "ev.m71.ops", f"{_pfx(nn)}.req.m.mod_operations.kc.modular_arithmetic",
        "JAMB Math p.2 (I.1c; objective iii)",
        "Perform operations in modulo arithmetic (objective iii).")
    _ev(s, interp, "ev.m71.pre", "cl.m71.pre.kc.modular_arithmetic",
        "JAMB Math p.2 (I.1c) — pedagogical inference",
        "Modulo arithmetic builds on integer arithmetic (division with "
        "remainders).")

    # =====================================================================
    # Batch 072 — Laws of indices (JAMB I.3 a; objective i; p.2)
    # =====================================================================
    nn = "72"
    interp, rev = _base(s, nn, "Human review of laws of indices batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.indices_laws",
             "Laws of indices: simplification and evaluation",
             "Apply the product, quotient and power laws to simplify and "
             "evaluate index expressions, including zero, negative and "
             "fractional indices.",
             " JAMB locator: I.3(a), JAMB Math p.2.")
    t = _tm(s, interp, rev, "tm.index_law_simplification",
            "Simplify and evaluate expressions using index laws")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets index-law simplification capability")
    _m_claims(s, interp, rev, nn, t.id, "m.apply_index_laws",
              "Apply product, quotient and power laws to simplify index "
              "expressions",
              ["kc.indices_laws", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.evaluate_fractional_powers",
              "Evaluate zero, negative and fractional indices",
              ["kc.indices_laws", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m72.pre.kc.indices_laws",
         "kc.integer_arithmetic", "kc.indices_laws", E, P_TM,
         "tm.index_law_simplification", ClaimOrigin.DERIVED,
         "EXECUTE: index evaluation exercises integer arithmetic "
         "(all-methods derived).")
    _pre(s, interp, rev, "cl.m72.pre.kc.equations_in_indices",
         "kc.indices_laws", "kc.equations_in_indices", E, P_ALL, None,
         ClaimOrigin.ASSERTED,
         "EXECUTE: solving equations involving indices applies the laws of "
         "indices; JAMB lists I.3(a) laws of indices before I.3(b) equations "
         "involving indices.")
    _item(s, interp, rev, "it.math.index_laws", t.id,
          "Evaluate 16^(1/2) + 27^(1/3).",
          ["7", "10", "5", "43"], "7")
    _ev(s, interp, "ev.m72.target", f"{_pfx(nn)}.targets.tm.index_law_simplification",
        "JAMB Math p.2 (I.3a; objective i)",
        "Laws of indices (I.3a): apply the laws of indices in calculation "
        "(objective i).")
    _ev(s, interp, "ev.m72.laws", f"{_pfx(nn)}.req.m.apply_index_laws.kc.indices_laws",
        "JAMB Math p.2 (I.3a; objective i)",
        "Apply the laws of indices in calculation (objective i).")
    _ev(s, interp, "ev.m72.frac", f"{_pfx(nn)}.req.m.evaluate_fractional_powers.kc.indices_laws",
        "JAMB Math p.2 (I.3a)",
        "Laws of indices (I.3a): evaluation of powers, including zero, "
        "negative and fractional indices.")
    _ev(s, interp, "ev.m72.eq", "cl.m72.pre.kc.equations_in_indices",
        "JAMB Math p.2 (I.3a-b) — ordering",
        "Equations involving indices (I.3b) follow the laws of indices (I.3a) "
        "in the syllabus; solving index equations applies index laws.")
    _ev(s, interp, "ev.m72.pre", "cl.m72.pre.kc.indices_laws",
        "JAMB Math p.2 (I.3a) — pedagogical inference",
        "Index evaluation exercises integer arithmetic.")

    # =====================================================================
    # Batch 073 — Surds (JAMB I.3 h; objectives v-vi; p.2)
    # =====================================================================
    nn = "73"
    interp, rev = _base(s, nn, "Human review of surds batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.surds",
             "Surds: simplification, operations and rationalisation",
             "Simplify surds by extracting square factors; perform basic "
             "operations on surd expressions; rationalise denominators "
             "involving surds.",
             " JAMB locator: I.3(h), JAMB Math p.2.")
    t = _tm(s, interp, rev, "tm.surd_problems",
            "Simplify surds and rationalise denominators")
    _targets(s, interp, rev, nn, t.id, kc.id, "targets surds capability")
    _m_claims(s, interp, rev, nn, t.id, "m.simplify_surds",
              "Simplify surds by extracting perfect-square factors",
              ["kc.surds", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.surd_operations",
              "Perform basic operations on surd expressions",
              ["kc.surds", "kc.algebraic_expressions", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.rationalise_denominator",
              "Rationalise a denominator of the form a x sqrt(b)",
              ["kc.surds", "kc.algebraic_expressions", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m73.pre.kc.surds.alg",
         "kc.algebraic_expressions", "kc.surds", E, P_TM,
         "tm.surd_problems", ClaimOrigin.DERIVED,
         "EXECUTE: surd operations and rationalisation are algebraic "
         "manipulations (all-methods derived).")
    _pre(s, interp, rev, "cl.m73.pre.kc.surds.int",
         "kc.integer_arithmetic", "kc.surds", E, P_TM,
         "tm.surd_problems", ClaimOrigin.DERIVED,
         "EXECUTE: extracting square factors and rationalising denominators "
         "exercise integer arithmetic (all-methods derived).")
    _pre(s, interp, rev, "cl.m73.pre.kc.surds.idx",
         "kc.indices_laws", "kc.surds", U, P_ALL, None,
         ClaimOrigin.ASSERTED,
         "UNDERSTAND: roots and fractional indices connect to surd "
         "simplification; JAMB groups Indices, Logarithms and Surds as one "
         "topic (I.3) — adjacency elaboration.")
    _item(s, interp, rev, "it.math.surd_simplify", t.id,
          "Simplify sqrt(50).",
          ["5 sqrt(2)", "2 sqrt(5)", "25 sqrt(2)", "10 sqrt(5)"], "5 sqrt(2)")
    _item(s, interp, rev, "it.math.surd_rationalise", t.id,
          "Rationalise 6 / sqrt(3).",
          ["2 sqrt(3)", "6 sqrt(3)", "3 sqrt(2)", "sqrt(3) / 2"], "2 sqrt(3)")
    _ev(s, interp, "ev.m73.target", f"{_pfx(nn)}.targets.tm.surd_problems",
        "JAMB Math p.2 (I.3h; objectives v-vi)",
        "Surds (I.3h): simplify and rationalise surds; perform basic "
        "operations on surds.")
    _ev(s, interp, "ev.m73.simpl", f"{_pfx(nn)}.req.m.simplify_surds.kc.surds",
        "JAMB Math p.2 (objective v)",
        "Simplify surds (objective v).")
    _ev(s, interp, "ev.m73.ops", f"{_pfx(nn)}.req.m.surd_operations.kc.surds",
        "JAMB Math p.2 (objective vi)",
        "Perform basic operations on surds (objective vi).")
    _ev(s, interp, "ev.m73.rat", f"{_pfx(nn)}.req.m.rationalise_denominator.kc.surds",
        "JAMB Math p.2 (objective v)",
        "Rationalise surds (objective v).")
    _ev(s, interp, "ev.m73.adj", "cl.m73.pre.kc.surds.idx",
        "JAMB Math p.2 (I.3 topic grouping) — adjacency",
        "Indices, Logarithms and Surds form one syllabus topic (I.3); roots "
        "and fractional indices connect to surd simplification.")
    _ev(s, interp, "ev.m73.pre", "cl.m73.pre.kc.surds.alg",
        "JAMB Math p.2 (I.3h) — pedagogical inference",
        "Surd simplification and rationalisation are algebraic manipulations.")

    # =====================================================================
    # Batch 074 — Approximation and errors (I.2 b-d; objectives ii-iii; p.2)
    # =====================================================================
    nn = "74"
    interp, rev = _base(s, nn, "Human review of approximation and errors batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.approximation_errors",
             "Approximation: significant figures, decimal places and percentage error",
             "Express numbers to a specified number of significant figures or "
             "decimal places; compute the percentage error of a measured value.",
             " JAMB locator: I.2(b-d), JAMB Math p.2. Absolute/relative error "
             "and bounds are not JAMB I.2 requirements and are not covered.")
    t = _tm(s, interp, rev, "tm.approximation_problems",
            "Approximate numbers and compute percentage error")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets approximation and error capability")
    _m_claims(s, interp, rev, nn, t.id, "m.round_to_precision",
              "Round numbers to a specified number of significant figures or "
              "decimal places",
              ["kc.approximation_errors", "kc.fraction_decimal_operations"])
    _m_claims(s, interp, rev, nn, t.id, "m.percentage_error",
              "Compute percentage error from the error and the true value",
              ["kc.approximation_errors", "kc.percentage_concept"])
    _pre(s, interp, rev, "cl.m74.pre.kc.approximation_errors.frac",
         "kc.fraction_decimal_operations", "kc.approximation_errors", E, P_M,
         "m.round_to_precision", ClaimOrigin.DERIVED,
         "EXECUTE: rounding decimals exercises fraction/decimal place-value "
         "operations (method-scoped).")
    _pre(s, interp, rev, "cl.m74.pre.kc.approximation_errors.pct",
         "kc.percentage_concept", "kc.approximation_errors", E, P_M,
         "m.percentage_error", ClaimOrigin.DERIVED,
         "EXECUTE: percentage error is computed with percentages "
         "(method-scoped).")
    _item(s, interp, rev, "it.math.rounding", t.id,
          "Express 0.0045678 correct to 3 significant figures.",
          ["0.00457", "0.004568", "0.00456", "0.457"], "0.00457")
    _item(s, interp, rev, "it.math.percent_error", t.id,
          "The measured length of a rope is 9.6 m while its true length is "
          "10.0 m. Find the percentage error.",
          ["4%", "0.4%", "40%", "4.17%"], "4%")
    _ev(s, interp, "ev.m74.target", f"{_pfx(nn)}.targets.tm.approximation_problems",
        "JAMB Math p.2 (I.2b-d)",
        "Significant figures; decimal places; percentage errors (I.2b-d).")
    _ev(s, interp, "ev.m74.round", f"{_pfx(nn)}.req.m.round_to_precision.kc.approximation_errors",
        "JAMB Math p.2 (objective ii)",
        "Express to specified number of significant figures and decimal "
        "places (objective ii).")
    _ev(s, interp, "ev.m74.pct", f"{_pfx(nn)}.req.m.percentage_error.kc.approximation_errors",
        "JAMB Math p.2 (objective iii)",
        "Calculate percentage error (objective iii).")
    _ev(s, interp, "ev.m74.pref", "cl.m74.pre.kc.approximation_errors.frac",
        "JAMB Math p.2 (I.2a-c) — pedagogical inference",
        "Rounding decimals exercises fraction/decimal place-value operations.")
    _ev(s, interp, "ev.m74.ppct", "cl.m74.pre.kc.approximation_errors.pct",
        "JAMB Math p.2 (I.2d; objective iii) — pedagogical inference",
        "Percentage error is computed with percentages.")

    # =====================================================================
    # Batch 075 — Standard form (JAMB I.3 c; p.2)
    # =====================================================================
    nn = "75"
    interp, rev = _base(s, nn, "Human review of standard form batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.standard_form",
             "Standard form: A x 10^n notation and calculations",
             "Write numbers in standard form with positive and negative "
             "indices; multiply and divide numbers expressed in standard form "
             "using index laws.",
             " JAMB locator: I.3(c), JAMB Math p.2 (content column; no "
             "objective names standard form explicitly).")
    t = _tm(s, interp, rev, "tm.standard_form_problems",
            "Convert to standard form and compute with standard-form numbers")
    _targets(s, interp, rev, nn, t.id, kc.id, "targets standard form capability")
    _m_claims(s, interp, rev, nn, t.id, "m.write_standard_form",
              "Write numbers as A x 10^n with 1 <= A < 10",
              ["kc.standard_form", "kc.indices_laws"])
    _m_claims(s, interp, rev, nn, t.id, "m.standard_form_arithmetic",
              "Multiply and divide numbers in standard form using index laws",
              ["kc.standard_form", "kc.indices_laws"])
    _pre(s, interp, rev, "cl.m75.pre.kc.standard_form",
         "kc.indices_laws", "kc.standard_form", E, P_TM,
         "tm.standard_form_problems", ClaimOrigin.DERIVED,
         "EXECUTE: standard form is powers-of-ten notation evaluated with "
         "index laws (all-methods derived).")
    _item(s, interp, rev, "it.math.standard_form", t.id,
          "Express 0.0000456 in standard form.",
          ["4.56 x 10^-5", "4.56 x 10^5", "45.6 x 10^-6", "0.456 x 10^-4"],
          "4.56 x 10^-5")
    _item(s, interp, rev, "it.math.standard_form_ops", t.id,
          "Evaluate (2 x 10^3) x (3 x 10^4), leaving the answer in standard form.",
          ["6 x 10^7", "6 x 10^12", "5 x 10^7", "6 x 10^1"], "6 x 10^7")
    _ev(s, interp, "ev.m75.target", f"{_pfx(nn)}.targets.tm.standard_form_problems",
        "JAMB Math p.2 (I.3c)",
        "Standard form (I.3c).")
    _ev(s, interp, "ev.m75.write", f"{_pfx(nn)}.req.m.write_standard_form.kc.standard_form",
        "JAMB Math p.2 (I.3c)",
        "Standard form (I.3c): numbers written as A x 10^n.")
    _ev(s, interp, "ev.m75.ops", f"{_pfx(nn)}.req.m.standard_form_arithmetic.kc.standard_form",
        "JAMB Math p.2 (I.3c; objective i)",
        "Apply the laws of indices in calculation (objective i) — "
        "standard-form products and quotients use index laws.")
    _ev(s, interp, "ev.m75.pre", "cl.m75.pre.kc.standard_form",
        "JAMB Math p.2 (I.3a, I.3c) — adjacency",
        "JAMB I.3 lists laws of indices and standard form under one topic; "
        "standard form is evaluated with index laws.")

    # =====================================================================
    # Batch 076 — Logarithms: change of base (I.3 e-f; objective iv; p.2)
    # Extends the existing b055 tm.logarithm_problems (records untouched).
    # =====================================================================
    nn = "76"
    interp, rev = _base(s, nn, "Human review of log change-of-base batch (Phase 20).")

    _m_claims(s, interp, rev, nn, "tm.logarithm_problems", "m.change_of_base",
              "Express a logarithm in a new base and evaluate logarithms to a "
              "given base",
              ["kc.logarithms", "kc.indices_laws", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.m76.pre.kc.logarithms",
         "kc.indices_laws", "kc.logarithms", E, P_M, "m.change_of_base",
         ClaimOrigin.DERIVED,
         "EXECUTE: the change-of-base method requires index laws "
         "(method-scoped).")
    _item(s, interp, rev, "it.mcq.log_change_base", "tm.logarithm_problems",
          "Given log10(2) = 0.3010, find log2(10) correct to 2 decimal places.",
          ["3.32", "0.30", "2.32", "1.00"], "3.32")
    _ev(s, interp, "ev.m76.cob",
        f"{_pfx(nn)}.own.tm.logarithm_problems.m.change_of_base",
        "JAMB Math p.2 (I.3e-f; objective iv)",
        "Logarithm of any positive number to a given base (I.3e); change of "
        "bases in logarithm and application (I.3f); solve problems in "
        "different bases in logarithms (objective iv).")
    _ev(s, interp, "ev.m76.req",
        f"{_pfx(nn)}.req.m.change_of_base.kc.indices_laws",
        "JAMB Math p.2 (I.3a, I.3d-f)",
        "Change of base applies index and logarithm laws.")
    _ev(s, interp, "ev.m76.pre", "cl.m76.pre.kc.logarithms",
        "JAMB Math p.2 (I.3a, I.3f) — derived",
        "DERIVED: the change-of-base method requires index laws.")

    # =====================================================================
    # Batch 077 — Financial mathematics (I.2 e, f, h; objectives iii-iv; p.2)
    # =====================================================================
    nn = "77"
    interp, rev = _base(s, nn, "Human review of financial mathematics batch (Phase 20).")

    # --- kc.simple_interest ---
    kc_si = _kc(s, interp, rev, "kc.simple_interest", "Simple interest",
                "Compute simple interest and amount using I = PRT/100; find "
                "principal, rate or time by rearranging the formula.",
                " JAMB locator: I.2(e), JAMB Math p.2.")
    t_si = _tm(s, interp, rev, "tm.simple_interest_problems",
               "Solve simple interest problems")
    _targets(s, interp, rev, nn, t_si.id, kc_si.id,
             "targets simple interest capability")
    _m_claims(s, interp, rev, nn, t_si.id, "m.simple_interest_formula",
              "Apply I = PRT/100 and rearrange for principal, rate or time",
              ["kc.simple_interest", "kc.percentage_concept"])
    _pre(s, interp, rev, "cl.m77.pre.kc.simple_interest",
         "kc.percentage_concept", "kc.simple_interest", E, P_TM,
         "tm.simple_interest_problems", ClaimOrigin.DERIVED,
         "EXECUTE: simple-interest rates are percentages "
         "(all-methods derived).")
    _item(s, interp, rev, "it.math.simple_interest", t_si.id,
          "Find the simple interest on N25,000 for 3 years at 4% per annum.",
          ["N3,000", "N1,000", "N30,000", "N750"], "N3,000")
    _ev(s, interp, "ev.m77.si.target", f"{_pfx(nn)}.targets.tm.simple_interest_problems",
        "JAMB Math p.2 (I.2e; objective iii)",
        "Simple interest (I.2e); calculate simple interest (objective iii).")
    _ev(s, interp, "ev.m77.si.depth", f"{_pfx(nn)}.req.m.simple_interest_formula.kc.simple_interest",
        "JAMB Math p.2 (objective iii)",
        "Calculate simple interest, profit and loss per cent (objective iii).")
    _ev(s, interp, "ev.m77.si.pre", "cl.m77.pre.kc.simple_interest",
        "JAMB Math p.2 (I.2d-e) — pedagogical inference",
        "Simple interest rates are percentages.")

    # --- kc.profit_and_loss ---
    kc_pl = _kc(s, interp, rev, "kc.profit_and_loss", "Profit and loss per cent",
                "Compute profit or loss and express it as a percentage of the "
                "cost price; find cost or selling price given a percentage.",
                " JAMB locator: I.2(f), JAMB Math p.2.")
    t_pl = _tm(s, interp, rev, "tm.profit_loss_problems",
               "Solve profit and loss per cent problems")
    _targets(s, interp, rev, nn, t_pl.id, kc_pl.id,
             "targets profit and loss capability")
    _m_claims(s, interp, rev, nn, t_pl.id, "m.profit_loss_percent",
              "Compute profit or loss per cent from cost and selling price",
              ["kc.profit_and_loss", "kc.percentage_concept"])
    _pre(s, interp, rev, "cl.m77.pre.kc.profit_and_loss",
         "kc.percentage_concept", "kc.profit_and_loss", E, P_TM,
         "tm.profit_loss_problems", ClaimOrigin.DERIVED,
         "EXECUTE: profit/loss per cent is expressed with percentages "
         "(all-methods derived).")
    _item(s, interp, rev, "it.math.profit_loss", t_pl.id,
          "An article bought for N500 is sold for N650. Find the profit per cent.",
          ["30%", "23%", "15%", "150%"], "30%")
    _ev(s, interp, "ev.m77.pl.target", f"{_pfx(nn)}.targets.tm.profit_loss_problems",
        "JAMB Math p.2 (I.2f; objective iii)",
        "Profit and loss percent (I.2f); calculate profit and loss per cent "
        "(objective iii).")
    _ev(s, interp, "ev.m77.pl.depth", f"{_pfx(nn)}.req.m.profit_loss_percent.kc.profit_and_loss",
        "JAMB Math p.2 (objective iii)",
        "Calculate profit and loss per cent (objective iii).")
    _ev(s, interp, "ev.m77.pl.pre", "cl.m77.pre.kc.profit_and_loss",
        "JAMB Math p.2 (I.2d, I.2f) — pedagogical inference",
        "Profit and loss per cent is computed with percentages.")

    # --- kc.shares_and_vat ---
    kc_sv = _kc(s, interp, rev, "kc.shares_and_vat",
                "Shares and value added tax (VAT)",
                "Divide amounts into shares in a given ratio; compute VAT on "
                "goods and services and prices including VAT.",
                " JAMB locator: I.2(h), JAMB Math p.2.")
    t_sv = _tm(s, interp, rev, "tm.shares_vat_problems",
               "Solve shares and VAT problems")
    _targets(s, interp, rev, nn, t_sv.id, kc_sv.id,
             "targets shares and VAT capability")
    _m_claims(s, interp, rev, nn, t_sv.id, "m.share_division",
              "Divide an amount into shares in a given ratio",
              ["kc.shares_and_vat", "kc.ratio_proportion_rate"])
    _m_claims(s, interp, rev, nn, t_sv.id, "m.vat_calculation",
              "Compute VAT at a given rate and prices including VAT",
              ["kc.shares_and_vat", "kc.percentage_concept"])
    _pre(s, interp, rev, "cl.m77.pre.kc.shares_and_vat.ratio",
         "kc.ratio_proportion_rate", "kc.shares_and_vat", E, P_M,
         "m.share_division", ClaimOrigin.DERIVED,
         "EXECUTE: share division uses ratio and proportion reasoning "
         "(method-scoped).")
    _pre(s, interp, rev, "cl.m77.pre.kc.shares_and_vat.pct",
         "kc.percentage_concept", "kc.shares_and_vat", E, P_M,
         "m.vat_calculation", ClaimOrigin.DERIVED,
         "EXECUTE: VAT is computed as a percentage (method-scoped).")
    _item(s, interp, rev, "it.math.shares", t_sv.id,
          "A sum of N60,000 is shared between two people in the ratio 2:3. "
          "Find the larger share.",
          ["N36,000", "N24,000", "N30,000", "N40,000"], "N36,000")
    _item(s, interp, rev, "it.math.vat", t_sv.id,
          "A trader sells goods for N8,000 and charges VAT at 7.5%. Find the "
          "total amount paid.",
          ["N8,600", "N8,075", "N9,600", "N6,000"], "N8,600")
    _ev(s, interp, "ev.m77.sv.target", f"{_pfx(nn)}.targets.tm.shares_vat_problems",
        "JAMB Math p.2 (I.2h; objective iv)",
        "Shares and valued added tax (VAT) (I.2h); solve problems involving "
        "share and VAT (objective iv).")
    _ev(s, interp, "ev.m77.sv.share", f"{_pfx(nn)}.req.m.share_division.kc.shares_and_vat",
        "JAMB Math p.2 (objective iv)",
        "Solve problems involving share (objective iv).")
    _ev(s, interp, "ev.m77.sv.vat", f"{_pfx(nn)}.req.m.vat_calculation.kc.shares_and_vat",
        "JAMB Math p.2 (objective iv)",
        "Solve problems involving VAT (objective iv).")
    _ev(s, interp, "ev.m77.sv.pre.ratio", "cl.m77.pre.kc.shares_and_vat.ratio",
        "JAMB Math p.2 (I.2g-h) — pedagogical inference",
        "Sharing amounts in a given ratio uses ratio and proportion.")
    _ev(s, interp, "ev.m77.sv.pre.pct", "cl.m77.pre.kc.shares_and_vat.pct",
        "JAMB Math p.2 (I.2d, I.2h) — pedagogical inference",
        "VAT is computed as a percentage of value.")

    # =====================================================================
    # Batch 078 — Change of subject: powers and roots (II.1 a; obj. i; p.2)
    # Extends the existing b009 tm.make_subject (records untouched).
    # =====================================================================
    nn = "78"
    interp, rev = _base(s, nn, "Human review of change-of-subject depth batch (Phase 20).")

    _m_claims(s, interp, rev, nn, "tm.make_subject", "m.subject_powers_roots",
              "Isolate the subject when it is raised to a power or lies under "
              "a root",
              ["kc.algebraic_expressions", "kc.integer_arithmetic"])
    _item(s, interp, rev, "it.mcq.subject_power", "tm.make_subject",
          "Make r the subject of A = pi r^2.",
          ["r = sqrt(A/pi)", "r = sqrt(A)/pi", "r = A/(2 pi)", "r = A/pi^2"],
          "r = sqrt(A/pi)")
    _ev(s, interp, "ev.m78.cob",
        f"{_pfx(nn)}.own.tm.make_subject.m.subject_powers_roots",
        "JAMB Math p.2 (II.1a; objective i)",
        "Change of subject of formula (II.1a); find the subject of the "
        "formula of a given equation (objective i).")
    _ev(s, interp, "ev.m78.req.alg",
        f"{_pfx(nn)}.req.m.subject_powers_roots.kc.algebraic_expressions",
        "JAMB Math p.2 (II.1a) — pedagogical inference",
        "Rearranging formulas with powers and roots requires algebraic "
        "manipulation.")
    _ev(s, interp, "ev.m78.req.int",
        f"{_pfx(nn)}.req.m.subject_powers_roots.kc.integer_arithmetic",
        "JAMB Math p.2 (II.1a) — pedagogical inference",
        "Power/root inversion exercises signed-number arithmetic.")

    # =====================================================================
    # Batch 079 — Factorisation: common factors and difference of squares
    # (II.1 c; objective iv; JAMB Math p.2 content, p.3 objective)
    # =====================================================================
    nn = "79"
    interp, rev = _base(s, nn, "Human review of factorisation extensions batch (Phase 20).")

    kc = _kc(s, interp, rev, "kc.factorisation_patterns",
             "Factorisation: common factors and difference of two squares",
             "Extract the highest common factor from algebraic expressions; "
             "factorise the difference of two squares.",
             " JAMB locator: II.1(c), JAMB Math p.2 (content); objective iv, "
             "p.3. Cubic factorisation and the factor/remainder theorems "
             "remain open (M-23).")
    t = _tm(s, interp, rev, "tm.factorise_common_patterns",
            "Factorise by common factors and difference of two squares")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets common-factor and difference-of-squares factorisation")
    _m_claims(s, interp, rev, nn, t.id, "m.common_factor_extraction",
              "Extract the highest common factor of the terms",
              ["kc.factorisation_patterns", "kc.algebraic_expressions",
               "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.difference_of_two_squares",
              "Factorise a^2 - b^2 as (a - b)(a + b)",
              ["kc.factorisation_patterns", "kc.algebraic_expressions",
               "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m79.pre.kc.factorisation_patterns.alg",
         "kc.algebraic_expressions", "kc.factorisation_patterns", E, P_TM,
         "tm.factorise_common_patterns", ClaimOrigin.DERIVED,
         "EXECUTE: factorisation requires manipulation of algebraic "
         "expressions (all-methods derived).")
    _pre(s, interp, rev, "cl.m79.pre.kc.factorisation_patterns.int",
         "kc.integer_arithmetic", "kc.factorisation_patterns", E, P_TM,
         "tm.factorise_common_patterns", ClaimOrigin.DERIVED,
         "EXECUTE: finding common factors and spotting squares exercises "
         "integer arithmetic (all-methods derived).")
    _item(s, interp, rev, "it.math.common_factor", t.id,
          "Factorise completely: 6x^2 + 9x.",
          ["3x(2x + 3)", "3(2x^2 + 3x)", "x(6x + 9)", "3x(2x + 9)"],
          "3x(2x + 3)")
    _item(s, interp, rev, "it.math.difference_squares", t.id,
          "Factorise completely: 4x^2 - 25.",
          ["(2x - 5)(2x + 5)", "(2x - 5)^2", "(4x - 5)(x + 5)", "(2x + 5)^2"],
          "(2x - 5)(2x + 5)")
    _ev(s, interp, "ev.m79.target", f"{_pfx(nn)}.targets.tm.factorise_common_patterns",
        "JAMB Math p.2 (II.1c); p.3 (objective iv)",
        "Factorization of polynomials of degree not exceeding 3 (II.1c); "
        "factorize by regrouping, difference of two squares, perfect squares "
        "and cubic expressions (objective iv).")
    _ev(s, interp, "ev.m79.cf", f"{_pfx(nn)}.req.m.common_factor_extraction.kc.factorisation_patterns",
        "JAMB Math p.3 (objective iv)",
        "Factorize by regrouping (objective iv) — common-factor extraction "
        "underpins regrouping.")
    _ev(s, interp, "ev.m79.dots", f"{_pfx(nn)}.req.m.difference_of_two_squares.kc.factorisation_patterns",
        "JAMB Math p.3 (objective iv)",
        "Factorize by difference of two squares (objective iv).")
    _ev(s, interp, "ev.m79.pre", "cl.m79.pre.kc.factorisation_patterns.alg",
        "JAMB Math p.2 (II.1c) — pedagogical inference",
        "Factorisation requires manipulation of algebraic expressions.")

    return s
