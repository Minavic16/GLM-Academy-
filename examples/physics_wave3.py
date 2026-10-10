"""Phase 12B Physics expansion B: batches 037-042 (waves, optics, circuits,
EMI/AC, modern physics, practical graduation). Chains from build_graph_v31."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, EvidenceRole, EvidenceStance, ExcerptKind,
                       PrerequisitePurpose, PrerequisiteScope, RelationshipType,
                       SourceType)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.physics_wave2 import build_graph_v31
from examples._batchkit import accept

SUBJ = "Physics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-10T12:10:00Z"
E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.p{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-10T12:00:00Z"))
    interp = f"act.p{nn}.interpret"
    rev = f"act.p{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-10T12:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-10T13:00:00Z",
                            rationale=note))
    return interp, rev


def _src(s, sid, title, url):
    if sid not in s.sources:
        s.add_source(Source(id=sid, title=title, identifier_or_url=url,
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
                            tier="reference"))


def _kc(s, interp, rev, kid, label, definition):
    k = KnowledgeComponent(id=kid, label=label, definition=definition, subject=SUBJ,
                           status=ClaimStatus.ACCEPTED, created_by_activity=interp,
                           cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = "Accepted in Phase 12B via human review."
    s.add_entity(k)
    return k


def _tm(s, interp, rev, tm_id, label, targets):
    t = TaskModel(id=tm_id, label=label, status=ClaimStatus.ACCEPTED, subject=SUBJ,
                  created_by_activity=interp, cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    for k in targets:
        c = Claim(id=f"cl.p{tm_id}.target.{k}", predicate=RelationshipType.TARGETS,
                  subject_id=tm_id, object_id=k, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, f"{tm_id} targets {k}", ASSESS, rev))
    return t


def _m(s, interp, rev, m_id, label, tm_id, reqs):
    m = Method(id=m_id, label=label, task_model_id=tm_id, subject=SUBJ,
               status=ClaimStatus.ACCEPTED, created_by_activity=interp, cdg_version="v0.2.0")
    m.reviewed_by_activity = rev
    s.add_entity(m)
    c = Claim(id=f"cl.p.own.{m_id}", predicate=RelationshipType.HAS_METHOD,
              subject_id=tm_id, object_id=m_id, claim_type=ClaimType.ASSESSMENT_DESIGN,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, f"{m_id} owned by {tm_id}", ASSESS, rev))
    for k in reqs:
        c = Claim(id=f"cl.p.req.{m_id}.{k}", predicate=RelationshipType.REQUIRES,
                  subject_id=m_id, object_id=k, claim_type=ClaimType.DEPENDENCY,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, f"{m_id} requires {k}", DEP, rev))
    return m


def _pre(s, interp, rev, cid, subj, obj, purpose, scope, ref, origin, rationale):
    c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
              object_id=obj, claim_type=ClaimType.DEPENDENCY, purpose=purpose,
              scope=scope, scope_ref=ref, origin=origin, created_by_activity=interp,
              created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, rationale, DEP, rev))


def _ev(s, interp, eid, cid, source, excerpt, locator="openstax section", direct=False):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=cid, source_id=source,
        role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
        stance=EvidenceStance.SUPPORTS, locator=locator,
        excerpt=excerpt, excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def _item(s, interp, iid, tm_id, stem, options, key):
    s.add_entity(Item(id=iid, label=f"MCQ: {stem[:40]}", task_model_id=tm_id,
                      stem=stem, options=options, key=key, subject=SUBJ,
                      status=ClaimStatus.ACCEPTED, created_by_activity=interp))


def build_graph_v32() -> CDGStore:
    s = build_graph_v31()

    # ---- 037 waves/sound ----
    interp, rev = _base(s, "37", "Human review of waves batch.")
    _src(s, "SRC.OSX.UP1.15.1", "University Physics Volume 1, 15.1 Simple Harmonic Motion",
         "https://openstax.org/books/university-physics-volume-1/pages/15-1-simple-harmonic-motion")
    _src(s, "SRC.OSX.UP1.16.1", "University Physics Volume 1, 16.1 Traveling Waves",
         "https://openstax.org/books/university-physics-volume-1/pages/16-1-traveling-waves")
    _kc(s, interp, rev, "kc.wave_phenomena", "Wave motion, frequency and wave speed",
        "Relate frequency, wavelength and speed v = fλ; describe transverse/longitudinal waves and sound.")
    _tm(s, interp, rev, "tm.wave_problems", "Solve wave speed/frequency problems",
        ["kc.wave_phenomena"])
    _m(s, interp, rev, "m.wave_equation", "Apply v = fλ to find the unknown",
       "tm.wave_problems", ["kc.displacement_velocity", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre37.disp_waves", "kc.displacement_velocity", "kc.wave_phenomena",
         E, P.SPECIFIC_TASK_MODEL, "tm.wave_problems",
         ClaimOrigin.DERIVED, "DERIVED: wave method needs displacement/velocity ideas")
    _pre(s, interp, rev, "cl.pre37.alg_waves", "kc.algebraic_expressions", "kc.wave_phenomena",
         E, P.SPECIFIC_TASK_MODEL, "tm.wave_problems",
         ClaimOrigin.DERIVED, "Math→Physics: v=fλ rearrangement needs algebra")
    _ev(s, interp, "ev.p37.t", "cl.ptm.wave_problems.target.kc.wave_phenomena",
         "SRC.OSX.UP1.16.1", "Wave speed equals frequency times wavelength.", False)
    _item(s, interp, "it.physics.waves", "tm.wave_problems",
          "A wave has frequency 50 Hz and wavelength 6.8 m. Its speed is…",
          ["340 m/s", "7.35 m/s", "56.8 m/s", "0.136 m/s"], "340 m/s")

    # ---- 038 geometrical optics ----
    interp, rev = _base(s, "38", "Human review of optics batch.")
    _src(s, "SRC.OSX.UP3.2.1", "University Physics Volume 3, 2.1 Images Formed by Plane Mirrors",
         "https://openstax.org/books/university-physics-volume-3/pages/2-1-images-formed-by-plane-mirrors")
    _kc(s, interp, rev, "kc.geometrical_optics", "Reflection, refraction and image formation",
        "Apply laws of reflection/refraction; use mirror/lens equations for image problems.")
    _tm(s, interp, rev, "tm.optics_problems", "Solve reflection/refraction/image problems",
        ["kc.geometrical_optics"])
    _m(s, interp, rev, "m.mirror_lens_equation", "Apply the mirror/lens equation and magnification",
       "tm.optics_problems", ["kc.algebraic_expressions", "kc.ratio_proportion_rate"])
    _m(s, interp, rev, "m.reflection_refraction", "Trace rays with reflection/refraction laws",
       "tm.optics_problems", ["kc.triangle_angle_properties", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre38.alg_optics", "kc.algebraic_expressions", "kc.geometrical_optics",
         E, P.SPECIFIC_TASK_MODEL, "tm.optics_problems",
         ClaimOrigin.DERIVED, "Math→Physics: image equations need algebra")
    _pre(s, interp, rev, "cl.pre38.ratio_optics", "kc.ratio_proportion_rate", "kc.geometrical_optics",
         E, P.SPECIFIC_METHOD, "m.mirror_lens_equation",
         ClaimOrigin.DERIVED, "Math→Physics: magnification method needs ratio reasoning")
    _pre(s, interp, rev, "cl.pre38.tri_optics", "kc.triangle_angle_properties", "kc.geometrical_optics",
         PrerequisitePurpose.UNDERSTAND, P.ALL_RELEVANT_METHODS, None,
         ClaimOrigin.ASSERTED, "UNDERSTAND: ray angles need triangle-angle ideas")
    _ev(s, interp, "ev.p38.t", "cl.ptm.optics_problems.target.kc.geometrical_optics",
         "SRC.OSX.UP3.2.1", "Plane-mirror images from the law of reflection.", False)
    _item(s, interp, "it.physics.optics", "tm.optics_problems",
          "Angle of incidence 30°. Angle of reflection is…",
          ["30°", "60°", "15°", "90°"], "30°")

    # ---- 039 electric circuits ----
    interp, rev = _base(s, "39", "Human review of circuits batch.")
    _src(s, "SRC.OSX.UP2.9.4", "University Physics Volume 2, 9.4 Ohm's Law",
         "https://openstax.org/books/university-physics-volume-2/pages/9-4-ohms-law")
    _src(s, "SRC.OSX.UP2.10.3", "University Physics Volume 2, 10.3 Kirchhoff's Rules",
         "https://openstax.org/books/university-physics-volume-2/pages/10-3-kirchhoffs-rules")
    _kc(s, interp, rev, "kc.electric_circuits", "Current, voltage, resistance and circuits",
        "Apply Ohm's law; reduce series/parallel networks; apply Kirchhoff's rules to loops.")
    _tm(s, interp, rev, "tm.circuit_analysis", "Analyse DC circuits",
        ["kc.electric_circuits"])
    _m(s, interp, rev, "m.ohms_law", "Apply V = IR to a single loop",
       "tm.circuit_analysis", ["kc.algebraic_expressions", "kc.ratio_proportion_rate"])
    _m(s, interp, rev, "m.kirchhoff_loops", "Set up and solve loop equations",
       "tm.circuit_analysis", ["kc.simultaneous_linear_equations", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre39.alg_circuits", "kc.algebraic_expressions", "kc.electric_circuits",
         E, P.SPECIFIC_TASK_MODEL, "tm.circuit_analysis",
         ClaimOrigin.DERIVED, "Math→Physics: circuit equations need algebra")
    _pre(s, interp, rev, "cl.pre39.ratio_circuits", "kc.ratio_proportion_rate", "kc.electric_circuits",
         E, P.SPECIFIC_METHOD, "m.ohms_law",
         ClaimOrigin.DERIVED, "Math→Physics: Ohm's-law method needs ratio reasoning")
    _pre(s, interp, rev, "cl.pre39.simlin_circuits", "kc.simultaneous_linear_equations", "kc.electric_circuits",
         E, P.SPECIFIC_METHOD, "m.kirchhoff_loops",
         ClaimOrigin.DERIVED, "Math→Physics: multi-loop method needs simultaneous equations")
    _ev(s, interp, "ev.p39.t", "cl.ptm.circuit_analysis.target.kc.electric_circuits",
         "SRC.OSX.UP2.9.4", "Ohm's law relates current, voltage and resistance.", False)
    _ev(s, interp, "ev.p39.m2", "cl.p.own.m.kirchhoff_loops",
         "SRC.OSX.UP2.10.3", "Kirchhoff's loop rule for multi-loop circuits.", False)
    _item(s, interp, "it.physics.circuits", "tm.circuit_analysis",
          "A 12 V battery drives 2 A through a resistor. R = ?",
          ["6 Ω", "24 Ω", "10 Ω", "14 Ω"], "6 Ω")

    # ---- 040 electromagnetism / AC ----
    interp, rev = _base(s, "40", "Human review of EMI/AC batch.")
    _src(s, "SRC.OSX.UP2.13.1", "University Physics Volume 2, 13.1 Faraday's Law",
         "https://openstax.org/books/university-physics-volume-2/pages/13-1-faradays-law")
    _src(s, "SRC.OSX.UP2.15.2", "University Physics Volume 2, 15.2 Simple AC Circuits",
         "https://openstax.org/books/university-physics-volume-2/pages/15-2-simple-ac-circuits")
    _kc(s, interp, rev, "kc.electromagnetism", "Electromagnetic induction and AC basics",
        "Apply Faraday's law as a rate of flux change; describe simple AC circuit behaviour.")
    _tm(s, interp, rev, "tm.emi_ac_problems", "Solve induction/AC problems",
        ["kc.electromagnetism"])
    _m(s, interp, rev, "m.faraday_rate", "Compute emf as rate of flux change",
       "tm.emi_ac_problems", ["kc.rate_of_change", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre40.rate_emi", "kc.rate_of_change", "kc.electromagnetism",
         E, P.SPECIFIC_METHOD, "m.faraday_rate",
         ClaimOrigin.DERIVED, "Math→Physics: Faraday-rate method needs rate of change")
    _pre(s, interp, rev, "cl.pre40.alg_emi", "kc.algebraic_expressions", "kc.electromagnetism",
         E, P.SPECIFIC_TASK_MODEL, "tm.emi_ac_problems",
         ClaimOrigin.DERIVED, "Math→Physics: induction equations need algebra")
    _ev(s, interp, "ev.p40.t", "cl.ptm.emi_ac_problems.target.kc.electromagnetism",
         "SRC.OSX.UP2.13.1", "Induced emf equals the rate of change of magnetic flux.", False)

    # ---- 041 modern physics ----
    interp, rev = _base(s, "41", "Human review of modern-physics batch.")
    _src(s, "SRC.OSX.UP3.6.2", "University Physics Volume 3, 6.2 Photoelectric Effect",
         "https://openstax.org/books/university-physics-volume-3/pages/6-2-photoelectric-effect")
    _src(s, "SRC.OSX.UP3.10.1", "University Physics Volume 3, 10.1 Properties of Nuclei",
         "https://openstax.org/books/university-physics-volume-3/pages/10-1-properties-of-nuclei")
    _kc(s, interp, rev, "kc.atomic_nuclear_physics", "Atomic structure, photoelectric effect and nuclei",
        "Apply the photoelectric equation; describe nuclear composition and decay basics.")
    _tm(s, interp, rev, "tm.modern_physics_problems", "Solve photoelectric/nuclear problems",
        ["kc.atomic_nuclear_physics"])
    _m(s, interp, rev, "m.photoelectric_equation", "Apply Einstein's photoelectric equation",
       "tm.modern_physics_problems", ["kc.equations_in_indices", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre41.indices_modern", "kc.equations_in_indices", "kc.atomic_nuclear_physics",
         E, P.SPECIFIC_METHOD, "m.photoelectric_equation",
         ClaimOrigin.DERIVED, "Math→Physics: photon energies need index/scientific notation")
    _pre(s, interp, rev, "cl.pre41.alg_modern", "kc.algebraic_expressions", "kc.atomic_nuclear_physics",
         E, P.SPECIFIC_TASK_MODEL, "tm.modern_physics_problems",
         ClaimOrigin.DERIVED, "Math→Physics: modern-physics equations need algebra")
    _ev(s, interp, "ev.p41.t", "cl.ptm.modern_physics_problems.target.kc.atomic_nuclear_physics",
         "SRC.OSX.UP3.6.2", "Photoelectrons ejected when light exceeds threshold frequency.", False)
    _ev(s, interp, "ev.p41.nuc", "cl.ptm.modern_physics_problems.target.kc.atomic_nuclear_physics",
         "SRC.OSX.UP3.10.1", "Nuclei described by proton and nucleon numbers.", False)

    # ---- 042 practical graduation ----
    interp, rev = _base(s, "42", "Human review of practical-skills batch.")
    for kid in ("kc.practical_measurement", "kc.measurement_errors_precision"):
        k = s.entities[kid]
        k.status = ClaimStatus.ACCEPTED
        k.reviewed_by_activity = rev
        k.review_rationale = "Accepted in Phase 12B via human review of practical TM."
    _tm(s, interp, rev, "tm.practical_physics", "Carry out measurements and analyse data",
        ["kc.practical_measurement", "kc.measurement_errors_precision"])
    _m(s, interp, rev, "m.instrument_tabulate", "Read instruments and tabulate observations",
       "tm.practical_physics", ["kc.measurement_units_dimensions", "kc.integer_arithmetic"])
    _m(s, interp, rev, "m.plot_gradient", "Plot graphs and read gradients/intercepts",
       "tm.practical_physics", ["kc.measurement_units_dimensions", "kc.gradient"])
    _pre(s, interp, rev, "cl.pre42.units_practical", "kc.measurement_units_dimensions", "kc.practical_measurement",
         E, P.SPECIFIC_TASK_MODEL, "tm.practical_physics",
         ClaimOrigin.DERIVED, "DERIVED: practical methods need units/dimensions")
    _pre(s, interp, rev, "cl.pre42.grad_practical", "kc.gradient", "kc.practical_measurement",
         E, P.SPECIFIC_METHOD, "m.plot_gradient",
         ClaimOrigin.DERIVED, "Math→Physics: graph-plotting method needs gradient")
    _pre(s, interp, rev, "cl.pre42.int_practical", "kc.integer_arithmetic", "kc.practical_measurement",
         E, P.SPECIFIC_METHOD, "m.instrument_tabulate",
         ClaimOrigin.DERIVED, "Math→Physics: tabulation needs integer arithmetic")
    _ev(s, interp, "ev.p42.t", "cl.ptm.practical_physics.target.kc.practical_measurement",
         "SRC.WAEC.PHYSICS", "WAEC alternative-to-practical paper assesses measurement, tabulation and graph skills (detail pending official PDF).",
         locator="WAEC practical requirement (detail unverified)", direct=False)
    _ev(s, interp, "ev.p42.m2", "cl.p.own.m.plot_gradient",
         "SRC.OSX.UP1.2.2", "Component/plot reading from coordinate data.", False)
    return s
