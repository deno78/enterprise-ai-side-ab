# Graph Report - exam-alpha  (2026-09-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 30 nodes · 70 edges · 6 communities (5 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.95)
- Token cost: 220 input · 19 output

## Graph Freshness
- Built from commit: `562031a0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- User Authentication and Routing
- index.html
- get_user_lang
- Facility
- login_required
- Reservation

## God Nodes (most connected - your core abstractions)
1. `Reservation` - 9 edges
2. `get_user_lang()` - 8 edges
3. `Facility` - 7 edges
4. `login_required()` - 7 edges
5. `User` - 6 edges
6. `api_payment()` - 5 edges
7. `api_reservation()` - 5 edges
8. `api_reservation_pdf()` - 5 edges
9. `api_reservations()` - 5 edges
10. `api_user()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `get_user_lang()` --uses--> `User`  [INFERRED]
  app.py → models.py
- `api_availability()` --uses--> `Facility`  [INFERRED]
  app.py → models.py
- `api_facilities()` --uses--> `Facility`  [INFERRED]
  app.py → models.py
- `api_payment()` --uses--> `Reservation`  [INFERRED]
  app.py → models.py
- `api_payment_qr()` --uses--> `Reservation`  [INFERRED]
  app.py → models.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Frontend Localization Flow** — templates_index_vue_app, templates_index_translations, templates_index [EXTRACTED 0.90]

## Communities (6 total, 1 thin omitted)

### Community 0 - "User Authentication and Routing"
Cohesion: 0.40
Nodes (8): api_login(), api_logout(), api_register(), api_translations(), api_user(), index(), User, route

### Community 1 - "index.html"
Cohesion: 0.40
Nodes (4): Reservation PDF API, Translations Object, Vue Application, Vue 3 Global Prod

### Community 2 - "get_user_lang"
Cohesion: 0.50
Nodes (4): api_facilities(), api_payment(), api_reservation(), get_user_lang()

### Community 3 - "Facility"
Cohesion: 0.50
Nodes (3): api_facility(), seed_data(), Facility

### Community 4 - "login_required"
Cohesion: 0.50
Nodes (4): api_payment_qr(), api_reservation_pdf(), api_reservations(), login_required()

## Knowledge Gaps
- **2 isolated node(s):** `Reservation PDF API`, `Translations Object`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Reservation` connect `Reservation` to `User Authentication and Routing`, `get_user_lang`, `login_required`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Why does `Facility` connect `Facility` to `User Authentication and Routing`, `get_user_lang`, `Reservation`?**
  _High betweenness centrality (0.068) - this node is a cross-community bridge._
- **Why does `get_user_lang()` connect `get_user_lang` to `User Authentication and Routing`, `Facility`, `login_required`?**
  _High betweenness centrality (0.018) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `Reservation` (e.g. with `api_availability()` and `api_payment()`) actually correct?**
  _`Reservation` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Facility` (e.g. with `api_availability()` and `api_facilities()`) actually correct?**
  _`Facility` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Reservation PDF API`, `Translations Object` to the rest of the system?**
  _2 weakly-connected nodes found - possible documentation gaps or missing edges._