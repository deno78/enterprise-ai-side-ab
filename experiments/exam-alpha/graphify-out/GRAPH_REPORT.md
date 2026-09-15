# Graph Report - exam-alpha  (2026-09-15)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 14 nodes · 8 edges · 7 communities (2 shown, 5 thin omitted)
- Extraction: 62% EXTRACTED · 38% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.93)
- Token cost: 162 input · 22 output

## Graph Freshness
- Built from commit: `3bc27fbb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Reservation Frontend Requirements
- PDF Document Generation
- Flask
- qrcode
- Flask-Bcrypt
- Flask-SQLAlchemy
- Pillow

## God Nodes (most connected - your core abstractions)
1. `Vue.js Frontend App` - 4 edges
2. `/api/reservations/<id>/pdf` - 2 edges
3. `PDF Output Requirement` - 2 edges
4. `Index Template` - 1 edges
5. `Facility Search Requirement` - 1 edges
6. `Reservation Function Requirement` - 1 edges
7. `fpdf2` - 1 edges
8. `Flask` - 1 edges
9. `System Overview` - 1 edges
10. `qrcode` - 1 edges

## Surprising Connections (you probably didn't know these)
- `/api/reservations/<id>/pdf` --implements--> `PDF Output Requirement`  [INFERRED]
  templates/index.html → spec.md
- `PDF Output Requirement` --references--> `fpdf2`  [INFERRED]
  spec.md → requirements.txt
- `Mock Payment Requirement` --references--> `qrcode`  [INFERRED]
  spec.md → requirements.txt
- `Vue.js Frontend App` --implements--> `Facility Search Requirement`  [EXTRACTED]
  templates/index.html → spec.md
- `Vue.js Frontend App` --implements--> `Reservation Function Requirement`  [EXTRACTED]
  templates/index.html → spec.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Reservation to PDF Flow** — spec_reservation_function, spec_mock_payment, spec_pdf_output, templates_index_vue_app [EXTRACTED 0.95]
- **Technology Stack Alignment** — requirements_flask, requirements_flask_sqlalchemy, spec_system_overview [EXTRACTED 1.00]

## Communities (7 total, 5 thin omitted)

### Community 0 - "Reservation Frontend Requirements"
Cohesion: 0.50
Nodes (4): Facility Search Requirement, Reservation Function Requirement, Index Template, Vue.js Frontend App

### Community 1 - "PDF Document Generation"
Cohesion: 0.67
Nodes (3): /api/reservations/<id>/pdf, fpdf2, PDF Output Requirement

## Knowledge Gaps
- **11 isolated node(s):** `Index Template`, `Facility Search Requirement`, `Reservation Function Requirement`, `fpdf2`, `Flask` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Vue.js Frontend App` connect `Reservation Frontend Requirements` to `PDF Document Generation`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Why does `/api/reservations/<id>/pdf` connect `PDF Document Generation` to `Reservation Frontend Requirements`?**
  _High betweenness centrality (0.103) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `PDF Output Requirement` (e.g. with `/api/reservations/<id>/pdf` and `fpdf2`) actually correct?**
  _`PDF Output Requirement` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Index Template`, `Facility Search Requirement`, `Reservation Function Requirement` to the rest of the system?**
  _11 weakly-connected nodes found - possible documentation gaps or missing edges._