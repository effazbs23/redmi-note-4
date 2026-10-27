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
HR user opens an employee, goes to the new Payroll tab and enters a numeric Size. The value is stored on the employee (hr.employee.size, Float).

### Happy path
1. Open http://localhost:8090 and go to Employees.
2. Open Johnny Goods.
3. Click the new "Payroll" tab (last tab on the form).
4. Enter 42 in the Size field and save. Expect the value to stay after saving and reloading.
5. Try a decimal such as 8.5. Expect it to save too.
Not covered: Size is not in the list view, search filters or reports. Undo: use Revert on the site for this branch.
