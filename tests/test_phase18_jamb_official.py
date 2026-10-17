"""Phase 18 regression tests for the official JAMB E-syllabus retrieval.

Phase 18 changes documentation only (no canonical-store changes). These tests
guard that the retrieval report, the three official JAMB coverage matrices and
the source-metadata records exist with the required structure and vocabulary,
that no subject is promoted to BOARD_VERIFIED, and that the canonical store
and protected records remain unchanged.
"""
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ARCH = ROOT / "docs" / "architecture"
SRC_DOCS = ROOT / "docs" / "source-documents"

MATRIX_FILES = {
    "JAMB Mathematics official": ARCH / "JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md",
    "JAMB Physics official": ARCH / "JAMB_PHYSICS_OFFICIAL_COVERAGE.md",
    "JAMB Chemistry official": ARCH / "JAMB_CHEMISTRY_OFFICIAL_COVERAGE.md",
}

EXPECTED_ROW_COUNTS = {
    "JAMB Mathematics official": 23,
    "JAMB Physics official": 40,
    "JAMB Chemistry official": 18,
}

SOURCE_RECORDS = {
    "SRC.JAMB.UTME.MATH.2025.json":
        "aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f",
    "SRC.JAMB.UTME.PHYS.2025.json":
        "62f5ac84592735cd5829296cb52da5bc8b582ee0f2227999cca73b58dcabfee5",
    "SRC.JAMB.UTME.CHEM.2025.json":
        "a3c15bfee3beac0f4106a32b0091e2a2c51eaec8baa62fafa44afcad72193738",
}

REQUIRED_MATRIX_COLUMNS = (
    "authority", "subject", "document_version", "official_topic",
    "official_subtopic_or_objective", "cdg_entity_ids", "coverage_status",
    "evidence_reference", "gap_description", "next_action",
)

ALLOWED_STATUSES = {
    "COVERED", "PARTIALLY_COVERED", "NOT_COVERED", "NOT_APPLICABLE", "UNRESOLVED",
}

RETRIEVAL_REPORT = ARCH / "PHASE18_RETRIEVAL_REPORT.md"


def _table_rows(path: Path) -> list[list[str]]:
    rows = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


@pytest.mark.phase18
def test_phase18_deliverables_exist():
    assert RETRIEVAL_REPORT.is_file()
    for label, path in MATRIX_FILES.items():
        assert path.is_file(), f"missing matrix: {label}"


@pytest.mark.phase18
def test_phase18_retrieval_report_contents():
    text = RETRIEVAL_REPORT.read_text()
    for token in (
        "ibass.jamb.gov.ng",
        "main.221b9987.js",
        "aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f",
        "62f5ac84592735cd5829296cb52da5bc8b582ee0f2227999cca73b58dcabfee5",
        "a3c15bfee3beac0f4106a32b0091e2a2c51eaec8baa62fafa44afcad72193738",
        "SRC.JAMB.IBASS.ATTEMPT.2026-10-17.json",
        "waecinternational.org/cass/Downloads",
        "lmis.nerdcportals.com.ng",
        "BOARD_UNVERIFIED",
    ):
        assert token in text, token


@pytest.mark.phase18
def test_phase18_source_metadata_records():
    import json

    for name, sha in SOURCE_RECORDS.items():
        p = SRC_DOCS / name
        assert p.is_file(), name
        meta = json.loads(p.read_text())
        for key in ("id", "organization", "title", "subject", "type",
                    "authority", "canonical_url", "download_url",
                    "retrieved_at", "bytes_retrieved", "content_extracted",
                    "sha256", "authenticity_established", "applicable_cycle",
                    "limitations", "notes"):
            assert key in meta, (name, key)
        assert meta["sha256"] == sha, name
        assert "OFFICIAL" in meta["authority"].upper(), name
        assert meta["bytes_retrieved"] is True, name
        assert meta["content_extracted"] is True, name
        assert meta["authenticity_established"] is True, name
        assert "UNRESOLVED" in meta["applicable_cycle"].upper(), name


@pytest.mark.phase18
def test_phase18_matrix_structure():
    for label, path in MATRIX_FILES.items():
        rows = _table_rows(path)
        assert rows, label
        assert rows[0] == list(REQUIRED_MATRIX_COLUMNS), (label, rows[0])
        assert len(rows) - 1 == EXPECTED_ROW_COUNTS[label], (label, len(rows) - 1)
        for row in rows[1:]:
            assert len(row) == len(REQUIRED_MATRIX_COLUMNS), (label, row)
            assert row[0].upper() == "JAMB", (label, row, "authority not JAMB")
            assert row[1], (label, row, "subject empty")
            assert row[3], (label, row, "official_topic empty")
            assert row[6] in ALLOWED_STATUSES, (label, row, "coverage_status invalid")
            assert row[7], (label, row, "evidence_reference empty")
            assert "official" in row[7].lower() or "official" in row[2].lower(), (
                label, row, "row must reference the official document")


@pytest.mark.phase18
def test_phase18_no_board_verified_promotion():
    """Official matrices must not promote any subject to BOARD_VERIFIED."""
    for label, path in MATRIX_FILES.items():
        text = path.read_text()
        assert "BOARD_UNVERIFIED" in text, label
        for row in _table_rows(path)[1:]:
            for cell in row:
                assert "BOARD_VERIFIED" not in cell, (label, row)
        for line in text.splitlines():
            if "BOARD_VERIFIED" in line:
                assert "promot" in line.lower(), (label, line)


@pytest.mark.phase18
def test_phase18_secondary_matrices_retained():
    """The Phase 16B secondary matrices remain labelled SECONDARY."""
    for name in ("JAMB_MATHEMATICS_SECONDARY_COVERAGE.md",
                 "JAMB_PHYSICS_SECONDARY_COVERAGE.md",
                 "JAMB_CHEMISTRY_SECONDARY_COVERAGE.md"):
        p = ARCH / name
        assert p.is_file(), name
        rows = _table_rows(p)
        for row in rows[1:]:
            assert row[1].upper() == "SECONDARY", (name, row)


@pytest.mark.phase18
def test_phase18_registers_updated():
    closure = (ARCH / "CLOSURE_REGISTERS.md").read_text()
    cross = (ARCH / "CROSS_SUBJECT_GAP_REGISTER.md").read_text()
    dedup = (ARCH / "DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md").read_text()
    for token in ("Phase 18", "JAMB official UTME E-syllabus obtained"):
        assert token in closure, token
        assert token in cross, token
    assert "Phase 18 — official JAMB E-syllabus confirmation" in dedup
    # corrections recorded
    assert "Modular arithmetic" in dedup and "I.1(c)" in dedup
    assert "Buffer solution" in dedup
    # new gaps recorded
    for token in ("P-18", "P-19", "C-15"):
        assert token in dedup, token


@pytest.mark.phase18
def test_phase18_no_out_of_scope_artifacts():
    for name in ("JAMB_BIOLOGY_OFFICIAL_COVERAGE.md",
                 "JAMB_ENGLISH_OFFICIAL_COVERAGE.md",
                 "WAEC_BIOLOGY_OFFICIAL_COVERAGE.md",
                 "BIOLOGY_SYLLABUS_COVERAGE.md"):
        assert not (ARCH / name).exists(), name


@pytest.mark.phase18
def test_phase18_store_and_protected_records_unchanged():
    """Phase 18 changes documentation only; the graph store is unchanged."""
    from examples.math_scope_expansion import build_graph_v40
    from cdg.enums import ClaimStatus, EntityType, RelationshipType
    from cdg.validation import run_store_validation

    s = build_graph_v40()
    assert run_store_validation(s) == []
    kc_counts = {}
    for subj in ("Mathematics", "Physics", "Chemistry", "Biology", "English"):
        kc_counts[subj] = sum(
            1 for e in s.entities.values()
            if e.entity_type == EntityType.KNOWLEDGE_COMPONENT and e.subject == subj)
    assert kc_counts == {"Mathematics": 44, "Physics": 25, "Chemistry": 21,
                         "Biology": 0, "English": 0}
    # the proposed indicates claim stays PROPOSED
    inds = [c for c in s.claims.values()
            if c.predicate == RelationshipType.INDICATES]
    assert len(inds) == 1 and inds[0].status == ClaimStatus.PROPOSED
    # entity-type enum remains at 13 types
    assert len(list(EntityType)) == 13
