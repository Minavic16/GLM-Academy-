#!/usr/bin/env python3
"""Generate deterministic visualizations of the canonical CDG.

Three artifacts per view:
  - <view>.svg  (static vector)
  - <view>.html (standalone, interactive: click any node for details
                 incl. its connections — no server needed)
  - <view>.dot  (Graphviz)

Deterministic: byte-identical output across runs given the same canonical
input. The canonical CDG is never modified.
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

KIND2COLOR = TYPE_COLORS
SUBJECT_COLORS = {"Mathematics": "#1b5e20", "Physics": "#0d47a1", "Chemistry": "#4a148c",
                  "Biology": "#b71c1c", "English": "#004d40", None: "#333"}


def _subj_color(nid, nodes):
    e = nodes[nid]
    return SUBJECT_COLORS.get(e.get("subject"), "#333")


def _load():
    with open(CANON) as f:
        d = json.load(f)
    return {e["id"]: e for e in d["entities"]}, d["claims"], d


def _details(nodes, claims, sources, evidence):
    """Per-node detail payload for the interactive HTML."""
    conn = collections.defaultdict(list)
    for c in claims:
        pred = c.get("predicate")
        if not pred or not c.get("object_id"):
            continue
        conn[c["subject_id"]].append(
            {"dir": "->", "predicate": pred, "other": c["object_id"], "claim": c["id"],
             "qualifiers": {k: c.get(k) for k in ("purpose", "scope", "origin") if c.get(k)}}
        )
        conn[c["object_id"]].append(
            {"dir": "<-", "predicate": pred, "other": c["subject_id"], "claim": c["id"],
             "qualifiers": {k: c.get(k) for k in ("purpose", "scope", "origin") if c.get(k)}}
        )
    ev_by_claim = collections.defaultdict(list)
    for e in evidence:
        ev_by_claim[e["claim_id"]].append(e)
    out = {}
    for nid, e in nodes.items():
        entry = {
            "id": nid,
            "entity_type": e["entity_type"],
            "label": e.get("label", ""),
            "subject": e.get("subject"),
            "status": e.get("status"),
            "legacy_ids": e.get("legacy_ids") or [],
            "connections": [],
        }
        for c in sorted(conn.get(nid, []), key=lambda x: (x["predicate"], x["other"], x["dir"])):
            other = nodes.get(c["other"])
            ev = [
                {k: e2.get(k) for k in ("id", "source_id", "legacy_id", "stance", "excerpt")}
                for e2 in ev_by_claim.get(c["claim"], [])
            ]
            entry["connections"].append({
                **c,
                "other_type": other["entity_type"] if other else None,
                "other_label": other.get("label", "") if other else None,
                "evidence": ev,
            })
        out[nid] = entry
    return out


def _layout(node_ids, nodes):
    by_type = collections.defaultdict(list)
    for nid in node_ids:
        by_type[nodes[nid]["entity_type"]].append(nid)
    pos = {}
    col = 0
    for t in sorted(by_type):
        for i, nid in enumerate(sorted(by_type[t])):
            pos[nid] = (col * 260 + 130, i * 56 + 60)
        col += 1
    return pos, max((y for _, y in pos.values()), default=60) + 60, col * 260 + 40


def _legend(nodes):
    seen = sorted({e["entity_type"] for e in nodes.values()},
                  key=lambda t: (t not in ("KnowledgeComponent", "TaskModel", "Method"), t))
    items = "".join(
        f'<span class="lg"><span class="sw" style="background:{TYPE_COLORS.get(t, "#eee")}"></span>{t}</span>'
        for t in seen)
    subs = sorted({e.get("subject") for e in nodes.values() if e.get("subject")})
    sub_items = "".join(
        f'<span class="lg"><span class="sw" style="background:{SUBJECT_COLORS.get(s, "#333")}"></span>{s}</span>'
        for s in subs)
    return f'<div id="legend">Type: {items} &nbsp;|&nbsp; Subject (outline): {sub_items}</div>'


def _svg(title, node_ids, nodes, edges):
    pos, height, width = _layout(node_ids, nodes)
    height = max(height, 200)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'id="cdg-svg" style="background:#ffffff;font-family:monospace">',
             f'<text x="20" y="30" font-size="18" font-weight="bold">{title}</text>',
             '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="8" refY="3" '
             'orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#888"/></marker></defs>']
    for cid, src, dst, pred in edges:
        if src not in pos or dst not in pos:
            continue
        x1, y1 = pos[src]
        x2, y2 = pos[dst]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#bbb" '
                     f'stroke-width="1" marker-end="url(#arrow)"><title>{pred} ({cid})</title></line>')
    for nid in sorted(node_ids):
        x, y = pos[nid]
        e = nodes[nid]
        fill = TYPE_COLORS.get(e["entity_type"], "#eee")
        label = e.get("label", "")[:36].replace('"', "'")
        sc = _subj_color(nid, nodes)
        parts.append(
            f'<g class="node" data-id="{nid}" onclick="cdgSelect(\'{nid}\', event)">'
            f'<rect x="{x-118}" y="{y-18}" width="236" height="36" rx="6" fill="{fill}" stroke="{sc}" stroke-width="4"/>'
            f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="11" fill="white">{label}</text>'
            f'<title>{nid} | {e["entity_type"]}</title></g>')
    parts.append('</svg>')
    return ''.join(parts), height, width


JS_TEMPLATE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "viz_panel.js")).read()


def _html(title, svg_markup, legend, details_json):
    js = JS_TEMPLATE.replace("__DETAILS__", json.dumps(details_json, sort_keys=True))
    return ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>' + title +
            '</title><style>body{font-family:system-ui,monospace;margin:0;padding:20px}'
            '#legend span{display:inline-block;margin-right:12px;font-size:12px}'
            '#legend .sw{display:inline-block;width:12px;height:12px;margin-right:4px;border:1px solid #333}'
            'g.node{cursor:pointer}g.node:hover rect{stroke:#d70000;stroke-width:3}'
            '#ccard{position:absolute;width:min(420px,92vw);max-height:70vh;overflow:auto;z-index:10;'
            'background:#fff;border:2px solid #333;border-radius:10px;padding:14px 16px;'
            'box-shadow:0 8px 24px rgba(0,0,0,.35)}'
            '#ccard.hidden{display:none}#ccard .x{position:absolute;right:8px;top:6px;cursor:pointer;'
            'font-size:20px;color:#666}#ccard .x:hover{color:#d70000}'
            '.c{border-bottom:1px solid #eee;padding:8px 0;font-size:13px}'
            '.m{color:#666;font-size:11px}.ev{color:#555;font-size:11px;margin-left:12px}</style></head>'
            '<body><h1>' + title + '</h1>' + legend +
            '<script>' + js + '</script>' + svg_markup +
            '<div id="ccard" class="hidden"></div></body></html>')


def _dot(title, node_ids, nodes, edges):
    lines = ['digraph g {', f'label="{title}";',
             'node [shape=box,style=filled,fontname="monospace"];']
    for nid in sorted(node_ids):
        e = nodes[nid]
        lines.append(f'"{nid}" [fillcolor="{TYPE_COLORS.get(e["entity_type"], "#eee")}",label="{nid}"];')
    for cid, src, dst, pred in edges:
        if src in node_ids and dst in node_ids:
            lines.append(f'"{src}" -> "{dst}" [label="{pred}"];')
    lines.append('}')
    return '\n'.join(lines)


def _write(stem, title, node_ids, nodes, edges, details):
    svg_markup, _, _ = _svg(title, node_ids, nodes, edges)
    legend = _legend(nodes)
    detail_view = {nid: details[nid] for nid in node_ids if nid in details}
    with open(os.path.join(OUT, stem + '.svg'), 'w') as f:
        f.write(svg_markup)
    with open(os.path.join(OUT, stem + '.html'), 'w') as f:
        f.write(_html(title, svg_markup, legend, detail_view))
    with open(os.path.join(OUT, stem + '.dot'), 'w') as f:
        f.write(_dot(title, node_ids, nodes, edges))


def main():
    nodes, claims, _ = _load()
    evidence = []
    with open(CANON) as f:
        evidence = json.load(f)["evidence"]
    details = _details(nodes, claims, {}, evidence)
    edges_all = [(c["id"], c["subject_id"], c["object_id"], c["predicate"])
                 for c in claims if c.get("predicate") and c.get("object_id")]
    all_ids = list(nodes)
    _write('mathematics_full', 'GLM CDG — Mathematics (full)', all_ids, nodes, edges_all, details)

    sub_ids = [e['id'] for e in nodes.values()
               if e['entity_type'] in ('KnowledgeComponent', 'TaskModel', 'Method')]
    sub_edges = [e for e in edges_all if e[3] in ('prerequisite', 'targets', 'hasMethod', 'requires')]
    _write('mathematics_kcs', 'Mathematics — KCs / TMs / Methods', sub_ids, nodes, sub_edges, details)

    tm_ids = [e['id'] for e in nodes.values() if e['entity_type'] == 'TaskModel']
    m_ids = [c['object_id'] for c in claims if c['predicate'] == 'hasMethod']
    kc_via_req = [c['object_id'] for c in claims if c['predicate'] == 'requires']
    tm_edges = [e for e in edges_all if e[3] in ('hasMethod', 'targets', 'requires')]
    _write('mathematics_tm_method', 'Mathematics — TaskModel/Method',
           tm_ids + m_ids + kc_via_req, nodes, tm_edges, details)

    print('visualizations written to', OUT)


if __name__ == '__main__':
    main()
