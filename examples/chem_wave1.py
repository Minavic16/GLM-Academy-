"""Phase 13 Chemistry wave 1: batches 043-047 (matter, atomic structure,
bonding, mole/stoichiometry, acids/bases). Chains from build_graph_v32."""
from __future__ import annotations

from cdg.claims import Claim
from cdg.entities import Item, KnowledgeComponent, Method, Subject, TaskModel
from cdg.enums import (AcceptanceBasis, ActivityType, ClaimOrigin, ClaimStatus,
                       ClaimType, EvidenceRole, EvidenceStance, ExcerptKind,
                       PrerequisitePurpose, PrerequisiteScope, RelationshipType,
                       SourceType)
from cdg.evidence import EvidenceItem
from cdg.provenance import Activity, Source
from cdg.store import CDGStore
from examples.physics_wave3 import build_graph_v32
from examples._batchkit import accept

SUBJ = "Chemistry"
ASSESS = (AcceptanceBasis.EXPERT,)
DEP = (AcceptanceBasis.EXPERT, AcceptanceBasis.EMPIRICAL)
STAMP = "2026-10-10T14:10:00Z"
E, P = PrerequisitePurpose.EXECUTE, PrerequisiteScope


def _base(s, nn, note):
    s.add_activity(Activity(id=f"act.c{nn}.extract", type=ActivityType.EXTRACTION,
                            agent_id="agent.ai.glm", time="2026-10-10T14:00:00Z"))
    interp = f"act.c{nn}.interpret"
    rev = f"act.c{nn}.review"
    s.add_activity(Activity(id=interp, type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-10T14:05:00Z"))
    s.add_activity(Activity(id=rev, type=ActivityType.REVIEW,
                            agent_id="agent.human.reviewer", time="2026-10-10T15:00:00Z",
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
    k.review_rationale = "Accepted in Phase 13 via human review."
    s.add_entity(k)
    return k


def _tm(s, interp, rev, tm_id, label, targets):
    t = TaskModel(id=tm_id, label=label, status=ClaimStatus.ACCEPTED, subject=SUBJ,
                  created_by_activity=interp, cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    for k in targets:
        c = Claim(id=f"cl.c{tm_id}.target.{k}", predicate=RelationshipType.TARGETS,
                  subject_id=tm_id, object_id=k, claim_type=ClaimType.ASSESSMENT_DESIGN,
                  created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
        s.add_claim(accept(c, f"{tm_id} targets {k}", ASSESS, rev))
    return t


def _m(s, interp, rev, m_id, label, tm_id, reqs):
    m = Method(id=m_id, label=label, task_model_id=tm_id, subject=SUBJ,
               status=ClaimStatus.ACCEPTED, created_by_activity=interp, cdg_version="v0.2.0")
    m.reviewed_by_activity = rev
    s.add_entity(m)
    c = Claim(id=f"cl.c.own.{m_id}", predicate=RelationshipType.HAS_METHOD,
              subject_id=tm_id, object_id=m_id, claim_type=ClaimType.ASSESSMENT_DESIGN,
              created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, f"{m_id} owned by {tm_id}", ASSESS, rev))
    for k in reqs:
        c = Claim(id=f"cl.c.req.{m_id}.{k}", predicate=RelationshipType.REQUIRES,
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


def build_graph_v33() -> CDGStore:
    s = build_graph_v32()
    if "sub.chemistry" not in s.entities:
        s.add_entity(Subject(id="sub.chemistry", label="Chemistry", subject="Chemistry",
                             status=ClaimStatus.ACCEPTED, created_by_activity="act.c43.interpret",
                             cdg_version="v0.2.0", legacy_ids=[]))
    s.add_activity(Activity(id="act.c43.interpret", type=ActivityType.INTERPRETATION,
                            agent_id="agent.ai.glm", time="2026-10-10T14:05:00Z"))

    # ---- 043 matter ----
    interp, rev = _base(s, "43", "Human review of matter batch.")
    _src(s, "SRC.OSX.CHEM2E.1.2", "OpenStax Chemistry 2e, 1.2 Phases and Classification of Matter",
         "https://openstax.org/books/chemistry-2e/pages/1-2-phases-and-classification-of-matter")
    _kc(s, interp, rev, "kc.matter_classification", "Elements, compounds, mixtures and separation",
        "Classify matter as element/compound/mixture; choose separation techniques.")
    _tm(s, interp, rev, "tm.classify_matter", "Classify matter and separate mixtures",
        ["kc.matter_classification"])
    _m(s, interp, rev, "m.separate_mixtures", "Select filtration/distillation/chromatography by property",
       "tm.classify_matter", ["kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre43.alg_matter", "kc.algebraic_expressions", "kc.matter_classification",
         E, P.SPECIFIC_TASK_MODEL, "tm.classify_matter",
         ClaimOrigin.DERIVED, "Math→Chemistry: quantitative comparison needs algebra")
    _ev(s, interp, "ev.c43.t", "cl.ctm.classify_matter.target.kc.matter_classification",
         "SRC.OSX.CHEM2E.1.2", "Matter classified as element, compound, or mixture.", False)

    # ---- 044 atomic structure ----
    interp, rev = _base(s, "44", "Human review of atomic-structure batch.")
    _src(s, "SRC.OSX.CHEM2E.2.1", "OpenStax Chemistry 2e, 2.1 Early Ideas in Atomic Theory",
         "https://openstax.org/books/chemistry-2e/pages/2-1-early-ideas-in-atomic-theory")
    _kc(s, interp, rev, "kc.atomic_structure_periodicity", "Atomic structure and the periodic table",
        "Describe subatomic particles, electron arrangement, groups/periods and periodic trends.")
    _tm(s, interp, rev, "tm.atomic_model_problems", "Deduce structure and predict periodic trends",
        ["kc.atomic_structure_periodicity"])
    _m(s, interp, rev, "m.electron_arrangement", "Write electron arrangement from atomic number",
       "tm.atomic_model_problems", ["kc.matter_classification", "kc.integer_arithmetic"])
    _m(s, interp, rev, "m.trend_prediction", "Predict reactivity/size trends from position",
       "tm.atomic_model_problems", ["kc.matter_classification"])
    _pre(s, interp, rev, "cl.pre44.matter_atomic", "kc.matter_classification", "kc.atomic_structure_periodicity",
         PrerequisitePurpose.UNDERSTAND, P.ALL_RELEVANT_METHODS, None,
         ClaimOrigin.ASSERTED, "UNDERSTAND: element concept precedes atomic models")
    _ev(s, interp, "ev.c44.t", "cl.ctm.atomic_model_problems.target.kc.atomic_structure_periodicity",
         "SRC.OSX.CHEM2E.2.1", "Dalton's postulates; atoms combine in simple ratios.", False)
    _item(s, interp, "it.chem.atomic", "tm.atomic_model_problems",
          "An atom has 11 protons. Its electron arrangement is…",
          ["2,8,1", "2,8,8", "2,7,2", "2,8,2"], "2,8,1")

    # ---- 045 bonding ----
    interp, rev = _base(s, "45", "Human review of bonding batch.")
    _src(s, "SRC.OSX.CHEM2E.7.1", "OpenStax Chemistry 2e, 7.1 Ionic Bonding",
         "https://openstax.org/books/chemistry-2e/pages/7-1-ionic-bonding")
    _src(s, "SRC.OSX.CHEM2E.7.2", "OpenStax Chemistry 2e, 7.2 Covalent Bonding",
         "https://openstax.org/books/chemistry-2e/pages/7-2-covalent-bonding")
    _kc(s, interp, rev, "kc.chemical_bonding", "Ionic and covalent bonding",
        "Predict bond type from electron transfer/sharing; write formulae from valency.")
    _tm(s, interp, rev, "tm.bonding_problems", "Classify bonds and write formulae",
        ["kc.chemical_bonding"])
    _m(s, interp, rev, "m.ionic_vs_covalent", "Decide ionic vs covalent from electron behaviour",
       "tm.bonding_problems", ["kc.atomic_structure_periodicity", "kc.algebraic_expressions"])
    _m(s, interp, rev, "m.formula_from_valency", "Write formulae by combining valencies",
       "tm.bonding_problems", ["kc.atomic_structure_periodicity", "kc.integer_arithmetic"])
    _pre(s, interp, rev, "cl.pre45.atomic_bonding", "kc.atomic_structure_periodicity", "kc.chemical_bonding",
         E, P.SPECIFIC_TASK_MODEL, "tm.bonding_problems",
         ClaimOrigin.DERIVED, "DERIVED: bonding methods need atomic structure")
    _ev(s, interp, "ev.c45.t", "cl.ctm.bonding_problems.target.kc.chemical_bonding",
         "SRC.OSX.CHEM2E.7.1", "Ionic bonding by electron transfer between metals and nonmetals.", False)
    _item(s, interp, "it.chem.bonding", "tm.bonding_problems",
          "Sodium (2,8,1) combines with chlorine (2,8,7). The bond is…",
          ["ionic", "covalent", "metallic", "dative"], "ionic")

    # ---- 046 mole/stoichiometry ----
    interp, rev = _base(s, "46", "Human review of mole batch.")
    _src(s, "SRC.OSX.CHEM2E.3.1", "OpenStax Chemistry 2e, 3.1 Formula Mass and the Mole Concept",
         "https://openstax.org/books/chemistry-2e/pages/3-1-formula-mass-and-the-mole-concept")
    _src(s, "SRC.OSX.CHEM2E.4.2", "OpenStax Chemistry 2e, 4.2 Classifying Chemical Reactions",
         "https://openstax.org/books/chemistry-2e/pages/4-2-classifying-chemical-reactions")
    _kc(s, interp, rev, "kc.mole_stoichiometry", "Mole concept and stoichiometry",
        "Convert mass/moles/particles; balance equations; solve mole-ratio problems.")
    _tm(s, interp, rev, "tm.stoichiometry_problems", "Solve mole and equation problems",
        ["kc.mole_stoichiometry"])
    _m(s, interp, rev, "m.mole_ratio", "Convert via balanced-equation mole ratios",
       "tm.stoichiometry_problems", ["kc.chemical_bonding", "kc.ratio_proportion_rate", "kc.algebraic_expressions"])
    _m(s, interp, rev, "m.empirical_formula", "Derive empirical formulae from percentage composition",
       "tm.stoichiometry_problems", ["kc.chemical_bonding", "kc.percentage_concept", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre46.bonding_mole", "kc.chemical_bonding", "kc.mole_stoichiometry",
         E, P.SPECIFIC_TASK_MODEL, "tm.stoichiometry_problems",
         ClaimOrigin.DERIVED, "DERIVED: formulae (bonding) precede mole calculations")
    _pre(s, interp, rev, "cl.pre46.ratio_mole", "kc.ratio_proportion_rate", "kc.mole_stoichiometry",
         E, P.SPECIFIC_TASK_MODEL, "tm.stoichiometry_problems",
         ClaimOrigin.DERIVED, "Math→Chemistry: mole ratios need ratio reasoning")
    _pre(s, interp, rev, "cl.pre46.pct_mole", "kc.percentage_concept", "kc.mole_stoichiometry",
         E, P.SPECIFIC_METHOD, "m.empirical_formula",
         ClaimOrigin.DERIVED, "Math→Chemistry: empirical formulae need percentages")
    _ev(s, interp, "ev.c46.t", "cl.ctm.stoichiometry_problems.target.kc.mole_stoichiometry",
         "SRC.OSX.CHEM2E.3.1", "One mole contains Avogadro's number of entities.", False)
    _item(s, interp, "it.chem.mole", "tm.stoichiometry_problems",
          "Moles in 8 g of NaOH (M = 40)?", ["0.2", "5", "32", "48"], "0.2")

    # ---- 047 acids/bases ----
    interp, rev = _base(s, "47", "Human review of acids batch.")
    _src(s, "SRC.OSX.CHEM2E.14.1", "OpenStax Chemistry 2e, 14.1 Brønsted-Lowry Acids and Bases",
         "https://openstax.org/books/chemistry-2e/pages/14-1-bronsted-lowry-acids-and-bases")
    _kc(s, interp, rev, "kc.acids_bases_salts", "Acids, bases, salts and neutralisation",
        "Classify acids/bases; write neutralisation equations; solve titration calculations.")
    _tm(s, interp, rev, "tm.acid_base_problems", "Solve neutralisation and titration problems",
        ["kc.acids_bases_salts"])
    _m(s, interp, rev, "m.neutralisation_titration", "Compute unknown concentration via titration ratio",
       "tm.acid_base_problems", ["kc.mole_stoichiometry", "kc.algebraic_expressions"])
    _pre(s, interp, rev, "cl.pre47.mole_acids", "kc.mole_stoichiometry", "kc.acids_bases_salts",
         E, P.SPECIFIC_TASK_MODEL, "tm.acid_base_problems",
         ClaimOrigin.DERIVED, "DERIVED: titration needs mole calculations")
    _ev(s, interp, "ev.c47.t", "cl.ctm.acid_base_problems.target.kc.acids_bases_salts",
         "SRC.OSX.CHEM2E.14.1", "Brønsted-Lowry acids donate protons; bases accept them.", False)
    return s
