# Cross-Subject Gap Register (Phase 16)

Register of gaps that span subjects or that require cross-subject
coordination. Maintained alongside docs/architecture/CLOSURE_REGISTERS.md
(CI-01…CI-10). Statuses: Open | Blocked | Deferred | Closed.

| ID | Subject(s) | Gap | Class | Status | Evidence / basis | Proposed resolution | Next action |
|---|---|---|---|---|---|---|---|
| CI-11 | Mathematics → Chemistry | Chemistry buffers proper require pH calculations (pH = −log[H⁺]); the logarithms KC lives in Mathematics. Creating the prerequisite edge would modify Mathematics-side records. | IMPLEMENTATION_GAP (cross-subject dependency) | Blocked (Phase 15 scope constraint) | NERDC Chem SSS1 p.15 / SSS2 (acids, bases and salts); CDG kc.ph_scale exists; cl.pre56.log_ph scoped to tm.ph_problems only | Owner-authorized, scoped change: add Mathematics→Chemistry prerequisite edge(s) for a new buffer TaskModel under tm.ph_problems or a new TM; do not alter existing Mathematics KC/claim records | Owner decision on scoped Mathematics extension; then implement buffer KCs in Chemistry |
| CI-12 | Chemistry | Buffers proper not implemented | IMPLEMENTATION_GAP | Open | CI-09; NERDC topic lists SSS1/SSS2 do not list "buffer" explicitly; SSS3 unreachable | Implement buffers only after CI-11 unblocked | Re-evaluate after CI-11 and after SSS3 retrieval |
| CI-13 | Chemistry | Polymers | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC SSS1/SSS2 topic lists contain no polymers topic | Owner decision to reopen | Revisit with owner authorization |
| CI-14 | Chemistry | Industrial chemistry | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC lists "Chemical industry" (SSS1 p.2, NOT_COVERED) and "Chemistry and industry" (SSS2 p.30 career day) | Owner decision | Revisit with owner authorization |
| CI-15 | Chemistry | Transition metals / electrolytic cells detail | IMPLEMENTATION_GAP | Deferred (owner-documented) | NERDC SSS1/SSS2 topic lists contain no transition-metals topic; electrolysis covered (COVERED via kc.redox_electrochemistry) | Owner decision | Revisit with owner authorization |
| CI-16 | Chemistry | Water | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Chem SSS1 p.17 and SSS2 p.10 (Water, NOT_COVERED) | Owner decision: add water KC or out of scope | Record in Chemistry coverage matrix; owner decision |
| CI-17 | Physics | Projectile Motion | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Phy SSS2 p.7 (NOT_COVERED); Mathematics quadratic dependencies exist | Implement projectile KC using existing Math→Physics edges | Owner decision: scope extension within Physics declared scope |
| CI-18 | Physics | Simple Harmonic Motion | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Phy SSS2 p.8 (NOT_COVERED) | Owner decision | Revisit |
| CI-19 | Physics | Introduction to Internet and Intranet | IMPLEMENTATION_GAP | Open / likely NOT_APPLICABLE to core physics | NERDC Phy SSS2 p.46 (NOT_COVERED) | Owner decision; likely outside CDG physics scope | Record as out-of-scope unless owner extends |
| CI-20 | Mathematics | Sets | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Math SSS1 p.7 / SSS2 p.9 (NOT_COVERED) | Owner decision | Revisit |
| CI-21 | Mathematics | Logic | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Math SSS1 p.8 / SSS2 p.9 (NOT_COVERED) | Owner decision | Revisit |
| CI-22 | Mathematics | Mensuration | IMPLEMENTATION_GAP (newly mapped vs NERDC) | Open | NERDC Math SSS1 p.11 (NOT_COVERED) | Owner decision | Revisit |
| CI-23 | Mathematics | Modular arithmetic / number bases / approximation / surds / sequence & series / bearings / proofs / construction / ogive | IMPLEMENTATION_GAP (partially documented deferrals) | Open / Deferred | NERDC Math SSS1/SSS2 topic lists (NOT_COVERED rows) | Owner decision per row | Update Mathematics roadmap; existing deferrals (ogive) stand |
| CI-24 | All subjects | Official-board verification (JAMB/WAEC/NERDC alignment) | OFFICIAL_VERIFICATION_GAP | Open | CI-05; JAMB official UTME E-syllabus obtained + content-checked for Math/Phys/Chem (Phase 18, IBASS static assets — PHASE18_RETRIEVAL_REPORT.md); WAEC documents still not obtained (CASS installers only); NERDC SSS1/SSS2 content-checked but SSS3 unretrieved | Continue retrieval: WAEC official WASSCE syllabus; NERDC SSS3; promote rows to BOARD_VERIFIED only on checked content (JAMB-side rows now checked — see JAMB_*_OFFICIAL_COVERAGE.md); do not claim BOARD_VERIFIED (WAEC outstanding) | M-1 official-source verification plan |
| CI-25 | Chemistry | Practical chemistry — WAEC practical detail | OFFICIAL_VERIFICATION_GAP | Open | CI-05; kc.practical_chemistry implementation adequate (titration, qualitative tests) but WAEC detail unverified | Obtain WAEC practical syllabus; map to practical KC methods/items | Same as CI-24 |
| CI-26 | Physics | Practical physics — WAEC practical detail | OFFICIAL_VERIFICATION_GAP | Open | Phase 14 roadmap R16; kc.practical_measurement implementation adequate | Same as CI-24 | Same as CI-24 |

## Notes

- Newly mapped gaps (CI-16…CI-23) come from the Phase 16 NERDC
  content check against the canonical CDG. They do NOT change any
  subject's implementation status: Mathematics and Physics remain
  IMPLEMENTATION_COMPLETE within the declared OpenStax-based scope
  (ratified OD-04 qualified completion); Chemistry remains
  IMPLEMENTATION_PARTIAL. Any scope extension to cover CI-16…CI-23
  requires an explicit owner decision and validated graph changes.
- CI-11 is cross-subject: it touches Mathematics records; per Phase 15/16
  restrictions, no Mathematics records are altered here. The edge, if
  authorized, must follow the normal prerequisite contract
  (purpose/scope/origin qualifiers; human review; evidence).
- No Biology or English artifacts are referenced anywhere in this
  register (OD-05: Biology on hold).
