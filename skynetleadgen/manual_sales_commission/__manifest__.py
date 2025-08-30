{
    'name': 'Manual Sales Commission',
    'version': '1.1',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions with PDF reports',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'web'],  # base and web required for QWeb reports
    'data': [
        'security/ir.model.access.csv',             # access rights
        'report/sales_commission_report.xml',       # report loaded first
        'views/sales_commission_menu.xml',          # views loaded after
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
