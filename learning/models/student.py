from odoo import models, fields, api

class Student(models.Model):
    _name = 'learning.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    vat = fields.Char(string='VAT', required=True)
    birth_date = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0
    