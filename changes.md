# Changes: `demo/2_work_brd-phase1`

One entry per commit, newest last. Added automatically when code is written through the connector.

## 2026-10-27 12:51 UTC · effazbs23
[ADD] presales_demo: BRD phase 1 (output logs, reorder suggestions, roles)
- `presales_demo/__init__.py`
- `presales_demo/__manifest__.py`
- `presales_demo/models/__init__.py`
- `presales_demo/models/hr_employee.py`
- `presales_demo/models/mrp_production.py`
- `presales_demo/models/mrp_production_output_log.py`
- `presales_demo/models/stock_orderpoint.py`
- `presales_demo/security/ir.access.csv`
- `presales_demo/security/security.xml`
- `presales_demo/views/hr_employee_views.xml`
- `presales_demo/views/mrp_production_views.xml`
- `presales_demo/views/stock_orderpoint_views.xml`

## 2026-10-27 12:55 UTC · effazbs23
[FIX] presales_demo: read config params without get_param (Odoo 20)
- `presales_demo/models/stock_orderpoint.py`

## 2026-10-27 12:56 UTC · effazbs23
[FIX] presales_demo: use Material icon for apply-suggestions button
- `presales_demo/views/stock_orderpoint_views.xml`
