# Phase 17 Report — Mathematics Scope Expansion (Sets, Logic, Sequences & Series, Matrices & Determinants, Mensuration)

Baseline commit: `1afe4a4` ("Phase 16B: secondary syllabus comparison … 151 tests green"),
working tree clean. Final commit: see `git log` after this phase.

## 1. Baseline (recorded before any changes)

- Commit: `1afe4a4`, working tree clean.
- Tests: 151 passing (`python3 -m pytest -q`).
- Store validation: `run_store_validation(build_graph_v39()) == []`.
- Canonical store: 340 entities / 554 claims / 276 evidence / 83 sources / 192 activities.
- Mathematics: 39 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED (declared scope).
- Physics: 25 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
- Chemistry: 21 KCs — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED.
- Biology: 0 KCs (on hold, OD-05); English: 0 KCs.
- `indicates` claim: single, PROPOSED (unchanged).
- Entity types: 13 (including `Subject`); frozen-count test passes.

## 2. Four-family audit (Phase 17A)

Documented in `docs/research/PHASE17_AUDIT.md`. Each family audited independently
against canonical records and NERDC official curriculum documents
(retrieved + text-extracted Phase 16; SSS1/SSS2; SSS3 unretrieved).

| Family | Audit verdict | Evidence | Deficiency |
|---|---|---|---|
| Sets and logic | MISSING | NERDC Math SSS1 p.7 (Sets), p.8 (Logic); SSS2 p.9 (Logic) | No sets/logic KC, TM, method, item |
| Sequences and series | MISSING | NERDC Math SSS2 p.1 | No sequences KC |
| Matrices and determinants | MISSING | JAMB SN6 / WAEC topic 11 via Syllabus NG (secondary) | No matrices KC; NOT in NERDC SSS1/SSS2 topic lists |
| Mensuration | MISSING | NERDC Math SSS1 p.11 | No mensuration KC |

No KC-id collisions with the 39 existing Mathematics KCs; no existing TM/Method/Item
covered these families; no cross-subject dependency changes required; no cycles
introduced (all new prerequisite edges point downward into existing foundational KCs).

## 3. Implementation (Phase 17D) — batches 066-069

Builder: `examples/math_scope_expansion.py` (`build_graph_v40()`, chains `build_graph_v39`).

Files changed:
- `examples/math_scope_expansion.py` (new) — builder `build_graph_v40()`.
- `examples/math_cdg_v2.json` — regenerated with the v40 chain.
- `tools/generate_math_cdg_docs.py` — imports v40; DOMAIN_OF/BATCH_OF entries added for the five new KCs.
- `tests/test_phase17_maths.py` (new) — ten focused tests.
- Regenerated: `docs/MATHEMATICS_CDG.md`, `docs/architecture/MATHEMATICS_COVERAGE.md`,
  `docs/visualizations/*.svg|html|dot` (six files).
- Documentation: `docs/architecture/MATHEMATICS_SYLLABUS_COVERAGE.md`,
  `docs/architecture/DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md`,
  `docs/architecture/SUBJECT_COMPLETION_ROADMAP.md`,
  `docs/architecture/CLOSURE_REGISTERS.md`,
  `docs/source-documents/SRC.SYLLABUSNG.JAMB.MATH.json`,
  `docs/source-documents/SRC.SYLLABUSNG.WAEC.MATH.json`.

Entities, claims, and edges added (subject Mathematics):
- 5 KnowledgeComponents — all ACCEPTED, HUMAN-reviewed:
  - `kc.sets_operations` (set definitions, notation, types, union/intersection/complement)
  - `kc.logical_reasoning` (simple/compound statements, operators, truth values)
  - `kc.sequences_series` (A.P./G.P., nth term, means, real-life problems)
  - `kc.matrix_algebra` (matrix notation/operations; determinants ≤3×3; inverses 2×2; simultaneous equations)
  - `kc.mensuration` (arcs, sectors, segments, solid shapes, frustum, compound shapes)
- 5 TaskModels, 10 Methods, 5 Items — all ACCEPTED.
- Claims: per TaskModel — `targets` (5), `hasMethod` (10), `requires` (10); prerequisites —
  4 UNDERSTAND (ASSERTED / ALL_RELEVANT_METHODS): logic→sets, sequences→integer arithmetic,
  matrices→linear equations, mensuration→circle theorems (all documented as curriculum-adjacency
  elaboration, not source-mandated).
- Sets/logic/sequences/mensuration evidenced by NERDC official documents (SSS1 pp.7/8/11;
  SSS2 p.1). Matrices evidenced ONLY by JAMB SN6 / WAEC topic 11 via Syllabus NG (secondary
  aggregator) — disclosed in KC rationale and documentation; not in NERDC SSS1/SSS2 topic lists
  (SSS3 unretrieved).
- Existing Mathematics and Physics records, legacy identifiers, and cross-subject edges
  unchanged (regression tests enforce).
- No `indicates` claim created or promoted; remains single PROPOSED.
- No new relation types; 13 entity types preserved; no Biology/English artifacts.

Sources and provenance:
- Existing sources `SRC.NERDC.SSS1.MATH.2025` and `SRC.NERDC.SSS2.MATH.2025` (registered
  Phase 16).
- Two new secondary sources: `SRC.SYLLABUSNG.JAMB.MATH`, `SRC.SYLLABUSNG.WAEC.MATH`
  (metadata only; direct access HTTP 403 JS challenge; content via reader proxy; no PDF).
- Every new claim's acceptance is backed by an `EvidenceItem` (INDIRECT, SUPPORTS) with a
  paraphrased excerpt and page locator. Every new entity/claim carries Phase 17 extraction,
  interpretation and human-review Activities.

## 4. Tests and validation

- Baseline: 151 tests passing (Phase 16B state).
- Final: **161 tests passing** (10 new, `tests/test_phase17_maths.py`).
- Store validation: `run_store_validation(build_graph_v40())` returns `[]`.
- Round-trip serialization and `export_view` verified; all claim endpoints resolve.
- Generators deterministic: repeated runs of `tools/generate_math_cdg_docs.py` and
  `tools/generate_cdg_visualization.py` produce byte-identical output.
- Full existing suite (historical builders v30–v39) passes unmodified.
- Entity types remain 13; frozen-count test passes.
- Final counts: 365 entities / 583 claims / 288 evidence / 85 sources / 192 activities.
  Mathematics KCs: 44 (was 39); Physics: 25; Chemistry: 21.

## 5. Regression checks confirmed

- Mathematics median/dispersion, logarithms, and all cross-subject edges: intact.
- Logarithms-to-pH dependency (`cl.pre56.log_ph`) intact; legacy IDs preserved.
- The `indicates` claim remains PROPOSED.
- No Biology or English entities (0 KCs each).
- Physics and Chemistry implementation records untouched.
- Generators deterministic; serialization round-trip correct.

## 6. Mathematics status (Subject Completion Standard v1.2)

- Implementation dimension: **IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED** (retained; declared
  scope expanded to include sets, logic, sequences & series, mensuration, and matrices &
  determinants).
- Board-verification dimension: **BOARD_UNVERIFIED** (unchanged). No official JAMB/WAEC/NERDC
  examination alignment has been verified; NERDC curriculum content-check alone is not
  board verification. Per ratified OD-04, both dimensions are tracked separately.
- Per clause C, IMPLEMENTATION_COMPLETE never implies JAMB/WAEC/NERDC alignment.
- Limitation disclosed: matrices & determinants were implemented on secondary Syllabus NG
  evidence only (not in NERDC SSS1/SSS2 topic lists; SSS3 unretrieved); this is not
  official confirmation.

## 7. Remaining gaps (Mathematics)

NOT_COVERED rows requiring owner scope decisions (per updated
MATHEMATICS_SYLLABUS_COVERAGE.md and DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER):
- Modular Arithmetic, Approximation, Surds, Bearings, Proofs of Some Basic Theorems,
  Construction, Cumulative Frequency Graph (Ogive — documented deferral).
- Matrices & determinants: implemented on secondary evidence only; official confirmation
  pending (SSS3 unretrieved; JAMB/WAEC official documents not obtained).

## 8. Recommended next step

Resume official-source verification: identify the IBASS API request contract from the SPA
bundle; retry JAMB per-subject PDFs; check waecnigeria.org publications for current WASSCE
syllabus PDFs (or submit an official request to WAEC Nigeria); attempt NERDC SSS 3 via
alternative official channels. Promote coverage rows to BOARD_VERIFIED only on checked
content. Owner decisions requested on the remaining NOT_COVERED Mathematics rows.
Biology remains on hold — not opened in this phase.
