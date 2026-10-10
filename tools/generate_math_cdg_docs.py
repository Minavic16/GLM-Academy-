#!/usr/bin/env python3
"""Deterministically generate GitHub-facing CDG documentation from the
canonical dataset. No LLM, no manual numbers."""
import collections
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from cdg.store import CDGStore
from cdg.serialization import dumps_store  # noqa: F401
from examples.physics_wave3 import build_graph_v32
from cdg.enums import EntityType, RelationshipType

OUT_CDG = os.path.join(ROOT, "docs", "MATHEMATICS_CDG.md")
OUT_COV = os.path.join(ROOT, "docs", "architecture", "MATHEMATICS_COVERAGE.md")

DOMAIN_OF = {
    "kc.algebraic_expressions": "Algebra",
    "kc.linear_equations_one_var": "Algebra",
    "kc.simultaneous_linear_equations": "Algebra",
    "kc.factorisation_quadratic_trinomial": "Algebra",
    "kc.quadratic_by_factorisation": "Algebra",
    "kc.completing_the_square": "Algebra",
    "kc.quadratic_formula": "Algebra",
    "kc.quadratic_roots": "Algebra",
    "kc.integer_arithmetic": "Number & Numeration",
    "kc.linear_inequalities_analytic": "Algebra",
    "kc.equations_in_indices": "Number & Numeration",
    "kc.change_of_subject": "Algebra",
    "kc.simultaneous_linear_quadratic": "Algebra",
    "kc.function_concept": "Functions",
    "kc.fraction_decimal_operations": "Number & Numeration",
    "kc.percentage_concept": "Number & Numeration",
    "kc.parallel_line_angles": "Geometry",
    "kc.triangle_angle_properties": "Geometry",
    "kc.gradient": "Coordinate Geometry",
    "kc.trig_ratios_acute": "Trigonometry",
    "kc.mean_ungrouped_data": "Statistics & Probability",
    "kc.differentiation_algebraic": "Calculus",
    "kc.rate_of_change": "Calculus",
    "kc.maxima_minima": "Calculus",
    "kc.integration_algebraic": "Calculus",
    "kc.theoretical_probability": "Statistics & Probability",
    "kc.sine_rule": "Trigonometry",
    "kc.cosine_rule": "Trigonometry",
    "kc.equation_of_line": "Coordinate Geometry",
    "kc.circle_angle_theorems": "Geometry",
    "kc.parallel_perpendicular_lines": "Coordinate Geometry",
    "kc.ratio_proportion_rate": "Number & Numeration",
    "kc.direct_variation": "Algebra",
    "kc.special_angle_values": "Trigonometry",
    "kc.counting_principle": "Statistics & Probability",
    "kc.distance_formula": "Coordinate Geometry",
    "kc.measurement_units_dimensions": "Physics",
    "kc.measurement_errors_precision": "Physics",
    "kc.displacement_velocity": "Physics",
    "kc.motion_equations_constant_acceleration": "Physics",
    "kc.motion_graph_interpretation": "Physics",
    "kc.newtons_laws": "Physics",
    "kc.mass_and_weight": "Physics",
    "kc.practical_measurement": "Physics",
    "kc.scalar_vector_quantities": "Physics",
    "kc.work_energy_power": "Physics",
    "kc.linear_momentum": "Physics",
    "kc.gravitation": "Physics",
    "kc.pressure_fluids": "Physics",
    "kc.heat_temperature": "Physics",
    "kc.wave_phenomena": "Physics",
    "kc.geometrical_optics": "Physics",
    "kc.electric_circuits": "Physics",
    "kc.electromagnetism": "Physics",
    "kc.atomic_nuclear_physics": "Physics",
}

BATCH_OF = {
    "kc.algebraic_expressions": "003",
    "kc.integer_arithmetic": "003",
    "kc.linear_equations_one_var": "002",
    "kc.factorisation_quadratic_trinomial": "004",
    "kc.quadratic_by_factorisation": "001",
    "kc.completing_the_square": "005",
    "kc.quadratic_formula": "005",
    "kc.quadratic_roots": "001",
    "kc.simultaneous_linear_equations": "001",
    "kc.function_concept": "006",
    "kc.linear_inequalities_analytic": "007",
    "kc.equations_in_indices": "008",
    "kc.change_of_subject": "009",
    "kc.simultaneous_linear_quadratic": "010",
    "kc.fraction_decimal_operations": "011",
    "kc.percentage_concept": "011",
    "kc.parallel_line_angles": "012",
    "kc.triangle_angle_properties": "012",
    "kc.gradient": "013",
    "kc.trig_ratios_acute": "014",
    "kc.mean_ungrouped_data": "015",
    "kc.differentiation_algebraic": "016",
    "kc.rate_of_change": "017",
    "kc.maxima_minima": "018",
    "kc.integration_algebraic": "019",
    "kc.theoretical_probability": "020",
    "kc.sine_rule": "021",
    "kc.cosine_rule": "021",
    "kc.equation_of_line": "022",
    "kc.circle_angle_theorems": "023",
    "kc.parallel_perpendicular_lines": "024",
    "kc.ratio_proportion_rate": "025",
    "kc.direct_variation": "026",
    "kc.special_angle_values": "027",
    "kc.counting_principle": "028",
    "kc.distance_formula": "029",
    "kc.measurement_units_dimensions": "030",
    "kc.displacement_velocity": "030",
    "kc.motion_equations_constant_acceleration": "030",
    "kc.motion_graph_interpretation": "030",
    "kc.newtons_laws": "030",
    "kc.mass_and_weight": "030",
    "kc.practical_measurement": "030",
    "kc.scalar_vector_quantities": "031",
    "kc.work_energy_power": "032",
    "kc.linear_momentum": "033",
    "kc.gravitation": "034",
    "kc.pressure_fluids": "035",
    "kc.heat_temperature": "036",
    "kc.wave_phenomena": "037",
    "kc.geometrical_optics": "038",
    "kc.electric_circuits": "039",
    "kc.electromagnetism": "040",
    "kc.atomic_nuclear_physics": "041",
    "kc.measurement_errors_precision": "030",
}


def status_str(e):
    return e.status.value


def main() -> None:
    s = build_graph_v32()
    kcs = sorted([e for e in s.entities.values() if e.entity_type == EntityType.KNOWLEDGE_COMPONENT], key=lambda e: e.id)
    tms = sorted([e for e in s.entities.values() if e.entity_type == EntityType.TASK_MODEL], key=lambda e: e.id)
    methods = sorted([e for e in s.entities.values() if e.entity_type == EntityType.METHOD], key=lambda e: e.id)
    items = sorted([e for e in s.entities.values() if e.entity_type == EntityType.ITEM], key=lambda e: e.id)
    miscs = sorted([e for e in s.entities.values() if e.entity_type == EntityType.MISCONCEPTION], key=lambda e: e.id)
    proposals = [c for c in s.claims.values() if c.status.value == "PROPOSED"]

    targets = collections.defaultdict(list)
    for c in s.claims.values():
        if c.predicate == RelationshipType.TARGETS:
            targets[c.subject_id].append(c.object_id)
    pre_by_obj = collections.defaultdict(list)
    for c in s.claims.values():
        if c.predicate == RelationshipType.PREREQUISITE:
            pre_by_obj[c.object_id].append(c)
    methods_by_tm = collections.defaultdict(list)
    for c in s.claims.values():
        if c.predicate == RelationshipType.HAS_METHOD:
            methods_by_tm[c.subject_id].append(c.object_id)

    view = s.export_view()
    lines = []
    lines.append("# Mathematics CDG — Human Inspection Index")
    lines.append("")
    lines.append("Generated deterministically from `examples/math_cdg_v2.json`")
    lines.append("by `tools/generate_math_cdg_docs.py`. Do not edit by hand.")
    lines.append("")
    lines.append("## Current Graph Statistics")
    lines.append("")
    lines.append(f"- Knowledge Components: {len(kcs)}")
    lines.append(f"- TaskModels: {len(tms)}")
    lines.append(f"- Methods: {len(methods)}")
    lines.append(f"- Items: {len(items)}")
    lines.append(f"- Misconceptions: {len(miscs)}")
    lines.append(f"- Claims: {len(s.claims)}")
    lines.append(f"- Evidence records: {len(s.evidence)}")
    lines.append(f"- Sources: {len(s.sources)}")
    lines.append(f"- Activities: {len(s.activities)}")
    lines.append(f"- Agents: {len(s.agents)}")
    lines.append(f"- Exported nodes: {len(view['nodes'])}")
    lines.append(f"- Exported edges: {len(view['edges'])}")
    accepted = sum(1 for c in s.claims.values() if c.status.value == 'ACCEPTED')
    lines.append(f"- Accepted Claims: {accepted}; PROPOSED Claims: {len(proposals)}")
    lines.append("")
    lines.append("## KC Index")
    lines.append("")
    lines.append("| ID | Name | Domain | Status | Owning TMs |")
    lines.append("|---|---|---|---|---|")
    for k in kcs:
        owners = sorted({tm for tm, tgts in targets.items() if k.id in tgts})
        lines.append(f"| `{k.id}` | {k.label} | {DOMAIN_OF.get(k.id, '?')} | {status_str(k)} | {', '.join(owners) if owners else '—'} |")
    lines.append("")
    lines.append("### KC Prerequisite Index")
    lines.append("")
    lines.append("| Prerequisite | → | Dependent | Purpose | Scope | Origin |")
    lines.append("|---|---|---|---|---|---|")
    for c in sorted([c for c in s.claims.values() if c.predicate == RelationshipType.PREREQUISITE], key=lambda c: c.id):
        lines.append(f"| `{c.subject_id}` | → | `{c.object_id}` | {c.purpose.value if c.purpose else '?'} | {c.scope.value if c.scope else '?'} | {c.origin.value if c.origin else '?'} |")
    lines.append("")
    lines.append("## TaskModel Index")
    lines.append("")
    for t in tms:
        lines.append(f"### `{t.id}` — {t.label}")
        lines.append("")
        tgts = targets.get(t.id, [])
        lines.append(f"- Targets: {', '.join(sorted(tgts)) if tgts else '—'}")
        ms = methods_by_tm.get(t.id, [])
        lines.append(f"- Methods: {', '.join(sorted(ms))}")
        lines.append(f"- Status: {t.status.value}")
        lines.append("")
    lines.append("## Method Index (AND within method, OR across methods)")
    lines.append("")
    for t in tms:
        ms = methods_by_tm.get(t.id, [])
        if not ms:
            continue
        lines.append(f"### `{t.id}`")
        lines.append("")
        for m in sorted(ms):
            reqs = sorted({c.object_id for c in s.claims.values()
                           if c.predicate == RelationshipType.REQUIRES and c.subject_id == m})
            lines.append(f"- **`{m}`** requires: {', '.join(reqs)}")
        lines.append("")
    lines.append("## Misconceptions")
    lines.append("")
    for m in miscs:
        lines.append(f"- `{m.id}` — {m.label} ({m.status.value})")
    lines.append("")
    lines.append("## Open Review Items")
    lines.append("")
    kc_proposed = [k for k in kcs if k.status.value == "PROPOSED"]
    lines.append(f"- PROPOSED KCs: {len(kc_proposed)}")
    for k in kc_proposed:
        lines.append(f"  - `{k.id}` — {k.label}")
    lines.append(f"- PROPOSED Claims: {len(proposals)} (misconception catalog entry, item indicator, etc.)")
    lines.append("- Owner sign-off: `indicates` domain (OWNER_SIGN_OFF_REQUIRED)")
    lines.append("- Owner input: 12 vs 13 frozen-entity count discrepancy")
    lines.append("- FREEZE document still absent")
    lines.append("")
    lines.append("## Batches")
    lines.append("")
    lines.append("See [`docs/batch_records/`](../batch_records/).")
    lines.append("")
    lines.append("| Batch | KC |")
    lines.append("|---|---|")
    for bid in sorted(set(BATCH_OF.values())):
        lines.append(f"| {bid} | {', '.join(sorted([k for k,v in BATCH_OF.items() if v==bid]))} |")
    lines.append("")

    with open(OUT_CDG, "w") as f:
        f.write("\n".join(lines))

    cov = ["# Mathematics CDG Coverage", ""]
    cov.append("Generated deterministically from the canonical dataset. Do not edit by hand.")
    cov.append("")
    cov.append("Statuses: NOT_STARTED (no representation), SOURCED (evidence located, no CDG records),")
    cov.append("IN_CONSTRUCTION (partial), REPRESENTED (modeled with reviewed evidence),")
    cov.append("REVIEW_REQUIRED (needs owner/reviewer decision), BLOCKED.")
    cov.append("")
    cov.append("| Domain | Subdomain | Status | KCs | TaskModels | Evidence | Open Issues |")
    cov.append("|---|---|---|---|---|---|---|")
    for domain in ["Mathematics", "Physics", "Algebra", "Number & Numeration", "Geometry", "Coordinate Geometry", "Trigonometry", "Calculus", "Statistics & Probability", "Functions"]:
        dkcs = [k for k in kcs if DOMAIN_OF.get(k.id) == domain]
        tm_count = len({tm for tm, tgts in targets.items() if any(k.id in tgts for k in dkcs)})
        evid = sum(1 for e in s.evidence.values() if any(
            c.id == e.claim_id and c.object_id in {k.id for k in dkcs} or c.subject_id in {k.id for k in dkcs}
            for c in s.claims.values()))
        status = "REPRESENTED" if dkcs else "NOT_STARTED"
        open_issue = "—" if dkcs else "no representation yet"
        cov.append(f"| {domain} | general | {status} | {len(dkcs)} | {tm_count} | {evid} | {open_issue} |")
    with open(OUT_COV, "w") as f:
        f.write("\n".join(cov))

    print(f"wrote {OUT_CDG} and {OUT_COV}")


if __name__ == "__main__":
    main()
