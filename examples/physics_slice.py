"""Phase 12 — first Physics CDG slice: Measurement, Kinematics, Newton's laws.

Pattern mirrors the Mathematics batches: evidence → agent proposal → human
review → acceptance → validation. Cross-subject Mathematics→Physics edges use
the existing prerequisite/requires contract with explicit subject attributes.
"""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, Subject, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, PrerequisitePurpose, PrerequisiteScope,
                       RelationshipType, SourceType)
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.wave2_batches import build_graph_v29
from examples._batchkit import accept, ev

B_REVIEW = "act.physics.review"
B_INTERP = "act.physics.interpret"
B_EXTRACT = "act.physics.extract"
SUBJ = "Physics"


def build_graph_v30() -> CDGStore:
    s = build_graph_v29()

    # ---- provenance + subject entities ----
    s.add_activity(Activity(id=B_EXTRACT, type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-08T08:00:00Z"))
    s.add_activity(Activity(id=B_INTERP, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-08T08:10:00Z"))
    s.add_activity(Activity(id=B_REVIEW, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-08T09:00:00Z",
                            rationale="Human review of first Physics slice (measurement/kinematics/Newton)."))

    for sid, name in [("sub.mathematics", "Mathematics"), ("sub.physics", "Physics")]:
        if sid not in s.entities:
            e = Subject(id=sid, label=name, subject=name, status=ClaimStatus.ACCEPTED,
                        created_by_activity=B_INTERP, cdg_version="v0.2.0",
                        legacy_ids=[])
            s.add_entity(e)

    def src(sid, title, url, stype=SourceType.TEXTBOOK, tier="reference"):
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=url, publisher="OpenStax",
                                source_type=stype, tier=tier))

    src("SRC.OSX.UP1.1.2", "University Physics Volume 1, 1.2 Units and Standards",
        "https://openstax.org/books/university-physics-volume-1/pages/1-2-units-and-standards")
    src("SRC.OSX.UP1.3.4", "University Physics Volume 1, 3.4 Motion with Constant Acceleration",
        "https://openstax.org/books/university-physics-volume-1/pages/3-4-motion-with-constant-acceleration")
    src("SRC.OSX.UP1.4.2", "University Physics Volume 1, 4.2 Acceleration Vector",
        "https://openstax.org/books/university-physics-volume-1/pages/4-2-acceleration-vector")
    src("SRC.OSX.UP1.5.2", "University Physics Volume 1, 5.2 Newton's First Law",
        "https://openstax.org/books/university-physics-volume-1/pages/5-2-newtons-first-law")
    src("SRC.OSX.UP1.5.4", "University Physics Volume 1, 5.4 Mass and Weight",
        "https://openstax.org/books/university-physics-volume-1/pages/5-4-mass-and-weight")
    # Official curriculum/exam sources: registered as Sources with metadata only.
    # PDF retrieval pending (JAMB IBASS serves via a JS SPA with hashed asset
    # URLs; WAEC/NERDC PDFs not yet downloaded). No content claims attached.
    for sid, title, url in [
        ("SRC.JAMB.IBASS.PHYSICS", "JAMB UTME Physics Syllabus (IBASS)",
         "https://ibass.jamb.gov.ng/e-syllabus"),
        ("SRC.WAEC.PHYSICS", "WAEC WASSCE Physics Syllabus", "https://www.waec.ng"),
        ("SRC.NERDC.SS.PHYSICS", "NERDC Senior Secondary Physics (2025 revision)",
         "https://nerdc.gov.ng/content_manager/new_senior_curriculum_home.html"),
    ]:
        if sid not in s.sources:
            s.add_source(Source(id=sid, title=title, identifier_or_url=url,
                                publisher="exam-board/curriculum body",
                                source_type=SourceType.SYLLABUS,
                                tier="primary", retrieved_at=None))

    def kc(kid, label, definition, status=ClaimStatus.ACCEPTED):
        k = KnowledgeComponent(id=kid, label=label, definition=definition, subject=SUBJ,
                               status=status, created_by_activity=B_INTERP,
                               cdg_version="v0.2.0")
        if status == ClaimStatus.ACCEPTED:
            k.reviewed_by_activity = B_REVIEW
            k.review_rationale = "Accepted in Phase 12 Physics slice via human review."
        s.add_entity(k)
        return k

    kc_units = kc("kc.measurement_units_dimensions", "Physical quantities, SI units and dimensions",
                  "Identify physical quantities, express them in SI units, and use dimensional analysis.")
    kc_error = kc("kc.measurement_errors_precision", "Measurement errors, precision and significant figures",
                  "Distinguish accuracy, precision, random and systematic error; use significant figures.",
                  status=ClaimStatus.PROPOSED)
    kc_disp = kc("kc.displacement_velocity", "Displacement, velocity and acceleration",
                 "Distinguish displacement/distance and speed/velocity; handle acceleration.")
    kc_kin = kc("kc.motion_equations_constant_acceleration", "Equations of motion (constant acceleration)",
                "Apply the constant-acceleration equations of motion.")
    kc_mg = kc("kc.motion_graph_interpretation", "Interpretation of motion graphs",
               "Read and produce displacement-time and velocity-time graphs.")
    kc_newton = kc("kc.newtons_laws", "Newton's laws of motion",
                   "Apply the three laws of motion to force/motion problems.")
    kc_mass = kc("kc.mass_and_weight", "Mass, weight and inertia",
                 "Distinguish mass from weight; use inertia in reasoning.")
    kc_practical = kc("kc.practical_measurement", "Experimental measurement practice",
                      "Carry out simple physics experiments with appropriate instruments.",
                      status=ClaimStatus.PROPOSED)

    def tm_and_method(tm_id, tm_label, mids_labels, target_ids):
        tm = TaskModel(id=tm_id, label=tm_label, status=ClaimStatus.ACCEPTED,
                       subject=SUBJ,
                       created_by_activity=B_INTERP, cdg_version="v0.2.0")
        tm.reviewed_by_activity = B_REVIEW
        s.add_entity(tm)
        for k in target_ids:
            c = Claim(id=f"cl.p.req.{tm_id}.target.{k}", predicate=RelationshipType.TARGETS,
                      subject_id=tm_id, object_id=k, claim_type=ClaimType.ASSESSMENT_DESIGN,
                      created_by_activity=B_INTERP, created_at="2026-10-08T08:10:00Z",
                      cdg_version="v0.2.0")
            s.add_claim(accept(c, f"{tm_id} targets {k}", (AcceptanceBasis.EXPERT,), B_REVIEW))
        for m_id, m_label in mids_labels:
            m = Method(id=m_id, label=m_label, task_model_id=tm_id,
                       subject=SUBJ,
                       status=ClaimStatus.ACCEPTED, created_by_activity=B_INTERP, cdg_version="v0.2.0")
            m.reviewed_by_activity = B_REVIEW
            s.add_entity(m)
            c = Claim(id=f"cl.p.own.{m_id}", predicate=RelationshipType.HAS_METHOD,
                      subject_id=tm_id, object_id=m_id, claim_type=ClaimType.ASSESSMENT_DESIGN,
                      created_by_activity=B_INTERP, created_at="2026-10-08T08:10:00Z",
                      cdg_version="v0.2.0")
            s.add_claim(accept(c, f"{m_id} owned by {tm_id}", (AcceptanceBasis.EXPERT,), B_REVIEW))
        return tm

    ASSESS = (AcceptanceBasis.EXPERT,)
    DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)

    def requires(m_id, kc_ids):
        for k in kc_ids:
            c = Claim(id=f"cl.p.req.{m_id}.{k}", predicate=RelationshipType.REQUIRES,
                      subject_id=m_id, object_id=k, claim_type=ClaimType.DEPENDENCY,
                      created_by_activity=B_INTERP, created_at="2026-10-08T08:10:00Z",
                      cdg_version="v0.2.0")
            s.add_claim(accept(c, f"{m_id} requires {k}", DEP, B_REVIEW))

    def prereq(cid, subj, obj, purpose, scope, scope_ref, origin, rationale, bases=DEP):
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj, object_id=obj,
                  claim_type=ClaimType.DEPENDENCY, purpose=purpose, scope=scope,
                  scope_ref=scope_ref, origin=origin, created_by_activity=B_INTERP,
                  created_at="2026-10-08T08:10:00Z", cdg_version="v0.2.0")
        s.add_claim(accept(c, rationale, bases, B_REVIEW))
        return c

    def evidence(eid, cid, source, excerpt, direct=False, legacy=None):
        s.add_evidence(ev(eid, cid, source, legacy or "none", excerpt, direct, B_INTERP,
                          legacy=False) if legacy else EvidenceItem(
            id=eid, claim_id=cid, source_id=source,
            role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
            stance=EvidenceStance.SUPPORTS, locator="openstax section",
            excerpt=excerpt, excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
            extracted_by_activity=B_INTERP))

    from cdg.evidence import EvidenceItem
    from cdg.enums import EvidenceRole, EvidenceStance, ExcerptKind

    # ---- Measurement ----
    tm_and_method("tm.convert_and_check_units", "Convert physical quantities and check dimensions",
                  [("m.si_prefix_conversion", "Convert using SI prefixes"),
                   ("m.dimensional_consistency", "Check dimensional consistency of formulas")],
                  [kc_units.id])
    requires("m.si_prefix_conversion", ["kc.algebraic_expressions"])
    requires("m.dimensional_consistency", ["kc.algebraic_expressions"])

    # ---- Kinematics: suvat ----
    tm_and_method("tm.solve_constant_acceleration", "Solve constant-acceleration motion problems",
                  [("m.suvat_equations", "Apply the equations of motion"),
                   ("m.graph_extract_motion", "Use motion graphs to extract unknowns")],
                  [kc_kin.id])
    requires("m.suvat_equations", ["kc.displacement_velocity", "kc.algebraic_expressions",
                                   "kc.linear_equations_one_var"])
    requires("m.graph_extract_motion", ["kc.motion_graph_interpretation", "kc.algebraic_expressions"])

    # ---- Kinematics: graphs ----
    tm_and_method("tm.interpret_motion_graph", "Interpret and construct motion graphs (displacement/velocity)",
                  [("m.slope_of_vt", "Read slope/area of velocity-time graphs"),
                   ("m.displacement_from_st", "Read displacement from displacement-time graphs")],
                  [kc_mg.id, kc_disp.id])
    requires("m.slope_of_vt", ["kc.gradient", "kc.algebraic_expressions", "kc.displacement_velocity"])
    requires("m.displacement_from_st", ["kc.gradient", "kc.displacement_velocity"])

    # ---- Newton's laws ----
    tm_and_method("tm.apply_newtons_second_law", "Apply Newton's second law to force problems",
                  [("m.resultant_force", "Find resultant force from a free-body sketch"),
                   ("m.f_equals_ma", "Compute acceleration from F = ma")],
                  [kc_newton.id, kc_mass.id])
    requires("m.resultant_force", ["kc.newtons_laws", "kc.mass_and_weight", "kc.algebraic_expressions"])
    requires("m.f_equals_ma", ["kc.newtons_laws", "kc.mass_and_weight", "kc.algebraic_expressions"])

    # ---- internal + cross-subject prerequisites ----
    prereq("cl.pre.kd_kin", kc_disp.id, kc_kin.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.solve_constant_acceleration",
           ClaimOrigin.DERIVED, "DERIVED: every method of tm.solve_constant_acceleration needs displacement/velocity")
    prereq("cl.pre.kmg_disp", kc_disp.id, kc_mg.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.interpret_motion_graph",
           ClaimOrigin.DERIVED, "DERIVED: methods of tm.interpret_motion_graph need displacement/velocity")
    prereq("cl.pre.newton_mass", kc_mass.id, kc_newton.id, PrerequisitePurpose.UNDERSTAND,
           PrerequisiteScope.ALL_RELEVANT_METHODS, None, ClaimOrigin.ASSERTED,
           "UNDERSTAND: distinction between mass and weight precedes force problems")
    # CROSS-SUBJECT Mathematics -> Physics (DERIVED, evidence-backed)
    prereq("cl.xs.math_alg_kin", "kc.algebraic_expressions", kc_kin.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.solve_constant_acceleration",
           ClaimOrigin.DERIVED, "Math→Physics: algebraic manipulation required by every method of tm.solve_constant_acceleration")
    prereq("cl.xs.math_lin_kin", "kc.linear_equations_one_var", kc_kin.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.solve_constant_acceleration",
           ClaimOrigin.DERIVED, "Math→Physics: linear-equation solving required by suvat method")
    prereq("cl.xs.math_grad_mg", "kc.gradient", kc_mg.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.interpret_motion_graph",
           ClaimOrigin.DERIVED, "Math→Physics: gradient computation required by motion-graph methods")
    prereq("cl.xs.math_alg_newton", "kc.algebraic_expressions", kc_newton.id, PrerequisitePurpose.EXECUTE,
           PrerequisiteScope.SPECIFIC_TASK_MODEL, "tm.apply_newtons_second_law",
           ClaimOrigin.DERIVED, "Math→Physics: algebraic rearrangement required by every method of tm.apply_newtons_second_law")

    # ---- item ----
    it = Item(id="it.physics.newton_1", label="MCQ: Newton's second law", task_model_id="tm.apply_newtons_second_law",
              stem="A 4 kg trolley has a resultant force of 12 N. Its acceleration is…",
              options=["3 m/s^2", "48 m/s^2", "0.33 m/s^2", "1/3 m/s^2"], key="3 m/s^2",
              status=ClaimStatus.ACCEPTED, subject=SUBJ, created_by_activity=B_INTERP)
    s.add_entity(it)

    # ---- evidence (all from retrievable OpenStax pages; official-syllabus
    #      confirmation pending — see SUBJECT_RESEARCH_READINESS) ----
    evidence("ev.p.units", "cl.p.req.tm.convert_and_check_units.target.kc.measurement_units_dimensions",
             "SRC.OSX.UP1.1.2", "Base SI units: length (m), mass (kg), time (s).", False)
    evidence("ev.p.suvat", "cl.p.req.tm.solve_constant_acceleration.target.kc.motion_equations_constant_acceleration",
             "SRC.OSX.UP1.3.4", "Equations of motion for constant acceleration solve unknowns.", False)
    evidence("ev.p.accel", "cl.p.req.tm.interpret_motion_graph.target.kc.motion_graph_interpretation",
             "SRC.OSX.UP1.4.2", "Acceleration is the time rate of change of the velocity vector.", False)
    evidence("ev.p.newton_first", "cl.p.req.tm.apply_newtons_second_law.target.kc.newtons_laws",
             "SRC.OSX.UP1.5.2", "Newton's first law states a body continues at rest or uniform motion unless acted on by a net external force.", True)
    evidence("ev.p.mass_weight", "cl.p.req.tm.apply_newtons_second_law.target.kc.mass_and_weight",
             "SRC.OSX.UP1.5.4", "Weight is the magnitude of the force of gravity: w = mg.", False)
    evidence("ev.p.r1", "cl.p.req.m.suvat_equations.kc.displacement_velocity",
             "SRC.OSX.UP1.3.4", "Kinematic equations relate displacement, velocity and acceleration.", False)
    evidence("ev.p.r2", "cl.p.req.m.slope_of_vt.kc.gradient",
             "SRC.OSX.UP1.4.2", "Slope of a velocity-time graph is acceleration.", False)
    evidence("ev.p.x1", "cl.xs.math_alg_kin", "SRC.OSX.UP1.3.4",
             "Solving kinematic equations requires algebraic manipulation.", False)
    evidence("ev.p.x2", "cl.xs.math_lin_kin", "SRC.OSX.UP1.3.4",
             "Reducing kinematic equations to a linear equation.", False)
    evidence("ev.p.x3", "cl.xs.math_grad_mg", "SRC.OSX.UP1.4.2",
             "Gradient used to read acceleration from a v-t graph.", False)
    evidence("ev.p.x4", "cl.xs.math_alg_newton", "SRC.OSX.UP1.5.2",
             "Rearranging F = ma for a needs algebraic manipulation.", False)
    return s
