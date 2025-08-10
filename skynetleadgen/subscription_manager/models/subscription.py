from odoo import models, fields

class SubscriptionManager(models.Model):
    _name = 'subscription.manager'
    _description = 'Software Subscription Manager'

    name = fields.Char(string='Software Name', required=True)
    user_id = fields.Char(string='User ID')
    password = fields.Char(string='Password')
    renewal_date = fields.Date(string='Renewal Date')
