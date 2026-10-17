# Phase 18 Retrieval Report — Official JAMB UTME E-Syllabus (IBASS)

Date: 2026-10-17. Status: JAMB official per-subject syllabus PDFs for
Mathematics, Physics and Chemistry RETRIEVED, TEXT-EXTRACTED and
authenticity-assessed. WAEC and NERDC SSS 3 remain unresolved (details below).

This resolves the retrieval dead end recorded in
`docs/source-documents/SRC.JAMB.IBASS.ATTEMPT.2026-10-17.json` (Phase 16:
"IBASS is a JavaScript SPA: every route returns the index.html shell").
The Phase 16 attempt guessed file paths (`/assets/uploads/*.pdf`). Phase 18
instead inspected the SPA bundle and found the syllabi as hashed static
assets of the official application.

## 1. Retrieval method

1. Fetched the IBASS SPA shell: `https://ibass.jamb.gov.ng/` (HTTP 200,
   text/html, 1257 bytes — the previously observed shell).
2. Extracted the bundle reference from the shell:
   `/static/js/main.221b9987.js` (1,065,548 bytes).
3. Searched the bundle for `static/media/*.pdf` references. The bundle
   embeds the complete E-syllabus/brochure document set as static assets:
   25 per-subject syllabus PDFs (Mathematics, Physics, Chemistry, Biology,
   Use of English, and 20 others) plus 12 programme/entry handbooks.
4. Downloaded the three in-scope PDFs (Mathematics, Physics, Chemistry) from
   `https://ibass.jamb.gov.ng/static/media/<Subject>.<hash>.pdf`.
5. Verified HTTP provenance (HTTP 200, `Content-Type: application/pdf`,
   Apache/2.4.63), recorded SHA-256, extracted full text with `pypdf`
   (already used for the Phase 16 NERDC documents).

Out-of-scope assets discovered (listed for inventory completeness only, NOT
retrieved/used): Biology and Use-of-English syllabus PDFs (subjects on hold),
plus Arabic, Agric, Art, CRS, Commerce, Computer, Economics, French,
Geography, Government, Hausa, History, Home-Economics, Igbo, Islamic,
Literature, Music, PHE, Principles-of-Accounting, Yoruba syllabi and
brochure handbooks (administration/agriculture/arts/education/engineering/
law/medical/sciences/social/NCE/ND courses).

## 2. Retrieved documents

| subject | URL (`https://ibass.jamb.gov.ng/static/media/…pdf`) | bytes | pages | SHA-256 |
|---|---|---|---|---|
| Mathematics | `Mathematics.c0621f4b8b674e75fd05.pdf` | 143,244 | 6 | `aff7a7c2cc46036902dda38db1d1567d10982de709305cfbfc90dc437329754f` |
| Physics | `Physics.16527a294cb7e7a87a35.pdf` | 300,452 | 20 | `62f5ac84592735cd5829296cb52da5bc8b582ee0f2227999cca73b58dcabfee5` |
| Chemistry | `Chemistry.9efd0b98043d56922aaa.pdf` | 226,932 | 16 | `a3c15bfee3beac0f4106a32b0091e2a2c51eaec8baa62fafa44afcad72193738` |

PDF metadata (all three): Author "Abeeb Ibrahim Adeyemi"; Creator/Producer
"Microsoft Word 2016"; creation dates 2025-07-30 (Chemistry) and 2025-07-31
(Mathematics, Physics) (+01:00).

Document structure (all three): per-subject UTME syllabus with GENERAL
OBJECTIVES, DETAILED SYLLABUS (TOPICS/CONTENTS/NOTES + OBJECTIVES columns),
and RECOMMENDED TEXTS. Mathematics declares five sections (Number and
Numeration; Algebra; Geometry/Trigonometry; Calculus; Statistics) with 23
topics. Physics has 40 numbered topics (1. Measurements and Units … 40.
Introduction to Fibre Optics and Lasers). Chemistry has 18 numbered topics
(1. Separation of Mixtures … 17. Chemistry and Industry, 18. Astronomical
Chemistry).

Source metadata records (committed):
`docs/source-documents/SRC.JAMB.UTME.MATH.2025.json`,
`SRC.JAMB.UTME.PHYS.2025.json`, `SRC.JAMB.UTME.CHEM.2025.json`.

## 3. Authenticity assessment

- Domain: `ibass.jamb.gov.ng` — the "Integrated Brochure & Syllabus System
  (IBASS)", JAMB's own e-syllabus system (linked from jamb.gov.ng).
- Delivery: hashed static assets referenced by the official application
  bundle; served with `Content-Type: application/pdf`.
- Content: internally consistent per-subject UTME syllabus documents
  (objectives → detailed topics → recommended texts; Physics pages carry
  printed brochure page numbers, e.g. "Physics 172").
- Assessment: authenticity established as official JAMB UTME syllabus
  publication. Recorded limitation: no UTME cycle/session year is printed in
  the documents; PDF metadata dates to July 2025. They are treated as the
  current official syllabus as published by JAMB on its live portal at
  retrieval time (2026-10-17); cycle-applicability remains marked UNRESOLVED
  rather than assumed.

## 4. Corroboration against the Phase 16B secondary source

The Phase 16B secondary comparison used Syllabus NG topic lists (labelled
SECONDARY). The official JAMB documents corroborate the secondary topic
lists at topic level for Mathematics (all 23 topic families present; the
secondary source was accurate on names) and extend them with detail the
secondary source omitted (e.g. sum-to-infinity of G.P.; earth-as-sphere
longitudes/latitudes; modular arithmetic in topic I.1; loci). One Phase 16B
statement is corrected: modular arithmetic IS an official JAMB requirement
(topic I.1(c)), contrary to the Phase 16B register note that "JAMB do not
show it explicitly". Official documents supersede the secondary source for
all JAMB-verification purposes; secondary matrices remain retained as audit
history (their rows stay labelled SECONDARY / BOARD_UNVERIFIED).

## 5. What this does and does not change

- Does: establish checked official JAMB content for Mathematics, Physics and
  Chemistry; enable the three official coverage matrices
  (`JAMB_*_OFFICIAL_COVERAGE.md`); allow the official-confirmation updates in
  the gap register; close the JAMB half of CI-24 for these three subjects.
- Does not: promote any subject to BOARD_VERIFIED. WAEC official WASSCE
  syllabus documents remain unretrieved, and NERDC SSS 3 remains
  unavailable; subject-level board verification stays BOARD_UNVERIFIED.
- Does not: change the canonical store (no entities/claims/edges), physics or
  chemistry implementation statuses, or any prior phase's historical record.

## 6. Repeated attempts (2026-10-17, Phase 18) — still unresolved

WAEC (official syllabus documents):
- `waecnigeria.org` root link inventory: no public syllabus downloads;
  `waecinternational.org/cass/Downloads` offers only the WAEC CASS desktop
  application installers (42.4 MB and 57.9 MB Windows binaries, not
  documents); `waec.edustat.ng` did not respond; `waeconline.org.ng`
  e-learning remains past-questions material (Phase 16 finding).
- Result: official WASSCE syllabus document still NOT obtained.

NERDC SSS 3:
- `lmis.nerdcportals.com.ng/sss_3/…` → HTTP 404; the LMIS portal is a
  login-gated LMS (login/forgot-password entry points only).
- `nerdc.org.ng` (root, /curriculum, /ecurriculum) → HTTP 500.
- Result: SSS 3 document still NOT obtained.

## 7. Local working copies (not committed)

`/tmp/phase18/ibass/jamb_{mathematics,physics,chemistry}.pdf` and the
extracted `.txt` files. Copyrighted board material is not committed; only
hashes, metadata and locators are recorded, matching the Phase 16 NERDC
practice.
