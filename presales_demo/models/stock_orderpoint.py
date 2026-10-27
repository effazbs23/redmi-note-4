import math
from datetime import timedelta

from odoo import fields, models


class StockWarehouseOrderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    avg_daily_consumption = fields.Float(
        string='Avg Daily Use', compute='_compute_suggestions')
    suggested_min_qty = fields.Float(
        string='Suggested Min', compute='_compute_suggestions')
    suggested_max_qty = fields.Float(
        string='Suggested Max', compute='_compute_suggestions')

    def _compute_suggestions(self):
        """Statistical suggestion (not AI) from past outgoing consumption.

        avg_daily = outgoing done quantity over the look-back period / days
        suggested_min = avg_daily * max(lead_days, 1) * safety_factor
        suggested_max = suggested_min + avg_daily * 7 (one week of review cover)
        Look-back days and safety factor are system parameters
        presales_demo.consumption_days (90) and presales_demo.safety_factor (1.2).
        """
        params = self.env['ir.config_parameter'].sudo()
        try:
            days = int(params.get_param('presales_demo.consumption_days', 90))
        except ValueError:
            days = 90
        try:
            safety = float(params.get_param('presales_demo.safety_factor', 1.2))
        except ValueError:
            safety = 1.2
        days = max(days, 1)
        since = fields.Datetime.now() - timedelta(days=days)
        Move = self.env['stock.move']
        for orderpoint in self:
            avg = 0.0
            if orderpoint.product_id and orderpoint.location_id:
                moves = Move.search([
                    ('state', '=', 'done'),
                    ('product_id', '=', orderpoint.product_id.id),
                    ('date', '>=', since),
                    ('location_id', 'child_of', orderpoint.location_id.id),
                    ('location_dest_id.usage', 'not in', ('internal', 'transit')),
                ])
                avg = sum(moves.mapped('quantity')) / days
            lead = max(orderpoint.lead_days or 0.0, 1.0)
            suggested_min = math.ceil(avg * lead * safety)
            orderpoint.avg_daily_consumption = avg
            orderpoint.suggested_min_qty = suggested_min
            orderpoint.suggested_max_qty = suggested_min + math.ceil(avg * 7)

    def action_apply_suggestions(self):
        for orderpoint in self:
            if orderpoint.avg_daily_consumption > 0:
                orderpoint.write({
                    'product_min_qty': orderpoint.suggested_min_qty,
                    'product_max_qty': orderpoint.suggested_max_qty,
                })
        return True
