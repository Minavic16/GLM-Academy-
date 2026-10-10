# Physics Source Research (Phase 12)

Date: 2026-10-08. Researcher: agent pipeline + human review gate.
Canonical slice: measurement / kinematics / Newton's laws only.

## Retrieval attempts (FACT)

| # | Target | Method | Result |
|---|---|---|---|
| 1 | JAMB IBASS e-syllabus portal (`https://ibass.jamb.gov.ng/e-syllabus`) | `curl` fetch + JS bundle inspection (`main.221b9987.js`, 336 KB) | VERIFIED reachable. Portal is a JS SPA; syllabus payloads load client-side. Per-subject PDF URLs are hashed asset paths, not indexed in the bundle. **Per-topic Physics PDF not retrieved.** Registered as `SRC.JAMB.IBASS.PHYSICS` (metadata only). |
| 2 | WAEC official portal (`https://www.waec.ng`, HTTP 200) | `curl` fetch + syllabus-link grep | VERIFIED reachable. Syllabus PDF pages not retrieved in this run. Registered as `SRC.WAEC.PHYSICS` (metadata only). |
| 3 | NERDC curriculum portal (`nerdc.gov.ng`, `nerdc.org.ng` e-Curriculum) | Public landing pages inspected in prior phase | VERIFIED reachable. Full SSS Physics documents behind eID portal. Registered as `SRC.NERDC.SS.PHYSICS` (metadata only). |
| 4 | OpenStax University Physics Vol. 1 §1.2 Units and Standards | `curl`, HTTP 200, content grep | VERIFIED + DOCUMENT_INSPECTED. Base SI units confirmed. → `SRC.OSX.UP1.1.2`. |
| 5 | OpenStax UP1 §3.4 Motion with Constant Acceleration | `curl`, HTTP 200 | VERIFIED + DOCUMENT_INSPECTED. "Equations of motion are to be used to solve for unknowns." → `SRC.OSX.UP1.3.4`. |
| 6 | OpenStax UP1 §4.2 Acceleration Vector | `curl`, HTTP 200 | VERIFIED + DOCUMENT_INSPECTED. → `SRC.OSX.UP1.4.2`. |
| 7 | OpenStax UP1 §5.2 Newton's First Law | `curl`, HTTP 200, title grepped | VERIFIED + DOCUMENT_INSPECTED. → `SRC.OSX.UP1.5.2`. |
| 8 | OpenStax UP1 §5.4 Mass and Weight | `curl`, HTTP 200 | VERIFIED + DOCUMENT_INSPECTED. → `SRC.OSX.UP1.5.4`. |

## Classification of slice content

- VERIFIED: the five OpenStax pages above (retrieved, HTTP 200, quoted or closely paraphrased in evidence excerpts).
- SOURCE-DERIVED: KC definitions for measurement units, motion equations, motion-graph interpretation, Newton's laws, mass/weight — each grounded in the corresponding OpenStax section.
- RESEARCH SYNTHESIS: KC/TM/Method decomposition (e.g., splitting motion-equation solving from graph interpretation; two Methods per TM) and the four Mathematics→Physics DERIVED prerequisites. Accepted only after human review activity `act.physics.review`.
- PROPOSED: `kc.measurement_errors_precision`, `kc.practical_measurement` (no syllabus-backed TM yet); misconception/`indicates` items untouched.
- UNVERIFIED: per-topic JAMB/WAEC/NERDC Physics requirements at KC granularity — official PDFs still pending.
- OWNER_REVIEW_REQUIRED: confirmation that the chosen slice topics match the official board topic lists once PDFs are retrieved; `indicates` sign-off; freeze-doc reconciliation if it appears.

## Source conflicts

None observed at slice scope: OpenStax content (SI units, constant-acceleration equations, Newton's laws) is board-agnostic foundation material. WAEC-vs-JAMB practical emphasis differs (WAEC assesses practicals, JAMB does not) — preserved in `PHYSICS_SCOPE.md`; the slice's practical KC stays PROPOSED for exactly this reason.

## What is still needed

Official per-topic Physics PDFs (JAMB IBASS resolved asset URL, WAEC syllabus PDF, NERDC SSS Physics) for board-level confirmation of the slice and for scoping Phase 13+.
