#!/usr/bin/env python3
"""Generate deterministic, standalone visualizations of the canonical CDG.

Inputs: examples/math_cdg_v2.json (canonical data) — no CDG mutation.
Outputs: docs/visualizations/*.svg, *.html, *.dot
"""
import collections
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANON = os.path.join(ROOT, "examples", "math_cdg_v2.json")
OUT = os.path.join(ROOT, "docs", "visualizations")

TYPE_COLORS = {
    "Subject": "#8e44ad",
    "CurriculumFramework": "#2980b9",
    "CurriculumItem": "#3498db",
    "KnowledgeComponent": "#27ae60",
    "TaskModel": "#e67e22",
    "Method": "#f1c40f",
    "Item": "#16a085",
    "Misconception": "#c0392b",
    "Claim": "#7f8c8d",
    "EvidenceItem": "#bdc3c7",
    "Source": "#95a5a6",
    "Agent": "#2c3e50",
    "Activity": "#34495e",
}


def _nodes_index(d):
    return {e["id"]: e for e in d["entities"]}


def _edge_index(d):
    out = []
    for c in d["claims"]:
        if c["predicate"] is None:
            continue
        out.append((c["id"], c["subject_id"], c["object_id"], c["predicate"]))
    return out


def _layout(node_ids):
    """Deterministic column-by-entity-type layout."""
    by_type = collections.defaultdict(list)
    nidx_lookup = {}
    for e in NODES.values():
        pass
    for nid in node_ids:
        t = NODES[nid]["entity_type"]
        by_type[t].append(nid)
    pos = {}
    col = 0
    for t in sorted(by_type):
        for i, nid in enumerate(sorted(by_type[t])):
            pos[nid] = (col * 260 + 130, i * 56 + 60)
        col += 1
    return pos, max((y for _, y in pos.values()), default=60) + 60, col * 260 + 40


NODES = {}


def _svg(title, node_ids, edges):
    pos, height, width = _layout(node_ids)
    height = max(height, 200)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'style="background:#ffffff;font-family:monospace">',
             f'<text x="20" y="30" font-size="18" font-weight="bold">{title}</text>',
             '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="8" refY="3" orient="auto">'
             '<path d="M0,0 L0,6 L9,3 z" fill="#888"/></marker></defs>']
    for cid, src, dst, pred in edges:
        if src not in pos or dst not in pos:
            continue
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#bbb" '
                     f'stroke-width="1" marker-end="url(#arrow)"><title>{pred} ({cid})</title></line>')
    for nid in sorted(node_ids):
        x, y = pos[nid]
        e = NODES[nid]
        fill = TYPE_COLORS.get(e["entity_type"], "#eee")
        parts.append(f'<g><rect x="{x-118}" y="{y-18}" width="236" height="36" rx="6" '
                     f'fill="{fill}" stroke="#333"/>'
                     f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="11" fill="white">'
                     f'{nid}</text><title>{e["entity_type"]} | {e["label"]}</title></g>')
    parts.append('</svg>')
    return ''.join(parts)


def _html(title, svg_text):
    return ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>' + title +
            '</title></head><body><h1>' + title + '</h1>' + svg_text + '</body></html>')


def _dot(title, node_ids, edges):
    lines = ['digraph g {', f'label="{title}";', 'node [shape=box,style=filled,fontname="monospace"];']
    for nid in sorted(node_ids):
        e = NODES[nid]
        lines.append(f'"{nid}" [fillcolor="{TYPE_COLORS.get(e["entity_type"], "#eee")}",label="{nid}"];')
    for cid, src, dst, pred in edges:
        if src in node_ids and dst in node_ids:
            lines.append(f'"{src}" -> "{dst}" [label="{pred}"];')
    lines.append('}')
    return '\n'.join(lines)


def _write(stem, svg_text, dot_text):
    with open(os.path.join(OUT, stem + '.svg'), 'w') as f:
        f.write(svg_text)
    with open(os.path.join(OUT, stem + '.html'), 'w') as f:
        f.write(_html(stem, svg_text))
    with open(os.path.join(OUT, stem + '.dot'), 'w') as f:
        f.write(dot_text)


def main():
    global NODES
    with open(CANON) as f:
        d = json.load(f)
    NODES = _nodes_index(d)
    edges = _edge_index(d)
    all_ids = list(NODES.keys())
    _write('mathematics_full', _svg('GLM CDG — Mathematics (full)', all_ids, edges),
           _dot('Mathematics', all_ids, edges))

    kc_ids = [e['id'] for e in d['entities'] if e['entity_type'] in
              ('KnowledgeComponent', 'TaskModel', 'Method')]
    preds = {'prerequisite', 'targets', 'hasMethod', 'requires'}
    sub_edges = [e for e in edges if e[2] and e[3] in preds]
    _write('mathematics_kcs', _svg('Mathematics — KCs / TMs / Methods', kc_ids, sub_edges),
           _dot('Mathematics KCs', kc_ids, sub_edges))

    from collections import defaultdict
    tms_to_m = collections.defaultdict(list)
    for c in d['claims']:
        if c['predicate'] == 'hasMethod':
            tms_to_m[c['subject_id']].append(c['object_id'])
    m_to_kc = collections.defaultdict(list)
    for c in d['claims']:
        if c['predicate'] == 'requires':
            m_to_kc[c['subject_id']].append(c['object_id'])
    tm_ids = [e['id'] for e in d['entities'] if e['entity_type'] == 'TaskModel']
    tm_edges = [e for e in edges if e[3] in ('hasMethod', 'targets', 'requires')]
    _write('mathematics_tm_method', _svg('Mathematics — TaskModel/Method', 
            tm_ids + [m for ms in tms_to_m.values() for m in ms] +
            [k for ms in m_to_kc.values() for k in ms], tm_edges),
           _dot('Mathematics TM/Method', tm_ids + [m for ms in tms_to_m.values() for m in ms] +
            [k for ms in m_to_kc.values() for k in ms], tm_edges))

    print('visualizations written to', OUT)


if __name__ == '__main__':
    main()
