"""Phase 14 Physics completion wave A: batches 059-061 (friction/machines,
EM spectrum depth, energy sources/society). Chains build_graph_v36."""
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
from examples.math_stats_closure import build_graph_v36
from examples._batchkit import accept

SUBJ = "Physics"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-15T11:10:00Z"
E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.q{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-15T11:00:00Z"))
    interp = f"act.q{nn}.interpret"
    rev = f"act.q{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-15T11:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-15T12:00:00Z",
                            rationale=note))
    return interp, rev


def _src(s, sid, title, url):
    if sid not in s.sources:
        s.add_source(Source(id=sid, title=title, identifier_or_url=url,
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
                            tier="reference"))


def _ev(s, interp, eid, cid, source, excerpt, direct=False):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=cid, source_id=source,
        role=EvidenceRole.DIRECT if direct else EvidenceRole.INDIRECT,
        stance=EvidenceStance.SUPPORTS, locator="openstax section",
        excerpt=excerpt, excerpt_kind=ExcerptKind.VERBATIM if direct else ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def build_graph_v37() -> CDGStore:
    s = build_graph_v36()

    # ---- 059 friction + machines ----
    interp, rev = _base(s, "59", "Human review of friction/machines batch.")
    _src(s, "SRC.OSX.UP1.6.2", "University Physics Volume 1, 6.2 Friction",
         "https://openstax.org/books/university-physics-volume-1/pages/6-2-friction")
    _kc = KnowledgeComponent(id="kc.friction", label="Frictional forces",
                             definition="Compute friction forces using the coefficient of friction; relate friction to work/energy losses.",
                             subject=SUBJ, status=ClaimStatus.ACCEPTED,
                             created_by_activity=interp, cdg_version="v0.2.0")
    _kc.reviewed_by_activity = rev
    _kc.review_rationale = "Accepted in Phase 14 via human review."
    s.add_entity(_kc)
    tm = TaskModel(id="tm.friction_machines", label="Solve friction and simple-machine problems",
                   subject=SUBJ, status=ClaimStatus.ACCEPTED,
                   created_by_activity=interp, cdg_version="v0.2.0")
    tm.reviewed_by_activity = rev
    s.add_entity(tm)
    m1 = Method(id="m.friction_calculation", label="Apply f = μN to find friction",
                task_model_id=tm.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    m1.reviewed_by_activity = rev
    m2 = Method(id="m.machine_efficiency", label="Compute efficiency / mechanical advantage",
                task_model_id=tm.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    m2.reviewed_by_activity = rev
    for mid, label in [("m.friction_calculation", "friction calculation"),
                       ("m.machine_efficiency", "machine efficiency")]:
        s.add_entity({"m.friction_calculation": m1, "m.machine_efficiency": m2}[mid])
        c = Claim(id=f"cl.q59.own.{mid}", predicate=RelationshipType.HAS_METHOD,
                  subject_id=tm.id, object_id=mid, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, "method ownership", ASSESS, rev))
    for cid, pred, subj, obj, rat in [
        ("cl.q59.target", RelationshipType.TARGETS, tm.id, _kc.id, "targets friction/machines"),
        ("cl.q59.req.m1.newton", RelationshipType.REQUIRES, m1.id, "kc.newtons_laws",
         "friction needs normal reaction (Newton)"),
        ("cl.q59.req.m1.alg", RelationshipType.REQUIRES, m1.id, "kc.algebraic_expressions",
         "friction equations need algebra"),
        ("cl.q59.req.m2.work", RelationshipType.REQUIRES, m2.id, "kc.work_energy_power",
         "efficiency needs work/energy"),
        ("cl.q59.req.m2.ratio", RelationshipType.REQUIRES, m2.id, "kc.ratio_proportion_rate",
         "efficiency needs ratio reasoning"),
    ]:
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=(ClaimType.ASSESSMENT_DESIGN if pred == RelationshipType.TARGETS
                              else ClaimType.DEPENDENCY),
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, (ASSESS if pred == RelationshipType.TARGETS else DEP), rev))
    for cid, subj, ref, purpose, rat in [
        ("cl.pre59.newton_friction", "kc.newtons_laws", None, PrerequisitePurpose.EXECUTE,
         "DERIVED: friction needs Newton's laws"),
        ("cl.pre59.work_friction", "kc.work_energy_power", None, PrerequisitePurpose.EXECUTE,
         "DERIVED: machine efficiency needs work/energy"),
    ]:
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
                  object_id=_kc.id, claim_type=ClaimType.DEPENDENCY, purpose=purpose,
                  scope=P.SPECIFIC_TASK_MODEL, scope_ref=tm.id,
                  origin=ClaimOrigin.DERIVED, created_by_activity=interp,
                  created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, DEP, rev))
    _ev(s, interp, "ev.q59.t", "cl.q59.target", "SRC.OSX.UP1.6.2",
        "Friction opposes relative motion; proportional to the normal force.", False)
    _ev(s, interp, "ev.q59.m2", "cl.q59.own.m.machine_efficiency",
        "SRC.OSX.UP1.6.2", "Machines trade force for distance, losing energy to friction.", False)

    # ---- 060 EM spectrum depth ----
    interp, rev = _base(s, "60", "Human review of EM-spectrum batch.")
    _src(s, "SRC.OSX.UP2.16.5", "University Physics Volume 2, 16.5 The Electromagnetic Spectrum",
         "https://openstax.org/books/university-physics-volume-2/pages/16-5-the-electromagnetic-spectrum")
    k2 = KnowledgeComponent(id="kc.em_spectrum",
                            label="Electromagnetic spectrum ordering and properties",
                            definition="Order the EM spectrum by wavelength/frequency; relate wavelength to energy and applications.",
                            subject=SUBJ, status=ClaimStatus.ACCEPTED,
                            created_by_activity=interp, cdg_version="v0.2.0")
    k2.reviewed_by_activity = rev
    s.add_entity(k2)
    t2 = TaskModel(id="tm.em_spectrum_problems",
                   label="Classify EM radiation and compare properties",
                   subject=SUBJ, status=ClaimStatus.ACCEPTED,
                   created_by_activity=interp, cdg_version="v0.2.0")
    t2.reviewed_by_activity = rev
    s.add_entity(t2)
    mm = Method(id="m.spectrum_ordering", label="Place radiation in the spectrum using wavelength/frequency",
                task_model_id=t2.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    mm.reviewed_by_activity = rev
    s.add_entity(mm)
    for cid, pred, subj, obj, rat in [
        ("cl.q60.target", RelationshipType.TARGETS, t2.id, k2.id, "targets EM spectrum"),
        ("cl.q60.own", RelationshipType.HAS_METHOD, t2.id, mm.id, "method ownership"),
        ("cl.q60.req.wave", RelationshipType.REQUIRES, mm.id, "kc.wave_phenomena",
         "spectrum needs wave properties"),
        ("cl.q60.req.alg", RelationshipType.REQUIRES, mm.id, "kc.algebraic_expressions",
         "wavelength/frequency relations need algebra"),
    ]:
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=(ClaimType.ASSESSMENT_DESIGN
                              if pred in (RelationshipType.TARGETS,) else ClaimType.DEPENDENCY),
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        if pred == RelationshipType.HAS_METHOD:
            c.claim_type = ClaimType.ASSESSMENT_DESIGN
        s.add_claim(accept(c, rat, (ASSESS if pred != RelationshipType.REQUIRES else DEP), rev))
    c = Claim(id="cl.pre60.wave_spectrum", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.wave_phenomena", object_id=k2.id,
              claim_type=ClaimType.DEPENDENCY, purpose=E,
              scope=P.SPECIFIC_TASK_MODEL, scope_ref=t2.id, origin=ClaimOrigin.DERIVED,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "DERIVED: spectrum method needs wave properties", DEP, rev))
    _ev(s, interp, "ev.q60.t", "cl.q60.target", "SRC.OSX.UP2.16.5",
        "The EM spectrum ordered by increasing frequency/energy.", False)

    # ---- 061 sources of energy / energy and society ----
    interp, rev = _base(s, "61", "Human review of energy-sources batch.")
    _src(s, "SRC.OSX.UP1.8.5", "University Physics Volume 1, 8.5 Sources of Energy",
         "https://openstax.org/books/university-physics-volume-1/pages/8-5-sources-of-energy")
    k3 = KnowledgeComponent(id="kc.energy_sources",
                            label="Sources of energy: renewable and non-renewable",
                            definition="Classify energy sources; distinguish renewable from non-renewable in societal context.",
                            subject=SUBJ, status=ClaimStatus.ACCEPTED,
                            created_by_activity=interp, cdg_version="v0.2.0")
    k3.reviewed_by_activity = rev
    s.add_entity(k3)
    t3 = TaskModel(id="tm.classify_energy_sources",
                   label="Classify energy sources and their uses",
                   subject=SUBJ, status=ClaimStatus.ACCEPTED,
                   created_by_activity=interp, cdg_version="v0.2.0")
    t3.reviewed_by_activity = rev
    s.add_entity(t3)
    m3 = Method(id="m.renewable_classification",
                label="Distinguish renewable from non-renewable sources with examples",
                task_model_id=t3.id, subject=SUBJ, status=ClaimStatus.ACCEPTED,
                created_by_activity=interp, cdg_version="v0.2.0")
    m3.reviewed_by_activity = rev
    s.add_entity(m3)
    for cid, pred, subj, obj, rat in [
        ("cl.q61.target", RelationshipType.TARGETS, t3.id, k3.id, "targets energy sources"),
        ("cl.q61.own", RelationshipType.HAS_METHOD, t3.id, m3.id, "method ownership"),
        ("cl.q61.req.work", RelationshipType.REQUIRES, m3.id, "kc.work_energy_power",
         "classification needs energy transformation ideas"),
    ]:
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=(ClaimType.ASSESSMENT_DESIGN
                              if pred != RelationshipType.REQUIRES else ClaimType.DEPENDENCY),
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, (ASSESS if pred != RelationshipType.REQUIRES else DEP), rev))
    c = Claim(id="cl.pre61.work_sources", predicate=RelationshipType.PREREQUISITE,
              subject_id="kc.work_energy_power", object_id=k3.id,
              claim_type=ClaimType.DEPENDENCY, purpose=E,
              scope=P.SPECIFIC_TASK_MODEL, scope_ref=t3.id, origin=ClaimOrigin.DERIVED,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "DERIVED: classification needs work/energy", DEP, rev))
    _ev(s, interp, "ev.q61.t", "cl.q61.target", "SRC.OSX.UP1.8.5",
        "Energy sources classified as renewable or non-renewable.", False)
    return s
