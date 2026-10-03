# GLM Academy CDG v0.2 — Architecture Bootstrap

This repository establishes the machine-readable architecture and implementation
contracts for the GLM Academy Curriculum Dependency Graph (CDG) v0.2.

It does **not** contain any generated curriculum data. The legacy JAMB Mathematics
research corpus is a separate, read-only input and is not authoritative v0.2 data.

## Layout

- `cdg/` — the typed domain contract package
  - `entities.py` — Subject, CurriculumFramework, CurriculumItem, KnowledgeComponent,
    TaskModel, Method, Item, Misconception (+ a `GraphNode` projection used only by
    storage/visualization plumbing)
  - `relationships.py` — frozen relation vocabulary with explicit domain/range,
    required qualifiers, self-loop and navigation-only rules
  - `claims.py` — every domain relationship is reified as exactly one `Claim`
  - `prerequisites` attributes on claims — `purpose` (EXECUTE/UNDERSTAND),
    `scope` (ALL_RELEVANT_METHODS/SPECIFIC_METHOD/SPECIFIC_TASK_MODEL), `origin`
    (ASSERTED/DERIVED)
  - `methods.py` — TaskModel AND(within Method)/OR(across Methods) evaluation rule
    plus ALL-scope EXECUTE prerequisite derivation
  - `evidence.py`, `provenance.py`, `status.py`, `migration.py`
  - `store.py` — in-memory typed store, diagnostic boundary, visualization projection
  - `validation.py` — machine-testable invariant validators
  - `serialization.py` — JSON round-trip (storage-neutral)
- `tests/` — contract tests (pytest)
- `docs/architecture/` — implementation plan, assessment, and developer documentation

## Quick start

```bash
python3 -m pytest -q
```

See `docs/architecture/CDG_CONTRACT_DOCUMENTATION.md` for how to create entities,
relationships, TaskModel/Method structures, prerequisites, evidence, status
transitions, and how legacy records will migrate.

## Human inspection (GitHub layer)

- `docs/MATHEMATICS_CDG.md` — human-readable CDG index (KC/TM/Method indexes,
  graph statistics, open review items)
- `docs/architecture/MATHEMATICS_COVERAGE.md` — coverage ledger by domain
- `docs/batch_records/` — per-batch construction records
- `examples/math_cdg_v2.json` — canonical serialized CDG data
- Regenerate with: `python3 tools/generate_math_cdg_docs.py`
