from odoo import models, fields, api

class Student(models.Model):
    _name = 'learning.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    vat = fields.Char(string='VAT', required=True)
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age')
    