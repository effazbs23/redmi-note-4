from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    size = fields.Float(string='Size')
