{
    'name': 'Manual Sales Commission',
    'version': '1.0',
    'summary': 'Manage sales commissions manually',
    'category': 'Sales',
    'sequence': 10,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/sales_commission_menu.xml',
        # Add other view files here
    ],
    'installable': True,
    'application': True,  
    'auto_install': False,
}
