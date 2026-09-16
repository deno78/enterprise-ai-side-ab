# Graph Report - exam-alpha  (2026-09-15)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 5 nodes · 4 edges · 2 communities (0 shown, 2 thin omitted)
- Extraction: 75% EXTRACTED · 25% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `562031a0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Reservation PDF API
- Vue Application

## God Nodes (most connected - your core abstractions)
1. `Reservation PDF API` - 2 edges
2. `Vue Application` - 2 edges
3. `Vue 3 CDN` - 1 edges
4. `Translations Object` - 1 edges

## Surprising Connections (you probably didn't know these)
- `Vue Application` --calls--> `Reservation PDF API`  [INFERRED]
  templates/index.html → templates/index.html  _Bridges community 0 → community 1_

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Frontend Localization** — templates_index_vue_app, templates_index_translations [EXTRACTED 1.00]

## Communities (2 total, 2 thin omitted)

## Knowledge Gaps
- **2 isolated node(s):** `Vue 3 CDN`, `Translations Object`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Reservation PDF API` connect `Reservation PDF API` to `Vue Application`?**
  _High betweenness centrality (0.667) - this node is a cross-community bridge._
- **Why does `Vue Application` connect `Vue Application` to `Reservation PDF API`?**
  _High betweenness centrality (0.500) - this node is a cross-community bridge._
- **What connects `Vue 3 CDN`, `Translations Object` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._