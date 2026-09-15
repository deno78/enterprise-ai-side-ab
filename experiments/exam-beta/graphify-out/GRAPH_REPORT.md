# Graph Report - exam-beta  (2026-09-15)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 75 nodes · 75 edges · 12 communities (7 shown, 5 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 289 input · 29 output

## Graph Freshness
- Built from commit: `3bc27fbb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Build and Initialization Scripts
- Agent Configuration and Skills
- bash
- references
- architect
- Project Agents Overview
- Architecture Overview
- Architect Agent Definition
- Reviewer Agent Definition
- API Design Specification
- Developer Agent Definition
- Python Dependencies

## God Nodes (most connected - your core abstractions)
1. `bash` - 6 edges
2. `command` - 5 edges
3. `developer` - 5 edges
4. `architect` - 5 edges
5. `reviewer` - 5 edges
6. `Project Agents Overview` - 5 edges
7. `edit` - 4 edges
8. `references` - 4 edges
9. `agent` - 4 edges
10. `build` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Project Agents Overview` --references--> `Backend Agent Instructions`  [EXTRACTED]
  AGENTS.md → skills/backend/instructions.md
- `Project Agents Overview` --references--> `Design Agent Instructions`  [EXTRACTED]
  AGENTS.md → skills/design/instructions.md
- `Project Agents Overview` --references--> `Documentation Agent Instructions`  [EXTRACTED]
  AGENTS.md → skills/documentation/instructions.md
- `Project Agents Overview` --references--> `QA Agent Instructions`  [EXTRACTED]
  AGENTS.md → skills/qa/instructions.md
- `Project Agents Overview` --references--> `UI Agent Instructions`  [EXTRACTED]
  AGENTS.md → skills/ui/instructions.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Collaboration Flow** — opencode_agents_architect, opencode_agents_developer, opencode_agents_reviewer [EXTRACTED 0.90]

## Communities (12 total, 5 thin omitted)

### Community 0 - "Build and Initialization Scripts"
Cohesion: 0.15
Nodes (13): description, template, command, build, dist, init-db, test, description (+5 more)

### Community 1 - "Agent Configuration and Skills"
Cohesion: 0.17
Nodes (11): compaction, auto, tail_turns, instructions, $schema, skills, paths, AGENTS.md (+3 more)

### Community 2 - "bash"
Cohesion: 0.21
Nodes (12): developer, permission, git *, rm *, description, mode, model, permission (+4 more)

### Community 3 - "references"
Cohesion: 0.20
Nodes (10): description, path, description, path, references, agent-instructions, design-docs, spec (+2 more)

### Community 4 - "architect"
Cohesion: 0.22
Nodes (9): agent, architect, reviewer, description, mode, model, description, mode (+1 more)

### Community 5 - "Project Agents Overview"
Cohesion: 0.38
Nodes (7): Project Agents Overview, Backend Agent Instructions, Design Agent Instructions, Documentation Agent Instructions, QA Agent Instructions, UI Agent Instructions, System Specification

### Community 6 - "Architecture Overview"
Cohesion: 0.40
Nodes (5): Architecture Overview, Database Schema Design, Frontend Structure Design, SQLite Database, Main SPA Entry Point

## Knowledge Gaps
- **43 isolated node(s):** `description`, `template`, `description`, `template`, `description` (+38 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `command` connect `Build and Initialization Scripts` to `Agent Configuration and Skills`?**
  _High betweenness centrality (0.211) - this node is a cross-community bridge._
- **Why does `agent` connect `architect` to `Agent Configuration and Skills`, `bash`?**
  _High betweenness centrality (0.191) - this node is a cross-community bridge._
- **Why does `references` connect `references` to `Agent Configuration and Skills`?**
  _High betweenness centrality (0.163) - this node is a cross-community bridge._
- **What connects `description`, `template`, `description` to the rest of the system?**
  _43 weakly-connected nodes found - possible documentation gaps or missing edges._