from odoo import api, fields, models
from datetime import date
import calendar

class SalesCommissionWizard(models.TransientModel):
    _name = "sales.commission.wizard"
    _description = "Sales Commission Report Wizard"

    month = fields.Date(
        string="Any date in month",
        required=True,
        default=lambda self: date.today().replace(day=1),
        help="Pick any date within the target month."
    )

    def _month_range(self, dt):
        first = dt.replace(day=1)
        last_day = calendar.monthrange(dt.year, dt.month)[1]
        last = dt.replace(day=last_day)
        return first, last

    def action_print(self):
        self.ensure_one()
        first, last = self._month_range(self.month)
        data = {
            "date_from": fields.Date.to_string(first),
            "date_to": fields.Date.to_string(last),
        }
        return self.env.ref(
            "sales_commission_report.action_report_sales_commission_per_salesperson"
        ).report_action(docids=[], data=data)
