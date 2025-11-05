from odoo import models, fields, api

class Subject(models.Model):
    _name = 'learning.subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    price = fields.Char(string='Price', required=True)
    difficulty = fields.Selection(string='Difficulty', selection=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    ])
    student_id = fields.Many2many('learning.student', string='Students')