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
