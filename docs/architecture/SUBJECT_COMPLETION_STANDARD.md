# Subject Completion Standard v1.2 (v1.0 Phase 13.5; editorial 2026-10-15; separate-status clause ratified by owner 2026-10-15)

Approval record: owner approved IN PRINCIPLE the separate-status model
(OD-01) and qualified implementation completion (OD-04), 2026-10-15.
Formal full-document ratification remains with the owner; nothing else in
v1.0/v1.1 policy changed in v1.2.

A subject is COMPLETE only when all clauses below hold. Otherwise it is
PARTIALLY_COMPLETE (gaps recorded) or BLOCKED (critical limitation).

## A. Curriculum scope
- Topic-family denominator traceable to inspected sources; JAMB, WAEC, NERDC
  assessed separately where they differ. Secondary mirrors never authoritative.
- Inclusions/exclusions documented; inaccessible documents recorded with
  attempts, never treated as verified.

## B. Knowledge representation
- Required concepts as bounded KCs; no material duplicates/omissions in scope.
- Defensible prerequisites (purpose/scope/origin); no unexplained cycles.
- Cross-subject dependencies represented where genuine.
- TMs/Methods/Items per approved scope; practicals addressed where required.

## C. Evidence and provenance
- Every ACCEPTED claim has supporting evidence for the exact assertion.
- Sources carry correct identity/authority/access status. Official alignment
  claimed only from official evidence. Unverified areas marked.

## D. Technical integrity
Store validation `[]`; references resolve; round-trip + export-view OK;
generators deterministic; regression green; subject-internal consistency.

## E. Governance
Acceptance states respected; owner-review items explicit; `indicates`
restricted; no unauthorized schema/relation changes; blockers visible.

## F. Verification status (per requirement)
IMPLEMENTED_EVIDENCED | IMPLEMENTED_PENDING_CONFIRMATION | PARTIAL |
NOT_IMPLEMENTED | BLOCKED | NOT_APPLICABLE. A subject with material
unverified board requirements is at most PARTIALLY_COMPLETE.


## G. Status dimensions (ratified OD-01/OD-04)
Two independent dimensions per subject:
- Implementation: IMPLEMENTATION_COMPLETE | IMPLEMENTATION_PARTIAL |
  IMPLEMENTATION_BLOCKED — per clauses A–E.
- Board verification: BOARD_VERIFIED | BOARD_UNVERIFIED — per clause F.
A subject without both IMPLEMENTATION_COMPLETE and BOARD_VERIFIED is never
described as "complete" in absolute terms. IMPLEMENTATION_COMPLETE never
implies JAMB/WAEC/NERDC alignment; that implication is a Clause-C violation.
Ontology: these are governance statuses recorded in closure registers and
roadmaps (no schema change; Claim.status remains claim-lifecycle only).
