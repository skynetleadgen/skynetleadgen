from odoo import models, fields, api

class ManualSalesCommission(models.Model):
    _name = "manual.sales.commission"
    _description = "Manual Sales Commission"

    name = fields.Char(string="Salesperson Name", required=True)
    month = fields.Char(string="Month")  # <-- Add this field
    no_of_leads = fields.Integer(string="Number of Leads", required=True)
    commission_amount = fields.Float(
        string="Commission Amount",
        compute="_compute_commission",
        store=True
    )

    @api.depends('no_of_leads')
    def _compute_commission(self):
        for record in self:
            record.commission_amount = record.no_of_leads * 500
