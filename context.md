# Context: employee_size_field

- Project: redmi-note
- Branch: `demo/1_work_employee-size-field` (from `main`)
- Odoo version: 20.0
- Started: 2026-10-27 12:34 UTC by effazbs23

## Request
In the presales_demo addon, inherit hr.employee and add a Char field "size" (label "Size"). Inherit the employee form view with an xpath to show it in a Payroll tab/group. No payroll app is installed, so the addon would add a "Payroll" page to the employee form (new notebook page) holding the Size field. No new models, no security changes (existing hr.employee access applies).

## Project notes
(none)

## Decisions
Why things were built this way, for whoever continues on this branch. Newest last.

## Workflow and happy path
### Workflow
HR manager opens an employee, goes to the existing Payroll tab and enters a numeric Size (hr.employee.size, Float), shown next to the Schedule group.

### Happy path
1. Open http://localhost:8090, go to Employees, open Johnny Goods.
2. Click the Payroll tab (only one should exist now).
3. Find the Size field beside the Schedule section.
4. Enter 42, save, reload. Expect 42 to remain. Decimals like 8.5 also save.
Note: the Payroll tab is visible to HR Managers only (existing Odoo restriction). Not covered: list view, filters, reports. Undo: Revert on the site.
