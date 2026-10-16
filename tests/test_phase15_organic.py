import json

from conftest import *

from examples.chemistry_organic_reactions import build_graph_v39
from cdg.serialization import dumps_store
from cdg.validation import run_store_validation, validate_relationship_claim


def _chem_kcs(s):
    return [e for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
            and e.subject == "Chemistry"]


def test_v39_store_clean():
    s = build_graph_v39()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


def test_phase15_new_kcs():
    s = build_graph_v39()
    expected = {
        "kc.reactions_of_alkanes",
        "kc.reactions_of_alkenes",
        "kc.isomerism",
        "kc.alcohols",
        "kc.ethers",
        "kc.aldehydes_ketones",
        "kc.carboxylic_acids",
        "kc.amines",
        "kc.amides",
    }
    kcs = {e.id for e in _chem_kcs(s) if e.id in expected}
    assert kcs == expected
    for kid in expected:
        kc = s.entities[kid]
        assert kc.subject == "Chemistry", kid
        assert kc.status == ClaimStatus.ACCEPTED, kid
        assert s.targeting_task_models(kid), kid


def test_phase15_new_tms_methods_items():
    s = build_graph_v39()
    for tm, kid in [
        ("tm.alkane_reactions", "kc.reactions_of_alkanes"),
        ("tm.alkene_reactions", "kc.reactions_of_alkenes"),
        ("tm.isomer_identification", "kc.isomerism"),
        ("tm.alcohol_properties", "kc.alcohols"),
        ("tm.ether_properties", "kc.ethers"),
        ("tm.aldehyde_reactions", "kc.aldehydes_ketones"),
        ("tm.carboxylic_acid_reactions", "kc.carboxylic_acids"),
        ("tm.amine_properties", "kc.amines"),
        ("tm.amide_reactions", "kc.amides"),
    ]:
        t = s.entities[tm]
        assert t.subject == "Chemistry", tm
        assert t.status == ClaimStatus.ACCEPTED, tm
        assert s.target_kcs_of_task_model(tm), tm
        owned = [
            c.object_id for c in s.claims.values()
            if c.predicate == RelationshipType.HAS_METHOD
            and c.subject_id == tm]
        assert owned, tm
        for mid in owned:
            m = s.entities[mid]
            assert m.task_model_id == tm, mid
            reqs = {
                c.object_id for c in s.claims.values()
                if c.predicate == RelationshipType.REQUIRES
                and c.subject_id == mid}
            assert reqs, mid


def test_phase15_understand_prerequisites_asserted():
    s = build_graph_v39()
    for c in s.claims.values():
        if (c.predicate == RelationshipType.PREREQUISITE
                and c.purpose == PrerequisitePurpose.UNDERSTAND):
            assert c.origin == ClaimOrigin.ASSERTED, c.id
            assert (c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS), c.id


def test_phase15_execute_prerequisite_scoped():
    s = build_graph_v39()
    c = s.claims["cl.pre065.mole_reactions"]
    assert c.subject_id == "kc.mole_stoichiometry"
    assert c.object_id == "kc.reactions_of_alkanes"
    assert c.purpose == PrerequisitePurpose.EXECUTE
    assert c.origin == ClaimOrigin.DERIVED
    assert c.scope == PrerequisiteScope.SPECIFIC_TASK_MODEL
    assert c.scope_ref == "tm.alkane_reactions"


def test_phase15_no_cross_subject_edges_added():
    s = build_graph_v39()
    for c in s.claims.values():
        if c.predicate != RelationshipType.PREREQUISITE:
            continue
        src = s.entities[c.subject_id]
        dst = s.entities[c.object_id]
        if src.subject and dst.subject and src.subject != dst.subject:
            assert c.id in (
                "cl.xs.math_alg_kin", "cl.xs.math_lin_kin",
                "cl.xs.math_grad_mg", "cl.xs.math_alg_newton",
                "cl.pre31.trig_vectors", "cl.pre31.alg_vectors",
                "cl.pre32.alg_work", "cl.pre32.rate_work",
                "cl.pre33.alg_mom", "cl.pre34.alg_grav",
                "cl.pre35.ratio_fluids", "cl.pre35.alg_fluids",
                "cl.pre36.alg_heat", "cl.pre36.ratio_heat",
                "cl.pre36.int_heat", "cl.pre37.alg_waves",
                "cl.pre38.alg_optics", "cl.pre38.ratio_optics",
                "cl.pre38.tri_optics", "cl.pre39.alg_circuits",
                "cl.pre39.ratio_circuits", "cl.pre39.simlin_circuits",
                "cl.pre40.rate_emi", "cl.pre40.alg_emi",
                "cl.pre41.indices_modern", "cl.pre41.alg_modern",
                "cl.pre42.grad_practical", "cl.pre42.int_practical",
                "cl.pre43.alg_matter", "cl.pre46.ratio_mole",
                "cl.pre46.pct_mole", "cl.pre48.circuits_redox",
                "cl.pre49b.fn_rates", "cl.pre50.ratio_gases",
                "cl.pre56.log_ph", "cl.pre56.alg_ph",
                "cl.r63.pre.kc.atomic_structure_periodicity",
            ), c.id
    # the new Phase 15 KCs themselves must not appear on any cross-subject edge
    new_kcs = {
        "kc.reactions_of_alkanes", "kc.reactions_of_alkenes", "kc.isomerism",
        "kc.alcohols", "kc.ethers", "kc.aldehydes_ketones",
        "kc.carboxylic_acids", "kc.amines", "kc.amides",
    }
    for c in s.claims.values():
        if c.predicate != RelationshipType.PREREQUISITE:
            continue
        src = s.entities[c.subject_id]
        dst = s.entities[c.object_id]
        if src.subject and dst.subject and src.subject != dst.subject:
            assert src.id not in new_kcs
            assert dst.id not in new_kcs


def test_phase15_baselines_intact():
    s = build_graph_v39()
    math_kcs = [
        e for e in s.entities.values()
        if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
        and e.subject == "Mathematics"]
    assert len(math_kcs) == 39
    # the logarithms-to-pH dependency is untouched
    edge = s.claims["cl.pre56.log_ph"]
    assert edge.status == ClaimStatus.ACCEPTED
    # legacy identifiers are preserved
    assert s.entities["kc.median_ungrouped"].legacy_ids == ["MATH.STAT.MEDIAN"]
    assert s.entities["kc.measures_of_dispersion"].legacy_ids == [
        "MATH.STAT.RANGE", "MATH.STAT.MEAN_DEVIATION",
        "MATH.STAT.VARIANCE", "MATH.STAT.STANDARD_DEVIATION"]
    # the proposed indicates claim stays PROPOSED
    inds = [c for c in s.claims.values()
            if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED


def test_phase15_no_bio_english_entities():
    s = build_graph_v39()
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []


def test_round_trip_and_export():
    s = build_graph_v39()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
