from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MrpProductionOutputLog(models.Model):
    _name = 'mrp.production.output.log'
    _description = 'Production Output Log'
    _order = 'log_date desc, id desc'

    production_id = fields.Many2one(
        'mrp.production', string='Manufacturing Order',
        required=True, ondelete='cascade', index=True)
    log_date = fields.Datetime(
        string='Date', required=True, default=fields.Datetime.now)
    quantity = fields.Float(string='Quantity Produced', required=True)
    user_id = fields.Many2one(
        'res.users', string='Operator', default=lambda self: self.env.user)
    note = fields.Char(string='Note')

    @api.constrains('quantity')
    def _check_quantity(self):
        for log in self:
            if log.quantity <= 0:
                raise ValidationError(
                    self.env._('The produced quantity must be greater than zero.'))
