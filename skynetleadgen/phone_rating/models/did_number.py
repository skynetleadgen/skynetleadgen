from odoo import models, fields

class PhoneNumber(models.Model):
    _name = 'did.number'
    _description = 'Phone Number with Rating'

    phone_number = fields.Char(string='Phone Number', required=True)
    rating = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars'),
    ], string='Rating', default='3')
