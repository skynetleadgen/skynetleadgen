{
    'name': 'Manual Sales Commission',
    'version': '1.1',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'web'],  # Add 'web' to support QWeb reports
    'data': [
        'security/ir.model.access.csv',
        'report/sales_commission_report.xml',  # Load report first
        'views/sales_commission_menu.xml',     # Load views after report
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
