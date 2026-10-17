# Phase 16 Retrieval and Authenticity Report

Date: 2026-10-17. Standard: Phase 16 retrieval & provenance rules (SUBJECT_COMPLETION_STANDARD.md clauses A, C; OD-01/OD-04 separation of dimensions).

## 1. Documents retrieved and content-checked (official, primary)

All five NERDC documents are "NEW REVISED SENIOR SECONDARY SCHOOL CURRICULUM"
(Federal Ministry of Education / NERDC, © October 2025), served as
application/pdf from the NERDC LMIS viewer portal
(lmis.nerdcportals.com.ng) and text-extracted successfully.

| ID | Document | Subject | Pages | SHA-256 | Retrieval | Extracted | Authentic |
|---|---|---|---|---|---|---|---|
| SRC.NERDC.SSEC.MATH.SS1 | Mathematics SSS 1 | Mathematics | 24 | a2f618…11c | yes | yes | yes |
| SRC.NERDC.SSEC.MATH.SS2 | Mathematics SSS 2 | Mathematics | 33 | f79d3f…f1cd | yes | yes | yes |
| SRC.NERDC.SSEC.CHEM.SS1 | Chemistry SSS 1 | Chemistry | 31 | e0f9b0…26c | yes | yes | yes |
| SRC.NERDC.SSEC.CHEM.SS2 | Chemistry SSS 2 | Chemistry | 45 | 5e1473…efd | yes | yes | yes |
| SRC.NERDC.SSEC.PHY.SS1 | Physics SSS 1 | Physics | 63 | fc0648…5ee | yes | yes | yes |
| SRC.NERDC.SSEC.PHY.SS2 | Physics SSS 2 | Physics | 62 | 88dd5d…236 | yes | yes | yes |

Corroborating record: SRC.FEDMOE.CURRICULUM.OFFERINGS.2025
("Basic and Senior Secondary Education Curriculum Offerings", NERDC/Federal
Ministry of Education, PDF metadata 2025-09-08) confirms Chemistry, Physics
and General Mathematics sit in the senior-secondary Science/Core fields.

Per-document metadata (URL, date, hash, limitations) is stored in
docs/source-documents/*.json. Copyrighted PDF bytes are NOT committed to the
repository (no repository policy permitting it); metadata, hashes and
permitted extracted topic evidence are retained instead.

## 2. Documents attempted but NOT obtained (verification unresolved)

| ID | Document | Attempted URL | Result |
|---|---|---|---|
| SRC.JAMB.IBASS.ATTEMPT.2026-10-17 | IBASS e-syllabus + per-subject PDFs | https://ibass.jamb.gov.ng/e-syllabus ; /assets/uploads/{Mathematics,Physics,Chemistry}.pdf | IBASS is a JavaScript SPA: every route returns the index.html shell (HTTP 200, text/html, 1257 bytes), not PDF bytes. The discovered API (ibass-api.jamb.gov.ng/api) returns {"error":true,...} on GET for /api/e-syllabus, /api/brochure-courses, /api/materials with no identifiable request contract. No per-subject syllabus PDF bytes obtained. |
| SRC.WAEC.ATTEMPT.2026-10-17 | WASSCE syllabuses | https://www.waecnigeria.org/ ; .../article/wassce-syllabuses-2017-2019 ; waeconline.org.ng e-learning subject pages | waecnigeria.org reachable, but the 2017–2019 article page has no downloadable syllabus PDFs for Mathematics/Physics/Chemistry; the archive must not be assumed current. waeconline e-learning pages contain past WASSCE questions only (zero "syllabus" mentions, no syllabus PDF links). No current-cycle WAEC document obtained. |
| SRC.NERDC.PORTAL.ATTEMPT.2026-10-17 | NERDC eCurriculum portal; SSS 3 portals | nerdc.org.ng/eCurriculum ; lmis.nerdcportals.com.ng/sss_3 | eCurriculum portal: HTTP 500. SSS 3 portals (sss_3, s3_core, s3_science): HTTP 404 — SSS 3 curriculum documents not retrievable. SSS 1 and SSS 2 viewers retrieved successfully (see section 1). |

## 3. Authenticity and applicability notes

- A URL returning HTTP 200 was NOT treated as proof of document retrieval:
  IBASS /assets/uploads/*.pdf return 200 with the SPA shell.
- NERDC documents carry document-footers "NEW REVISED SENIOR SECONDARY
  SCHOOL CURRICULUM … © October 2025" and Federal Ministry of Education
  branding; authenticity established via the official nerdc.gov.ng domain
  linkage (content_manager/new_senior_curriculum_home.html → LMIS viewers).
- Applicable cycle established as "2025 revised senior-secondary
  curriculum" from the documents themselves; formal UTME/WASSCE adoption
  endorsement by JAMB/WAEC not established (those bodies' documents were not
  obtained).
- SSS 3 is out of reach via the portal; coverage comparison below is based
  on SSS 1 and SSS 2 only.

## 4. Next retrieval actions

1. Identify the IBASS API request contract (inspect the SPA bundle's axios
   calls) or contact JAMB for official Mathematics/Physics/Chemistry UTME
   syllabus PDFs.
2. Check waecnigeria.org article index / publications page and linked
   attachments for current WASSCE syllabus PDFs; failing that, address an
   official request to WAEC Nigeria.
3. Attempt NERDC SSS 3 via alternative official channels once SSS 1–2
   mapping is complete.
4. Only after documents are obtained and content-checked may any subject be
   considered for BOARD_VERIFIED; all three subjects remain
   BOARD_UNVERIFIED at the end of this phase.
