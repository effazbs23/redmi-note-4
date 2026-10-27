from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    output_log_ids = fields.One2many(
        'mrp.production.output.log', 'production_id', string='Output Logs')
    output_logged_qty = fields.Float(
        string='Logged Output', compute='_compute_output_logged')
    output_progress = fields.Float(
        string='Output Progress (%)', compute='_compute_output_logged')

    @api.depends('output_log_ids.quantity', 'product_qty')
    def _compute_output_logged(self):
        for production in self:
            total = sum(production.output_log_ids.mapped('quantity'))
            production.output_logged_qty = total
            production.output_progress = (
                total / production.product_qty * 100.0
            ) if production.product_qty else 0.0
