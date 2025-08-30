{
    'name': 'Manual Sales Commission',
    'version': '1.0',
    'summary': 'Manage manual sales commissions',
    'description': 'Module to handle manual sales commissions and generate PDF reports',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',           # access rights
        'report/sales_commission_report.xml',     # report action & template
        'views/sales_commission_menu.xml',        # tree/form views + menu
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
