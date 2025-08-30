{
    'name': 'Manual Sales Commission',
    'version': '1.1',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'web'],  # important for QWeb reports
    'data': [
        'security/ir.model.access.csv',
        'report/sales_commission_report.xml',  # report loaded first
        'views/sales_commission_menu.xml',     # views loaded after
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
