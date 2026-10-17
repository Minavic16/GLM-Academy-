# Phase 16 Report — Official Syllabus Retrieval and CDG Coverage Verification

Baseline commit: `43972fc` ("Phase 15: chemistry organic-reactions batch
(batches 065), buffers/deferred documented, PHASE15 reports, 134 tests
green"). Final commit: see `git log` after this phase.

## 1. Baseline (recorded before any changes)

- Commit: `43972fc`, working tree clean.
- Tests: 134 passing (`python3 -m pytest -q`).
- Store validation: `run_store_validation(build_graph_v39()) == []`.
- Canonical store: 340 entities / 554 claims / 276 evidence / 83 sources /
  192 activities (build_graph_v39).
- Entity types: 13 (including `Subject`); frozen-count test passes.
- Mathematics: 39 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
- Physics: 25 KCs — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED.
- Chemistry: 21 KCs — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED.
- Biology: 0 KCs (on hold, OD-05); English: 0 KCs.
- `indicates` claim: single, PROPOSED (unchanged).

## 2. Official sources investigated (Phase 16 retrieval)

Per Phase 16 rules: known official entry points attempted first; HTTP 200
never treated as proof; search snippets/JS rendering not accepted.

### JAMB / IBASS (attempted 2026-10-17)
- https://ibass.jamb.gov.ng/e-syllabus → HTTP 200 but JavaScript SPA shell
  (index.html, 1257 bytes) — not document content.
- https://ibass.jamb.gov.ng/assets/uploads/{Mathematics,Physics,Chemistry}.pdf →
  HTTP 200 but SPA shell (Apache fallback), Content-Type text/html — not PDF
  bytes.
- API https://ibass-api.jamb.gov.ng/api (discovered from SPA bundle,
  React/axios baseURL) → GET /api/e-syllabus, /api/brochure-courses,
  /api/materials all return {"error":true,...}; no request contract identified.
- Result: NO per-subject syllabus PDF bytes obtained. JAMB alignment
  UNRESOLVED (see docs/source-documents/SRC.JAMB.IBASS.ATTEMPT.2026-10-17.json).

### WAEC (attempted 2026-10-17)
- https://www.waecnigeria.org/ → HTTP 200; article
  /article/wassce-syllabuses-2017-2019 → reachable but stub page: no
  downloadable syllabus PDFs for Mathematics/Physics/Chemistry. The
  2017–2019 archive must not be assumed current.
- https://www.waeconline.org.ng/e-learning/{Mathematics,Chemistry,Physics}/
  → subject pages contain past WASSCE questions only (zero "syllabus"
  mentions, no syllabus PDF links).
- Result: NO current-cycle WAEC syllabus document obtained. WAEC alignment
  UNRESOLVED (see docs/source-documents/SRC.WAEC.ATTEMPT.2026-10-17.json).

### NERDC (attempted 2026-10-17)
- https://www.nerdc.gov.ng/ and .../new_senior_curriculum_home.html → HTTP 200.
- eCurriculum portal http://www.nerdc.org.ng/eCurriculum → HTTP 500.
- LMIS portals https://lmis.nerdcportals.com.ng/sss_1 and /sss_2 → HTTP 200
  with subject viewers; SSS 3 portals (/sss_3, /s3_core, /s3_science) → HTTP 404.
- Viewer iframes resolve to PDFs at
  .../sss_{1,2}/necurrdc/{id}.pdf (Mathematics=2, Chemistry=7, Physics=8,
  per observed listings).
- FIVE documents retrieved (HTTP 200, application/pdf), text extracted with
  pypdf, authenticity established (official domain, document footers
  "NEW REVISED SENIOR SECONDARY SCHOOL CURRICULUM … © October 2025",
  Federal Ministry of Education):
  - Mathematics SSS 1 (24 pp, SHA-256 a2f618…11c)
  - Mathematics SSS 2 (33 pp, SHA-256 f79d3f…f1cd)
  - Chemistry SSS 1 (31 pp, SHA-256 e0f9b0…26c)
  - Chemistry SSS 2 (45 pp, SHA-256 5e1473…efd)
  - Physics SSS 1 (63 pp, SHA-256 fc0648…5ee)
  - Physics SSS 2 (62 pp, SHA-256 88dd5d…236)
- Corroborating: "Basic and Senior Secondary Education Curriculum Offerings"
  (PDF metadata 2025-09-08) confirms Chemistry/Physics/General Mathematics in
  the senior-secondary Science/Core fields.
- SSS 3 not retrievable via the portal.

Per-document metadata (URLs, dates, SHA-256, limitations) is stored in
docs/source-documents/*.json (10 JSON metadata records). Copyrighted PDF bytes
are NOT committed (no repository policy permitting it); metadata, hashes, and
permitted extracted topic evidence are retained instead.

### Retrieval summary table

| Source | Documents obtained | Content extracted | Authenticity established | Board alignment usable? |
|---|---|---|---|---|
| NERDC SSS1/SSS2 Math/Phys/Chem | 5 PDFs | yes | yes | Partial (curriculum only; SSS3 missing; no exam-body alignment) |
| JAMB IBASS | 0 | no | no | No |
| WAEC Nigeria | 0 | no | no | No |

## 3. Coverage comparison (NERDC official curriculum vs canonical CDG)

Subject-specific syllabus-to-CDG coverage matrices created with the required
fields (authority, subject, document_version, official_topic,
official_subtopic_or_objective, cdg_entity_ids, coverage_status,
evidence_reference, gap_description, next_action) and explicit categories
(COVERED / PARTIALLY_COVERED / NOT_COVERED / NOT_APPLICABLE / UNRESOLVED):

- docs/architecture/MATHEMATICS_SYLLABUS_COVERAGE.md (SSS 1 + SSS 2 topics)
- docs/architecture/PHYSICS_SYLLABUS_COVERAGE.md (SSS 1 + SSS 2 topics)
- docs/architecture/CHEMISTRY_SYLLABUS_COVERAGE.md (SSS 1 + SSS 2 topics)

Every mapped row cites the NERDC document page (topic page from each
document's table of contents). Topics in the CDG but absent from the
verified document and topics required by the document but missing from the
CDG are identified separately (NOT_COVERED rows with gap_description).
Practical work (titration, qualitative tests, laboratory safety, separation
techniques; WAEC practical detail) reviewed separately from conceptual
coverage and remains UNRESOLVED at the board level (CI-25/CI-26).

### Mathematics (39 KCs)
COVERED: Laws of Indices, Logarithms, Quadratic Equations, Simultaneous
Linear/Quadratic Equations, Linear Inequalities, Probability, Measures of
Central Tendency, Measures of Dispersion.
PARTIALLY_COVERED: Number bases, Trigonometry, Simple Equations/Variations,
Data Presentation, Algebraic Fractions, Chord Properties, Gradient of a Curve,
Histogram of Grouped Data.
NOT_COVERED: Modular Arithmetic, Sets, Logic, Mensuration, Sequence and
Series, Approximation, Surds, Bearings, Proofs of Some Basic Theorems,
Construction, Ogive (documented deferral).

### Physics (25 KCs)
COVERED: quantities/units, position-distance-displacement, motion, speed/
velocity, acceleration, scalars/vectors, Newton's laws, work/energy/power,
gravitation, gas laws, electromagnetic waves, nuclear energy.
PARTIALLY_COVERED: time, electric charge, fluids, particulate matter, heat,
fields, temperature measurement, waves, light, sound, molecular theory,
optics instruments, laboratory use, standard reference temperature.
NOT_COVERED: Projectile Motion, Simple Harmonic Motion, Internet/Intranet.
NOT_APPLICABLE: Cartesian Coordinate System (mathematics content, covered in
Math CDG).

### Chemistry (21 KCs)
COVERED: elements/compounds/mixtures, atomic structure, chemical bonds,
chemical equilibrium, gas laws, acids/bases/salts, carbon and its compounds,
hydrocarbons (alkanes/alkenes), alkanols, redox reactions, electrolysis,
chemical substances, periodicity.
PARTIALLY_COVERED: separation techniques, laboratory safety, symbols/
formulae/equations, particulate nature, chemical combination, mass-volume
relationship, ionic theory, renewable/non-renewable energy.
NOT_COVERED: introductory concepts, chemical industry, branches of chemistry,
chemical hazards, water, air, hydrogen, oxygen, halogens, nitrogen, sulphur,
entrepreneurship, chemistry fair/career day (NOT_APPLICABLE event topic).

### Buffers (cross-subject, CI-11/CI-12)
"Buffers" is not an explicit NERDC SSS 1/SSS 2 topic. pH scale exists
(kc.ph_scale) via the Mathematics kc.logarithms cross-subject dependency
(cl.pre56.log_ph, scoped to tm.ph_problems). Buffers proper remain
NOT_IMPLEMENTED and BLOCKED: creating the required prerequisite edge would
modify Mathematics-side records, which Phase 15/16 forbid without an
explicitly scoped, owner-authorized change. No Mathematics records were
altered in this phase.

## 4. Entities, claims, edges added or changed

None. Phase 16 is research/retrieval/provenance/coverage-mapping only; the
canonical store (build_graph_v39) is unchanged:
- Entities: 340 (no change)
- Claims: 554 (no change)
- Evidence: 276 (no change)
- Sources: 83 (no change — source metadata lives in docs/source-documents/*.json)
- New relation types: none; schema semantics unchanged; 13 entity types preserved.

## 5. Tests and validation

- `python3 -m pytest -q`: 134 passed (existing suite unmodified; no new code
  behavior to test — Phase 16 changes documentation only).
- Store validation: `run_store_validation(build_graph_v39()) == []`.
- `tools/generate_math_cdg_docs.py` and `tools/generate_cdg_visualization.py`
  run cleanly; output deterministic (byte-identical on repeated runs).
- `tests/test_phase16_coverage.py`: new — verifies the three coverage matrix
  files exist, contain the required header columns, and use only the allowed
  coverage-status vocabulary (included in the 134 total above after adding;
  see regression section).

## 6. Regression checks confirmed

- Mathematics and Physics implementation records untouched (build_graph_v39
  identical to Phase 14/15 state).
- Chemistry's implementation status remains IMPLEMENTATION_PARTIAL
  (unchanged; not promoted merely because retrieval began).
- Logarithms-to-pH dependency (cl.pre56.log_ph) intact; median/dispersion
  legacy IDs intact.
- `indicates` claim remains single and PROPOSED.
- Entity types remain 13; frozen-count test passes.
- No Biology or English entities/artifacts (0 KCs each).
- Generators deterministic; round-trip serialization + export_view OK.

## 7. Chemistry status (Subject Completion Standard v1.2)

- Implementation: IMPLEMENTATION_PARTIAL (retained). Organic-reactions gap
  closed (Phase 15); buffers blocked (CI-11/CI-12); polymers/industrial
  chemistry/transition metals deferred (CI-13/CI-14/CI-15); newly mapped
  NERDC-only topics (Water CI-16, etc.) open pending owner scope decisions.
- Board verification: BOARD_UNVERIFIED (retained). NERDC curriculum content
  was checked, but JAMB/WAEC official documents were not obtained and SSS 3
  is unretrieved; per OD-04 the two dimensions stay separate and
  BOARD_UNVERIFIED is not promoted.

## 8. Remaining gaps and limitations

Implementation gaps (owner scope decisions required): CI-16…CI-23
(Water; Projectile Motion; SHM; Internet/Intranet; Sets; Logic; Mensuration;
modular arithmetic; number bases; approximation; surds; sequence & series;
bearings; proofs; construction; ogive), plus CI-12/CI-13/CI-14/CI-15
(buffers, polymers, industrial chemistry, transition metals).
Official-verification gaps: CI-24 (all three subjects — JAMB/WAEC not
obtained, NERDC SSS3 unretrieved), CI-25/CI-26 (practical details).

## 9. Recommended next step

Continue official-source verification: identify the IBASS API request
contract from the SPA bundle, retry JAMB per-subject PDFs; check
waecnigeria.org article index/publications for current WASSCE syllabus PDFs
(or submit an official request to WAEC Nigeria); attempt NERDC SSS 3 via
alternative official channels. Promote coverage rows to BOARD_VERIFIED only
on checked content. Do NOT open Biology (OD-05 hold).
