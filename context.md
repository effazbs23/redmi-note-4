# Context: brd_phase1

- Project: redmi-note
- Branch: `demo/2_work_brd-phase1` (from `main`)
- Odoo version: 20.0
- Started: 2026-10-27 12:50 UTC by effazbs23

## Request
Phase 1, in presales_demo (inherit only, no core edits). (1) Continuous production: new model mrp.production.output.log (MO, date/time, quantity, operator, note), a "Production Output" tab on the manufacturing order form, and computed total logged qty plus % of planned qty on the MO. (2) Reorder suggestions: on stock.warehouse.orderpoint add Suggested Min / Suggested Max computed from average daily outgoing consumption over a configurable look-back (default 90 days) times lead time and a safety factor, shown in the reordering rules list, with an "Apply Suggestions" button/server action copying them to Min/Max. This is statistical, not an LLM. (3) Roles: groups Finance Manager, Operations Lead and Warehouse/Field Light User, each implying existing standard groups (accounting manager, stock/MRP/purchase manager, stock user), plus ir.access.csv rows for the new log model.

## Project notes
(none)

## Decisions
Why things were built this way, for whoever continues on this branch. Newest last.

## Workflow and happy path
### Workflow
1) Operator logs produced quantity on a manufacturing order during a run; the MO shows total logged and % of planned qty. 2) Inventory user opens Reordering Rules, sees avg daily use and suggested Min/Max from past outgoing moves, and applies them per row or in bulk via Actions. 3) Admin assigns Finance Manager / Operations Lead / Warehouse/Field Light User groups to users. Employee Size field (Payroll tab) is carried over.

### Happy path
Production output: 1. Manufacturing > Manufacturing Orders, open or create an MO (e.g. 10 units, confirm it). 2. Open the "Production Output" tab, add a line with quantity 4, then another with 3. Save. Expect Logged Output 7 and Output Progress 70. 3. Try quantity 0: expect an error. 4. Mark the MO done: the tab becomes read-only.
Reorder suggestions: 1. Create a storable product with stock and deliver some quantity (done outgoing delivery in the last 90 days). 2. Inventory > Operations > Replenishment (Reordering Rules), create a rule for the product. 3. Enable columns Avg Daily Use, Suggested Min, Suggested Max. Expect non-zero values once there are deliveries. 4. Click the magic-wand icon on the row, or select rows and use Actions > Apply Suggested Min/Max. Expect Min/Max to update. Tune via System Parameters presales_demo.consumption_days (90) and presales_demo.safety_factor (1.2).
Roles: 1. Settings > Users, open a user. 2. Assign Finance Manager, Operations Lead or Warehouse/Field Light User and confirm the matching apps open and others stay limited.
Employee Size: Employees > Johnny Goods > Payroll tab > Size.
Not covered: AI agents, natural-language CRM, offline field service/barcode, MCP, duplicate-bill detection (phase 2). Suggestions are statistical, not AI. Undo: Revert on the site.
