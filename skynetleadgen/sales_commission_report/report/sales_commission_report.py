from odoo import api, models, fields

class ReportSalesCommission(models.AbstractModel):
    _name = "report.sales_commission_report.report_sales_commission_per_salesperson"
    _description = "Sales Commission Report (Per Salesperson)"

    def _get_lead_count(self, salesperson_name, date_from, date_to):
        Commission = self.env["manual.sales.commission"]
        recs = Commission.search([
            ("name", "=", salesperson_name),
            ("create_date", ">=", date_from),
            ("create_date", "<=", date_to),
        ])
        return sum(r.no_of_leads for r in recs)

    def _get_commission_amount(self, salesperson_name, date_from, date_to):
        Commission = self.env["manual.sales.commission"]
        recs = Commission.search([
            ("name", "=", salesperson_name),
            ("create_date", ">=", date_from),
            ("create_date", "<=", date_to),
        ])
        return sum(r.commission_amount for r in recs)

    @api.model
    def _get_report_values(self, docids, data=None):
        data = data or {}
        date_from = data.get("date_from")
        date_to = data.get("date_to")

        Commission = self.env["manual.sales.commission"]
        salespeople = Commission.search([
            ("create_date", ">=", date_from),
            ("create_date", "<=", date_to),
        ]).mapped("name")

        docs = []
        for sp in set(salespeople):
            lead_count = self._get_lead_count(sp, date_from, date_to)
            amount = self._get_commission_amount(sp, date_from, date_to)
            docs.append({
                "salesperson_name": sp,
                "month_label": fields.Date.from_string(date_from).strftime("%B %Y"),
                "lead_count": lead_count,
                "commission_amount": amount,
            })

        return {
            "docs": docs,
            "date_from": date_from,
            "date_to": date_to,
            "company": self.env.company,
            "currency": self.env.company.currency_id,
        }
