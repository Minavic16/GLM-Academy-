# Phase 15 Report — Chemistry Organic-Reactions Gap Closure

Baseline commit: `b20c53b` ("Phase 14: physics completion wave (batches
059-064), UNDERSTAND-scope defect fix, roadmap/register updates, 125
tests green"). Final commit: see `git log` after this phase.

## Gaps audited (with dispositions) — see PHASE15_GAP_AUDIT.md

All documented Chemistry gaps were re-audited against the canonical store
and verified against OpenStax Chemistry 2e chapter coverage:

| Gap | Class | Disposition |
|---|---|---|
| Organic reactions (reactions of alkanes/alkenes, carbonyl reactions, amines/amides) | IMPLEMENTATION_GAP | **Implemented** — batch 065 (Phase 15B). |
| Buffers proper | BLOCKED (scope constraint) | Not implemented; see "Remaining gaps". |
| Polymers / industrial chemistry | DEFERRED (owner-documented) | Not implemented; unchanged. |
| Electrolytic cells detail / transition metals | DEFERRED (owner-documented) | Not implemented; unchanged. |
| Practical chemistry, official detail | OFFICIAL_VERIFICATION_GAP | Implementation complete; unchanged (CI-05). |
| All other existing 12 Chemistry KCs | — | No implementation gap found; all closure-audit records hold. |

## Implementation (Phase 15B) — batch 065

Files changed:
- `examples/chemistry_organic_reactions.py` (new) — builder
  `build_graph_v39()` chains `build_graph_v38`.
- `examples/math_cdg_v2.json` — regenerated with the v39 chain.
- `tools/generate_math_cdg_docs.py` — imports v39; DOMAIN_OF/BATCH_OF
  entries added for the nine new KCs.
- `tests/test_phase15_organic.py` (new) — nine focused tests.
- Regenerated: `docs/MATHEMATICS_CDG.md`,
  `docs/architecture/MATHEMATICS_COVERAGE.md`,
  `docs/visualizations/*.svg|html|dot` (six files).

Entities, claims, and edges added (subject Chemistry):
- 9 KnowledgeComponents: `kc.reactions_of_alkanes`,
  `kc.reactions_of_alkenes`, `kc.isomerism`, `kc.alcohols`,
  `kc.ethers`, `kc.aldehydes_ketones`, `kc.carboxylic_acids`,
  `kc.amines`, `kc.amides` — all ACCEPTED, HUMAN-reviewed.
- 9 TaskModels, 13 Methods, 9 Items — all ACCEPTED.
- Claims (subject Chemistry): per TaskModel — `targets` (9), `hasMethod`
  (13), `requires` (13); prerequisites — 8 UNDERSTAND (ASSERTED /
  ALL_RELEVANT_METHODS) and 1 EXECUTE (DERIVED /
  SPECIFIC_TASK_MODEL) on `kc.mole_stoichiometry`.
- No new cross-subject dependency claims were created (Phase 15
  restriction). All prerequisite claims are Chemistry-internal.
- No `indicates` claim was created or promoted; the single existing
  `indicates` claim remains PROPOSED.
- Existing Mathematics and Physics records, legacy identifiers, and
  cross-subject edges are byte-identical to the v38 state (regression
  tests enforce).

Sources and provenance:
- Three new Sources, all OpenStax Chemistry 2e chapters 20-2, 20-3,
  20-4 (20-1 already registered): `SRC.OSX.CHEM2E.20.2/20.3/20.4`.
  All four chapter URLs were verified HTTP 200 and their content quoted
  in the store before citation. Every new claim's acceptance is backed
  by an `EvidenceItem` (INDIRECT, SUPPORTS) drawn from these pages.
- Every new entity/claim carries the Phase 15 extraction, interpretation,
  and human-review Activities.

## Tests and validation

- Baseline: 125 tests passing (Phase 14 state).
- Final: **134 tests passing** (9 new, `tests/test_phase15_organic.py`).
- Store validation: `run_store_validation(build_graph_v39())` returns `[]`.
- Round-trip serialization and `export_view` verified.
- Generators deterministic: repeated runs of
  `tools/generate_math_cdg_docs.py` and `tools/generate_cdg_visualization.py`
  produce byte-identical output (md5-stable).
- Entity types remain 13 (`Subject` included); frozen-count test passes.
- Final counts: 340 entities / 554 claims / 276 evidence / 83 sources /
  192 activities. Chemistry KCs: 21 (was 12); Physics KCs: 25;
  Mathematics KCs: 39.

## Regression checks confirmed

- Mathematics median/dispersion records, legacy ids, and cross-subject
  edges: intact (`test_phase15_baselines_intact`).
- Logarithms-to-pH dependency (`cl.pre56.log_ph`) and its scoped
  prerequisite: intact.
- The `indicates` claim remains PROPOSED.
- No Biology or English entities exist.
- Existing cross-subject prerequisite claims unchanged (33 at v38,
  none added; see `test_phase15_no_cross_subject_edges_added`).
- All pre-existing test files (historical builders v30–v38) pass
  unmodified.

## Chemistry status (Subject Completion Standard v1.2)

- Implementation dimension: **IMPLEMENTATION_PARTIAL** (retained).
  The organic-reactions gap is closed, but the buffers gap is blocked and
  the deferred families (polymers, industrial chemistry, transition
  metals) remain out of scope.
- Board-verification dimension: **BOARD_UNVERIFIED** (unchanged).
  No official JAMB/WAEC/NERDC content has ever been verified, and none
  was claimed in this phase.
- Per ratified OD-04, both dimensions are tracked separately; this
  subject is never described as complete while BOARD_UNVERIFIED holds.

## Remaining gaps and limitations

1. **Buffers proper (BLOCKED).** Buffer-solution depth requires the
   Mathematics logarithms KC; creating that prerequisite edge would
   modify Mathematics-side records, which Phase 15 forbids. Blocked by
   an explicit phase restriction, not by missing evidence.
2. **Polymers, industrial chemistry (DEFERRED).** Explicitly deferred by
   owner-documented scope decisions; OpenStax Chemistry 2e has no such
   chapters. Requires owner authorization to reopen.
3. **Electrolytic cells detail / transition metals (DEFERRED).** Same:
   explicitly deferred; chapter 19 exists in OpenStax but the deferral
   stands.
4. **Official-board verification (all three subjects).** IBASS is a
   hashed JS SPA, WAEC links no syllabus PDF, NERDC is unreachable.
   No official content has ever been verified. Blocked pending owner
   decision on whether/which official retrieval is authorized.

## Recommended next step

**Phase 16 — official-source verification (M-1)**: a shared plan for
retrieving JAMB/WAEC/NERDC syllabus documents, content-checking them
against the CDG coverage matrices, and promoting rows from
BOARD_UNVERIFIED to BOARD_VERIFIED only on checked content. This is the
only remaining implementation-gap-free workstream; Biology remains on
hold until Mathematics, Physics, and Chemistry are sufficiently closed
and the owner authorizes it.

No Biology implementation work occurred at any point in Phase 15.
