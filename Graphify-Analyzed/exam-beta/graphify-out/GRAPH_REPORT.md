# Graph Report - exam-beta  (2026-09-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 88 nodes · 126 edges · 21 communities (7 shown, 14 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.95)
- Token cost: 467 input · 197 output

## Graph Freshness
- Built from commit: `562031a0`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Reservation Management
- User Authentication
- Payment Processing
- Facility Management API
- App Configuration and Models
- Facility Detail View
- Internationalization Support
- State Management
- Frontend Application Entry
- Admin Facility Management
- Admin Reservation Management
- Facility List View
- Login Page
- Payment Page
- User Profile Page
- User Registration Page
- Reservation Detail View
- Reservation Form
- Reservation List View

## God Nodes (most connected - your core abstractions)
1. `ReservationLog` - 6 edges
2. `User` - 5 edges
3. `Facility` - 5 edges
4. `create_reservation()` - 5 edges
5. `Reservation` - 4 edges
6. `Payment` - 4 edges
7. `cancel_reservation()` - 4 edges
8. `download_pdf()` - 4 edges
9. `update_reservation()` - 4 edges
10. `make_payment()` - 4 edges

## Surprising Connections (you probably didn't know these)
- `create_app()` --uses--> `Config`  [INFERRED]
  app.py → config.py
- `create_facility()` --calls--> `Facility`  [EXTRACTED]
  routes/facilities.py → models/facility.py
- `cancel_reservation()` --calls--> `ReservationLog`  [EXTRACTED]
  routes/reservations.py → models/reservation_log.py
- `create_reservation()` --calls--> `ReservationLog`  [EXTRACTED]
  routes/reservations.py → models/reservation_log.py
- `update_reservation()` --calls--> `ReservationLog`  [EXTRACTED]
  routes/reservations.py → models/reservation_log.py

## Import Cycles
- None detected.

## Communities (21 total, 14 thin omitted)

### Community 0 - "Reservation Management"
Cohesion: 0.26
Nodes (11): ReservationLog, Reservation, cancel_reservation(), create_reservation(), download_pdf(), get_reservation(), list_reservations(), login_required (+3 more)

### Community 1 - "User Authentication"
Cohesion: 0.27
Nodes (9): User, get_me(), login(), logout(), login_required, route, register(), update_profile() (+1 more)

### Community 2 - "Payment Processing"
Cohesion: 0.31
Nodes (5): Payment, get_payment(), make_payment(), login_required, route

### Community 3 - "Facility Management API"
Cohesion: 0.42
Nodes (8): create_facility(), delete_facility(), get_availability(), get_facility(), list_facilities(), login_required, route, update_facility()

### Community 4 - "App Configuration and Models"
Cohesion: 0.39
Nodes (4): create_app(), _seed_data(), Config, Facility

## Knowledge Gaps
- **15 isolated node(s):** `AdminReservations`, `FacilityList`, `LoginPage`, `PaymentPage`, `ProfilePage` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `User` connect `User Authentication` to `Reservation Management`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `Facility` connect `App Configuration and Models` to `Reservation Management`, `Facility Management API`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `Payment` connect `Payment Processing` to `Reservation Management`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **What connects `AdminReservations`, `FacilityList`, `LoginPage` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._