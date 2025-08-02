{
    'name': 'Sales Commission Module',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Calculate sales commissions for salespeople',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/commission_views.xml',
    ],
    'installable': True,
    'application': True,
}
