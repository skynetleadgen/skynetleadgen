from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission_percentage = fields.Float(string="Commission (%)", default=5.0)
    commission_amount = fields.Monetary(string="Commission Amount", compute="_compute_commission", store=True)

    @api.depends('amount_total', 'commission_percentage')
    def _compute_commission(self):
        for order in self:
            order.commission_amount = (order.amount_total * order.commission_percentage) / 100
