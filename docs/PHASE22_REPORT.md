# Phase 22 — Mathematics P1 closure + retrieval sprint (owner-authorized)

Date: 2026-10-17. Baseline: `main` @ `63f4567` (Phase 20 close-out), remote
`origin` = `https://github.com/Minavic16/GLM-Academy-.git`. Working tree
carried only the uncommitted Phase 21 documentation set (2 modified, 2 new),
preserved unchanged.

## 1. Authorization and scope

The owner authorized the P1 closure package of the Phase 21 audit
(`OWNER_DECISION_BRIEF_PHASE21.md`, decisions D1/D2/D3; D4 operative in
substance — see §10 there):

- Implement the three P1 Mathematics topics, controlled by the official JAMB
  UTME Mathematics E-syllabus (SRC.JAMB.UTME.MATH.2025):
  - II.5 binary operations (p.3) — properties of closure, commutativity,
    associativity and distributivity; identity and inverse elements (simple
    cases only);
  - III.3 loci (p.4) + the relevant construction objectives under III.1
    (p.3, objective iv: construction procedures of special angles, e.g.
    30°, 45°, 60°, 75°, 90°) — perpendicular bisectors, angle bisectors,
    other syllabus-supported constructions, intersection-of-loci problems;
  - V.1 representation of data (p.5) — frequency distribution; histogram,
    bar chart and pie chart.
- Declared target: all 23 official JAMB Mathematics topics implemented at
  topic level, with residual depth documented and prioritized separately
  (P2 depth waves NOT authorized; ogive/cumulative-frequency deferral
  stands; no new subjects; 13-entity-type architecture unchanged; no
  BOARD_VERIFIED promotions; `indicates` remains PROPOSED).
- Run a bounded official-source retrieval sprint (WAEC syllabus; NERDC SSS3;
  JAMB applicable cycle) without letting it delay or fabricate anything.
- Close out: tests, docs, canonical export, commit/push; end at
  IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.

## 2. Baseline audit (live, before any change)

- `build_graph_v41()`: entities 424 / claims 678 / evidence 337 / sources
  86 / activities 234; Mathematics KCs 54; `run_store_validation == []`;
  suite `199 passed, 58 warnings`.
- All baseline figures were recomputed from the builder at the start of the
  phase (not quoted from memory); the Phase 21 docs set in the tree was
  preserved and committed ahead of the Phase 22 changes (see §7).

## 3. Implementation record (batches 080–082, build_graph_v42)

Sole new canonical authority: `examples/math_p1_closure_phase22.py`
(`build_graph_v42()` chains `build_graph_v41()`; every earlier record is
carried forward unchanged — verified by regression test).

| Batch | Topic | New records |
|---|---|---|
| 080 | Binary operations (II.5) | kc.binary_operations; tm.binary_operations_problems; m.evaluate_binary_operation; m.binary_operation_properties; m.identity_inverse_elements; it.math.binary_operation; it.math.binary_identity |
| 081 | Loci & construction (III.3; III.1d objective iv) | kc.loci_and_construction; tm.loci_construction_problems; m.describe_locus; m.construct_perpendicular_bisector; m.construct_angle_bisector; m.construct_special_angles; m.apply_loci_intersections; it.math.loci; it.math.loci_construction; it.math.special_angle_construction |
| 082 | Representation of data (V.1) | kc.data_representation; tm.data_representation_problems; m.frequency_distribution_table; m.construct_bar_chart; m.construct_histogram; m.construct_pie_chart; it.math.frequency_table; it.math.pie_chart; it.math.data_representation_choice |

Totals after Phase 22 (all re-verified live):

- entities 450 (424 + 3 KCs + 3 TMs + 12 methods + 8 items);
- claims 725 (678 + 47: 3 targets + 12 hasMethod + 25 requires + 7
  prerequisite);
- evidence 359 (337 + 22); sources 86 (unchanged; the JAMB source was
  registered in Phase 20); activities 243 (234 + 9);
- Mathematics KCs 57 (54 + 3); `run_store_validation == []`; deterministic
  (`dumps_store` byte-identical across rebuilds).

Provenance: every new evidence record cites SRC.JAMB.UTME.MATH.2025 with
precise locators (`JAMB Math p.3 (II.5)`; `p.3/4 (III.1d; III.3)`;
`p.5 (V.1)`); excerpts are paraphrase-grade of the exact official
content/objective wording extracted from the retrieved revision
(SHA-256 aff7a7c2…754f). No secondhand aggregator is cited anywhere in the
new records. All new claims ACCEPTED with HUMAN review; no record is
backdated or rewritten; 13 entity types; no Biology/English artifacts; no
cross-subject edges added (regression-tested).

Disclosed boundaries (no hidden scope claims):

- II.5 implemented at the UTME treatment only — evaluation under a defined
  rule/table; the four properties; identity/inverse in simple cases. No
  abstract-algebra or group-theory expansion.
- III.3/III.1(d) implemented as the syllabus construction procedures
  (perpendicular/angle bisectors, special angles 30°–90°, intersections of
  loci). No unrestricted Euclidean-geometry expansion; polygon/cyclic-
  quadrilateral/intersecting-chord depth stays open under M-27.
- V.1 implemented as representation only (frequency tables; histogram, bar
  chart, pie chart). Ogive/cumulative frequency remain excluded (standing
  owner deferral); the location/dispersion KCs are untouched; no P2
  statistics depth work was performed.

## 4. Coverage reconciliation (official JAMB dimension)

| Row | Phase 21 state | Phase 22 effect |
|---|---|---|
| II.5 binary operations | NOT_COVERED | COVERED (batch 080) |
| III.1 Euclidean geometry (construction component) | construction not evidenced | construction procedures implemented (batch 081); row remains PARTIALLY_COVERED for the polygon/cyclic/chord depth under M-27 |
| III.3 loci | NOT_COVERED | COVERED (batch 081) |
| V.1 representation of data | NOT_COVERED | COVERED (batch 082) |

Updated official counts (live-verified from the matrix, 23 rows):
**COVERED 8 / PARTIALLY_COVERED 15 / NOT_COVERED 0** — the declared
23-topic target is met at topic level. The 15 PARTIALLY_COVERED rows are
the documented P2 depth residuals in `MATHEMATICS_GAP_REGISTER.md`; they
are registered, unauthorized and prioritized separately (not part of this
authorization). Register dispositions: M-09 and M-10 closed at
implementation level; M-15's data-representation component implemented
(audit split M-15a; M-15b residuals remain: mode, grouped data,
cumulative frequency/ogive deferral, grouped dispersion).

## 5. Bounded retrieval sprint (official channels only)

| Blocker | Probes run this phase | Outcome |
|---|---|---|
| WAEC official WASSCE Mathematics syllabus | `waecnigeria.org/sitemap.xml` (404); site search “mathematics syllabus” and “syllabus” (Drupal search) — only the Bookkeeping & Office Practice 2022–2025 syllabus article, selected-texts lists and FAQ pages; no Mathematics syllabus article/attachment | **NOT OBTAINED** — the attachment channel exists (per-subject syllabus articles) but no Mathematics document is published there |
| NERDC SSS 3 Mathematics curriculum | `lmis.nerdcportals.com.ng/sss_3/` recheck (404, unchanged); LMIS root (login gate: “Please log in to continue” + registration link); `nerdc.org.ng` recheck (HTTP 500, unchanged) | **NOT OBTAINED** — no alternative official SSS3 publication found |
| JAMB applicable cycle for the official PDF | PDF metadata re-inspected (CreationDate = ModDate = 2025-07-31; no cycle field); extracted text re-grepped (no year/cycle marker); official IBASS SPA bundle re-grepped (no cycle strings); `jamb.gov.ng` context check (2026 cycle active at retrieval; no statement tying the e-syllabus revision to a cycle) | **UNRESOLVED** — a metadata date alone is insufficient |

No third-party source was substituted for any of these; no status was
promoted on the basis of nothing. Concrete follow-ups (unchanged from the
Phase 21 brief, still recommended): official WAEC enquiry for the published
“Regulations & Syllabuses” compilation; registered-institution LMIS access
route or official NERDC request; periodic rechecks. Evidence needed to
close the cycle question: an official JAMB artifact tying the IBASS
e-syllabus revision to a UTME cycle (or a versioned syllabus listing).
CI-24 remains Open; the subject stays BOARD_UNVERIFIED.

## 6. Documentation and registers updated

- `JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md`: Phase 22 note; baseline
  build_graph_v42; four rows refreshed (II.5, III.1 construction, III.3,
  V.1); summary counts 8/15/0 (Phase 19/20 records retained verbatim).
- `JAMB_MATHEMATICS_RECONCILIATION.md`: new §13 (disposition table +
  sprint probe log; §12/§11 history retained).
- `MATHEMATICS_GAP_REGISTER.md`: Phase 22 update paragraph; M-09, M-10
  closed; M-15 representation component recorded; owner-authorization note
  appended.
- `MATHEMATICS_SYLLABUS_COVERAGE.md` (NERDC dimension): Phase 22 update;
  Construction row closed; Data Presentation and Histogram of Grouped Data
  rows updated; remaining NOT_COVERED: Bearings, Proofs, Ogive (deferred).
- `CLOSURE_REGISTERS.md`: CI-23 updated (remaining: bearings, proofs,
  ogive); CI-24 updated with the Phase 22 sprint outcomes; Phase 22 log
  appended.
- `SUBJECT_COMPLETION_ROADMAP.md`: Mathematics header/status and remaining
  items updated; Phase 21 + Phase 22 entries added; next task updated.
- `DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md` and
  `CONSOLIDATED_NERDC_JAMB_WAEC_COMPARISON.md`: Phase 22 sections appended.
- `OWNER_DECISION_BRIEF_PHASE21.md`: §10 resolution note (D1–D4).
- Generated outputs: `examples/math_cdg_v2.json` = `dumps_store(build_graph_v42())`;
  `docs/MATHEMATICS_CDG.md`, `docs/architecture/MATHEMATICS_COVERAGE.md`
  and the Mathematics visualizations regenerated via the deterministic
  generators — double-run byte-stable (md5 unchanged across two runs).

## 7. Verification log

- Baseline: `199 passed, 58 warnings` (Phase 20 suite state).
- Phase 22 suite: `tests/test_phase22_math_p1_closure.py` (24 guards:
  schema/validation, count deltas, traceability, prerequisite qualifiers +
  acyclicity, evidence provenance/locators, no-ogive/no-P2-creep, no
  subject drift, serialization/export/determinism, docs/register/report
  currency).
- Full suite after changes: **214 passed, 73 warnings** (199 baseline + 15
  new Phase 22 guards); `run_store_validation(build_graph_v42()) == []`;
  JSON export identical to builder output; generators double-run
  byte-stable.
- Superseded assertions updated minimally in `test_phase19_…` (counts
  8/15/0; M-09 closure) and `test_phase20_…` (matrix counts superseded by
  Phase 22, Phase 20 history retained). No other test was weakened.
- Git: Phase 21 documentation set committed first (docs-only, baseline
  `63f4567`), then the Phase 22 change set; push only if the remote/branch
  check stays safe. No force-push.

## 8. What Phase 22 does not do (boundary record)

- No P2 depth work (13 residual rows remain unauthorized as a wave);
  no ogive/cumulative frequency (deferral stands); no new subjects.
- No schema/entity-type change; no subject-status promotion; `indicates`
  remains PROPOSED; no indication claim added.
- No rewrite of historical records: all Phase 18–21 text is preserved;
  updates are append-only or clearly-marked Phase 22 dispositions.
- No hand-edits of generated outputs: regenerated only via the
  deterministic builder/generator path.

## 9. Recommended next owner decision

Mathematics is IMPLEMENTATION_COMPLETE (declared scope) / BOARD_UNVERIFIED
at subject level, with all 23 official JAMB topics implemented and 15
documented depth residuals. Recommended: (1) accept the P1 closure and the
documented-residuals posture (D2(a)); (2) decide whether to schedule the
P2 depth waves or leave them registered, prioritizing `MATHEMATICS_GAP_
REGISTER.md` residuals (statistics depth / ogive reversal is the
highest-visibility cluster); (3) continue official WAEC/NERDC SSS3
retrieval for CI-24 when an owner decision or external access changes; (4)
note that Physics/Chemistry gap triage remains available as a follow-on.
