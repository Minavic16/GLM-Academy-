import json

from conftest import *

from examples.chem_wave2 import build_graph_v34
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim, validate_acyclicity


def test_v34_store_clean_and_all_claims_valid():
    s = build_graph_v34()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_chemistry_subject_identity():
    s = build_graph_v34()
    chem = [e for e in s.entities.values() if (e.id.startswith(("kc.", "tm.", "m.")) and e.id in (
        "kc.matter_classification", "kc.atomic_structure_periodicity",
        "kc.chemical_bonding", "kc.mole_stoichiometry", "kc.acids_bases_salts",
        "kc.redox_electrochemistry", "kc.chemical_energetics", "kc.rates_equilibrium",
        "kc.gas_behaviour", "kc.organic_foundations", "kc.practical_chemistry"))]
    assert len(chem) == 11
    for e in chem:
        assert e.subject == "Chemistry", e.id
        assert e.status == ClaimStatus.ACCEPTED
        assert s.targeting_task_models(e.id), e.id


def test_no_bio_english_entities():
    s = build_graph_v34()
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []


def test_math_physics_baselines_intact():
    s = build_graph_v34()
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Mathematics"]
    phys_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == "Physics"]
    assert len(math_kcs) == 36
    assert len(phys_kcs) == 19


def test_cross_subject_edges_principled():
    s = build_graph_v34()
    xs = [c for c in s.claims.values()
          if c.predicate == RelationshipType.PREREQUISITE
          and s.entities[c.subject_id].subject != s.entities[c.object_id].subject]
    assert xs, "cross-subject edges must exist"
    for c in xs:
        if c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
        else:
            assert c.origin == ClaimOrigin.DERIVED, c.id
        assert c.status == ClaimStatus.ACCEPTED
    # no duplicated Math/Physics KCs inside Chemistry
    dupes = [e.id for e in s.entities.values()
             if e.subject == "Chemistry" and e.id in (
                 "kc.algebraic_expressions", "kc.ratio_proportion_rate",
                 "kc.electric_circuits")]
    assert dupes == []


def test_no_new_indicates_and_pair_intact():
    s = build_graph_v34()
    inds = [c for c in s.claims.values() if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED
    mis = s.entities.get("mis.factorisation_sign_error")
    assert mis is not None and mis.status == ClaimStatus.PROPOSED


def test_serialization_round_trip_and_export():
    s = build_graph_v34()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
    assert len(view["nodes"]) == len(s.entities)
