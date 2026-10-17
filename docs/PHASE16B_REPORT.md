# Phase 16B Report — Secondary Syllabus Comparison Using Syllabus NG

Baseline commit: `0fc3140` ("Phase 16: official syllabus retrieval and CDG coverage verification —
NERDC SSS 1/SSS 2 Math/Physics/Chemistry retrieved and content-checked, JAMB/WAEC unresolved,
coverage matrices + gap register + reports, 141 tests green"). Final commit: see `git log` after
this phase.

## 1. Baseline (recorded before any changes)

- Commit: `0fc3140`, working tree clean.
- Tests: 141 passing (`python3 -m pytest -q`).
- Store validation: `run_store_validation(build_graph_v39()) == []`.
- Canonical store unchanged: 340 entities / 554 claims / 276 evidence / 83 sources / 192 activities.
- Mathematics: 39 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
- Physics: 25 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
- Chemistry: 21 KCs — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED.
- Biology: 0 KCs (on hold, OD-05); English: 0 KCs.
- `indicates` claim: single, PROPOSED (unchanged).
- Entity types: 13 (including `Subject`); frozen-count test passes.

## 2. Sources inspected (Phase 16B)

Syllabus NG (syllabus.ng) is a THIRD-PARTY/SECONDARY syllabus aggregator — NOT an official
examination board. Direct access returns a JavaScript challenge page (HTTP 403); content was
extracted through the r.jina.ai reader proxy on 2026-10-17. No downloadable PDF files were found
on any page. All six pages carry a "Published Time" (2024) but no explicit displayed syllabus
year or country applicability; applicability to any specific UTME/WASSCE cycle is UNRESOLVED.

| Page | URL | Source title | Published Time (page metadata) | PDF/download file | Retrieved |
|---|---|---|---|---|---|
| JAMB Mathematics | https://syllabus.ng/jamb/math/ | JAMB Mathematics Syllabus | 2024-03-30T15:01:46+00:00 | none | yes (via reader proxy) |
| JAMB Physics | https://syllabus.ng/jamb/physics/ | JAMB Physics Syllabus | 2024-03-21T20:55:46+00:00 | none | yes |
| JAMB Chemistry | https://syllabus.ng/jamb/chemistry/ | JAMB Chemistry Syllabus | 2024-03-31T10:40:46+00:00 | none | yes |
| WAEC Mathematics | https://syllabus.ng/waec/math/ | WAEC Mathematics Syllabus | 2024-04-28T15:26:26+00:00 | none | yes |
| WAEC Physics | https://syllabus.ng/waec/physics/ | WAEC Physics Syllabus | 2024-05-01T05:51:12+00:00 | none | yes (see data-quality note) |
| WAEC Chemistry | https://syllabus.ng/waec/chemistry/ | WAEC Chemistry Syllabus | 2024-05-01T05:59:05+00:00 | none | yes |
| WAEC directory | https://syllabus.ng/waec/ | WAEC Syllabus | 2024-04-24T08:43:56+00:00 | none | yes (navigation only) |

### Data-quality notes
- **WAEC Physics page anomaly**: topics 1–8 on the /waec/physics/ page are Physics content;
  topics 9–44 are Mathematics content (identical to the /waec/math/ page). This is a syllabus.ng
  page defect. Topics 9–44 are treated as NOT_APPLICABLE to Physics. Consequently the WAEC
  Physics secondary source covers only topics 1–8 and is insufficient alone to assess Physics
  coverage.
- No page links to a downloadable PDF, so no file hash/metadata could be recorded for syllabus.ng.
- Syllabus NG content is secondary evidence: it must never be used to promote any subject to
  BOARD_VERIFIED.

## 3. Six secondary-source coverage matrices created

Each matrix follows the existing coverage-matrix conventions with the required columns:
authority_claimed_by_source, source_type (explicitly "SECONDARY"), subject,
displayed_syllabus_year, source_url, topic, subtopic_or_objective, cdg_entity_ids,
coverage_status, evidence_reference, gap_description, recommended_action,
official_verification_status.

Allowed coverage vocabulary used: COVERED | PARTIALLY_COVERED | NOT_COVERED |
NOT_APPLICABLE | UNRESOLVED.

| Matrix file | Subjects/examination | Rows | COVERED | PARTIALLY_COVERED | NOT_COVERED | NOT_APPLICABLE |
|---|---|---|---|---|---|---|
| docs/architecture/JAMB_MATHEMATICS_SECONDARY_COVERAGE.md | JAMB UTME Mathematics | 23 | 2 | 15 | 6 | 0 |
| docs/architecture/JAMB_PHYSICS_SECONDARY_COVERAGE.md | JAMB UTME Physics | 39 | 1 | 33 | 3 | 0 |
| docs/architecture/JAMB_CHEMISTRY_SECONDARY_COVERAGE.md | JAMB UTME Chemistry | 18 | 0 | 12 | 6 | 0 |
| docs/architecture/WAEC_MATHEMATICS_SECONDARY_COVERAGE.md | WAEC WASSCE Mathematics | 25 | 0 | 22 | 3 | 0 |
| docs/architecture/WAEC_PHYSICS_SECONDARY_COVERAGE.md | WAEC WASSCE Physics | 9 | 0 | 8 | 0 | 1 (page anomaly) |
| docs/architecture/WAEC_CHEMISTRY_SECONDARY_COVERAGE.md | WAEC WASSCE Chemistry | 17 | 0 | 16 | 3 | 0 |

Coverage rule applied: a topic is COVERED only if the CDG supports the relevant scope and depth
of the listed topic/objective. A matching topic name alone is insufficient. Consequently nearly
all matched topics are PARTIALLY_COVERED at best — the CDG has the KC but not method-level
evidence for every listed performance objective.

## 4. Consolidated comparison

Created docs/architecture/CONSOLIDATED_NERDC_JAMB_WAEC_COMPARISON.md — one consolidated topic
matrix per subject (Mathematics, Physics, Chemistry) showing, for each topic family:
- NERDC SSS1/SSS2 evidence (Phase 16 primary source)
- JAMB secondary-source evidence
- WAEC secondary-source evidence
- Existing CDG entities and claims
- Coverage disagreements
- Missing CDG content
- Official-verification status
- Recommended next action

Key reconciliation findings:
- NERDC SSS1/SSS2 topic lists omit several topics that JAMB and WAEC both list (sets, logic,
  sequences & series, matrices, mensuration, loci/construction, calculus detail, financial
  maths, friction as standalone, water, air, non-metals, metals, industry, pollution). This is
  NOT evidence of error in NERDC — SSS3 remains unretrieved and the topic lists are summaries —
  but these discrepancies are flagged for owner decision.
- JAMB and WAEC are broadly consistent; WAEC includes a detailed practical paper (quantitative
  titrations + qualitative analysis) that JAMB (written UTME) does not.
- The CDG covers the core families but lacks entire families: sets, logic, matrices, mensuration,
  projectile motion, SHM, water, air, non-metals, metals, polymers, industry.

## 5. Deduplicated proposed implementation-gap register

Created docs/architecture/DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md — 45 proposed gaps
deduplicated by topic family per subject (19 Mathematics, 17 Physics, 14 Chemistry, 1
cross-subject), each listing every source evidencing it (NERDC / JAMB / WAEC), the affected
CDG entities, gap class, status (Open / Blocked / Deferred), rationale, proposed resolution,
and next action.

Cross-subject gap X-01 (Chemistry buffers ← Mathematics logarithms): blocked by the Phase 15/16
scope constraint — creating the prerequisite edge would modify Mathematics-side records. No
Mathematics records were altered in Phase 16B.

## 6. Topics requiring official confirmation

All gaps above carry official_verification_status BOARD_UNVERIFIED. Topics requiring explicit
official confirmation before any scope decision:
- Present in JAMB/WAEC secondary sources but absent from NERDC SSS1/SSS2 topic lists:
  modular arithmetic; matrices; loci/construction; vectors (Math); transformations;
  simple machines; elasticity; air; metals; polymers; industrial chemistry; pollution;
  solubility.
- Present in NERDC but not evidenced at CDG method level: all PARTIAL_GAP rows.
- Official JAMB/WAEC documents were not obtained in Phase 16 (IBASS SPA shell; WAEC archive
  stub; e-learning = past questions only), and NERDC SSS3 is unretrieved — so no topic can be
  promoted to COVERED-at-official level yet.

## 7. Scope and implementation restrictions observed

- No canonical CDG entities, claims, or edges were added or edited (build_graph_v39 unchanged).
- No canonical 13 entity types changed; no relation semantics altered.
- No subject implementation status changed; no subject promoted to BOARD_VERIFIED.
- The existing `indicates` claim was not promoted (still single, PROPOSED).
- No Biology or English artifacts introduced.
- No previously deferred Chemistry topic silently reopened; all Chemistry deferrals (polymers,
  industrial chemistry, transition metals) remain documented deferrals.
- No Mathematics-side records modified to resolve the Chemistry buffers dependency (X-01 remains
  blocked pending owner-authorized scoped change).
- New potential gaps are recorded in the proposed register only — not implemented.

## 8. Quality assurance — test results

### New test file: tests/test_phase16b_secondary.py
Verifies:
- All six matrices exist.
- Each row has a source URL, source type, topic, coverage status, and evidence reference.
- Every Syllabus NG row is explicitly labelled "SECONDARY".
- Secondary-source evidence cannot promote official board-verification status (all matrix
  official_verification_status values are BOARD_UNVERIFIED).
- Existing canonical store counts and protected records remain unchanged (340 entities / 554
  claims; Math 39 / Physics 25 / Chemistry 21 KCs; Biology 0; English 0).
- No Biology or English artifacts introduced.

### Results
- `python3 -m pytest -q`: **162 passed** (141 baseline + 21 new Phase 16B tests).
- Store validation: `run_store_validation(build_graph_v39()) == []`.
- Serialization round-trip and export_view verified.
- `tools/generate_math_cdg_docs.py` and `tools/generate_cdg_visualization.py` run cleanly;
  output deterministic (byte-identical on repeated runs).

## 9. Subject implementation and board-verification statuses (unchanged)

| Subject | Implementation | Board verification | Basis |
|---|---|---|---|
| Mathematics | IMPLEMENTATION_COMPLETE | BOARD_UNVERIFIED | Declared scope complete; JAMB/WAEC official docs not obtained |
| Physics | IMPLEMENTATION_COMPLETE | BOARD_UNVERIFIED | Declared scope complete; JAMB/WAEC official docs not obtained |
| Chemistry | IMPLEMENTATION_PARTIAL | BOARD_UNVERIFIED | Buffers blocked (CI-12); polymers/industry/transition metals deferred |
| Biology | ON HOLD | — | OD-05 hold; no artifacts created |

## 10. Conclusions (three separate conclusions)

### A. What the secondary-source comparison suggests is missing from the CDG
Mathematics: sets, logic, modular arithmetic, surds, sequences & series, matrices,
mensuration, loci/construction, binary operations, permutation/combination, coordinate-geometry
line forms, trigonometry applications, calculus limits/area, grouped-data statistics/ogive,
compound probability, vectors, transformations, financial mathematics.
Physics: projectile motion, SHM, simple machines, elasticity, circular motion, electrostatics,
capacitors, electric cells, circuit-analysis methods, A.C. circuits, modern-physics detail,
viscosity/Stoke's law, energy-society applications.
Chemistry: water; air; non-metals; metals; alkynes/benzene/carbohydrates/proteins; polymers;
industrial chemistry; pollution; solubility; separation-technique methods; salt
preparation/hydrolysis; buffers (blocked); WAEC-specific titration and qualitative-analysis
detail.
All of the above are PROPOSED gaps requiring owner scope decisions — none implemented.

### B. What has been verified against retrieved NERDC curriculum documents
NERDC SSS1/SSS2 Mathematics, Physics, Chemistry (October 2025, Federal Ministry of Education)
were retrieved, extracted, authenticity established, and topic-mapped in Phase 16. Core families
are represented in the CDG: algebra/trigonometry/calculus/statistics (Math); mechanics/waves/
optics/electricity/modern physics (Physics); atoms/bonding/mole/acids/redox/organic (Chemistry).
SHA-256 hashes recorded for all five NERDC PDFs; metadata in docs/source-documents/.

### C. What remains unverified
Official JAMB UTME and WAEC WASSCE syllabus documents were NOT obtained (IBASS is a JS SPA
returning shell HTML; WAEC 2017–2019 archive is a stub; WAEC e-learning = past questions only),
and NERDC SSS3 is unretrieved. Therefore no subject can be BOARD_VERIFIED; all three remain
BOARD_UNVERIFIED. Syllabus NG is a secondary source and cannot substitute for official
verification.

## 11. Recommended next step

Proceed to owner decisions on the deduplicated implementation-gap register
(Docs/architecture/DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md), prioritizing gaps evidenced by
two or more sources (sets, logic, sequences & series, matrices, projectile motion, SHM, water,
air, non-metals, metals, polymers, industrial chemistry). Then resume official-source retrieval:
identify the IBASS API request contract from the SPA bundle; check waecnigeria.org publications
for current WASSCE syllabus PDFs; attempt NERDC SSS 3 via alternative official channels. Biology
remains on hold — do not open Biology.
