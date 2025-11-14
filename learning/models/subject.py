from odoo import models, fields, api
from odoo.exceptions import UserError

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
    student_names = fields.Char(string='Students', compute='_compute_student_names')
    # each subject belongs to one course
    course_id = fields.Many2one('learning.course', string='Course')
    # One2many inverse to show scores for this subject
    score_ids = fields.One2many('learning.score', 'subject_id', string='Scores')

    # compute student names
    @api.depends('student_id')
    def _compute_student_names(self):
        for rec in self:
            rec.student_names = ', '.join(rec.student_id.mapped('name')) if rec.student_id else ''

    # prevent reassigning a subject that already belongs to a course
    def write(self, vals):
        if 'course_id' in vals:
            for rec in self:
                if rec.course_id and vals.get('course_id') and rec.course_id.id != vals.get('course_id'):
                    raise UserError(
                        "Subject '%s' is already assigned to course '%s' and cannot be reassigned."
                        % (rec.name or _('(no name)'), rec.course_id.name or _('(no course)'))
                    )
        return super().write(vals)