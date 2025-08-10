{
    'name': 'Subscription Manager',
    'version': '1.0.0',
    'summary': 'Manage your software subscriptions including credentials and renewal dates.',
    'description': 'Store and manage subscription details such as software name, user ID, password, and renewal dates.',
    'category': 'Productivity',
    'author': 'Your Name or Company',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'views/subscription_views.xml',
    ],
    'installable': True,
    'application': True,  # Makes it appear in the Apps list
    'auto_install': False,
}
