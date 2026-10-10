"""Phase 13.5 closure fixes: kc.logarithms (Math, JAMB I.3) + kc.ph_scale
(Chemistry). Resolves the pH DEPENDENCY_BLOCKER. Chains build_graph_v34."""
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
from examples.chem_wave2 import build_graph_v34
from examples._batchkit import accept

ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-10T16:10:00Z"
E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.x{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-10T16:00:00Z"))
    interp = f"act.x{nn}.interpret"
    rev = f"act.x{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-10T16:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-10T17:00:00Z",
                            rationale=note))
    return interp, rev


def build_graph_v35() -> CDGStore:
    s = build_graph_v34()

    # ---- logarithms (Math) ----
    interp, rev = _base(s, "55", "Human review of logarithms closure batch.")
    if "SRC.OSX.IA2E.10.4" not in s.sources:
        s.add_source(Source(id="SRC.OSX.IA2E.10.4",
                            title="Intermediate Algebra 2e, 10.4 Use the Properties of Logarithms",
                            identifier_or_url="https://openstax.org/books/intermediate-algebra-2e/pages/10-4-use-the-properties-of-logarithms",
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
                            tier="reference"))
    k = KnowledgeComponent(id="kc.logarithms", label="Logarithms and their laws",
                           definition="Evaluate logarithms; apply product/quotient/power laws; convert between exponential and logarithmic form.",
                           subject="Mathematics", status=ClaimStatus.ACCEPTED,
                           legacy_ids=["MATH.NUM.LOGARITHM_CONCEPT", "MATH.NUM.LAWS_OF_LOGARITHMS",
                                       "MATH.NUM.LOG_ANY_BASE"],
                           created_by_activity=interp, cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = "Accepted in Phase 13.5 via human review."
    s.add_entity(k)
    t = TaskModel(id="tm.logarithm_problems", label="Evaluate and manipulate logarithms",
                  status=ClaimStatus.ACCEPTED, created_by_activity=interp, cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    for mid, mlab in [("m.convert_exp_log", "Convert between exponential and logarithmic form"),
                      ("m.apply_log_laws", "Simplify using logarithm laws")]:
        m = Method(id=mid, label=mlab, task_model_id=t.id,
                   status=ClaimStatus.ACCEPTED, created_by_activity=interp, cdg_version="v0.2.0")
        m.reviewed_by_activity = rev
        s.add_entity(m)
        for cid, pred, subj, obj, ctype, rat, bases in [
            (f"cl.x55.own.{mid}", RelationshipType.HAS_METHOD, t.id, mid,
             ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS),
            (f"cl.x55.req.{mid}.indices", RelationshipType.REQUIRES, mid, "kc.equations_in_indices",
             ClaimType.DEPENDENCY, f"{mid} requires index laws", DEP),
            (f"cl.x55.req.{mid}.alg", RelationshipType.REQUIRES, mid, "kc.algebraic_expressions",
             ClaimType.DEPENDENCY, f"{mid} requires algebra", DEP),
        ]:
            c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                      claim_type=ctype, created_by_activity=interp,
                      created_at=STAMP, cdg_version="v0.2.0")
            s.add_claim(accept(c, rat, bases, rev))
    c = Claim(id="cl.x55.target", predicate=RelationshipType.TARGETS, subject_id=t.id,
              object_id=k.id, claim_type=ClaimType.ASSESSMENT_DESIGN,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "targets logarithms", ASSESS, rev))
    for cid, subj, scope, ref, rat in [
        ("cl.pre55.indices_log", "kc.equations_in_indices", P.SPECIFIC_TASK_MODEL, "tm.logarithm_problems",
         "DERIVED: both log methods need index laws"),
        ("cl.pre55.alg_log", "kc.algebraic_expressions", P.SPECIFIC_TASK_MODEL, "tm.logarithm_problems",
         "Math: log manipulation needs algebra"),
    ]:
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
                  object_id=k.id, claim_type=ClaimType.DEPENDENCY, purpose=E,
                  scope=scope, scope_ref=ref, origin=ClaimOrigin.DERIVED,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, DEP, rev))
    for eid, cid, src, exc, leg, locator in [
        ("ev.x55.t", "cl.x55.target", "SRC.OSX.IA2E.10.4",
         "Logarithm laws: product, quotient and power rules.", None, "openstax section"),
        ("ev.x55.leg1", "cl.x55.target", "SRC.JAMB.UTME.MATH",
         "Node listed/entailed in JAMB syllabus: I.3(g).", "E0458", "legacy JAMB pointer"),
        ("ev.x55.leg2", "cl.pre55.indices_log", "SRC.JAMB.UTME.MATH",
         "Node listed/entailed in JAMB syllabus: I.3(d).", "E0459", "legacy JAMB pointer"),
    ]:
        s.add_evidence(EvidenceItem(
            id=eid, claim_id=cid, source_id=src,
            role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS, locator=locator,
            excerpt=exc, excerpt_kind=ExcerptKind.PARAPHRASE,
            extracted_by_activity=interp,
            inherited_from_legacy=bool(leg), legacy_id=leg))

    # ---- pH scale (Chemistry) ----
    interp, rev = _base(s, "56", "Human review of pH closure batch.")
    if "SRC.OSX.CHEM2E.14.2" not in s.sources:
        s.add_source(Source(id="SRC.OSX.CHEM2E.14.2",
                            title="OpenStax Chemistry 2e, 14.2 pH and pOH",
                            identifier_or_url="https://openstax.org/books/chemistry-2e/pages/14-2-ph-and-poh",
                            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
                            tier="reference"))
    k2 = KnowledgeComponent(id="kc.ph_scale", label="pH scale and calculations",
                            definition="Compute pH from hydrogen-ion concentration and interpret the pH scale.",
                            subject="Chemistry", status=ClaimStatus.ACCEPTED,
                            created_by_activity=interp, cdg_version="v0.2.0")
    k2.reviewed_by_activity = rev
    k2.review_rationale = "Accepted in Phase 13.5 via human review."
    s.add_entity(k2)
    t2 = TaskModel(id="tm.ph_problems", label="Compute pH from concentration",
                   status=ClaimStatus.ACCEPTED, subject="Chemistry",
                   created_by_activity=interp, cdg_version="v0.2.0")
    t2.reviewed_by_activity = rev
    s.add_entity(t2)
    m2 = Method(id="m.ph_from_concentration", label="Apply pH = -log[H+]",
                task_model_id=t2.id, subject="Chemistry",
                status=ClaimStatus.ACCEPTED, created_by_activity=interp, cdg_version="v0.2.0")
    m2.reviewed_by_activity = rev
    s.add_entity(m2)
    for cid, pred, subj, obj, ctype, rat, bases in [
        ("cl.x56.target", RelationshipType.TARGETS, t2.id, k2.id,
         ClaimType.ASSESSMENT_DESIGN, "targets pH calculations", ASSESS),
        ("cl.x56.own", RelationshipType.HAS_METHOD, t2.id, m2.id,
         ClaimType.ASSESSMENT_DESIGN, "method ownership", ASSESS),
        ("cl.x56.req.log", RelationshipType.REQUIRES, m2.id, "kc.logarithms",
         ClaimType.DEPENDENCY, "pH needs logarithms", DEP),
        ("cl.x56.req.acids", RelationshipType.REQUIRES, m2.id, "kc.acids_bases_salts",
         ClaimType.DEPENDENCY, "pH needs acid/base ideas", DEP),
        ("cl.x56.req.alg", RelationshipType.REQUIRES, m2.id, "kc.algebraic_expressions",
         ClaimType.DEPENDENCY, "pH needs algebra", DEP),
    ]:
        c = Claim(id=cid, predicate=pred, subject_id=subj, object_id=obj,
                  claim_type=ctype, created_by_activity=interp,
                  created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, bases, rev))
    for cid, subj, scope, ref, rat in [
        ("cl.pre56.log_ph", "kc.logarithms", P.SPECIFIC_METHOD, "m.ph_from_concentration",
         "Math→Chemistry: pH method needs logarithms (unblocks Phase 13 item)"),
        ("cl.pre56.acids_ph", "kc.acids_bases_salts", P.SPECIFIC_TASK_MODEL, "tm.ph_problems",
         "DERIVED: pH method needs acid/base ideas"),
        ("cl.pre56.alg_ph", "kc.algebraic_expressions", P.SPECIFIC_TASK_MODEL, "tm.ph_problems",
         "Math→Chemistry: pH arithmetic needs algebra"),
    ]:
        c = Claim(id=cid, predicate=RelationshipType.PREREQUISITE, subject_id=subj,
                  object_id=k2.id, claim_type=ClaimType.DEPENDENCY, purpose=E,
                  scope=scope, scope_ref=ref, origin=ClaimOrigin.DERIVED,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, rat, DEP, rev))
    s.add_evidence(EvidenceItem(
        id="ev.x56.t", claim_id="cl.x56.target", source_id="SRC.OSX.CHEM2E.14.2",
        role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS, locator="openstax section",
        excerpt="pH defined as the negative logarithm of hydrogen-ion concentration.",
        excerpt_kind=ExcerptKind.PARAPHRASE, extracted_by_activity=interp))
    s.add_entity(Item(id="it.chem.ph", label="MCQ: pH of 0.01 M HCl", task_model_id=t2.id,
                      stem="[H+] = 0.01 mol/dm³. pH = ?", options=["2", "4", "12", "0.01"],
                      key="2", subject="Chemistry",
                      status=ClaimStatus.ACCEPTED, created_by_activity=interp))
    return s
