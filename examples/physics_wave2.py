"""Phase 12B Physics expansion A: batches 031-036 (vectors, work/energy,
momentum, gravitation, fluids, heat). Each batch: KC + TM + Methods +
requires + prerequisite claims + evidence + human review."""
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
from examples.physics_slice import build_graph_v30
from examples._batchkit import accept

SUBJ = "Physics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-10T10:10:00Z"


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.p{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-10T10:00:00Z"))
    interp = f"act.p{nn}.interpret"
    rev = f"act.p{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-10T10:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-10T11:00:00Z",
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


def _ev(s, interp, eid, cid, source, excerpt, direct=False):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=cid, source_id=source,
        role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
        stance=EvidenceStance.SUPPORTS, locator="openstax section",
        excerpt=excerpt, excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def _item(s, interp, iid, tm_id, stem, options, key):
    s.add_entity(Item(id=iid, label=f"MCQ: {stem[:40]}", task_model_id=tm_id,
                      stem=stem, options=options, key=key, subject=SUBJ,
                      status=ClaimStatus.ACCEPTED, created_by_activity=interp))


def build_graph_v31() -> CDGStore:
    s = build_graph_v30()

    # ---- 031 vectors ----
    interp, rev = _base(s, "31", "Human review of vectors batch.")
    _src(s, "SRC.OSX.UP1.2.2", "University Physics Volume 1, 2.2 Coordinate Systems and Components of a Vector",
         "https://openstax.org/books/university-physics-volume-1/pages/2-2-coordinate-systems-and-components-of-a-vector")
    _kc(s, interp, rev, "kc.scalar_vector_quantities", "Scalars, vectors and vector resolution",
        "Distinguish scalar and vector quantities; resolve vectors into components.")
    _tm(s, interp, rev, "tm.resolve_vectors", "Classify quantities and resolve vectors",
        ["kc.scalar_vector_quantities"])
    _m(s, interp, rev, "m.classify_quantities", "Classify as scalar or vector",
       "tm.resolve_vectors", ["kc.measurement_units_dimensions"])
    _m(s, interp, rev, "m.resolve_components", "Resolve into components with trigonometry",
       "tm.resolve_vectors", ["kc.trig_ratios_acute", "kc.algebraic_expressions"])
    E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope
    _pre(s, interp, rev, "cl.pre31.units_vectors", "kc.measurement_units_dimensions",
         "kc.scalar_vector_quantities", E, P.SPECIFIC_METHOD, "m.classify_quantities",
         ClaimOrigin.DERIVED, "DERIVED: classification method needs units/dimensions")
    _pre(s, interp, rev, "cl.pre31.trig_vectors", "kc.trig_ratios_acute",
         "kc.scalar_vector_quantities", E, P.SPECIFIC_METHOD, "m.resolve_components",
         ClaimOrigin.DERIVED, "Math→Physics: resolution needs trig ratios")
    _pre(s, interp, rev, "cl.pre31.alg_vectors", "kc.algebraic_expressions",
         "kc.scalar_vector_quantities", E, P.SPECIFIC_METHOD, "m.resolve_components",
         ClaimOrigin.DERIVED, "Math→Physics: component equations need algebra")
    _ev(s, interp, "ev.p31.t", "cl.ptm.resolve_vectors.target.kc.scalar_vector_quantities",
         "SRC.OSX.UP1.2.2", "Vector components from magnitude and direction.", False)
    _ev(s, interp, "ev.p31.x", "cl.pre31.trig_vectors",
         "SRC.OSX.UP1.2.2", "Component equations use sine and cosine.", False)
    _item(s, interp, "it.physics.vectors", "tm.resolve_vectors",
          "A 10 N force acts at 30° to the x-axis. Its x-component is…",
          ["8.66 N", "5 N", "10 N", "17.3 N"], "8.66 N")

    # ---- 032 work/energy/power ----
    interp, rev = _base(s, "32", "Human review of work/energy batch.")
    _src(s, "SRC.OSX.UP1.7.1", "University Physics Volume 1, 7.1 Work",
         "https://openstax.org/books/university-physics-volume-1/pages/7-1-work")
    _src(s, "SRC.OSX.UP1.7.3", "University Physics Volume 1, 7.3 Work-Energy Theorem",
         "https://openstax.org/books/university-physics-volume-1/pages/7-3-work-energy-theorem")
    _src(s, "SRC.OSX.UP1.8.1", "University Physics Volume 1, 8.1 Potential Energy of a System",
         "https://openstax.org/books/university-physics-volume-1/pages/8-1-potential-energy-of-a-system")
    _kc(s, interp, rev, "kc.work_energy_power", "Work, energy and power",
        "Compute work from force and displacement; apply energy conservation; compute power.")
    _tm(s, interp, rev, "tm.work_energy_problems", "Solve work/energy/power problems",
        ["kc.work_energy_power"])
    _m(s, interp, rev, "m.work_from_force", "Compute W = F·d from force and displacement",
       "tm.work_energy_problems", ["kc.newtons_laws", "kc.algebraic_expressions"])
    _m(s, interp, rev, "m.power_as_rate", "Compute power as energy per unit time",
       "tm.work_energy_problems", ["kc.newtons_laws", "kc.algebraic_expressions", "kc.rate_of_change"])
    _pre(s, interp, rev, "cl.pre32.newton_work", "kc.newtons_laws", "kc.work_energy_power",
         E, P.SPECIFIC_TASK_MODEL, "tm.work_energy_problems",
         ClaimOrigin.DERIVED, "DERIVED: every work/energy method needs Newton's laws")
    _pre(s, interp, rev, "cl.pre32.alg_work", "kc.algebraic_expressions", "kc.work_energy_power",
         E, P.SPECIFIC_TASK_MODEL, "tm.work_energy_problems",
         ClaimOrigin.DERIVED, "Math→Physics: work/energy equations need algebra")
    _pre(s, interp, rev, "cl.pre32.rate_work", "kc.rate_of_change", "kc.work_energy_power",
         E, P.SPECIFIC_METHOD, "m.power_as_rate",
         ClaimOrigin.DERIVED, "Math→Physics: power-as-rate needs rate of change")
    _ev(s, interp, "ev.p32.t", "cl.ptm.work_energy_problems.target.kc.work_energy_power",
         "SRC.OSX.UP1.7.3", "Work-energy theorem relates net work to kinetic-energy change.", False)
    _ev(s, interp, "ev.p32.x", "cl.pre32.rate_work",
         "SRC.OSX.UP1.7.1", "Power is the rate of doing work.", False)

    # ---- 033 momentum ----
    interp, rev = _base(s, "33", "Human review of momentum batch.")
    _src(s, "SRC.OSX.UP1.9.1", "University Physics Volume 1, 9.1 Linear Momentum",
         "https://openstax.org/books/university-physics-volume-1/pages/9-1-linear-momentum")
    _kc(s, interp, rev, "kc.linear_momentum", "Linear momentum and its conservation",
        "Compute momentum p = mv; apply conservation in collisions.")
    _tm(s, interp, rev, "tm.momentum_problems", "Solve momentum and collision problems",
        ["kc.linear_momentum"])
    _m(s, interp, rev, "m.conservation_collisions", "Apply momentum conservation to collisions",
       "tm.momentum_problems", ["kc.newtons_laws", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre33.newton_mom", "kc.newtons_laws", "kc.linear_momentum",
         E, P.SPECIFIC_TASK_MODEL, "tm.momentum_problems",
         ClaimOrigin.DERIVED, "DERIVED: momentum method needs Newton's laws")
    _pre(s, interp, rev, "cl.pre33.alg_mom", "kc.algebraic_expressions", "kc.linear_momentum",
         E, P.SPECIFIC_TASK_MODEL, "tm.momentum_problems",
         ClaimOrigin.DERIVED, "Math→Physics: momentum equations need algebra")
    _ev(s, interp, "ev.p33.t", "cl.ptm.momentum_problems.target.kc.linear_momentum",
         "SRC.OSX.UP1.9.1", "Momentum is the product of mass and velocity.", False)

    # ---- 034 gravitation ----
    interp, rev = _base(s, "34", "Human review of gravitation batch.")
    _src(s, "SRC.OSX.UP1.13.1", "University Physics Volume 1, 13.1 Newton's Law of Universal Gravitation",
         "https://openstax.org/books/university-physics-volume-1/pages/13-1-newtons-law-of-universal-gravitation")
    _kc(s, interp, rev, "kc.gravitation", "Gravitation and gravitational field",
        "Apply Newton's law of gravitation; relate g to orbital/satellite motion.")
    _tm(s, interp, rev, "tm.gravitation_problems", "Solve gravitation and g-field problems",
        ["kc.gravitation"])
    _m(s, interp, rev, "m.inverse_square", "Apply the inverse-square gravitation law",
       "tm.gravitation_problems", ["kc.newtons_laws", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre34.newton_grav", "kc.newtons_laws", "kc.gravitation",
         E, P.SPECIFIC_TASK_MODEL, "tm.gravitation_problems",
         ClaimOrigin.DERIVED, "DERIVED: gravitation method needs Newton's laws")
    _pre(s, interp, rev, "cl.pre34.alg_grav", "kc.algebraic_expressions", "kc.gravitation",
         E, P.SPECIFIC_TASK_MODEL, "tm.gravitation_problems",
         ClaimOrigin.DERIVED, "Math→Physics: inverse-square equations need algebra")
    _ev(s, interp, "ev.p34.t", "cl.ptm.gravitation_problems.target.kc.gravitation",
         "SRC.OSX.UP1.13.1", "Gravitational force follows an inverse-square law.", False)

    # ---- 035 fluids/pressure ----
    interp, rev = _base(s, "35", "Human review of fluids batch.")
    _src(s, "SRC.OSX.UP1.14.1", "University Physics Volume 1, 14.1 Fluids, Density, and Pressure",
         "https://openstax.org/books/university-physics-volume-1/pages/14-1-fluids-density-and-pressure")
    _kc(s, interp, rev, "kc.pressure_fluids", "Density, pressure and fluids at rest",
        "Compute density and hydrostatic pressure; relate pressure to depth.")
    _tm(s, interp, rev, "tm.fluid_pressure_problems", "Solve density/pressure problems",
        ["kc.pressure_fluids"])
    _m(s, interp, rev, "m.hydrostatic", "Apply p = ρgh for fluids at rest",
       "tm.fluid_pressure_problems", ["kc.ratio_proportion_rate", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre35.ratio_fluids", "kc.ratio_proportion_rate", "kc.pressure_fluids",
         E, P.SPECIFIC_TASK_MODEL, "tm.fluid_pressure_problems",
         ClaimOrigin.DERIVED, "Math→Physics: density/pressure ratios need ratio reasoning")
    _pre(s, interp, rev, "cl.pre35.alg_fluids", "kc.algebraic_expressions", "kc.pressure_fluids",
         E, P.SPECIFIC_TASK_MODEL, "tm.fluid_pressure_problems",
         ClaimOrigin.DERIVED, "Math→Physics: hydrostatic equations need algebra")
    _ev(s, interp, "ev.p35.t", "cl.ptm.fluid_pressure_problems.target.kc.pressure_fluids",
         "SRC.OSX.UP1.14.1", "Pressure in a fluid increases with depth.", False)

    # ---- 036 heat/temperature ----
    interp, rev = _base(s, "36", "Human review of heat batch.")
    _src(s, "SRC.OSX.UP2.1.1", "University Physics Volume 2, 1.1 Temperature and Thermal Equilibrium",
         "https://openstax.org/books/university-physics-volume-2/pages/1-1-temperature-and-thermal-equilibrium")
    _kc(s, interp, rev, "kc.heat_temperature", "Heat, temperature and thermal behaviour",
        "Use calorimetry Q = mcΔθ and gas-law relations for thermal problems.")
    _tm(s, interp, rev, "tm.thermal_problems", "Solve heat/temperature/gas problems",
        ["kc.heat_temperature"])
    _m(s, interp, rev, "m.calorimetry", "Apply Q = mcΔθ to heating problems",
       "tm.thermal_problems", ["kc.algebraic_expressions", "kc.integer_arithmetic"])
    _m(s, interp, rev, "m.gas_law", "Apply gas-law proportions at constant conditions",
       "tm.thermal_problems", ["kc.algebraic_expressions", "kc.ratio_proportion_rate"])
    _pre(s, interp, rev, "cl.pre36.alg_heat", "kc.algebraic_expressions", "kc.heat_temperature",
         E, P.SPECIFIC_TASK_MODEL, "tm.thermal_problems",
         ClaimOrigin.DERIVED, "Math→Physics: thermal equations need algebra")
    _pre(s, interp, rev, "cl.pre36.ratio_heat", "kc.ratio_proportion_rate", "kc.heat_temperature",
         E, P.SPECIFIC_METHOD, "m.gas_law",
         ClaimOrigin.DERIVED, "Math→Physics: gas-law method needs ratio reasoning")
    _pre(s, interp, rev, "cl.pre36.int_heat", "kc.integer_arithmetic", "kc.heat_temperature",
         E, P.SPECIFIC_METHOD, "m.calorimetry",
         ClaimOrigin.DERIVED, "Math→Physics: calorimetry arithmetic needs integers")
    _ev(s, interp, "ev.p36.t", "cl.ptm.thermal_problems.target.kc.heat_temperature",
         "SRC.OSX.UP2.1.1", "Temperature measures average kinetic energy; heat flows on difference.", False)
    return s
