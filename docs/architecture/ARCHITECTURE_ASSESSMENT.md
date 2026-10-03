# GLM CDG v0.2 — Architecture Assessment

## Repository state

- `Minavic16/GLM-Academy-` is empty; the local clone at `/root/glm-academy` had
  no files. No existing GLM code, schemas, migrations, APIs, or visualization
  code were found anywhere on the device.
- Legacy research corpus: `glm_cdg_package.zip` (2026-09-28), JAMB Mathematics
  candidate map: ~169 nodes, ~287 edges, ~609 evidence records across
  `glm_cdg_nodes/edges/evidence` (+ sources, qc). All legacy records are
  PROPOSED. Relationship types in legacy data (`prerequisite_of`,
  `alternative_group`, `related_to`, `necessity_class`, …) do not match the v0.2
  vocabulary and will need disposition during migration.
- Unrelated local projects (nestquant, mt5 bridge, orchestrator) were reviewed
  only for conventions; none is a GLM dependency.

## Existing infrastructure

- Python 3.12 + pytest 9.1.1 available; no graph DB, vector DB, or document DB
  installed or referenced by any GLM artifact.
- No existing API, data model, or UI for the CDG.

## Conflicts with CDG v0.2 found

1. Authoritative spec `docs/architecture/GLM_CDG_v0.2_FREEZE.md` is missing
   (owner-confirmed to proceed using the Sanity Check review as the contract
   source; recorded in IMPLEMENTATION_PLAN.md §0).
2. Legacy node ids encode subject (`MATH.*`); v0.2 requires opaque ids. Migration
   contract keeps legacy ids in `legacy_ids` only.
3. Legacy `prerequisite_of` edges carry `necessity_class` and `dependency_strength`
   fields that v0.2 does not support; they will be reinterpreted, never copied
   verbatim into authoritative fields.
4. Legacy "evidence" attaches to candidate edges; v0.2 evidence attaches to
   Claims only, with Source/EvidenceItem/Activity separation.

## Storage decision

No new database introduced. The frozen model is expressible with typed Python
records + validators + JSON serialization. This preserves future optionality and
avoids creating unnecessary dependencies.

## Visualization boundary

`CDGStore.export_view()` produces a neutral projection for future rendering.
It is not a source of truth and builds no UI in this phase.
