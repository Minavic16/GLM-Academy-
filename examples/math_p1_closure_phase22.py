"""Phase 22 Mathematics P1 closure (owner-authorized, batches 080-082).

Implements the three P1 topics identified by the Phase 21 audit as the
smallest complete package for the declared target "all 23 official JAMB
Mathematics syllabus topics implemented at topic level". Controlled by the
official JAMB UTME Mathematics E-syllabus (SRC.JAMB.UTME.MATH.2025 —
IBASS static asset; SHA-256
aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f;
locators "JAMB Math p.N" = extracted-text page N of that exact revision):

- 080 Binary operations      II.5 a-b      (JAMB Math p.3)
- 081 Loci & construction    III.3 + III.1(d) objective iv
                                             (JAMB Math pp.3-4)
- 082 Representation of data V.1 a-b       (JAMB Math p.5)

Provenance discipline (Phase 18/19/20 rules preserved):
- All new records are Phase 22 records; no historical claim, evidence or
  review rationale is rewritten or backdated. build_graph_v42 chains
  build_graph_v41; every earlier record is carried forward unchanged.
- The three topics are official JAMB requirements; the JAMB source record
  (registered Phase 20) is the controlling evidence for all new claims.
  Excerpts are paraphrase-grade (ExcerptKind.PARAPHRASE) of the official
  content/objectives text, with precise locators.
- Disclosed boundaries (see PHASE22_REPORT.md): II.5 is implemented at the
  UTME treatment (properties; identity/inverse in simple cases; evaluation
  by rule/table) — no abstract-algebra expansion; III.3/III.1(d) cover the
  syllabus construction procedures (perpendicular/angle bisectors, special
  angles 30-90 degrees, intersection-of-loci problems) — no unrestricted
  Euclidean-geometry expansion; V.1 covers representation only (frequency
  distribution; histogram, bar chart, pie chart) — ogives/cumulative
  frequency remain excluded (standing owner deferral), and the existing
  location/dispersion KCs are untouched. P2 depth gaps are not implemented
  in this phase.

Chains build_graph_v41. No schema change; 13 entity types preserved; no
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
from examples.math_wave_a_phase20 import build_graph_v41

SUBJ = "Mathematics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-17T12:10:00Z"
E = PrerequisitePurpose.EXECUTE
U = PrerequisitePurpose.UNDERSTAND
P_ALL = PrerequisiteScope.ALL_RELEVANT_METHODS
P_M = PrerequisiteScope.SPECIFIC_METHOD
P_TM = PrerequisiteScope.SPECIFIC_TASK_MODEL
JAMB = "SRC.JAMB.UTME.MATH.2025"


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.m{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-17T12:00:00Z"))
    interp = f"act.m{nn}.interpret"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-17T12:10:00Z"))
    rev = f"act.m{nn}.review"
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-17T13:00:00Z",
                            rationale=note))
    return interp, rev


def _src_jamb(s):
    """Register the official JAMB Mathematics E-syllabus PDF if absent.

    The source was registered canonically in Phase 20 (build_graph_v41);
    this guarded call is a no-op on the Phase 22 chain and keeps the
    registration self-contained if the chain order ever changes.
    """
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
    k.review_rationale = ("Accepted in Phase 22 via human review."
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


def build_graph_v42() -> CDGStore:
    s = build_graph_v41()

    # Official controlling source for this wave (registered Phase 20; guard).
    _src_jamb(s)

    # =====================================================================
    # Batch 080 — Binary operations (JAMB II.5 a-b; JAMB Math p.3)
    # =====================================================================
    nn = "80"
    interp, rev = _base(s, nn, "Human review of binary operations batch (Phase 22).")

    kc = _kc(s, interp, rev, "kc.binary_operations",
             "Binary operations: properties, identity and inverse elements",
             "Interpret binary operations defined on sets of numbers, "
             "including operations defined by a rule or an operation table; "
             "evaluate expressions under a defined operation; establish "
             "closure, commutativity, associativity and distributivity; "
             "determine identity and inverse elements in simple cases.",
             " JAMB locator: II.5, JAMB Math p.3.")
    t = _tm(s, interp, rev, "tm.binary_operations_problems",
            "Evaluate and analyse binary operations")
    _targets(s, interp, rev, nn, t.id, kc.id, "targets binary operations capability")
    _m_claims(s, interp, rev, nn, t.id, "m.evaluate_binary_operation",
              "Evaluate expressions under a binary operation defined by a "
              "rule or an operation table",
              ["kc.binary_operations", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.binary_operation_properties",
              "Test closure, commutativity, associativity and distributivity "
              "of a defined operation",
              ["kc.binary_operations", "kc.integer_arithmetic",
               "kc.algebraic_expressions"])
    _m_claims(s, interp, rev, nn, t.id, "m.identity_inverse_elements",
              "Determine identity and inverse elements under a defined "
              "operation (simple cases)",
              ["kc.binary_operations", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.m80.pre.kc.binary_operations",
         "kc.integer_arithmetic", "kc.binary_operations", E, P_TM,
         "tm.binary_operations_problems", ClaimOrigin.DERIVED,
         "EXECUTE: evaluating operations and testing their properties on "
         "sets of numbers exercises integer arithmetic (all-methods derived).")
    _pre(s, interp, rev, "cl.m80.pre.kc.binary_operations.alg",
         "kc.algebraic_expressions", "kc.binary_operations", E, P_M,
         "m.binary_operation_properties", ClaimOrigin.DERIVED,
         "EXECUTE: distributivity tests expand and simplify algebraic "
         "expressions (method-scoped).")
    _item(s, interp, rev, "it.math.binary_operation", t.id,
          "A binary operation * is defined on the set of real numbers by "
          "a * b = a + b + ab. Evaluate 2 * 3.",
          ["11", "5", "6", "12"], "11")
    _item(s, interp, rev, "it.math.binary_identity", t.id,
          "A binary operation * is defined on the set of real numbers by "
          "a * b = a + b - ab. Find the identity element of the operation.",
          ["0", "1", "-1", "a"], "0")
    _ev(s, interp, "ev.m80.target", f"{_pfx(nn)}.targets.tm.binary_operations_problems",
        "JAMB Math p.3 (II.5)",
        "Binary Operations (II.5): properties of closure, commutativity, "
        "associativity and distributivity; identity and inverse elements "
        "(simple cases only).")
    _ev(s, interp, "ev.m80.eval", f"{_pfx(nn)}.req.m.evaluate_binary_operation.kc.binary_operations",
        "JAMB Math p.3 (II.5)",
        "Binary operations (II.5): evaluate simple expressions under a "
        "defined operation, including operations defined by a rule or table.")
    _ev(s, interp, "ev.m80.props", f"{_pfx(nn)}.req.m.binary_operation_properties.kc.binary_operations",
        "JAMB Math p.3 (II.5a)",
        "Properties of closure, commutativity, associativity and "
        "distributivity (II.5a).")
    _ev(s, interp, "ev.m80.ident", f"{_pfx(nn)}.req.m.identity_inverse_elements.kc.binary_operations",
        "JAMB Math p.3 (II.5b)",
        "Identity and inverse elements — simple cases only (II.5b).")
    _ev(s, interp, "ev.m80.pre", "cl.m80.pre.kc.binary_operations",
        "JAMB Math p.3 (II.5) — pedagogical inference",
        "Evaluating and testing binary operations on sets of numbers "
        "exercises integer arithmetic.")
    _ev(s, interp, "ev.m80.pre.alg", "cl.m80.pre.kc.binary_operations.alg",
        "JAMB Math p.3 (II.5a) — pedagogical inference",
        "Distributivity tests expand and simplify algebraic expressions.")

    # =====================================================================
    # Batch 081 — Loci & construction (JAMB III.3 p.4; III.1d objective iv p.3)
    # =====================================================================
    nn = "81"
    interp, rev = _base(s, nn, "Human review of loci and construction batch (Phase 22).")

    kc = _kc(s, interp, rev, "kc.loci_and_construction",
             "Loci and constructions in two dimensions",
             "Identify and interpret loci in two dimensions (parallel lines, "
             "perpendicular bisectors, angle bisectors, circles); construct "
             "perpendicular bisectors, angle bisectors and special angles "
             "(30, 45, 60, 75, 90 degrees) with appropriate instruments; "
             "solve construction problems using the intersections of loci.",
             " JAMB locators: III.3, JAMB Math p.4; III.1(d) objective iv, "
             "JAMB Math p.3.")
    t = _tm(s, interp, rev, "tm.loci_construction_problems",
            "Interpret loci and perform geometric constructions")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets loci and construction capability")
    _m_claims(s, interp, rev, nn, t.id, "m.describe_locus",
              "Identify and interpret loci relating to parallel lines, "
              "perpendicular bisectors, angle bisectors and circles",
              ["kc.loci_and_construction", "kc.mensuration"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_perpendicular_bisector",
              "Construct the perpendicular bisector of a line segment with "
              "ruler and compasses",
              ["kc.loci_and_construction", "kc.mensuration"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_angle_bisector",
              "Construct the bisector of a given angle with ruler and "
              "compasses",
              ["kc.loci_and_construction", "kc.triangle_angle_properties"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_special_angles",
              "Apply construction procedures for the special angles "
              "30, 45, 60, 75 and 90 degrees",
              ["kc.loci_and_construction", "kc.triangle_angle_properties"])
    _m_claims(s, interp, rev, nn, t.id, "m.apply_loci_intersections",
              "Solve construction problems using the intersections of loci",
              ["kc.loci_and_construction", "kc.mensuration"])
    _pre(s, interp, rev, "cl.m81.pre.kc.loci_and_construction",
         "kc.mensuration", "kc.loci_and_construction", E, P_TM,
         "tm.loci_construction_problems", ClaimOrigin.DERIVED,
         "EXECUTE: loci and constructions use circles, arcs, radii and "
         "distances — mensuration supplies these concepts (all methods of "
         "the task model).")
    _pre(s, interp, rev, "cl.m81.pre.kc.loci_and_construction.ang",
         "kc.triangle_angle_properties", "kc.loci_and_construction", E, P_TM,
         "tm.loci_construction_problems", ClaimOrigin.DERIVED,
         "EXECUTE: constructing angle bisectors and special angles applies "
         "angle properties (angle constructions).")
    _pre(s, interp, rev, "cl.m81.pre.kc.loci_and_construction.par",
         "kc.parallel_line_angles", "kc.loci_and_construction", U, P_ALL,
         None, ClaimOrigin.ASSERTED,
         "UNDERSTAND: the parallel-lines locus builds on parallel-line "
         "concepts; JAMB III.1 (lines and angles) precedes III.3 (loci) in "
         "the syllabus.")
    _item(s, interp, rev, "it.math.loci", t.id,
          "The locus of points at a constant distance d from a fixed "
          "point P is",
          ["a circle with centre P and radius d", "a pair of parallel lines",
           "the perpendicular bisector of a segment",
           "the angle bisector of an angle"],
          "a circle with centre P and radius d")
    _item(s, interp, rev, "it.math.loci_construction", t.id,
          "The locus of points equidistant from two intersecting straight "
          "lines is",
          ["the angle bisectors of the angles between the lines",
           "the perpendicular bisector of a segment joining them",
           "a circle with centre at the point of intersection",
           "a line parallel to one of the lines"],
          "the angle bisectors of the angles between the lines")
    _item(s, interp, rev, "it.math.special_angle_construction", t.id,
          "Which construction procedure produces an angle of 30 degrees?",
          ["Bisect a 60 degree angle", "Bisect an 80 degree angle",
           "Bisect a 100 degree angle", "Bisect a 120 degree angle"],
          "Bisect a 60 degree angle")
    _ev(s, interp, "ev.m81.target", f"{_pfx(nn)}.targets.tm.loci_construction_problems",
        "JAMB Math pp.3-4 (III.1d; III.3)",
        "Loci (III.3): locus in two dimensions based on geometric principles "
        "relating to lines and curves — identify and interpret loci relating "
        "to parallel lines, perpendicular bisectors, angle bisectors and "
        "circles. Construction of special angles (III.1 objective iv): "
        "30, 45, 60, 75, 90 degrees.")
    _ev(s, interp, "ev.m81.describe", f"{_pfx(nn)}.req.m.describe_locus.kc.loci_and_construction",
        "JAMB Math p.4 (III.3)",
        "Identify and interpret loci relating to parallel lines, "
        "perpendicular bisectors, angle bisectors and circles (III.3).")
    _ev(s, interp, "ev.m81.pb", f"{_pfx(nn)}.req.m.construct_perpendicular_bisector.kc.loci_and_construction",
        "JAMB Math p.4 (III.3)",
        "Construct the perpendicular-bisector locus (points equidistant from "
        "two fixed points) with ruler and compasses (III.3).")
    _ev(s, interp, "ev.m81.ab", f"{_pfx(nn)}.req.m.construct_angle_bisector.kc.loci_and_construction",
        "JAMB Math p.4 (III.3)",
        "Construct the angle-bisector locus (points equidistant from two "
        "intersecting lines) with ruler and compasses (III.3).")
    _ev(s, interp, "ev.m81.sa", f"{_pfx(nn)}.req.m.construct_special_angles.kc.loci_and_construction",
        "JAMB Math p.3 (III.1d; objective iv)",
        "Identify construction procedures of special angles, e.g. 30, 45, "
        "60, 75, 90 degrees (III.1 objective iv).")
    _ev(s, interp, "ev.m81.inter", f"{_pfx(nn)}.req.m.apply_loci_intersections.kc.loci_and_construction",
        "JAMB Math p.4 (III.3)",
        "Solve construction problems using the intersection of loci in two "
        "dimensions (III.3).")
    _ev(s, interp, "ev.m81.pre.mens", "cl.m81.pre.kc.loci_and_construction",
        "JAMB Math p.4 (III.3) — pedagogical inference",
        "Loci and constructions use circles, arcs and distances; mensuration "
        "supplies these concepts.")
    _ev(s, interp, "ev.m81.pre.ang", "cl.m81.pre.kc.loci_and_construction.ang",
        "JAMB Math pp.3-4 (III.1d; III.3) — pedagogical inference",
        "Constructing angle bisectors and special angles applies angle "
        "properties (III.1).")
    _ev(s, interp, "ev.m81.pre.par", "cl.m81.pre.kc.loci_and_construction.par",
        "JAMB Math p.4 (III.3) — ordering",
        "The parallel-lines locus relates to parallel-line concepts; III.1 "
        "(lines and angles) precedes III.3 (loci) in the syllabus.")

    # =====================================================================
    # Batch 082 — Representation of data (JAMB V.1 a-b; JAMB Math p.5)
    # =====================================================================
    nn = "82"
    interp, rev = _base(s, nn, "Human review of data representation batch (Phase 22).")

    kc = _kc(s, interp, rev, "kc.data_representation",
             "Representation of data: frequency distribution and charts",
             "Organise raw data into frequency distribution tables; "
             "construct, read and interpret bar charts, histograms and pie "
             "charts; select a suitable representation for a given data set.",
             " JAMB locator: V.1, JAMB Math p.5. Scope distinction: "
             "representation only — the location/dispersion KCs remain "
             "separate; ogive/cumulative frequency excluded (standing owner "
             "deferral).")
    t = _tm(s, interp, rev, "tm.data_representation_problems",
            "Organise data and construct statistical charts")
    _targets(s, interp, rev, nn, t.id, kc.id,
             "targets data representation capability")
    _m_claims(s, interp, rev, nn, t.id, "m.frequency_distribution_table",
              "Organise raw data into a frequency distribution table",
              ["kc.data_representation", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_bar_chart",
              "Construct and read bar charts for given data",
              ["kc.data_representation", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_histogram",
              "Construct and read histograms for grouped data",
              ["kc.data_representation", "kc.integer_arithmetic"])
    _m_claims(s, interp, rev, nn, t.id, "m.construct_pie_chart",
              "Construct pie charts by converting frequencies to sector "
              "angles",
              ["kc.data_representation", "kc.ratio_proportion_rate"])
    _pre(s, interp, rev, "cl.m82.pre.kc.data_representation",
         "kc.integer_arithmetic", "kc.data_representation", E, P_TM,
         "tm.data_representation_problems", ClaimOrigin.DERIVED,
         "EXECUTE: tallying frequencies and chart scales exercise integer "
         "arithmetic (all-methods derived).")
    _pre(s, interp, rev, "cl.m82.pre.kc.data_representation.ratio",
         "kc.ratio_proportion_rate", "kc.data_representation", E, P_M,
         "m.construct_pie_chart", ClaimOrigin.DERIVED,
         "EXECUTE: pie-chart sector angles are computed from proportions of "
         "the whole (method-scoped).")
    _item(s, interp, rev, "it.math.frequency_table", t.id,
          "The marks of ten students are 2, 3, 2, 5, 3, 2, 4, 5, 2, 4. "
          "What is the frequency of the mark 2?",
          ["4", "2", "3", "5"], "4")
    _item(s, interp, rev, "it.math.pie_chart", t.id,
          "In a pie chart representing 240 items, a sector of angle 60 "
          "degrees represents how many items?",
          ["40", "24", "60", "80"], "40")
    _item(s, interp, rev, "it.math.data_representation_choice", t.id,
          "Which chart is most suitable for representing grouped continuous "
          "data?",
          ["Histogram", "Pie chart", "Bar chart", "List of raw data"],
          "Histogram")
    _ev(s, interp, "ev.m82.target", f"{_pfx(nn)}.targets.tm.data_representation_problems",
        "JAMB Math p.5 (V.1)",
        "Representation of data (V.1): (a) frequency distribution; "
        "(b) histogram, bar chart and pie chart.")
    _ev(s, interp, "ev.m82.freq", f"{_pfx(nn)}.req.m.frequency_distribution_table.kc.data_representation",
        "JAMB Math p.5 (V.1a)",
        "Frequency distribution of data (V.1a).")
    _ev(s, interp, "ev.m82.bar", f"{_pfx(nn)}.req.m.construct_bar_chart.kc.data_representation",
        "JAMB Math p.5 (V.1b)",
        "Bar chart representation (V.1b).")
    _ev(s, interp, "ev.m82.hist", f"{_pfx(nn)}.req.m.construct_histogram.kc.data_representation",
        "JAMB Math p.5 (V.1b)",
        "Histogram representation (V.1b).")
    _ev(s, interp, "ev.m82.pie", f"{_pfx(nn)}.req.m.construct_pie_chart.kc.data_representation",
        "JAMB Math p.5 (V.1b)",
        "Pie chart representation (V.1b).")
    _ev(s, interp, "ev.m82.pre.int", "cl.m82.pre.kc.data_representation",
        "JAMB Math p.5 (V.1) — pedagogical inference",
        "Tallying frequencies and chart scales exercise integer arithmetic.")
    _ev(s, interp, "ev.m82.pre.ratio", "cl.m82.pre.kc.data_representation.ratio",
        "JAMB Math p.5 (V.1b) — pedagogical inference",
        "Pie-chart sector angles convert frequencies to angles in proportion "
        "to the whole (360 degrees).")

    return s


if __name__ == "__main__":
    from cdg.serialization import dumps_store
    store = build_graph_v42()
    print(dumps_store(store)[:200])
    print(f"entities={len(store.entities)} claims={len(store.claims)} "
          f"evidence={len(store.evidence)} sources={len(store.sources)} "
          f"activities={len(store.activities)}")
