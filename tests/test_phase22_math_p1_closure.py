"""Phase 22 Mathematics P1 closure regression tests.

Covers batches 080-082 (binary operations; loci & construction; representation
of data) implemented in `examples.math_p1_closure_phase22` (build_graph_v42,
chains build_graph_v41).

Phase 22 adds 3 KCs, 3 TMs, 12 Methods, 8 Items, 47 ACCEPTED claims
(3 targets + 12 hasMethod + 25 requires + 7 prerequisite), 22 evidence
records citing the official JAMB UTME Mathematics E-syllabus
(SRC.JAMB.UTME.MATH.2025) and 9 activities. The three former NOT_COVERED
official JAMB topics (II.5, III.3, V.1) are implemented at topic level;
ogive/cumulative frequency remain excluded (standing owner deferral); P2
depth gaps are not implemented; Physics/Chemistry/other subjects untouched;
`indicates` untouched (PROPOSED); no BOARD_VERIFIED promotion.

Guards:
- new entities conform to schema; IDs unique; references resolve
- requirement -> KC -> TM -> methods -> items traceability per topic
- claim types/statuses valid; prerequisite qualifiers present; acyclic
- evidence provenance: every new claim supported from the JAMB source with
  its official locator (II.5 / III.3 + III.1(d) / V.1)
- no P2/ogive scope creep; no cross-subject edges; no subject drift
- coverage dispositions recorded in the gap register / official matrix
- store validation []; deterministic; serialization round-trip OK
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(ROOT))

from examples.math_p1_closure_phase22 import build_graph_v42  # noqa: E402
from examples.math_wave_a_phase20 import build_graph_v41  # noqa: E402
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
    "kc.binary_operations", "kc.loci_and_construction",
    "kc.data_representation",
]

NEW_TMS = [
    "tm.binary_operations_problems", "tm.loci_construction_problems",
    "tm.data_representation_problems",
]

NEW_METHODS = [
    "m.evaluate_binary_operation", "m.binary_operation_properties",
    "m.identity_inverse_elements", "m.describe_locus",
    "m.construct_perpendicular_bisector", "m.construct_angle_bisector",
    "m.construct_special_angles", "m.apply_loci_intersections",
    "m.frequency_distribution_table", "m.construct_bar_chart",
    "m.construct_histogram", "m.construct_pie_chart",
]

NEW_ITEMS = [
    "it.math.binary_operation", "it.math.binary_identity", "it.math.loci",
    "it.math.loci_construction", "it.math.special_angle_construction",
    "it.math.frequency_table", "it.math.pie_chart",
    "it.math.data_representation_choice",
]

# The three owner-authorized P1 topics -> (KC, TM, methods, items) chains.
TOPIC_CHAINS = [
    ("Binary operations (II.5)", "kc.binary_operations",
     "tm.binary_operations_problems",
     ["m.evaluate_binary_operation", "m.binary_operation_properties",
      "m.identity_inverse_elements"],
     ["it.math.binary_operation", "it.math.binary_identity"]),
    ("Loci & construction (III.3; III.1d)", "kc.loci_and_construction",
     "tm.loci_construction_problems",
     ["m.describe_locus", "m.construct_perpendicular_bisector",
      "m.construct_angle_bisector", "m.construct_special_angles",
      "m.apply_loci_intersections"],
     ["it.math.loci", "it.math.loci_construction",
      "it.math.special_angle_construction"]),
    ("Representation of data (V.1)", "kc.data_representation",
     "tm.data_representation_problems",
     ["m.frequency_distribution_table", "m.construct_bar_chart",
      "m.construct_histogram", "m.construct_pie_chart"],
     ["it.math.frequency_table", "it.math.pie_chart",
      "it.math.data_representation_choice"]),
]

EXPECTED_PREREQS = {
    ("kc.integer_arithmetic", "kc.binary_operations"),
    ("kc.algebraic_expressions", "kc.binary_operations"),
    ("kc.mensuration", "kc.loci_and_construction"),
    ("kc.triangle_angle_properties", "kc.loci_and_construction"),
    ("kc.parallel_line_angles", "kc.loci_and_construction"),
    ("kc.integer_arithmetic", "kc.data_representation"),
    ("kc.ratio_proportion_rate", "kc.data_representation"),
}


@pytest.mark.phase22
def test_v42_store_clean():
    s = build_graph_v42()
    assert run_store_validation(s) == []
    for c in s.claims.values():
        assert validate_relationship_claim(c, s.entities) == [], c.id


@pytest.mark.phase22
def test_v42_counts_and_math_kcs():
    s = build_graph_v42()
    assert len(s.entities) == 450
    assert len(s.claims) == 725
    assert len(s.evidence) == 359
    assert len(s.sources) == 86
    assert len(s.activities) == 243
    math_kcs = [e for e in s.entities.values()
                if e.entity_type == EntityType.KNOWLEDGE_COMPONENT
                and e.subject == "Mathematics"]
    assert len(math_kcs) == 57  # 54 Phase 20 baseline + 3 Phase 22


@pytest.mark.phase22
def test_v42_delta_vs_v41():
    s41 = build_graph_v41()
    s = build_graph_v42()
    # added entities are exactly the 26 new records; nothing removed
    added = set(s.entities) - set(s41.entities)
    assert added == set(NEW_KCS + NEW_TMS + NEW_METHODS + NEW_ITEMS)
    assert not (set(s41.entities) - set(s.entities))
    # claims: +47, distributed per the phase record
    new_claims = [s.claims[c] for c in set(s.claims) - set(s41.claims)]
    assert len(new_claims) == 47
    by_pred = {}
    for c in new_claims:
        by_pred[c.predicate] = by_pred.get(c.predicate, 0) + 1
    assert by_pred.get(RelationshipType.TARGETS) == 3
    assert by_pred.get(RelationshipType.HAS_METHOD) == 12
    assert by_pred.get(RelationshipType.REQUIRES) == 25
    assert by_pred.get(RelationshipType.PREREQUISITE) == 7
    assert sum(by_pred.values()) == 47
    # evidence: +22, all from this phase; activities +9; sources unchanged
    new_ev = [s.evidence[e] for e in set(s.evidence) - set(s41.evidence)]
    assert len(new_ev) == 22
    for e in new_ev:
        assert e.id.startswith(("ev.m80", "ev.m81", "ev.m82")), e.id
    new_acts = set(s.activities) - set(s41.activities)
    assert len(new_acts) == 9
    assert set(s.sources) == set(s41.sources)


@pytest.mark.phase22
def test_v42_new_kcs_present_and_accepted():
    s = build_graph_v42()
    for kid in NEW_KCS:
        kc = s.entities[kid]
        assert kc.status == ClaimStatus.ACCEPTED, kid
        assert kc.subject == "Mathematics", kid
        assert kc.label and kc.definition, kid
        assert "Phase 22" in kc.review_rationale, kid
        assert JAMB_SRC in kc.review_rationale, kid


@pytest.mark.phase22
def test_v42_topic_chains_traceability():
    s = build_graph_v42()
    for topic, kc_id, tm_id, methods, items in TOPIC_CHAINS:
        tm = s.entities[tm_id]
        assert tm.status == ClaimStatus.ACCEPTED, topic
        # targets: TM -> KC
        tgts = [c for c in s.claims.values()
                if c.predicate == RelationshipType.TARGETS
                and c.subject_id == tm_id and c.object_id == kc_id]
        assert len(tgts) == 1, topic
        # hasMethod: TM -> each method
        owned = [c.object_id for c in s.claims.values()
                 if c.predicate == RelationshipType.HAS_METHOD
                 and c.subject_id == tm_id]
        assert set(methods) <= set(owned), topic
        # requires: each method requires its owning KC
        for mid in methods:
            reqs = [c.object_id for c in s.claims.values()
                    if c.predicate == RelationshipType.REQUIRES
                    and c.subject_id == mid]
            assert kc_id in reqs, (topic, mid)
        # items belong to the topic TM
        for iid in items:
            assert s.entities[iid].task_model_id == tm_id, iid


@pytest.mark.phase22
def test_v42_requires_dependencies():
    s = build_graph_v42()

    def reqs(mid):
        return {c.object_id for c in s.claims.values()
                if c.predicate == RelationshipType.REQUIRES
                and c.subject_id == mid}

    assert reqs("m.binary_operation_properties") >= {
        "kc.binary_operations", "kc.integer_arithmetic",
        "kc.algebraic_expressions"}
    assert reqs("m.construct_angle_bisector") >= {
        "kc.loci_and_construction", "kc.triangle_angle_properties"}
    assert reqs("m.construct_special_angles") >= {
        "kc.loci_and_construction", "kc.triangle_angle_properties"}
    assert reqs("m.construct_pie_chart") >= {
        "kc.data_representation", "kc.ratio_proportion_rate"}
    assert reqs("m.frequency_distribution_table") >= {
        "kc.data_representation", "kc.integer_arithmetic"}


@pytest.mark.phase22
def test_v42_prerequisite_qualifiers_and_acyclic():
    s = build_graph_v42()
    new_prereqs = [c for c in s.claims.values()
                   if c.predicate == RelationshipType.PREREQUISITE
                   and c.id.startswith(("cl.m80.pre", "cl.m81.pre",
                                        "cl.m82.pre"))]
    assert len(new_prereqs) == 7
    actual = {(c.subject_id, c.object_id) for c in new_prereqs}
    assert actual == EXPECTED_PREREQS
    for c in new_prereqs:
        assert c.claim_type == ClaimType.DEPENDENCY, c.id
        assert c.status == ClaimStatus.ACCEPTED, c.id
        assert c.purpose in (PrerequisitePurpose.EXECUTE,
                             PrerequisitePurpose.UNDERSTAND), c.id
        assert c.scope is not None and c.origin is not None, c.id
        if c.purpose == PrerequisitePurpose.UNDERSTAND:
            assert c.origin == ClaimOrigin.ASSERTED, c.id
        if (c.purpose == PrerequisitePurpose.EXECUTE
                and c.scope in (PrerequisiteScope.SPECIFIC_METHOD,
                                PrerequisiteScope.SPECIFIC_TASK_MODEL)):
            assert c.origin == ClaimOrigin.DERIVED, c.id
            assert c.scope_ref, c.id
        if c.scope == PrerequisiteScope.SPECIFIC_METHOD:
            assert s.entities[c.scope_ref].entity_type == EntityType.METHOD
        if c.scope == PrerequisiteScope.SPECIFIC_TASK_MODEL:
            assert s.entities[c.scope_ref].entity_type == EntityType.TASK_MODEL
        if c.scope == PrerequisiteScope.ALL_RELEVANT_METHODS:
            assert c.scope_ref in (None, ""), c.id
    edges = [(c.subject_id, c.object_id) for c in s.claims.values()
             if c.predicate == RelationshipType.PREREQUISITE]
    assert validate_acyclicity(edges), "prerequisite graph must be acyclic"


@pytest.mark.phase22
def test_v42_evidence_provenance_and_locators():
    s = build_graph_v42()
    new_ev = [e for e in s.evidence.values()
              if e.id.startswith(("ev.m80", "ev.m81", "ev.m82"))]
    assert len(new_ev) == 22
    for e in new_ev:
        assert e.source_id == JAMB_SRC, e.id
        assert e.claim_id in s.claims, e.id
        assert e.locator.startswith("JAMB Math p"), e.id
        assert e.extracted_by_activity in (
            "act.m80.interpret", "act.m81.interpret", "act.m82.interpret"), e.id
        assert e.excerpt.strip(), e.id
    # official locators per topic
    assert all("II.5" in e.locator for e in new_ev if e.id.startswith("ev.m80"))
    assert all("III." in e.locator for e in new_ev if e.id.startswith("ev.m81"))
    assert all("V.1" in e.locator for e in new_ev if e.id.startswith("ev.m82"))
    # every new claim is traceable to the canonical store's JAMB source
    new_claim_ids = {c.id for c in s.claims.values()
                     if c.id.startswith(("cl.m80.", "cl.m81.", "cl.m82."))}
    assert len(new_claim_ids) == 47
    evidenced = {e.claim_id for e in new_ev}
    # targets + own-KC requires + prerequisites are directly evidenced
    assert all(cid in evidenced for cid in (
        "cl.m80.targets.tm.binary_operations_problems",
        "cl.m81.targets.tm.loci_construction_problems",
        "cl.m82.targets.tm.data_representation_problems",
        "cl.m80.req.m.evaluate_binary_operation.kc.binary_operations",
        "cl.m81.req.m.describe_locus.kc.loci_and_construction",
        "cl.m82.req.m.construct_pie_chart.kc.data_representation",
    ))


@pytest.mark.phase22
def test_v42_no_ogive_or_p2_scope_creep():
    s = build_graph_v42()
    added = set(s.entities) - set(build_graph_v41().entities)
    for eid in added:
        assert "ogive" not in eid.lower(), eid
        assert "cumulative" not in eid.lower(), eid
    for iid in NEW_ITEMS:
        stem = s.entities[iid].stem.lower()
        assert "ogive" not in stem and "cumulative" not in stem, iid
    # owner-deferred and P2 families untouched (no new mode/grouped-data work)
    for tok in ("mode", "grouped_data", "dispersion"):
        assert not any(tok in eid for eid in added), tok


@pytest.mark.phase22
def test_v42_no_unintended_subject_changes():
    s41 = build_graph_v41()
    s = build_graph_v42()
    for eid in set(s.entities) & set(s41.entities):
        assert s.entities[eid] == s41.entities[eid], eid
    assert not (set(s41.entities) - set(s.entities))
    for cid in set(s41.claims):
        assert s.claims[cid].status == s41.claims[cid].status, cid
        assert s.claims[cid].predicate == s41.claims[cid].predicate, cid
    assert not (set(s41.evidence) - set(s.evidence))
    assert not (set(s41.activities) - set(s.activities))
    kcs = [e for e in s.entities.values()
           if e.entity_type == EntityType.KNOWLEDGE_COMPONENT]
    assert sum(1 for k in kcs if k.subject == "Physics") == 25
    assert sum(1 for k in kcs if k.subject == "Chemistry") == 21
    assert sum(1 for k in kcs if k.subject == "Mathematics") == 57
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []
    assert len(list(EntityType)) == 13
    # PROPOSED set unchanged: `indicates` + factsign misconception only
    proposed = {c.id for c in s.claims.values()
                if c.status == ClaimStatus.PROPOSED}
    assert proposed == {"cl.it.indicates", "cl.mis.factsign"}


@pytest.mark.phase22
def test_v42_cross_subject_edges_not_added():
    s41 = build_graph_v41()
    s = build_graph_v42()
    new_rel = [c for c in s.claims.values()
               if c.predicate in (RelationshipType.PREREQUISITE,
                                  RelationshipType.REQUIRES)
               and c.id not in s41.claims]
    assert new_rel
    for c in new_rel:
        subj = s.entities[c.subject_id]
        obj = s.entities[c.object_id]
        assert subj.subject == "Mathematics", c.id
        assert obj.subject == "Mathematics", c.id


@pytest.mark.phase22
def test_v42_serialization_export_and_determinism():
    s = build_graph_v42()
    parsed = __import__("json").loads(dumps_store(s))
    assert len(parsed["entities"]) == len(s.entities)
    assert len(parsed["claims"]) == len(s.claims)
    view = s.export_view()
    assert len(view["edges"]) == len(s.claims)
    cur = open(ROOT / "examples" / "math_cdg_v2.json").read()
    assert cur == dumps_store(s)
    assert dumps_store(build_graph_v42()) == dumps_store(build_graph_v42())


@pytest.mark.phase22
def test_v42_generated_docs_current():
    doc = (ROOT / "docs" / "MATHEMATICS_CDG.md").read_text()
    for token in ("kc.binary_operations", "kc.loci_and_construction",
                  "kc.data_representation"):
        assert token in doc, token
    for batch in ("| 080 |", "| 081 |", "| 082 |"):
        assert batch in doc, batch
    wf = (ROOT / "tools" / "generate_math_cdg_docs.py").read_text()
    assert "build_graph_v42" in wf and "build_graph_v41()" not in wf


@pytest.mark.phase22
def test_v42_coverage_dispositions_recorded():
    matrix = (ROOT / "docs" / "architecture"
              / "JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md").read_text()
    assert "8 of 23" in matrix
    assert "PARTIALLY_COVERED: 15" in matrix
    assert "NOT_COVERED: 0" in matrix
    reg = (ROOT / "docs" / "architecture"
           / "MATHEMATICS_GAP_REGISTER.md").read_text()
    m09 = [ln for ln in reg.splitlines() if ln.startswith("| M-09 |")][0]
    assert "COVERED" in m09 and "Phase 22" in m09
    m10 = [ln for ln in reg.splitlines() if ln.startswith("| M-10 |")][0]
    assert "COVERED" in m10 and "Phase 22" in m10
    m15 = [ln for ln in reg.splitlines() if ln.startswith("| M-15 |")][0]
    assert "Phase 22" in m15 and "batch 082" in m15
    assert "ogive" in m15.lower()  # deferral explicitly retained


@pytest.mark.phase22
def test_v42_report_exists_and_marks_dimensions():
    report = (ROOT / "docs" / "PHASE22_REPORT.md").read_text()
    for token in ("build_graph_v42", "BOARD_UNVERIFIED",
                  "IMPLEMENTATION_COMPLETE", "SRC.JAMB.UTME.MATH.2025",
                  "WAEC", "NERDC", "450"):
        assert token in report, token
