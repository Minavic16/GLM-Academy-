"""Phase 15 Chemistry completion wave: batches 065 (organic reactions).

Chains build_graph_v38 (Phase 14 builder). Adds the organic-reactions
family, the only documented Chemistry implementation gap Phase 15 is
authorized to close (see docs/research/PHASE15_GAP_AUDIT.md).

All new prerequisite edges are Chemistry-internal: Phase 15 forbids new
cross-subject dependency claims, so no edge references a Mathematics or
Physics entity. Evidence is verified OpenStax Chemistry 2e chapter 20
sections 20-1 to 20-4 (URLs verified HTTP 200 before citation).
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
from examples.physics_completion_b import build_graph_v38

SUBJ = "Chemistry"
ASSESS = (AcceptanceBasis.EXPERT,)
STAMP = "2026-10-16T09:00:00Z"
E = PrerequisitePurpose.EXECUTE
U = PrerequisitePurpose.UNDERSTAND
P_TM = PrerequisiteScope.SPECIFIC_TASK_MODEL
P_ALL = PrerequisiteScope.ALL_RELEVANT_METHODS


def _base(s, note):
    nn = "65"
    s.add_activity(Activity(
        id=f"act.c{nn}.extract", type=ActivityType.EXTRACTION,
        agent_id="agent.ai.glm", time="2026-10-16T08:30:00Z"))
    interp = f"act.c{nn}.interpret"
    s.add_activity(Activity(
        id=interp, type=ActivityType.INTERPRETATION,
        agent_id="agent.ai.glm", time="2026-10-16T08:35:00Z"))
    rev = f"act.c{nn}.review"
    s.add_activity(Activity(
        id=rev, type=ActivityType.REVIEW,
        agent_id="agent.human.reviewer", time="2026-10-16T10:00:00Z",
        rationale=note))
    return interp, rev


def _src(s, sid, title, url):
    if sid not in s.sources:
        s.add_source(Source(
            id=sid, title=title, identifier_or_url=url,
            publisher="OpenStax", source_type=SourceType.TEXTBOOK,
            tier="reference"))


def _kc(s, interp, rev, kid, label, definition):
    k = KnowledgeComponent(
        id=kid, label=label, definition=definition, subject=SUBJ,
        status=ClaimStatus.ACCEPTED, created_by_activity=interp,
        cdg_version="v0.2.0")
    k.reviewed_by_activity = rev
    k.review_rationale = "Accepted in Phase 15 via human review."
    s.add_entity(k)
    return k


def _tm(s, interp, rev, tid, label):
    t = TaskModel(
        id=tid, label=label, subject=SUBJ,
        status=ClaimStatus.ACCEPTED, created_by_activity=interp,
        cdg_version="v0.2.0")
    t.reviewed_by_activity = rev
    s.add_entity(t)
    return t


def _method(s, interp, rev, mid, tmid, label):
    m = Method(
        id=mid, label=label, task_model_id=tmid, subject=SUBJ,
        status=ClaimStatus.ACCEPTED, created_by_activity=interp,
        cdg_version="v0.2.0")
    m.reviewed_by_activity = rev
    s.add_entity(m)
    return m


def _item(s, interp, rev, iid, tm_id, stem, options, key):
    it = Item(
        id=iid, stem=stem, options=options, key=key, task_model_id=tm_id,
        subject=SUBJ, status=ClaimStatus.ACCEPTED,
        created_by_activity=interp, cdg_version="v0.2.0")
    it.reviewed_by_activity = rev
    s.add_entity(it)
    return it


def _targets(s, interp, rev, tid, kid):
    c = Claim(
        id=f"cl.q065.targets.{tid}", predicate=RelationshipType.TARGETS,
        subject_id=tid, object_id=kid, claim_type=ClaimType.ASSESSMENT_DESIGN,
        created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, f"targets {kid}", ASSESS, rev))


def _own_method(s, interp, rev, tid, mid):
    c = Claim(
        id=f"cl.q065.own.{tid}.{mid}", predicate=RelationshipType.HAS_METHOD,
        subject_id=tid, object_id=mid,
        claim_type=ClaimType.ASSESSMENT_DESIGN,
        created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "method ownership", ASSESS, rev))


def _requires(s, interp, rev, mid, kid):
    c = Claim(
        id=f"cl.q065.req.{mid}", predicate=RelationshipType.REQUIRES,
        subject_id=mid, object_id=kid,
        claim_type=ClaimType.DEPENDENCY,
        created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, f"{mid} requires {kid}", ASSESS, rev))


def _underunderstand(s, interp, rev, source_kc, target_kc):
    c = Claim(
        id=f"cl.pre065.organic.{target_kc}",
        predicate=RelationshipType.PREREQUISITE,
        subject_id=source_kc, object_id=target_kc,
        claim_type=ClaimType.DEPENDENCY, purpose=U,
        scope=P_ALL, origin=ClaimOrigin.ASSERTED,
        created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "UNDERSTAND: organic functional-group knowledge",
                     ASSESS, rev))


def _execute(s, interp, rev, prerequisite_kc, target_kc, tm_id):
    c = Claim(
        id="cl.pre065.mole_reactions", predicate=RelationshipType.PREREQUISITE,
        subject_id=prerequisite_kc, object_id=target_kc,
        claim_type=ClaimType.DEPENDENCY, purpose=E,
        scope=P_TM, scope_ref=tm_id, origin=ClaimOrigin.DERIVED,
        created_by_activity=interp, created_at=STAMP, cdg_version="v0.2.0")
    s.add_claim(accept(c, "DERIVED: balancing combustion needs the mole concept",
                     ASSESS, rev))


def _ev(s, interp, eid, claim_id, source_id, locator, text):
    s.add_evidence(EvidenceItem(
        id=eid, claim_id=claim_id, source_id=source_id,
        role=EvidenceRole.INDIRECT, stance=EvidenceStance.SUPPORTS,
        locator=locator, excerpt=text,
        excerpt_kind=ExcerptKind.PARAPHRASE,
        extracted_by_activity=interp))


def build_graph_v39() -> CDGStore:
    s = build_graph_v38()

    # ============ sources (verified OpenStax Chemistry 2e ch. 20) ============
    _src(s, "SRC.OSX.CHEM2E.20.1",
         "OpenStax Chemistry 2e, 20.1 Hydrocarbons",
         "https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons")
    _src(s, "SRC.OSX.CHEM2E.20.2",
         "OpenStax Chemistry 2e, 20.2 Alcohols and Ethers",
         "https://openstax.org/books/chemistry-2e/pages/20-2-alcohols-and-ethers")
    _src(s, "SRC.OSX.CHEM2E.20.3",
         "OpenStax Chemistry 2e, 20.3 Aldehydes, Ketones, Carboxylic Acids and Esters",
         "https://openstax.org/books/chemistry-2e/pages/20-3-aldehyde-ketones-carboxylic-acids-and-esters")
    _src(s, "SRC.OSX.CHEM2E.20.4",
         "OpenStax Chemistry 2e, 20.4 Amines and Amides",
         "https://openstax.org/books/chemistry-2e/pages/20-4-amines-and-amides")

    # ============ 065a/b/c: hydrocarbons, alkenes, isomers ============
    interp, rev = _base(s, "Human review of the hydrocarbons batch.")

    k_alkanes = _kc(
        s, interp, rev,
        "kc.reactions_of_alkanes", "Reactions characteristic of alkanes",
        "Describe the reactions characteristic of saturated hydrocarbons, "
        "in particular the highly exothermic combustion that makes "
        "alkanes excellent fuels.")
    t_alkanes = _tm(
        s, interp, rev, "tm.alkane_reactions",
        "Analyse combustion and fuel behaviour of alkanes")
    m_comb = _method(
        s, interp, rev, "m.combustion_analysis", "tm.alkane_reactions",
        "Write and balance the complete combustion of alkanes")
    m_fuel = _method(
        s, interp, rev, "m.fuel_comparison", "tm.alkane_reactions",
        "Compare the use of alkanes as fuels")
    _targets(s, interp, rev, "tm.alkane_reactions", "kc.reactions_of_alkanes")
    _own_method(s, interp, rev, "tm.alkane_reactions", m_comb.id)
    _own_method(s, interp, rev, "tm.alkane_reactions", m_fuel.id)
    _requires(s, interp, rev, m_comb.id, "kc.mole_stoichiometry")
    _requires(s, interp, rev, m_comb.id, "kc.chemical_energetics")
    _requires(s, interp, rev, m_fuel.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations",
                   "kc.reactions_of_alkanes")
    _execute(s, interp, rev, "kc.mole_stoichiometry", "kc.reactions_of_alkanes",
             "tm.alkane_reactions")
    _ev(s, interp, "ev.q065.alkanes", "cl.q065.targets.tm.alkane_reactions",
        "SRC.OSX.CHEM2E.20.1", "20-1 hydrocarbons",
        "Alkanes are saturated hydrocarbons; combustion is highly "
        "exothermic and alkanes are excellent fuels.")

    k_alkenes = _kc(
        s, interp, rev,
        "kc.reactions_of_alkenes", "Reactions characteristic of alkenes",
        "Describe the characteristic reactions of alkenes, principally "
        "addition reactions across the carbon-carbon double bond.")
    t_alkenes = _tm(
        s, interp, rev, "tm.alkene_reactions",
        "Analyse addition reactions of alkenes")
    m_add = _method(
        s, interp, rev, "m.addition_reactions", "tm.alkene_reactions",
        "Predict the products of alkene addition reactions")
    _targets(s, interp, rev, "tm.alkene_reactions", "kc.reactions_of_alkenes")
    _own_method(s, interp, rev, "tm.alkene_reactions", m_add.id)
    _requires(s, interp, rev, m_add.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations",
                   "kc.reactions_of_alkenes")
    _ev(s, interp, "ev.q065.alkenes", "cl.q065.targets.tm.alkene_reactions",
        "SRC.OSX.CHEM2E.20.1", "20-1 hydrocarbons",
        "Unsaturated hydrocarbons contain double or triple bonds; their "
        "characteristic reactions include addition reactions.")

    k_isomers = _kc(
        s, interp, rev,
        "kc.isomerism", "Structural and geometric isomers",
        "Identify structural (constitutional) and geometric isomers of "
        "hydrocarbons and explain why their properties differ.")
    t_isomers = _tm(
        s, interp, rev, "tm.isomer_identification",
        "Identify isomers and compare their properties")
    m_iso = _method(
        s, interp, rev, "m.isomer_comparison", "tm.isomer_identification",
        "Compare structural and geometric isomers")
    _targets(s, interp, rev, "tm.isomer_identification", "kc.isomerism")
    _own_method(s, interp, rev, "tm.isomer_identification", m_iso.id)
    _requires(s, interp, rev, m_iso.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations", "kc.isomerism")
    _ev(s, interp, "ev.q065.isomers", "cl.q065.targets.tm.isomer_identification",
        "SRC.OSX.CHEM2E.20.1", "20-1 hydrocarbons",
        "Structural isomers have the same molecular formula but different "
        "arrangements; geometric isomers differ in the orientation of "
        "groups around a double bond.")

    # ============ 065d/e: alcohols and ethers ============
    k_alcohols = _kc(
        s, interp, rev,
        "kc.alcohols", "Alcohols",
        "Describe the structure and properties of alcohols, including "
        "polyols, and their IUPAC naming.")
    t_alcohols = _tm(
        s, interp, rev, "tm.alcohol_properties",
        "Describe properties and naming of alcohols")
    m_struct = _method(
        s, interp, rev, "m.alcohol_structure", "tm.alcohol_properties",
        "Describe the hydroxyl functional group and alcohol properties")
    m_names = _method(
        s, interp, rev, "m.alcohol_naming", "tm.alcohol_properties",
        "Name and draw structures for alcohols")
    _targets(s, interp, rev, "tm.alcohol_properties", "kc.alcohols")
    _own_method(s, interp, rev, "tm.alcohol_properties", m_struct.id)
    _own_method(s, interp, rev, "tm.alcohol_properties", m_names.id)
    _requires(s, interp, rev, m_struct.id, "kc.organic_foundations")
    _requires(s, interp, rev, m_names.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations", "kc.alcohols")
    _ev(s, interp, "ev.q065.alcohols",
        "cl.q065.targets.tm.alcohol_properties",
        "SRC.OSX.CHEM2E.20.2", "20-2 alcohols",
        "Alcohols carry a hydroxyl group; their names follow the parent "
        "hydrocarbon with an -ol suffix.")

    k_ethers = _kc(
        s, interp, rev,
        "kc.ethers", "Ethers",
        "Describe the structure and properties of ethers and identify "
        "them by name.")
    t_ethers = _tm(
        s, interp, rev, "tm.ether_properties",
        "Describe properties and naming of ethers")
    m_ether = _method(
        s, interp, rev, "m.ether_structure", "tm.ether_properties",
        "Describe the ether linkage and ether properties")
    _targets(s, interp, rev, "tm.ether_properties", "kc.ethers")
    _own_method(s, interp, rev, "tm.ether_properties", m_ether.id)
    _requires(s, interp, rev, m_ether.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations", "kc.ethers")
    _ev(s, interp, "ev.q065.ethers",
        "cl.q065.targets.tm.ether_properties",
        "SRC.OSX.CHEM2E.20.2", "20-2 ethers",
        "Alcohols and ethers are derivatives of hydrocarbons in which "
        "an oxygen atom is attached by single bonds.")

    # ============ 065f/g: aldehydes/ketones and carboxylic acids/esters ============
    k_aldehydes = _kc(
        s, interp, rev,
        "kc.aldehydes_ketones", "Aldehydes and ketones",
        "Describe the structure and reactions of aldehydes and ketones, "
        "including nucleophilic addition and oxidation/reduction.")
    t_aldehydes = _tm(
        s, interp, rev, "tm.aldehyde_reactions",
        "Analyse reactions of aldehydes and ketones")
    m_nuc = _method(
        s, interp, rev, "m.nucleophilic_addition", "tm.aldehyde_reactions",
        "Predict nucleophilic addition reactions of aldehydes and ketones")
    m_oxred = _method(
        s, interp, rev, "m.oxidation_reduction", "tm.aldehyde_reactions",
        "Predict oxidation and reduction of alcohols and carbonyl compounds")
    _targets(s, interp, rev, "tm.aldehyde_reactions", "kc.aldehydes_ketones")
    _own_method(s, interp, rev, "tm.aldehyde_reactions", m_nuc.id)
    _own_method(s, interp, rev, "tm.aldehyde_reactions", m_oxred.id)
    _requires(s, interp, rev, m_nuc.id, "kc.organic_foundations")
    _requires(s, interp, rev, m_oxred.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations",
                   "kc.aldehydes_ketones")
    _ev(s, interp, "ev.q065.aldehydes",
        "cl.q065.targets.tm.aldehyde_reactions",
        "SRC.OSX.CHEM2E.20.3", "20-3 carbonyl reactions",
        "Aldehydes and ketones contain a carbonyl group; many reactions "
        "start with nucleophilic attack on the polar carbonyl group.")

    k_acids = _kc(
        s, interp, rev,
        "kc.carboxylic_acids", "Carboxylic acids and esters",
        "Describe the structure and reactions of carboxylic acids and "
        "their esters, including esterification.")
    t_acids = _tm(
        s, interp, rev, "tm.carboxylic_acid_reactions",
        "Analyse esterification of carboxylic acids")
    m_ester = _method(
        s, interp, rev, "m.esterification", "tm.carboxylic_acid_reactions",
        "Write the esterification of carboxylic acids with alcohols")
    _targets(s, interp, rev, "tm.carboxylic_acid_reactions",
             "kc.carboxylic_acids")
    _own_method(s, interp, rev, "tm.carboxylic_acid_reactions", m_ester.id)
    _requires(s, interp, rev, m_ester.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations",
                   "kc.carboxylic_acids")
    _ev(s, interp, "ev.q065.carboxylic_acids",
        "cl.q065.targets.tm.carboxylic_acid_reactions",
        "SRC.OSX.CHEM2E.20.3", "20-3 esters",
        "Carboxylic acids react with alcohols to form esters; water is "
        "eliminated in the process.")

    # ============ 065h/i: amines and amides ============
    k_amines = _kc(
        s, interp, rev,
        "kc.amines", "Amines",
        "Describe the structure and properties of amines and their "
        "nomenclature.")
    t_amines = _tm(
        s, interp, rev, "tm.amine_properties",
        "Describe properties and naming of amines")
    m_amnaming = _method(
        s, interp, rev, "m.amine_naming", "tm.amine_properties",
        "Name and draw structures for amines")
    m_amnaph = _method(
        s, interp, rev, "m.amine_properties", "tm.amine_properties",
        "Describe the properties of amines")
    _targets(s, interp, rev, "tm.amine_properties", "kc.amines")
    _own_method(s, interp, rev, "tm.amine_properties", m_amnaming.id)
    _own_method(s, interp, rev, "tm.amine_properties", m_amnaph.id)
    _requires(s, interp, rev, m_amnaming.id, "kc.organic_foundations")
    _requires(s, interp, rev, m_amnaph.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations", "kc.amines")
    _ev(s, interp, "ev.q065.amines",
        "cl.q065.targets.tm.amine_properties",
        "SRC.OSX.CHEM2E.20.4", "20-4 amines",
        "Amines contain carbon-nitrogen bonds; their nomenclature uses "
        "the -ine suffix.")

    k_amides = _kc(
        s, interp, rev,
        "kc.amides", "Amides",
        "Describe the structure and reactions of amides, including "
        "amidisation and peptide bond formation.")
    t_amides = _tm(
        s, interp, rev, "tm.amide_reactions",
        "Analyse amide reactions")
    m_amides = _method(
        s, interp, rev, "m.amide_reactions", "tm.amide_reactions",
        "Predict condensation and hydrolysis of amides")
    _targets(s, interp, rev, "tm.amide_reactions", "kc.amides")
    _own_method(s, interp, rev, "tm.amide_reactions", m_amides.id)
    _requires(s, interp, rev, m_amides.id, "kc.organic_foundations")
    _underunderstand(s, interp, rev, "kc.organic_foundations", "kc.amides")
    _ev(s, interp, "ev.q065.amides",
        "cl.q065.targets.tm.amide_reactions",
        "SRC.OSX.CHEM2E.20.4", "20-4 amides",
        "Amides form by amidation of carboxylic acids; peptide bonds "
        "link amino acids through condensation reactions.")

    # ============ items ============
    _item(s, interp, rev, "it.chem.alkanes",
         "tm.alkane_reactions",
         "Write the balanced equation for the complete combustion of ethane.",
         ["CH4 + O2 -> CO2 + H2O", "CH4 + H2O -> CO + H2", "C2H6 -> C3H8"],
         "balanced equation")
    _item(s, interp, rev, "it.chem.alkenes",
         "tm.alkene_reactions",
         "The double bond in propene is broken during addition. Identify "
         "the type of reaction.",
         ["Addition across the double bond", "Substitution",
          "Elimination", "Neutralisation"], "addition")
    _item(s, interp, rev, "it.chem.isomers",
         "tm.isomer_identification",
         "Hex-1-ene and hex-2-ene differ only in the position of the "
         "double bond. Identify the geometric relationship.",
         ["Geometric isomers", "Structural isomers", "Stereoisomers",
          "Conformers"], "geometric")
    _item(s, interp, rev, "it.chem.alcohols",
         "tm.alcohol_properties",
         "The hydroxyl group is attached to carbon 2 of a five-carbon "
         "chain. Name the alcohol.",
         ["Pentan-2-ol", "Pentan-1-ol", "Pentane", "1-Pentanol"], "pentan-2-ol")
    _item(s, interp, rev, "it.chem.ethers",
         "tm.ether_properties",
         "1-Ethoxypropane has an oxygen atom bonded to two alkyl groups. "
         "Identify the class of compound.",
         ["Ether", "Alcohol", "Aldehyde", "Ketone"], "ether")
    _item(s, interp, rev, "it.chem.aldehydes",
         "tm.aldehyde_reactions",
         "An aldehyde has a carbonyl group bonded to at least one "
         "hydrogen atom. Identify the class of compound.",
         ["Aldehyde", "Ketone", "Ester", "Carboxylic acid"], "aldehyde")
    _item(s, interp, rev, "it.chem.carboxylic_acids",
         "tm.carboxylic_acid_reactions",
         "Ethanoic acid reacts with ethanol to form an ester. Identify "
         "the type of reaction.",
         ["Esterification", "Neutralisation", "Disproportionation",
          "Polymerisation"], "esterification")
    _item(s, interp, rev, "it.chem.amines",
         "tm.amine_properties",
         "Pyridine is a heterocyclic amine. Identify the functional "
         "class of this compound.",
         ["Amine", "Ester", "Carboxylic acid", "Ether"], "amine")
    _item(s, interp, rev, "it.chem.amides",
         "tm.amide_reactions",
         "Two amino acids connect to form a peptide link. Identify the "
         "type of reaction.",
         ["Condensation", "Addition", "Substitution", "Elimination"],
         "condensation")

    return s
