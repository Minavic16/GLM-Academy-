"""Phase 17 Mathematics scope expansion: batches 066-069.

Implements the four owner-authorized Mathematics topic families:
- 066 Sets and logic
- 067 Sequences and series
- 068 Matrices and determinants
- 069 Mensuration

Chains build_graph_v39 (Phase 15/16 state). No schema change; 13 entity types
preserved; no Biology/English artifacts; `indicates` untouched (PROPOSED).

Evidence: NERDC Senior Secondary School Curriculum — Mathematics SSS 1 / SSS 2
(© October 2025, retrieved and text-extracted Phase 16) for sets, logic,
sequences & series, and mensuration. Matrices & determinants appear in NERDC
SSS1/SSS2 topic lists only via secondary JAMB/WAEC evidence (Syllabus NG);
this is disclosed per batch and the subject remains BOARD_UNVERIFIED.

All new claims ACCEPTED with HUMAN review; prerequisite claims carry
purpose/scope/origin qualifiers per the frozen CDG v0.2 contract.
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
from examples.chemistry_organic_reactions import build_graph_v39

SUBJ = "Mathematics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-17T09:00:00Z"
E = PrerequisitePurpose.EXECUTE
U = PrerequisitePurpose.UNDERSTAND
P_ALL = PrerequisiteScope.ALL_RELEVANT_METHODS


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.m{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-17T08:00:00Z"))
    interp = f"act.m{nn}.interpret"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-17T08:10:00Z"))
    rev = f"act.m{nn}.review"
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-17T09:00:00Z",
                            rationale=note))
    return interp, rev


def _src(s, sid, title, url, publisher, tier="reference"):
    if sid not in s.sources:
        s.add_source(Source(id=sid, title=title, identifier_or_url=url,
                            publisher=publisher, source_type=SourceType.TEXTBOOK,
                            tier=tier))


def _kc(s, interp, rev, kid, label, definition, note_suffix=""):
    k = KnowledgeComponent(id=kid, label=label, definition=definition, subject=SUBJ,
                           status=ClaimStatus.ACCEPTED,
                           created_by_activity=interp, cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = ("Accepted in Phase 17 via human review." + note_suffix)
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


def _ev(s, interp, eid, claim_id, source_id, locator, text):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=claim_id, source_id=source_id,
        role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS,
        locator=locator, excerpt=text, excerpt_kind=ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def _pfx(nn):
    return f"cl.m{nn}"


def build_graph_v40() -> CDGStore:
    s = build_graph_v39()

    # Register secondary sources used only for the matrices family (disclosed below).
    _src(s, "SRC.SYLLABUSNG.JAMB.MATH",
         "Syllabus NG — JAMB UTME Mathematics Syllabus",
         "https://syllabus.ng/jamb/math/",
         "Syllabus NG (secondary aggregator)", tier="reference")
    _src(s, "SRC.SYLLABUSNG.WAEC.MATH",
         "Syllabus NG — WAEC WASSCE Mathematics Syllabus",
         "https://syllabus.ng/waec/math/",
         "Syllabus NG (secondary aggregator)", tier="reference")

    # =====================================================================
    # Batch 066 — Sets and logic (NERDC Math SSS1 pp. 7–8; SSS2 p.9 duplicate)
    # =====================================================================
    nn = "66"
    interp, rev = _base(s, nn, "Human review of sets and logic batch.")

    # --- kc.sets_operations (foundational; no prerequisite) ---
    k_sets = _kc(
        s, interp, rev,
        "kc.sets_operations", "Set theory: definitions, notation and operations",
        "Define a set; identify set notations (roster/rule/set-builder); "
        "distinguish types of sets (empty, subset, infinite, universal); "
        "perform set operations (union, intersection, complement); apply sets "
        "to daily-life problems.",
        " Evidence: NERDC Math SSS1 p.7 (official).")
    t_sets = _tm(s, interp, rev, "tm.set_operations", "Work with sets and set operations")
    m_set_notation = _method(s, interp, rev, "m.set_notation",
                             "tm.set_operations",
                             "Identify set notation and types of sets")
    m_set_ops = _method(s, interp, rev, "m.set_operations", "tm.set_operations",
                        "Perform union, intersection and complement operations")
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.tm.set_operations",
           RelationshipType.TARGETS, "tm.set_operations", "kc.sets_operations",
           ClaimType.ASSESSMENT_DESIGN, "targets set theory capability", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.set_operations.m.set_notation",
           RelationshipType.HAS_METHOD, "tm.set_operations", m_set_notation.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.set_operations.m.set_operations",
           RelationshipType.HAS_METHOD, "tm.set_operations", m_set_ops.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.set_notation",
           RelationshipType.REQUIRES, m_set_notation.id, "kc.sets_operations",
           ClaimType.DEPENDENCY, "notation requires sets KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.set_operations",
           RelationshipType.REQUIRES, m_set_ops.id, "kc.sets_operations",
           ClaimType.DEPENDENCY, "operations require sets KC", DEP)
    _item(s, interp, rev, "it.math.sets_basic", "tm.set_operations",
          "Given A = {1, 2, 3} and B = {2, 3, 4}, find A u B.",
          ["{1, 2, 3, 4}", "{2, 3}", "{1, 4}", "{5}"], "{1, 2, 3, 4}")
    _ev(s, interp, f"ev.m{nn}.sets.target", f"{_pfx(nn)}.targets.tm.set_operations",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.7",
        "Define a set; identify set notations (listing, rule, set-builder).")
    _ev(s, interp, f"ev.m{nn}.sets.types", f"{_pfx(nn)}.req.m.set_notation",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.7",
        "Types of sets: empty set, subset, infinite sets, universal sets.")
    _ev(s, interp, f"ev.m{nn}.sets.ops", f"{_pfx(nn)}.req.m.set_operations",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.7",
        "Set operations: union, intersection and complement.")

    # --- kc.logical_reasoning (UNDERSTAND -> sets, curriculum adjacency) ---
    k_logic = _kc(
        s, interp, rev,
        "kc.logical_reasoning", "Logical statements and truth values",
        "Form simple and compound statements; identify logical operators and "
        "symbols (negation, conjunction, disjunction, implication, "
        "bi-implication); determine truth values of compound statements.",
        " Evidence: NERDC Math SSS1 p.8 / SSS2 p.9 (official). "
        "Prerequisite link to sets is curriculum-adjacency elaboration, not "
        "source-mandated.")
    t_logic = _tm(s, interp, rev, "tm.logical_reasoning",
                  "Evaluate simple and compound logical statements")
    m_logic_statements = _method(s, interp, rev, "m.logic_statements",
                                 "tm.logical_reasoning",
                                 "Form and classify simple and compound statements")
    m_logic_truth = _method(s, interp, rev, "m.logic_truth_values", "tm.logical_reasoning",
                            "Determine truth values using logical operators")
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.tm.logical_reasoning",
           RelationshipType.TARGETS, "tm.logical_reasoning", "kc.logical_reasoning",
           ClaimType.ASSESSMENT_DESIGN, "targets logic capability", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.logical_reasoning.m.logic_statements",
           RelationshipType.HAS_METHOD, "tm.logical_reasoning", m_logic_statements.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.logical_reasoning.m.logic_truth_values",
           RelationshipType.HAS_METHOD, "tm.logical_reasoning", m_logic_truth.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.logic_statements",
           RelationshipType.REQUIRES, m_logic_statements.id, "kc.logical_reasoning",
           ClaimType.DEPENDENCY, "statements require logic KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.logic_truth_values",
           RelationshipType.REQUIRES, m_logic_truth.id, "kc.logical_reasoning",
           ClaimType.DEPENDENCY, "truth values require logic KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.pre.kc.logical_reasoning",
           RelationshipType.PREREQUISITE, "kc.sets_operations", "kc.logical_reasoning",
           ClaimType.DEPENDENCY,
           "UNDERSTAND: logic and sets are adjacent Algebraic-Processes topics "
           "(curriculum-adjacency elaboration)", DEP,
           purpose=U, scope=P_ALL, origin=ClaimOrigin.ASSERTED)
    _item(s, interp, rev, "it.math.logic_truth", "tm.logical_reasoning",
          "If p is true and q is false, what is the truth value of p and q?",
          ["True", "False", "Undefined", "Both"], "False")
    _ev(s, interp, f"ev.m{nn}.logic.target", f"{_pfx(nn)}.targets.tm.logical_reasoning",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.8",
        "Form simple and compound statements; identify logical operators and symbols.")
    _ev(s, interp, f"ev.m{nn}.logic.truth", f"{_pfx(nn)}.req.m.logic_truth_values",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.8",
        "Determine the truth value of compound statements (negation, conjunction, disjunction).")

    # =====================================================================
    # Batch 067 — Sequences and series (NERDC Math SSS2 p.1)
    # =====================================================================
    nn = "67"
    interp, rev = _base(s, nn, "Human review of sequences and series batch.")

    k_seq = _kc(
        s, interp, rev,
        "kc.sequences_series", "Arithmetic and geometric progressions",
        "Describe types of sequences and series; solve problems involving "
        "arithmetic progressions (first term, common difference, nth term, "
        "arithmetic mean) and geometric progressions (first term, common "
        "ratio, nth term, geometric mean); solve real-life problems involving "
        "A.P. and G.P.",
        " Evidence: NERDC Math SSS2 p.1 (official).")
    t_seq = _tm(s, interp, rev, "tm.sequences_series", "Solve sequence and series problems")
    m_apgp_nth = _method(s, interp, rev, "m.ap_gp_nth_term", "tm.sequences_series",
                         "Find nth term of A.P. and G.P.")
    m_apgp_prob = _method(s, interp, rev, "m.ap_gp_problems", "tm.sequences_series",
                          "Solve A.P./G.P. problems including real-life applications")
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.tm.sequences_series",
           RelationshipType.TARGETS, "tm.sequences_series", "kc.sequences_series",
           ClaimType.ASSESSMENT_DESIGN, "targets sequences and series capability", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.sequences_series.m.ap_gp_nth_term",
           RelationshipType.HAS_METHOD, "tm.sequences_series", m_apgp_nth.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.sequences_series.m.ap_gp_problems",
           RelationshipType.HAS_METHOD, "tm.sequences_series", m_apgp_prob.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.ap_gp_nth_term",
           RelationshipType.REQUIRES, m_apgp_nth.id, "kc.sequences_series",
           ClaimType.DEPENDENCY, "nth term requires sequences KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.ap_gp_problems",
           RelationshipType.REQUIRES, m_apgp_prob.id, "kc.sequences_series",
           ClaimType.DEPENDENCY, "applications require sequences KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.pre.kc.sequences_series",
           RelationshipType.PREREQUISITE, "kc.integer_arithmetic", "kc.sequences_series",
           ClaimType.DEPENDENCY,
           "UNDERSTAND: number-pattern work builds on integer arithmetic "
           "(curriculum-adjacency elaboration)", DEP,
           purpose=U, scope=P_ALL, origin=ClaimOrigin.ASSERTED)
    _item(s, interp, rev, "it.math.ap_gp", "tm.sequences_series",
          "Find the 5th term of the A.P. 3, 7, 11, ...",
          ["15", "17", "19", "21"], "19")
    _ev(s, interp, f"ev.m{nn}.seq.target", f"{_pfx(nn)}.targets.tm.sequences_series",
        "SRC.NERDC.SSS2.MATH.2025", "NERDC Math SSS2 p.1",
        "Describe types of sequences and series; solve problems involving "
        "arithmetic and geometric progressions.")
    _ev(s, interp, f"ev.m{nn}.seq.ap", f"{_pfx(nn)}.req.m.ap_gp_nth_term",
        "SRC.NERDC.SSS2.MATH.2025", "NERDC Math SSS2 p.1",
        "Calculation of first term, common difference, nth term and arithmetic mean of A.P.")
    _ev(s, interp, f"ev.m{nn}.seq.gp", f"{_pfx(nn)}.req.m.ap_gp_problems",
        "SRC.NERDC.SSS2.MATH.2025", "NERDC Math SSS2 p.1",
        "Calculation of first term, common ratio, nth term and geometric mean of G.P.")

    # =====================================================================
    # Batch 068 — Matrices and determinants (SECONDARY evidence only)
    # NOTE: not present in NERDC SSS1/SSS2 topic lists; JAMB/WAEC evidence via
    # Syllabus NG (secondary aggregator). Disclosed below; subject stays
    # BOARD_UNVERIFIED.
    # =====================================================================
    nn = "68"
    interp, rev = _base(s, nn, "Human review of matrices and determinants batch.")

    k_mat = _kc(
        s, interp, rev,
        "kc.matrix_algebra", "Matrices and determinants",
        "Use matrix notation, dimensions and equality; perform matrix "
        "operations (addition, subtraction, scalar multiplication, "
        "multiplication); compute determinants (up to 3 x 3) and inverses "
        "(2 x 2); solve simultaneous equations using matrices.",
        " Evidence: JAMB SN6 / WAEC topic 11 via Syllabus NG (secondary "
        "aggregator). NOT present in NERDC Math SSS1/SSS2 topic lists "
        "(SSS3 unretrieved) — secondary evidence only, disclosed; official "
        "verification remains BOARD_UNVERIFIED.")
    t_mat = _tm(s, interp, rev, "tm.matrix_algebra", "Work with matrices and determinants")
    m_mat_ops = _method(s, interp, rev, "m.matrix_operations", "tm.matrix_algebra",
                        "Perform matrix addition, subtraction, scalar and matrix multiplication")
    m_mat_det = _method(s, interp, rev, "m.determinants_inverses", "tm.matrix_algebra",
                        "Compute determinants and 2 x 2 inverses; solve simultaneous equations using matrices")
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.tm.matrix_algebra",
           RelationshipType.TARGETS, "tm.matrix_algebra", "kc.matrix_algebra",
           ClaimType.ASSESSMENT_DESIGN, "targets matrix algebra capability", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.matrix_algebra.m.matrix_operations",
           RelationshipType.HAS_METHOD, "tm.matrix_algebra", m_mat_ops.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.matrix_algebra.m.determinants_inverses",
           RelationshipType.HAS_METHOD, "tm.matrix_algebra", m_mat_det.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.matrix_operations",
           RelationshipType.REQUIRES, m_mat_ops.id, "kc.matrix_algebra",
           ClaimType.DEPENDENCY, "operations require matrices KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.determinants_inverses",
           RelationshipType.REQUIRES, m_mat_det.id, "kc.matrix_algebra",
           ClaimType.DEPENDENCY, "determinants require matrices KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.pre.kc.matrix_algebra",
           RelationshipType.PREREQUISITE, "kc.linear_equations_one_var", "kc.matrix_algebra",
           ClaimType.DEPENDENCY,
           "UNDERSTAND: solving simultaneous equations via matrices builds on "
           "linear-equation reasoning (curriculum-adjacency elaboration)", DEP,
           purpose=U, scope=P_ALL, origin=ClaimOrigin.ASSERTED)
    _item(s, interp, rev, "it.math.matrix", "tm.matrix_algebra",
          "For M = [[1, 2], [3, 4]], the determinant is:",
          ["-2", "2", "10", "5"], "-2")
    _ev(s, interp, f"ev.m{nn}.mat.target", f"{_pfx(nn)}.targets.tm.matrix_algebra",
        "SRC.SYLLABUSNG.JAMB.MATH", "Syllabus NG JAMB SN6 (secondary)",
        "Algebra of matrices not exceeding 3 x 3; determinants up to 3 x 3; inverses of 2 x 2 matrices.")
    _ev(s, interp, f"ev.m{nn}.mat.det", f"{_pfx(nn)}.req.m.determinants_inverses",
        "SRC.SYLLABUSNG.WAEC.MATH", "Syllabus NG WAEC topic 11 (secondary)",
        "Determinant of a matrix; inverse of a 2 x 2 matrix.")

    # =====================================================================
    # Batch 069 — Mensuration (NERDC Math SSS1 p.11)
    # =====================================================================
    nn = "69"
    interp, rev = _base(s, nn, "Human review of mensuration batch.")

    k_mens = _kc(
        s, interp, rev,
        "kc.mensuration", "Mensuration: arcs, sectors, solids and compound shapes",
        "Find lengths of arcs and perimeters/areas of sectors and segments of "
        "circles; relate sector area to cone surface area; calculate surface "
        "areas and volumes of solid shapes (cube, cuboid, cylinder, cone, "
        "prism, pyramid); compute frustum of cone/pyramid and compound-shape "
        "surface areas and volumes.",
        " Evidence: NERDC Math SSS1 p.11 (official).")
    t_mens = _tm(s, interp, rev, "tm.mensuration", "Solve mensuration problems on circles and solids")
    m_mens_circle = _method(s, interp, rev, "m.circle_mensuration", "tm.mensuration",
                            "Find arc lengths and sector/segment areas of circles")
    m_mens_solid = _method(s, interp, rev, "m.solid_mensuration", "tm.mensuration",
                           "Find surface areas and volumes of solids, frustums and compound shapes")
    _claim(s, interp, rev, f"{_pfx(nn)}.targets.tm.mensuration",
           RelationshipType.TARGETS, "tm.mensuration", "kc.mensuration",
           ClaimType.ASSESSMENT_DESIGN, "targets mensuration capability", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.mensuration.m.circle_mensuration",
           RelationshipType.HAS_METHOD, "tm.mensuration", m_mens_circle.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.own.tm.mensuration.m.solid_mensuration",
           RelationshipType.HAS_METHOD, "tm.mensuration", m_mens_solid.id,
           ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.circle_mensuration",
           RelationshipType.REQUIRES, m_mens_circle.id, "kc.mensuration",
           ClaimType.DEPENDENCY, "circle mensuration requires mensuration KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.req.m.solid_mensuration",
           RelationshipType.REQUIRES, m_mens_solid.id, "kc.mensuration",
           ClaimType.DEPENDENCY, "solid mensuration requires mensuration KC", DEP)
    _claim(s, interp, rev, f"{_pfx(nn)}.pre.kc.mensuration",
           RelationshipType.PREREQUISITE, "kc.circle_angle_theorems", "kc.mensuration",
           ClaimType.DEPENDENCY,
           "UNDERSTAND: circle measurement (arcs, sectors) builds on circle "
           "geometry (curriculum-adjacency elaboration)", DEP,
           purpose=U, scope=P_ALL, origin=ClaimOrigin.ASSERTED)
    _item(s, interp, rev, "it.math.mensuration", "tm.mensuration",
          "Find the area of a sector of radius 7 cm and angle 60° (use pi = 22/7).",
          ["25.67 cm^2", "154 cm^2", "49 cm^2", "11 cm^2"], "25.67 cm^2")
    _ev(s, interp, f"ev.m{nn}.mens.target", f"{_pfx(nn)}.targets.tm.mensuration",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.11",
        "Find length of arc of a circle; perimeter and area of sectors and segments.")
    _ev(s, interp, f"ev.m{nn}.mens.solid", f"{_pfx(nn)}.req.m.solid_mensuration",
        "SRC.NERDC.SSS1.MATH.2025", "NERDC Math SSS1 p.11",
        "Calculate surface area and volume of solid shapes; frustum of cone "
        "and pyramid; compound shapes.")

    return s
