from odoo import models, fields, api

class course(models.Model):
    _name = 'learning.course'
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    subject_id = fields.One2many('learning.subject', 'course_id', string='Subjects')
    subject_names = fields.Char(string='Subjects', compute='_compute_subject_names')

    @api.depends('subject_id')
    def _compute_subject_names(self):
        for rec in self:
            rec.subject_names = ', '.join(rec.subject_id.mapped('name')) if rec.subject_id else ''

