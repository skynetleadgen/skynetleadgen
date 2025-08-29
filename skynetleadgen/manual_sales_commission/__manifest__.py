{
    'name': 'Manual Sales Commission',
    'version': '1.0',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_commission_menu.xml',
        'report/sales_commission_report.xml',   # <-- IMPORTANT
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
