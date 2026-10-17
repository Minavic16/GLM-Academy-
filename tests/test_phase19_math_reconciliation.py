"""Phase 19 regression tests for the Mathematics JAMB reconciliation + triage.

Phase 19 changes documentation only (no canonical-store changes). These tests
guard that the reconciliation report, the deduplicated Mathematics gap
register and the owner decision brief exist with the required structure and
vocabulary; that the official JAMB matrix carries the Phase 19 refinements
(I.1 correction, traceability section, depth exposures) and promotes nothing
to BOARD_VERIFIED; that the registers are cross-linked; and that the canonical
store, the five Phase 17 KCs and their provenance remain unchanged.
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
import sys
sys.path.insert(0, str(ROOT))

from examples.math_scope_expansion import build_graph_v40  # noqa: E402
from cdg.enums import (  # noqa: E402
    ClaimStatus, EntityType, RelationshipType,
)
from cdg.validation import run_store_validation  # noqa: E402
from cdg.serialization import dumps_store  # noqa: E402

ARCH = ROOT / "docs" / "architecture"
REPORT = ROOT / "docs" / "PHASE19_REPORT.md"

RECON = ARCH / "JAMB_MATHEMATICS_RECONCILIATION.md"
REGISTER = ARCH / "MATHEMATICS_GAP_REGISTER.md"
BRIEF = ARCH / "OWNER_DECISION_BRIEF_PHASE19.md"
MATRIX = ARCH / "JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md"
DEDUP = ARCH / "DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md"
CLOSURE = ARCH / "CLOSURE_REGISTERS.md"
ROADMAP = ARCH / "SUBJECT_COMPLETION_ROADMAP.md"
COMPARISON = ARCH / "CONSOLIDATED_NERDC_JAMB_WAEC_COMPARISON.md"
NERDC_MATRIX = ARCH / "MATHEMATICS_SYLLABUS_COVERAGE.md"

PHASE17_KCS = [
    "kc.sets_operations", "kc.logical_reasoning",
    "kc.sequences_series", "kc.matrix_algebra", "kc.mensuration",
]

# identifier -> still-secondary Syllabus NG source (Phase 17 provenance)
SECONDARY_MATRICES_EVIDENCE = {
    "ev.m68.mat.target": "SRC.SYLLABUSNG.JAMB.MATH",
    "ev.m68.mat.det": "SRC.SYLLABUSNG.WAEC.MATH",
}

DISPOSITIONS = (
    "NO_ACTION_COVERED", "DOCUMENTATION_CORRECTION", "OWNER_SCOPE_DECISION",
    "IMPLEMENTATION_CANDIDATE", "EVIDENCE_RETRIEVAL_REQUIRED", "UNRESOLVED",
)

OFFICIAL_LOCATORS = [
    "I.1", "I.2", "I.3", "I.4",
    "II.1", "II.2", "II.3", "II.4", "II.5", "II.6",
    "III.1", "III.2", "III.3", "III.4", "III.5",
    "IV.1", "IV.2", "IV.3",
    "V.1", "V.2", "V.3", "V.4", "V.5",
]


def _flat(path):
    """Whitespace-normalized text (line wraps should not break assertions)."""
    return " ".join(path.read_text(encoding="utf-8").split())


@pytest.mark.phase19
def test_phase19_deliverables_exist():
    for p in (RECON, REGISTER, BRIEF):
        assert p.exists(), f"missing Phase 19 deliverable: {p}"
        assert p.stat().st_size > 1000, f"implausibly small: {p}"
    assert REPORT.exists(), "missing Phase 19 report"
    flat = _flat(REPORT)
    for token in ("765a292", "COVERED 2 / PARTIALLY_COVERED 17 / NOT_COVERED 4",
                  "181 passed", "Wave A", "BOARD_UNVERIFIED", "204"):
        assert token in flat, f"Phase 19 report missing token: {token!r}"


@pytest.mark.phase19
def test_phase19_reconciliation_covers_all_23_topics():
    flat = _flat(RECON)
    for loc in OFFICIAL_LOCATORS:
        assert f"| {loc} p" in flat, f"official topic {loc} missing"
    for token in (
        "corrected from PARTIALLY_COVERED",
        "NOT_IMPLEMENTED",
        "204 activities",
        "I.1(c)",
        "No duplicate KC was created",
        "Syllabus NG",
        "WAEC official",
        "UNRESOLVED",
    ):
        assert token in flat, f"reconciliation report missing token: {token!r}"


@pytest.mark.phase19
def test_phase19_matrix_refinements_and_traceability():
    lines = MATRIX.read_text(encoding="utf-8").splitlines()
    rows = [l for l in lines if l.startswith("| JAMB |")]
    assert len(rows) == 23, "official Mathematics matrix must keep 23 topic rows"
    # I.1 was corrected to NOT_COVERED in Phase 19 (recorded in the note) and
    # implemented in Phase 20 — the row now reads COVERED with a Phase 20 note.
    i1 = [r for r in rows if "Number bases/Modular Arithmetic" in r]
    assert len(i1) == 1 and "| COVERED |" in i1[0] and "Phase 20" in i1[0]
    # no other topic rows changed to NOT_APPLICABLE etc. silently
    statuses = []
    for r in rows:
        for s in ("COVERED", "PARTIALLY_COVERED", "NOT_COVERED",
                  "NOT_APPLICABLE", "UNRESOLVED"):
            if f"| {s} |" in r:
                statuses.append(s)
                break
    # counts as of Phase 20 were 5/15/3; the Phase 22 P1 closure implemented
    # II.5, III.3 and V.1 -> now 8/15/0 (see docs/PHASE22_REPORT.md)
    assert statuses.count("COVERED") == 8    # + II.5, III.3, V.1 (Phase 22)
    assert statuses.count("NOT_COVERED") == 0
    assert statuses.count("PARTIALLY_COVERED") == 15
    flat = _flat(MATRIX)
    assert "I.1 was corrected to NOT_COVERED" in flat  # Phase 19 record retained
    assert "Phase 19 traceability" in flat
    for chain in ("tm.matrix_algebra", "m.determinants_inverses",
                  "tm.sequences_series", "m.quartile_from_ordered"):
        assert chain in flat, f"matrix missing traceability chain: {chain!r}"
    assert "COVERED 2 / PARTIALLY_COVERED 17 / NOT_COVERED 4" in flat
    assert "COVERED 5 / PARTIALLY_COVERED 15 / NOT_COVERED 3" in flat
    low = flat.lower()
    for token in ("midpoint", "standard form", "change of base",
                  "chord lengths", "experimental probability",
                  "cyclic quadrilaterals"):
        assert token in low, f"matrix missing depth exposure: {token!r}"


@pytest.mark.phase19
def test_phase19_gap_register_rows_and_vocabulary():
    flat = _flat(REGISTER)
    for i in range(1, 30):
        assert f"| M-{i:02d} |" in flat, f"gap row M-{i:02d} missing"
    for disp in DISPOSITIONS:
        assert disp in flat, f"disposition {disp} not documented"
    for p in ("P1", "P2", "P3"):
        assert p in flat, f"priority tier {p} missing"
    # key rows
    m03 = [l for l in REGISTER.read_text(encoding="utf-8").splitlines()
           if l.startswith("| M-03 |")][0]
    assert "COVERED (Phase 20 batch 071)" in m03 and "OFFICIAL CONFIRMED" in m03
    m07 = [l for l in REGISTER.read_text(encoding="utf-8").splitlines()
           if l.startswith("| M-07 |")][0]
    assert "NO_ACTION_COVERED" in m07 and "Syllabus NG" in m07
    m09 = [l for l in REGISTER.read_text(encoding="utf-8").splitlines()
           if l.startswith("| M-09 |")][0]
    # Phase 22 implemented the component (batch 081); the row records closure
    assert "COVERED (Phase 22 batch 081)" in m09
    assert "NO_ACTION_COVERED" in m09
    assert "Owner authorization (Phase 20) covered only the ten-topic wave" in flat


@pytest.mark.phase19
def test_phase19_owner_brief_scope():
    flat = _flat(BRIEF)
    for token in ("Decision 1", "Wave A", "recommended",
                  "Deliberately not asked", "OD-01", "immediate blocker"):
        assert token in flat, f"owner brief missing token: {token!r}"
    assert "not blocking now" in flat


@pytest.mark.phase19
def test_phase19_no_board_verified_promotion():
    for p in (RECON, REGISTER, BRIEF, MATRIX):
        for line in p.read_text(encoding="utf-8").splitlines():
            if "BOARD_VERIFIED" in line:
                low = line.lower()
                assert any(t in low for t in
                           ("not ", "no ", "never", "unreachable",
                            "promot", "without")), \
                    f"{p.name}: possible promotion claim: {line!r}"
        assert "BOARD_UNVERIFIED" in p.read_text(encoding="utf-8"), p.name


@pytest.mark.phase19
def test_phase19_evidence_dimensions_separated():
    report = _flat(RECON)
    for token in ("JAMB-OFFICIAL", "NERDC-SS1/SS2-OFFICIAL",
                  "SECONDARY-SyllabusNG", "WAEC-OFFICIAL", "NERDC-SSS3"):
        assert token in report, f"evidence dimension {token} not separated"
    # NERDC matrix cross-reference note
    assert "Evidence dimensions (Phase 19" in _flat(NERDC_MATRIX)
    # consolidated comparison Phase 19 pointer
    assert "Phase 19 note" in _flat(COMPARISON)


@pytest.mark.phase19
def test_phase19_register_cross_links():
    assert "Phase 19 — Mathematics gap triage" in _flat(DEDUP)
    assert "MATHEMATICS_GAP_REGISTER.md" in _flat(DEDUP)
    closure = _flat(CLOSURE)
    assert "Phase 19 (2026-10-17)" in closure
    assert "OWNER_DECISION_BRIEF_PHASE19.md" in closure
    road = _flat(ROADMAP)
    assert "Phase 19" in road and "MATHEMATICS_GAP_REGISTER.md" in road


@pytest.mark.phase19
def test_phase19_store_and_provenance_unchanged():
    s = build_graph_v40()
    assert run_store_validation(s) == []
    assert len(s.entities) == 365
    assert len(s.claims) == 583
    assert len(s.evidence) == 288
    assert len(s.sources) == 85
    assert len(s.activities) == 204  # v40 total; v39 had 192 (+12 batches 66-69)
    assert len(list(EntityType)) == 13  # schema-level entity-type count preserved
    # subject KC counts unchanged
    kc_counts = {}
    for e in s.entities.values():
        if e.entity_type == EntityType.KNOWLEDGE_COMPONENT:
            kc_counts[e.subject] = kc_counts.get(e.subject, 0) + 1
    assert kc_counts.get("Mathematics") == 44
    assert kc_counts.get("Physics") == 25
    assert kc_counts.get("Chemistry") == 21
    # five Phase 17 KCs exist and remain accepted
    for kid in PHASE17_KCS:
        kc = s.entities[kid]
        assert kc.status.value == "ACCEPTED", kid
    # Phase 17 provenance preserved: matrices evidence still secondary
    for eid, expected_src in SECONDARY_MATRICES_EVIDENCE.items():
        assert s.evidence[eid].source_id == expected_src
    # `indicates` claim untouched (PROPOSED)
    inds = [c for c in s.claims.values()
            if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED
    # no Biology/English entities
    bad = [e.id for e in s.entities.values()
           if (e.subject or "") in ("Biology", "English")]
    assert bad == []


@pytest.mark.phase19
def test_phase19_no_bio_english_artifacts():
    for name in ("BIOLOGY_SYLLABUS_COVERAGE.md", "ENGLISH_SYLLABUS_COVERAGE.md",
                 "JAMB_BIOLOGY_OFFICIAL_COVERAGE.md",
                 "JAMB_ENGLISH_OFFICIAL_COVERAGE.md"):
        assert not (ARCH / name).exists(), f"out-of-scope artifact: {name}"


@pytest.mark.phase19
def test_phase19_deterministic_store():
    assert dumps_store(build_graph_v40()) == dumps_store(build_graph_v40())
