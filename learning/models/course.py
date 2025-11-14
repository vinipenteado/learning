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

    # average score across all students that belong to this course (via subjects)
    average_score = fields.Float(
        string='Average Score',
        compute='_compute_average_score',
        store=True,
        digits=(6, 2),
    )

    @api.depends('subject_id.student_id.average_score')
    def _compute_average_score(self):
        for rec in self:
            students = rec.subject_id.mapped('student_id')
            # consider only students with average_score > 0.0
            valid_scores = [s.average_score for s in students if s.average_score and s.average_score > 0.0]
            rec.average_score = float(sum(valid_scores) / len(valid_scores)) if valid_scores else 0.0

    @api.depends('subject_id')
    def _compute_subject_names(self):
        for rec in self:
            rec.subject_names = ', '.join(rec.subject_id.mapped('name')) if rec.subject_id else ''