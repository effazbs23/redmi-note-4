{
    'name': 'Presales Demo',
    'version': '20.0.1.1.0',
    'summary': 'Presales demo customisations (BRD phase 1)',
    'author': 'Presales',
    'license': 'LGPL-3',
    'depends': ['hr', 'stock', 'mrp'],
    'data': [
        'security/security.xml',
        'security/ir.access.csv',
        'views/hr_employee_views.xml',
        'views/mrp_production_views.xml',
        'views/stock_orderpoint_views.xml',
    ],
    'installable': True,
    'application': False,
}
