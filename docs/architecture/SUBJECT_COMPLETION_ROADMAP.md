# Subject Completion Roadmap (Phase 13.8, ratified policy OD-01/OD-04)

Status model (ratified): each subject carries
`IMPLEMENTATION_COMPLETE | IMPLEMENTATION_PARTIAL | IMPLEMENTATION_BLOCKED`
× `BOARD_VERIFIED | BOARD_UNVERIFIED`. "COMPLETE" without a board dimension
is meaningless; IMPLEMENTATION_COMPLETE never implies official alignment.

Verified counts (canonical store, 2026-10-15):
Mathematics 39 KCs / Physics 19 KCs / Chemistry 12 KCs; 70 KCs total;
subject map generated separately per batch.

---

## Mathematics — IMPLEMENTATION_COMPLETE / BOARD_UNVERIFIED

Implementation closure: median (b057), dispersion (b058), logarithms (b055)
all accepted with legacy ids preserved (MATH.STAT.MEDIAN,
RANGE/MEAN_DEVIATION/VARIANCE/STANDARD_DEVIATION, LOGARITHM*); log→pH
edge intact; quartiles/IQR documented PARTIAL (row 4 of PHASE136 matrix).

Remaining tasks:
1. M-1 (evidence): board verification plan (see §Verification Plan).
2. M-2 (optional, owner-scope): median-mode/mean-grouped extension if owner
   extends declared scope; otherwise OUT_OF_SCOPE documented.
3. M-3: none for declared-scope implementation.

Closure criterion: BOARD_VERIFIED requires retrieved+content-checked JAMB
WAEC NERDC topic lists mapped to KC rows (M-1). Next recommended task: M-1.

## Physics — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED

Counts verified: 19 KCs / ~xx TMs / ~xx Methods (see generated index).
Recorded partial/deferred (confirmed against current records):
- Fibre optics, LASER, electronics — NOT_IMPLEMENTED (SHOULD-deferral).
- Friction/machines, EM spectrum depth, energy-society — PARTIAL via parent
  KCs (work/energy, waves) — accepted partial rows.
- Practicals — PARTIAL (TM exists; WAEC practical detail unverified).

Closure criterion: owner-scope decision for the SHOULD rows (implement or
document as OUT_OF_SCOPE), then implement chosen rows with evidence + review,
then board verification. Next recommended task: Physics SHOULD-row triage
batch (fibre/LASER/electronics), pending owner scope confirmation.

## Chemistry — IMPLEMENTATION_PARTIAL / BOARD_UNVERIFIED

Counts verified: 12 KCs; pH dependency (kc.logarithms→kc.ph_scale,
cl.pre56.log_ph) intact.
Recorded partial/deferred (confirmed):
- Organic: naming/classification only — reactions NOT_IMPLEMENTED.
- Practical: PARTIAL (WAEC detail unverified).
- Unimplemented families: buffers proper, polymers, industrial chemistry,
  transition metals.

Closure criterion: owner-scope decision for deferred families, then
implementation with evidence + review, then board verification.
Next recommended task: Chemistry organic-reactions batch (per ECUES style:
alkene/alkane reaction families), pending owner scope confirmation.

## Cross-subject invariants (must remain intact; regression-guarded)
- 28 Math→Physics edges + Science/Math edges incl. log→pH.
- No duplicated cross-subject KCs; DERIVED-origin rule for method/tm scopes.
- Misconception/`indicates` pair PROPOSED unchanged.

## Verification plan (targeted, not repeated scraping)
Required official documents: JAMB UTME syllabus PDFs (Math/Physics/Chemistry),
WAEC WASSCE syllabus + practical requirements, NERDC SSS scheme.
Evidence sufficient: document located on official domain, title/subject
verified, relevant sections extracted, mapping rows added to each
`*_COVERAGE_MATRIX.md` with SOURCE_DERIVED rows promoted to BOARD_VERIFIED.
Latest attempts 2026-10-14: IBASS 200 (SPA, hashed assets — no per-subject
PDF URL), WAEC 200 (no syllabus links in landing HTML), NERDC unreachable.
