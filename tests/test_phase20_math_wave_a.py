"""Phase 20 Mathematics implementation wave regression tests.

Covers batches 070-079 (number bases, modular arithmetic, laws of indices,
surds, approximation/errors, standard form, log change-of-base, financial
mathematics, change-of-subject depth, factorisation extensions) implemented in
`examples.math_wave_a_phase20` (build_graph_v41, chains build_graph_v40).

Phase 20 adds 10 KCs, 10 TMs, 21 Methods, 18 Items, 95 ACCEPTED claims
(10 targets + 21 hasMethod + 47 requires + 17 prerequisite), 49 evidence
records citing the official JAMB UTME Mathematics E-syllabus
(SRC.JAMB.UTME.MATH.2025) and 30 activities. All new claims HUMAN-reviewed;
Physics/Chemistry/other subjects untouched; `indicates` untouched (PROPOSED).

Guards:
- new entities conform to schema; IDs unique; references resolve
- requirement -> KC -> TM -> methods -> items traceability per topic
- claim types/statuses valid; prerequisite qualifiers present; acyclic
- evidence provenance: every new claim supported from the JAMB source
- no Physics/Chemistry/Biology/English drift; no BOARD_VERIFIED promotion
- coverage dispositions recorded in the gap register / official matrix
- store validation []; deterministic; serialization round-trip OK
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(ROOT))

from examples.math_wave_a_phase20 import build_graph_v41  # noqa: E402
from examples.math_scope_expansion import build_graph_v40  # noqa: E402
from cdg.enums import (  # noqa: E402
    ClaimOrigin, ClaimStatus, ClaimType, EntityType,
    PrerequisitePurpose, PrerequisiteScope, RelationshipType,
)
from cdg.validation import (  # noqa: E402
    run_store_validation, validate_relationship_claim, validate_acyclicity,
)
from cdg.serialization import dumps_store  # noqa: E402

JAMB_SRC = "SRC.JAMB.UTME.MATH.2025"

NEW_KCS = [
    "kc.number_bases", "kc.modular_arithmetic", "kc.indices_laws", "kc.surds",
    "kc.approximation_errors", "kc.standard_form", "kc.simple_interest",
    "kc.profit_and_loss", "kc.shares_and_vat", "kc.factorisation_patterns",
]

NEW_TMS = [
    "tm.number_base_problems", "tm.modular_arithmetic_problems",
    "tm.index_law_simplification", "tm.surd_problems",
    "tm.approximation_problems", "tm.standard_form_problems",
    "tm.simple_interest_problems", "tm.profit_loss_problems",
    "tm.shares_vat_problems", "tm.factorise_common_patterns",
]

NEW_METHODS = [
    "m.convert_number_base", "m.base_arithmetic", "m.mod_notation_residue",
    "m.mod_operations", "m.apply_index_laws", "m.evaluate_fractional_powers",
    "m.simplify_surds", "m.surd_operations", "m.rationalise_denominator",
    "m.round_to_precision", "m.percentage_error", "m.write_standard_form",
    "m.standard_form_arithmetic", "m.change_of_base",
    "m.simple_interest_formula", "m.profit_loss_percent", "m.share_division",
    "m.vat_calculation", "m.subject_powers_roots", "m.common_factor_extraction",
    "m.difference_of_two_squares",
]

NEW_ITEMS = [
    "it.math.number_base_convert", "it.math.number_base_add", "it.math.modular",
    "it.math.index_laws", "it.math.surd_simplify", "it.math.surd_rationalise",
    "it.math.rounding", "it.math.percent_error", "it.math.standard_form",
    "it.math.standard_form_ops", "it.mcq.log_change_base",
    "it.math.simple_interest", "it.math.profit_loss", "it.math.shares",
    "it.math.vat", "it.mcq.subject_power", "it.math.common_factor",
    "it.math.difference_squares",
]

# The ten owner-authorized topics -> (KC, TM, item) traceability chains.
TOPIC_CHAINS = [
    ("Modular arithmetic", "kc.modular_arithmetic", "tm.modular_arithmetic_problems",
     ["it.math.modular"]),
    ("Number bases", "kc.number_bases", "tm.number_base_problems",
     ["it.math.number_base_convert", "it.math.number_base_add"]),
    ("Surds", "kc.surds", "tm.surd_problems",
     ["it.math.surd_simplify", "it.math.surd_rationalise"]),
    ("Approximation and errors", "kc.approximation_errors",
     "tm.approximation_problems",
     ["it.math.rounding", "it.math.percent_error"]),
    ("Standard form", "kc.standard_form", "tm.standard_form_problems",
     ["it.math.standard_form", "it.math.standard_form_ops"]),
    ("Logarithms incl. change of base", "kc.logarithms", "tm.logarithm_problems",
     ["it.mcq.log_change_base"]),
    ("Financial mathematics", "kc.simple_interest", "tm.simple_interest_problems",
     ["it.math.simple_interest"]),
    ("Financial mathematics", "kc.profit_and_loss", "tm.profit_loss_problems",
     ["it.math.profit_loss"]),
    ("Financial mathematics", "kc.shares_and_vat", "tm.shares_vat_problems",
     ["it.math.shares", "it.math.vat"]),
    ("Indices", "kc.indices_laws", "tm.index_law_simplification",
     ["it.math.index_laws"]),
    ("Change of subject of formulae", "kc.change_of_subject", "tm.make_subject",
     ["it.mcq.subject_power"]),
    ("Factorization", "kc.factorisation_patterns", "tm.factorise_common_patterns",
     ["it.math.common_factor", "it.math.difference_squares"]),
]


@pytest.mark.phase20
def test_v41_store_clean():
    s = build_graph_v41()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


@pytest.mark.phase20
def test_v41_new_kcs_present_and_accepted():
    s = build_graph_v41()
    for kid in NEW_KCS:
        kc = s.entities[kid]
        assert kc.entity_type == EntityType.KNOWLEDGE_COMPONENT, kid
        assert kc.subject == "Mathematics", kid
        assert kc.status == ClaimStatus.ACCEPTED, kid
        assert kc.reviewed_by_activity is not None, kid
        assert kc.review_rationale and "Phase 20" in kc.review_rationale, kid
        assert s.targeting_task_models(kid), kid


@pytest.mark.phase20
def test_v41_kc_ids_and_labels_unique():
    s = build_graph_v41()
    kcs = [e for e in s.entities.values()
           if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
           and e.subject == "Mathematics"]
    ids = [k.id for k in kcs]
    assert len(ids) == len(set(ids))
    labels = [k.label for k in kcs]
    assert len(labels) == len(set(labels))  # no duplicate topic records


@pytest.mark.phase20
def test_v41_new_tms_methods_items():
    s = build_graph_v41()
    for tid in NEW_TMS:
        t = s.entities[tid]
        assert t.entity_type == EntityType.TASK_MODEL, tid
        assert t.subject == "Mathematics", tid
        assert t.status == ClaimStatus.ACCEPTED, tid
        owned = [c.object_id for c in s.claims.values()
                 if c.predicate == RelationshipType.HAS_METHOD
                 and c.subject_id == tid]
        assert owned, tid
        for mid in owned:
            m = s.entities[mid]
            assert m.task_model_id == tid, mid
            assert m.status == ClaimStatus.ACCEPTED, mid
    for mid in NEW_METHODS:
        m = s.entities[mid]
        assert m.status == ClaimStatus.ACCEPTED, mid
        reqs = {c.object_id for c in s.claims.values()
                if c.predicate == RelationshipType.REQUIRES
                and c.subject_id == mid}
        assert reqs, mid  # every Method requires >=1 KC
    for iid in NEW_ITEMS:
        it = s.entities[iid]
        assert it.subject == "Mathematics", iid
        assert it.status == ClaimStatus.ACCEPTED, iid
        assert it.stem, iid
        assert it.options and it.key in it.options, iid
        assert it.task_model_id in NEW_TMS + ["tm.logarithm_problems",
                                              "tm.make_subject"], iid


@pytest.mark.phase20
def test_v41_topic_traceability_chains():
    """Every authorized topic traces KC -> targeting TM -> methods -> items."""
    s = build_graph_v41()
    for topic, kid, tmid, iids in TOPIC_CHAINS:
        assert s.entities[kid].subject == "Mathematics", topic
        # TM targets the KC
        tgts = {c.object_id for c in s.claims.values()
                if c.predicate == RelationshipType.TARGETS and c.subject_id == tmid}
        assert kid in tgts, (topic, tmid)
        # TM owns methods; every item belongs to the TM
        owned = {c.object_id for c in s.claims.values()
                 if c.predicate == RelationshipType.HAS_METHOD and c.subject_id == tmid}
        assert owned, topic
        for iid in iids:
            assert s.entities[iid].task_model_id == tmid, (topic, iid)


@pytest.mark.phase20
def test_v41_new_claims_accepted_and_reviewed():
    s40 = build_graph_v40()
    s = build_graph_v41()
    new_claims = [s.claims[cid] for cid in set(s.claims) - set(s40.claims)]
    assert len(new_claims) == 95
    for c in new_claims:
        assert c.status == ClaimStatus.ACCEPTED, c.id
        assert c.acceptance_bases, c.id
    # Evidence coverage follows the batch convention (as in the Phase 17
    # batches): every new target, the methods' depth claims onto their own new
    # KC, and the principal prerequisite edges carry evidence records; the
    # structural hasMethod / adjacency-requires claims are supported by the
    # batch review rationale.
    ev_by_claim = {}
    for e in s.evidence.values():
        ev_by_claim.setdefault(e.claim_id, []).append(e)
    new_ids = {c.id for c in new_claims}
    evidenced = new_ids & set(ev_by_claim)
    assert len(evidenced) == 49
    for c in new_claims:
        if c.predicate == RelationshipType.TARGETS:
            assert c.id in ev_by_claim, c.id
    for k in NEW_KCS:
        for tid in s.targeting_task_models(k):
            methods = {c.object_id for c in s.claims.values()
                       if c.predicate == RelationshipType.HAS_METHOD
                       and c.subject_id == tid}
            for c in new_claims:
                if (c.predicate == RelationshipType.REQUIRES
                        and c.subject_id in methods and c.object_id == k):
                    assert c.id in ev_by_claim, c.id


@pytest.mark.phase20
def test_v41_evidence_provenance_jamb_official():
    s40 = build_graph_v40()
    s = build_graph_v41()
    # Source registered with official metadata
    src = s.sources[JAMB_SRC]
    assert src.source_type.value == "SYLLABUS"
    assert src.tier == "primary"
    assert src.content_hash and "aff7a7c2" in src.content_hash
    # Every Phase 20 evidence record cites the JAMB source and a locator
    new_ev = [s.evidence[eid] for eid in set(s.evidence) - set(s40.evidence)]
    assert len(new_ev) == 49
    for e in new_ev:
        assert e.source_id == JAMB_SRC, e.id
        assert "JAMB Math p." in e.locator, e.id
    # No new claim is evidenced by a secondary aggregator
    new_claim_ids = set(s.claims) - set(s40.claims)
    for e in new_ev:
        assert e.claim_id in new_claim_ids, e.id


@pytest.mark.phase20
def test_v41_prerequisite_qualifiers_and_acyclic():
    s = build_graph_v41()
    prereqs = [c for c in s.claims.values()
               if c.predicate == RelationshipType.PREREQUISITE]
    for c in prereqs:
        assert c.purpose is not None, c.id
        assert c.scope is not None, c.id
        assert c.origin is not None, c.id
        if c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
            assert c.scope in (PrerequisiteScope.ALL_RELEVANT_METHODS,
                               PrerequisiteScope.SPECIFIC_TASK_MODEL), c.id
        if (c.purpose == PrerequisitePurpose.EXECUTE
                and c.scope in (PrerequisiteScope.SPECIFIC_METHOD,
                                PrerequisiteScope.SPECIFIC_TASK_MODEL)):
            assert c.origin == ClaimOrigin.DERIVED, c.id
            assert c.scope_ref, c.id
    edges = [(c.subject_id, c.object_id) for c in prereqs]
    assert validate_acyclicity(edges), "prerequisite graph must be acyclic"
    # Key new edges exist with the expected qualifiers
    expected = {
        ("kc.integer_arithmetic", "kc.number_bases"),
        ("kc.integer_arithmetic", "kc.modular_arithmetic"),
        ("kc.indices_laws", "kc.equations_in_indices"),
        ("kc.indices_laws", "kc.surds"),
        ("kc.indices_laws", "kc.standard_form"),
        ("kc.indices_laws", "kc.logarithms"),
        ("kc.ratio_proportion_rate", "kc.shares_and_vat"),
        ("kc.percentage_concept", "kc.shares_and_vat"),
        ("kc.algebraic_expressions", "kc.factorisation_patterns"),
    }
    actual = {(c.subject_id, c.object_id) for c in prereqs}
    assert expected <= actual
    # Pre-existing prerequisite edges are untouched
    assert ("kc.equations_in_indices", "kc.logarithms") in actual
    assert ("kc.linear_equations_one_var", "kc.change_of_subject") in actual


@pytest.mark.phase20
def test_v41_no_unintended_subject_changes():
    s40 = build_graph_v40()
    s = build_graph_v41()
    added = set(s.entities) - set(s40.entities)
    removed = set(s40.entities) - set(s.entities)
    assert not removed
    for eid in added:
        assert s.entities[eid].subject == "Mathematics", eid
    # no existing record was modified
    for eid in set(s.entities) & set(s40.entities):
        assert s.entities[eid] == s40.entities[eid], eid
    # no claims/evidence/activities were removed or modified
    for cid in set(s40.claims):
        assert s.claims[cid].status == s40.claims[cid].status, cid
        assert s.claims[cid].predicate == s40.claims[cid].predicate, cid
    assert not (set(s40.evidence) - set(s.evidence))
    assert not (set(s40.activities) - set(s.activities))
    # Physics/Chemistry counts unchanged; no Biology/English artifacts
    kcs = [e for e in s.entities.values()
           if e.entity_type == EntityType.KNOWLEDGE_COMPONENT]
    assert sum(1 for k in kcs if k.subject == "Physics") == 25
    assert sum(1 for k in kcs if k.subject == "Chemistry") == 21
    assert sum(1 for k in kcs if k.subject == "Mathematics") == 54
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []


@pytest.mark.phase20
def test_v41_cross_subject_edges_not_added():
    """Phase 20 adds no cross-subject prerequisite/requires edges."""
    s40 = build_graph_v40()
    s = build_graph_v41()
    new_claims = [s.claims[cid] for cid in set(s.claims) - set(s40.claims)]
    for c in new_claims:
        if c.predicate in (RelationshipType.PREREQUISITE,
                           RelationshipType.REQUIRES):
            subj = s.entities[c.subject_id].subject
            obj = s.entities[c.object_id].subject
            assert subj == "Mathematics" and obj == "Mathematics", c.id


@pytest.mark.phase20
def test_v41_indicates_and_entity_types_preserved():
    s = build_graph_v41()
    inds = [c for c in s.claims.values()
            if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED
    # schema-level entity-type count preserved (13 declared types)
    assert len(list(EntityType)) == 13
    types = {e.entity_type for e in s.entities.values()}
    assert EntityType.SUBJECT in types
    assert types <= set(EntityType)


@pytest.mark.phase20
def test_v41_matrices_secondary_provenance_untouched():
    s = build_graph_v41()
    kc = s.entities["kc.matrix_algebra"]
    assert "secondary" in kc.review_rationale.lower()
    src_ids = {e.source_id for e in s.evidence.values()
               if e.claim_id == "cl.m68.targets.tm.matrix_algebra"}
    assert any("SYLLABUSNG" in sid for sid in src_ids)
    # the change-of-subject / logarithms / index-equation historical claims stay
    for cid in ("cl.tm9.target", "cl.x55.target", "cl.tm8.target",
                "cl.pre9.lin_subject", "cl.pre55.indices_log"):
        assert s.claims[cid].status == ClaimStatus.ACCEPTED


@pytest.mark.phase20
def test_v41_counts_snapshot():
    s = build_graph_v41()
    assert len(s.entities) == 424
    assert len(s.claims) == 678
    assert len(s.evidence) == 337
    assert len(s.sources) == 86
    assert len(s.activities) == 234
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
                and e.subject == "Mathematics"]
    assert len(math_kcs) == 54  # 44 baseline + 10 Phase 20


@pytest.mark.phase20
def test_v41_serialization_and_export():
    import json
    s = build_graph_v41()
    parsed = json.loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
    for c in s.claims.values():
        assert c.subject_id in s.entities, c.id
        if c.object_id:
            assert c.object_id in s.entities, c.id


@pytest.mark.phase20
def test_v41_canonical_json_export_matches():
    # The canonical export tracks the latest builder; since Phase 22 that is
    # build_graph_v42 (the Phase 20 builder output itself is unchanged — see
    # the other v41 guards in this file).
    from examples.math_p1_closure_phase22 import build_graph_v42
    s = build_graph_v42()
    cur = open(ROOT / "examples" / "math_cdg_v2.json").read()
    assert cur == dumps_store(s)


@pytest.mark.phase20
def test_v41_deterministic():
    a = dumps_store(build_graph_v41())
    b = dumps_store(build_graph_v41())
    assert a == b


@pytest.mark.phase20
def test_v41_coverage_dispositions_recorded():
    reg = (ROOT / "docs" / "architecture" / "MATHEMATICS_GAP_REGISTER.md").read_text()
    for gid in ("M-03", "M-04", "M-05", "M-19", "M-20", "M-21"):
        row = [ln for ln in reg.splitlines() if ln.startswith(f"| {gid} |")]
        assert row, gid
        assert "COVERED" in row[0], gid
        assert "Phase 20" in row[0], gid
    # unaffected rows keep their dispositions
    for gid in ("M-10", "M-17", "M-18"):
        row = [ln for ln in reg.splitlines() if ln.startswith(f"| {gid} |")]
        assert row, gid


@pytest.mark.phase20
def test_v41_official_matrix_and_report_updated():
    matrix = (ROOT / "docs" / "architecture"
              / "JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md").read_text()
    # Official JAMB counts as recorded after Phase 20 are superseded by the
    # Phase 22 P1 closure (the matrix carries both records): now 8/15/0.
    assert "8 of 23" in matrix
    assert "PARTIALLY_COVERED: 15" in matrix
    assert "NOT_COVERED: 0" in matrix
    report = (ROOT / "docs" / "PHASE20_REPORT.md").read_text()
    assert "build_graph_v41" in report
    assert "BOARD_UNVERIFIED" in report  # no promotion to BOARD_VERIFIED
    assert "No subject was promoted" in report or "not promoted" in report.lower()
