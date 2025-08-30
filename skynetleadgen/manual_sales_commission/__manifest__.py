{
    'name': 'Manual Sales Commission',
    'version': '1.1',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'report'],  # required for PDF reports
    'data': [
        'security/ir.model.access.csv',           # access rights first
        'report/sales_commission_report.xml',    # report loaded first
        'views/sales_commission_menu.xml',       # views loaded after
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
