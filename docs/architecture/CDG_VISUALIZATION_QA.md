# CDG Visualization QA (Phase 11)

## Output formats
- SVG (deterministic, offline-viewable)
- Standalone HTML wrapper per SVG
- Graphviz DOT companion file

## Commands
```
python3 tools/generate_cdg_visualization.py
```
Outputs to: `docs/visualizations/`:
- `mathematics_full.svg/.html/.dot` — 151 nodes, 219 edges (canonical claims with predicates)
- `mathematics_kcs.svg/.html/.dot` — TaskModel→Method→requires subgraph
- `mathematics_tm_method.svg/.html/.dot` — TaskModel/Method/KC structure only

## QA checks performed
- Determinism: generator run twice → byte-identical SVGs (`diff` empty).
- Coverage: every canonical KC/TM/Method ID appears as a node in the
  `mathematics_full` SVG; tested in `test_viz_node_edge_resolution`.
- Edge direction: every SVG edge carries the canonical claim's
  `predicate` in its title; marker-end on lines shows source→target only.
  The claim ID is embedded in the edge title for traceability.
- Method semantics: the KCs subgraph uses only `targets`, `hasMethod`,
  `requires`, `prerequisite` predicates; no flattened all-prerequisites view
  is produced anywhere.
- Subject identity: Mathematics KC nodes carry their plain IDs; subject
  grouping is visible through same column colour (no clustering applied).
- Canonical data NOT modified by the generator (read-only JSON input).
- All existing tests pass (82 at QA time).

## Known limitations
- Layout is deterministic but may overlap on very dense method-heavy
  TMs in the KCs subgraph; the full view is the densest.
- No interactive drill-down; use the `mathematics_tm_method` SVG for
  the cleaner per-TM view. Tooltip titles in the SVG carry entity id,
  type, claim id and label.
- Physics/Chemistry visualization will follow the same generator once
  their KCs enter the store; no inference will be added.

## Update (interactive layer)

The HTML artifacts are now clickable: every node rect is a `<g class="node"
onclick="cdgSelect('<id>')">` card that opens a floating card positioned just below the clicked node showing the
node's id, type, status, label, subject, legacy IDs, and every canonical
claim in which it participates (direction, predicate, other endpoint
id/type/label, prerequisite purpose/scope/origin, and any linked evidence
excerpt + legacy id + source id). Deterministic: bytes identical across
runs. Verified by `test_viz_node_edge_resolution`,
`test_viz_clickable_cards_and_details`, `test_viz_deterministic`.

## Update (floating card)

Details now render as an on-svg floating card (`#ccard`) anchored to the
clicked node (clamped to the viewport), with a close button and Escape-key
close, instead of a fixed side panel. Selected node is highlighted in red.
Deterministic and covered by `test_viz_clickable_cards_and_details`.
