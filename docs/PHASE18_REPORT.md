# Phase 18 Report — Official JAMB UTME E-Syllabus Retrieved and Content-Checked

Date: 2026-10-17. Scope: documentation/verification only (no canonical-store
changes, no new phases of implementation).

## 1. Result in one line

The official JAMB UTME syllabus documents for **Mathematics, Physics and
Chemistry** were retrieved from JAMB's own Integrated Brochure & Syllabus
System (IBASS) after the Phase 16 dead end was solved by inspecting the SPA
bundle; all three were content-checked and three official coverage matrices
were produced. WAEC official documents and NERDC SSS 3 remain unretrieved.

## 2. What changed

New documents:
- `docs/architecture/PHASE18_RETRIEVAL_REPORT.md` — retrieval method,
  provenance, hashes, authenticity assessment and remaining blockers.
- `docs/architecture/JAMB_MATHEMATICS_OFFICIAL_COVERAGE.md` (23 topic rows),
  `JAMB_PHYSICS_OFFICIAL_COVERAGE.md` (40 topic rows),
  `JAMB_CHEMISTRY_OFFICIAL_COVERAGE.md` (18 topic rows) — official JAMB
  content checked directly against the CDG; completely separate from the
  Phase 16B secondary matrices, which are retained unchanged as history.
- `docs/source-documents/SRC.JAMB.UTME.{MATH,PHYS,CHEM}.2025.json` — source
  records with SHA-256, sizes, page counts, HTTP provenance, PDF metadata and
  the cycle-year limitation.

Updated documents:
- `CLOSURE_REGISTERS.md` — CI-24 updated (JAMB obtained for the three
  subjects; WAEC + NERDC SSS 3 outstanding) and a Phase 18 entry appended.
- `CROSS_SUBJECT_GAP_REGISTER.md` — CI-24 updated.
- `DEDUPLICATED_IMPLEMENTATION_GAP_REGISTER.md` — Phase 18 section added;
  two Phase 16B statements corrected (below); three new gap rows added
  (P-18, P-19, C-15); depth exposures listed.
- `SUBJECT_COMPLETION_ROADMAP.md` — Phase 18 recorded for Mathematics,
  Physics and Chemistry; next-phase list updated.
- `CONSOLIDATED_NERDC_JAMB_WAEC_COMPARISON.md` — Phase 18 supersession note.
- `tests/test_phase18_jamb_official.py` — 9 regression tests (structure,
  vocabulary, no-promotion guards, store invariance).

## 3. Corrections to the Phase 16B record (evidence-based)

1. **Modular arithmetic (M-03)**: Phase 16B stated that JAMB does not show it
   explicitly. The official JAMB Mathematics syllabus topic I.1(c) DOES
   include modular arithmetic. Row corrected; requirement officially
   confirmed.
2. **Buffers (C-12)**: Phase 16B stated no topic list shows "buffer"
   explicitly. Official JAMB Chemistry topic 8 (Acids, Bases and Salts)
   explicitly lists "Buffer solution" (p.6). Requirement officially
   confirmed; the CI-11/CI-12 block itself is unchanged.
3. Physics locator corrections: P-14 viscosity/Stokes is officially topic 6
   (not topic 7); P-16 energy-society is officially topic 7 (not topic 6b).

## 4. Newly exposed requirements (not previously registered)

- **P-18** Vapours & humidity (official Physics topic 17).
- **P-19** Light energy: sources, propagation, shadows/eclipse, pinhole
  (official Physics topic 23).
- **C-15** Astronomical Chemistry (official Chemistry topic 18 — a topic
  absent from the Phase 16B secondary lists).
- Depth exposures recorded in the official matrices (not yet rowed): physics
  pressure instruments, upthrust/Archimedes, physics-side gas laws, kinetic
  theory of matter, wave equation, sound echoes/harmonics, prism refraction,
  optical instruments, dispersion/colours, magnetic fields, motor/force on
  conductors, gas discharge; mathematics Venn/cardinality, factor/remainder
  theorems, graphical/quadratic inequalities, AP/GP sums and sum to infinity,
  earth-as-sphere, bearings/graphs/triangle area, limits, area under curve,
  grouped dispersion; chemistry proportion laws, quantum-number detail,
  entropy/ΔG. All await owner scoping.

## 5. What did NOT change

- No canonical store change: 365 entities / 583 claims / 288 evidence /
  85 sources / 192 activities; KC counts Math 44 / Physics 25 / Chemistry 21
  / Biology 0 / English 0; `run_store_validation(build_graph_v40()) == []`.
- No subject promoted to **BOARD_VERIFIED** (WAEC official documents and
  NERDC SSS 3 outstanding; CI-24 stays Open). WAEC-facing rows in the
  secondary matrices remain SECONDARY.
- Matrices & determinants: the JAMB requirement is now officially confirmed,
  but the CDG implementation's evidence basis remains secondary (Syllabus
  NG) — disclosed, no implementation change, no evidence overwritten.
- Physics/Chemistry implementation statuses unchanged
  (IMPLEMENTATION_COMPLETE / IMPLEMENTATION_PARTIAL as before).
- Deferrals unchanged (Chemistry polymers / industrial chemistry / transition
  metals; Mathematics ogive; Biology hold).
- No Biology or English artifacts; 13 entity types; one `indicates` claim
  remains PROPOSED.

## 6. Verification

- `python3 -m pytest -q` → **170 passed** (161 previous + 9 Phase 18).
- `run_store_validation(build_graph_v40()) == []`.
- `python3 tools/generate_math_cdg_docs.py` and
  `python3 tools/generate_cdg_visualization.py` → byte-identical rewrites
  (no generated drift; no store change).

## 7. Remaining blockers and next moves

1. **WAEC official WASSCE syllabus documents** — still unretrieved
   (2017–2019 archive is a stub; downloads are CASS installers; e-learning is
   past questions). Needed before any BOARD_VERIFIED claim and before M-17,
   M-18, C-13/C-14 receive official status.
2. **NERDC SSS 3** — LMIS portal login-gated; nerdc.org.ng returns HTTP 500.
3. Owner decisions on the register: M-03/M-04/M-05/M-09/M-10/M-11/M-12/
   M-13/M-14/M-15/M-16/M-19 and depth exposures; P-01…P-19; C-01…C-15;
   the buffers unblock decision (CI-11/CI-12, now an officially confirmed
   requirement).
4. Then, and only then, Biology pending explicit owner authorization.
