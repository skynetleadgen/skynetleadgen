{
    "name": "Sales Commission Report (Per Salesperson)",
    "summary": "QWeb report showing commissions per salesperson (manual.commission model)",
    "version": "16.0.1.0.0",
    "author": "Your Company",
    "website": "https://yourcompany.com",
    "license": "LGPL-3",
    "depends": ["base"],  # No crm or users dependency
    "data": [
        "security/ir.model.access.csv",
        "wizard/sales_commission_wizard_views.xml",
        "report/sales_commission_report.xml",
    ],
    "application": False,
    "installable": True,
}
