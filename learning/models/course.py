from odoo import models, fields, api

class course(models.Model):
    _name = 'learning.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    subject_id = fields.Many2many('learning.subject', string='Subjects')
