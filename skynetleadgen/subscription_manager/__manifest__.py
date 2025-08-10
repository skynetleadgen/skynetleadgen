{
    'name': 'Subscription Manager',
    'version': '1.0.0',
    'summary': 'Manage software subscriptions including credentials and renewal dates.',
    'description': """
        Manage your software subscriptions with fields for software name, user ID, password, and renewal date.
    """,
    'category': 'Productivity',
    'author': 'Your Name',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/subscription_views.xml',
    ],
    'images': ['static/description/icon.png'],  # optional
    'installable': True,
    'application': True,
    'auto_install': False,
}
