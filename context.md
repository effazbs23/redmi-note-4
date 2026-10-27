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
