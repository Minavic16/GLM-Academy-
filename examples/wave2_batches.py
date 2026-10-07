"""Priority Wave 2 batches 024-029, each evidence-backed and human-reviewable."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.batch23_circles import build_graph_v23
from examples._batchkit import accept, ev


def _base(s: CDGStore, nn, review_note):
    s.add_activity(Activity(id=f"act.b{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-07T14:00:00Z"))
    s.add_activity(Activity(id=f"act.b{nn}.interpret", type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-07T14:10:00Z"))
    s.add_activity(Activity(id=f"act.b{nn}.review", type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-07T15:00:00Z",
                            rationale=review_note))
    return s


def _src(s, sid, title, publisher="OpenStax", stype=SourceType.TEXTBOOK):
    if sid not in s.sources:
        s.add_source(Source(id=sid, title=title, identifier_or_url=f"legacy:{sid}",
                            publisher=publisher, source_type=stype, tier="reference"))


def _add_claim(s, nn_review, cid, pred, subj, obj, ctype, rationale, bases, **kw):
    c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
              claim_type=ctype, created_by_activity=nn,
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0", **kw) \
        if False else Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                            claim_type=ctype, created_by_activity=kw.pop('interp', None),
                            created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0", **kw)
    s.add_claim(accept(c, rationale, bases, nn_review))


def _tm_bundle(s, nn, review, tm_id, tm_label, m_id, m_label, kc_id,
               reqs, target_rationale):
    tm = TaskModel(id=tm_id, label=tm_label, status=ClaimStatus.ACCEPTED,
                   created_by_activity=f"act.b{nn}.interpret", cdg_version="v0.2.0")
    tm.reviewed_by_activity = review
    m = Method(id=m_id, label=m_label, task_model_id=tm_id,
               status=ClaimStatus.ACCEPTED, created_by_activity=f"act.b{nn}.interpret", cdg_version="v0.2.0")
    m.reviewed_by_activity = review
    s.add_entity(tm); s.add_entity(m)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def claim(cid, pred, subj, obj, ctype, rationale, bases=(AcceptanceBasis.EXPERT,),
              purpose=None, scope=None, scope_ref=None, origin=None):
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, purpose=purpose, scope=scope, scope_ref=scope_ref,
                  origin=origin, created_by_activity=f"act.b{nn}.interpret",
                  created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
        s.add_claim(accept(c, rationale, bases, review))

    claim(f"cl.{m_id}.target", RelationshipType.TARGETS, tm_id, kc_id,
          ClaimType.ASSESSMENT_DESIGN, target_rationale)
    claim(f"cl.{m_id}.own", RelationshipType.HAS_METHOD, tm_id, m_id,
          ClaimType.ASSESSMENT_DESIGN, "method ownership")
    for r_id, r_kc in reqs:
        claim(r_id, RelationshipType.REQUIRES, m_id, r_kc, ClaimType.DEPENDENCY,
              f"{m_id} requires {r_kc}", DEP)
    return s


def _kc(s, kid, label, definition, legacy, review):
    k = KnowledgeComponent(id=kid, label=label, definition=definition, subject="Mathematics",
                           status=ClaimStatus.ACCEPTED, legacy_ids=[legacy],
                           created_by_activity=f"act.b{review[-3]}", cdg_version="v0.2.0") if False else None
    return k


def _mkkc(s, kid, label, definition, legacy, nn, review):
    k = KnowledgeComponent(id=kid, label=label, definition=definition, subject="Mathematics",
                           status=ClaimStatus.ACCEPTED, legacy_ids=[legacy],
                           created_by_activity=f"act.b{nn}.interpret", cdg_version="v0.2.0")
    k.reviewed_by_activity = review
    s.add_entity(k)
    return k


def _item(s, iid, nn, tm_id, stem, options, key):
    it = Item(id=iid, label=f"MCQ: {stem[:30]}", task_model_id=tm_id, stem=stem,
              options=options, key=key, status=ClaimStatus.ACCEPTED,
              created_by_activity=f"act.b{nn}.interpret")
    s.add_entity(it)


def _evi(s, nn, reviews_target, claim_id, source, legacy, excerpt, direct):
    s.add_evidence(ev(f"ev.b{nn}.{len(s.evidence)}" if False else f"ev.b{nn}.{claim_id[-8:]}.{len(s.evidence)%100}",
                      claim_id, source, legacy, excerpt, direct, f"act.b{nn}.interpret"))


# ---------- Batch 024: parallel/perpendicular lines ----------
def build_graph_v24() -> CDGStore:
    s = build_graph_v23()
    nn, rev = "24", "act.b24.review"
    _base(s, nn, "Human review of coordinate parallel/perpendicular batch.")
    _src(s, "SRC.OSX.IA2E.3.2", "Intermediate Algebra 2e, 3.2 Slope of a Line")
    _mkkc(s, "kc.parallel_perpendicular_lines", "Conditions for parallel and perpendicular lines",
          "Parallel lines have equal gradients; perpendicular lines have gradients multiplying to -1.",
          "MATH.COORD.PARALLEL_PERPENDICULAR", nn, rev)
    _tm_bundle(s, nn, rev, "tm.classify_line_relationships",
               "Classify whether two lines are parallel, perpendicular or neither",
               "m.compare_gradients", "Compare gradients for equality or product -1",
               "kc.parallel_perpendicular_lines",
               [("cl.req24.grad", "kc.gradient"), ("cl.req24.int", "kc.integer_arithmetic")],
               "targets classification by gradient conditions")
    _item(s, "it.mcq.parperp", nn, "tm.classify_line_relationships",
          "Gradients are 2 and -1/2. The lines are…", ["perpendicular", "parallel", "the same", "neither"], "perpendicular")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    c = Claim(id="cl.pre24.grad_pp", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.gradient", object_id="kc.parallel_perpendicular_lines",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.classify_line_relationships",
              origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
    s.add_claim(accept(c, "EXECUTE, all methods of the TM", DEP, rev))
    s.add_evidence(ev("ev.b24.t", "cl.m.compare_gradients.target", "SRC.OSX.IA2E.3.2", "E0252",
                      "Use slopes to identify parallel and perpendicular lines.", False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b24.r1", "cl.req24.grad", "SRC.JAMB.UTME.MATH", "E0253",
                      "identify conditions for parallelism and perpendicularity.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b24.p1", "cl.pre24.grad_pp", "SRC.OSX.IA2E.3.2", "E0252",
                      "Requires gradient to compare.", False, f"act.b{nn}.interpret"))
    return s


# ---------- Batch 025: ratio, proportion and rate ----------
def build_graph_v25() -> CDGStore:
    s = build_graph_v24()
    nn, rev = "25", "act.b25.review"
    _base(s, nn, "Human review of ratios/proportion batch.")
    _src(s, "SRC.OSX.CM.10.8", "OpenStax reference 10.8")
    _src(s, "SRC.SIEGLER.2012", "Siegler et al. (2012) fractions and algebra knowledge", publisher="Science")
    _mkkc(s, "kc.ratio_proportion_rate", "Ratio, proportion and rate",
          "Interpret and use ratios as comparisons; solve proportion and rate problems.",
          "MATH.NUM.RATIO_PROPORTION_RATE", nn, rev)
    _tm_bundle(s, nn, rev, "tm.solve_proportions", "Solve proportion and rate problems",
               "m.unitary_method", "Use the unitary method / cross-multiplication",
               "kc.ratio_proportion_rate",
               [("cl.req25.frac", "kc.fraction_decimal_operations"),
                ("cl.req25.int", "kc.integer_arithmetic")],
               "targets ratio/proportion/rate capability")
    _item(s, "it.mcq.ratio", nn, "tm.solve_proportions",
          "3 pencils cost ₦15. Cost of 7 pencils?", ["₦35", "₦28", "₦21", "₦45"], "₦35")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    c = Claim(id="cl.pre25.frac_ratio", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.fraction_decimal_operations", object_id="kc.ratio_proportion_rate",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.solve_proportions",
              origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
    s.add_claim(accept(c, "EXECUTE via tm25 methods", DEP, rev))
    s.add_evidence(ev("ev.b25.t", "cl.m.unitary_method.target", "SRC.OSX.CM.10.8", "E0033",
                      "A fraction is a ratio, the ratio of the numerator to the denominator.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b25.r1", "cl.req25.frac", "SRC.SIEGLER.2012", "E0034",
                      "Fraction knowledge uniquely predicts later algebra knowledge.", False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b25.p1", "cl.pre25.frac_ratio", "SRC.OSX.CM.10.8", "E0033",
                      "Ratios are fractions.", True, f"act.b{nn}.interpret"))
    return s


# ---------- Batch 026: direct variation ----------
def build_graph_v26() -> CDGStore:
    s = build_graph_v25()
    nn, rev = "26", "act.b26.review"
    _base(s, nn, "Human review of direct-variation batch.")
    _mkkc(s, "kc.direct_variation", "Direct variation",
          "Recognise y ∝ x and solve problems using y = kx.",
          "MATH.ALG.DIRECT_VARIATION", nn, rev)
    _tm_bundle(s, nn, rev, "tm.direct_variation_problems", "Solve direct-variation problems",
               "m.find_constant", "Find the constant k then evaluate",
               "kc.direct_variation",
               [("cl.req26.lin", "kc.linear_equations_one_var"),
                ("cl.req26.int", "kc.integer_arithmetic")],
               "targets direct variation")
    _item(s, "it.mcq.direct", nn, "tm.direct_variation_problems",
          "y varies directly as x; y=12 when x=3. y when x=5?", ["20", "15", "18", "24"], "20")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    c = Claim(id="cl.pre26.lin_var", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.linear_equations_one_var", object_id="kc.direct_variation",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.direct_variation_problems",
              origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
    s.add_claim(accept(c, "EXECUTE via tm26 methods", DEP, rev))
    s.add_evidence(ev("ev.b26.t", "cl.m.find_constant.target", "SRC.NERDC.SSS1.MATH.2025", "E0211",
                      "'Simple Equations and Variations' taught as one topic.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b26.r1", "cl.req26.lin", "SRC.NERDC.SSS1.MATH.2025", "E0211",
                      "Variation problems reduce to linear equations.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b26.p1", "cl.pre26.lin_var", "SRC.NERDC.SSS1.MATH.2025", "E0211",
                      "Variations taught with simple equations.", True, f"act.b{nn}.interpret"))
    return s


# ---------- Batch 027: special-angle trig values ----------
def build_graph_v27() -> CDGStore:
    s = build_graph_v26()
    nn, rev = "27", "act.b27.review"
    _base(s, nn, "Human review of special-angle trig batch.")
    _src(s, "SRC.OSX.CM.10.8", "OpenStax reference 10.8")
    _mkkc(s, "kc.special_angle_values", "Exact trigonometric values of special angles",
          "Recall sin/cos/tan for 30°, 45°, 60°, 90° from special triangles.",
          "MATH.TRIG.SPECIAL_ANGLE_VALUES", nn, rev)
    _tm_bundle(s, nn, rev, "tm.recall_special_values", "State exact trig values at special angles",
               "m.from_special_triangles", "Read off values from 30-60-90 and 45-45-90 triangles",
               "kc.special_angle_values",
               [("cl.req27.trig", "kc.trig_ratios_acute"),
                ("cl.req27.alg", "kc.algebraic_expressions")],
               "targets exact special-angle values")
    _item(s, "it.mcq.special_angle", nn, "tm.recall_special_values",
          "sin 60° = ?", ["√3/2", "1/2", "√2/2", "1"], "√3/2")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    c = Claim(id="cl.pre27.trig_sp", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.trig_ratios_acute", object_id="kc.special_angle_values",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.recall_special_values",
              origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
    s.add_claim(accept(c, "EXECUTE via tm27 methods", DEP, rev))
    s.add_evidence(ev("ev.b27.t", "cl.m.from_special_triangles.target", "SRC.OSX.CM.10.8", "E0265",
                      "Since this is a 30-60-90 triangle and side b should equal x.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b27.r1", "cl.req27.trig", "SRC.OSX.CM.10.8", "E0265",
                      "Special values come from the ratio definitions.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b27.p1", "cl.pre27.trig_sp", "SRC.OSX.CM.10.8", "E0265",
                      "Builds on acute-angle trig ratios.", True, f"act.b{nn}.interpret"))
    return s


# ---------- Batch 028: multiplication counting principle ----------
def build_graph_v28() -> CDGStore:
    s = build_graph_v27()
    nn, rev = "28", "act.b28.review"
    _base(s, nn, "Human review of counting-principle batch.")
    _src(s, "SRC.OSX.CM.7.2", "OpenStax reference 7.2")
    _src(s, "SRC.OSX.AT2E.13.5", "Algebra and Trigonometry 2e, 13.5 Multiplication Principle")
    _mkkc(s, "kc.counting_principle", "Fundamental (multiplication) counting principle",
          "Count outcomes of multi-stage experiments by multiplying choices.",
          "MATH.STAT.COUNTING_PRINCIPLE", nn, rev)
    _tm_bundle(s, nn, rev, "tm.count_outcomes", "Count outcomes of a multi-stage experiment",
               "m.multiply_choices", "Apply the multiplication counting rule",
               "kc.counting_principle",
               [("cl.req28.int", "kc.integer_arithmetic"),
                ("cl.req28.ratio", "kc.ratio_proportion_rate")],
               "targets the counting principle")
    _item(s, "it.mcq.count", nn, "tm.count_outcomes",
          "2 shirts and 3 pairs of trousers: number of outfits?", ["6", "5", "8", "12"], "6")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    c = Claim(id="cl.pre28.int_count", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.integer_arithmetic", object_id="kc.counting_principle",
              claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
              scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.count_outcomes",
              origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
              created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
    s.add_claim(accept(c, "EXECUTE via tm28 methods", DEP, rev))
    s.add_evidence(ev("ev.b28.t", "cl.m.multiply_choices.target", "SRC.OSX.CM.7.2", "E0364",
                      "Use the Multiplication Rule for Counting.", True, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b28.r1", "cl.req28.int", "SRC.OSX.AT2E.13.5", "E0365",
                      "Multiplication Principle requires counting outcomes.", False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b28.p1", "cl.pre28.int_count", "SRC.OSX.CM.7.2", "E0364",
                      "Apply multiplication for counts.", True, f"act.b{nn}.interpret"))
    return s


# ---------- Batch 029: distance between two points ----------
def build_graph_v29() -> CDGStore:
    s = build_graph_v28()
    nn, rev = "29", "act.b29.review"
    _base(s, nn, "Human review of distance-formula batch.")
    _src(s, "SRC.OSX.IA2E.11.1", "Intermediate Algebra 2e, 11.1 Distance and Midpoint")
    _mkkc(s, "kc.distance_formula", "Distance between two points in the plane",
          "Compute d = sqrt((x2-x1)^2 + (y2-y1)^2).",
          "MATH.COORD.DISTANCE_FORMULA", nn, rev)
    _tm_bundle(s, nn, rev, "tm.compute_distance", "Compute the distance between two coordinate points",
               "m.distance_formula", "Apply the distance formula",
               "kc.distance_formula",
               [("cl.req29.alg", "kc.algebraic_expressions"),
                ("cl.req29.int", "kc.integer_arithmetic"),
                ("cl.req29.grid", "kc.gradient")],
               "targets distance between two points")
    _item(s, "it.mcq.distance", nn, "tm.compute_distance",
          "Distance between (1,2) and (4,6)?", ["5", "3", "7", "25"], "5")
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
    for subj, src, leg, exc, purp in [
        ("kc.gradient", "SRC.OSX.IA2E.11.1", "E0249", "Find the length of the hypotenuse — gradient/coordinate linkage.", "EXECUTE"),
        ("kc.algebraic_expressions", "SRC.OSX.IA2E.5.4", "E0100", "Requires squaring and expanding.", "EXECUTE"),
    ]:
        c = Claim(id=f"cl.pre29.{subj[3:]}_dist", predicate=RelationshipType.PREREQUISITE,
                  subject_id=subj, object_id="kc.distance_formula",
                  claim_type=ClaimType.DEPENDENCY, purpose=PrerequisitePurpose.EXECUTE,
                  scope=PrerequisiteScope.SPECIFIC_TASK_MODEL, scope_ref="tm.compute_distance",
                  origin=ClaimOrigin.DERIVED, created_by_activity=f"act.b{nn}.interpret",
                  created_at="2026-10-07T14:10:00Z", cdg_version="v0.2.0")
        s.add_claim(accept(c, f"{purp} via tm29", DEP, rev))
        s.add_evidence(ev(f"ev.b29.p.{subj[3:]}", c.id, src, leg, exc, False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b29.t", "cl.m.distance_formula.target", "SRC.OSX.IA2E.11.1", "E0249",
                      "Find the length of the hypotenuse of a right triangle.", False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b29.r1", "cl.req29.alg", "SRC.OSX.IA2E.5.4", "E0100",
                      "Requires algebraic expansion.", False, f"act.b{nn}.interpret"))
    s.add_evidence(ev("ev.b29.r2", "cl.req29.grid", "SRC.WAEC.WASSCE.MATH.SYL", "E0247",
                      "Distance on a coordinate grid.", True, f"act.b{nn}.interpret"))
    return s
