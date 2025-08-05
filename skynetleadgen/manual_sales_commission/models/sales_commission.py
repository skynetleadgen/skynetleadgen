from odoo import models, fields

class SalesCommission(models.Model):
    _name = "sales.commission"
    _description = "Sales Commission"

    name = fields.Char(string="Salesperson Name", required=True)
    no_of_leads = fields.Integer(string="Number of Leads", required=True)
    commission_amount = fields.Float(
        string="Commission Amount",
        compute="_compute_commission",
        store=True
    )

    def _compute_commission(self):
        for record in self:
            record.commission_amount = record.no_of_leads * 500
