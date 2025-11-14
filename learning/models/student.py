from odoo import models, fields, api

class Student(models.Model):
    _name = 'learning.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    vat = fields.Char(string='VAT', required=True)
    birth_date = fields.Date(string='Date of Birth')
    partner_id = fields.Many2one('res.partner', string='Partner')
    # One2many to scores (ensure Score model uses student_id Many2one)
    score_ids = fields.One2many('learning.score', 'student_id', string='Scores')

    # Compute age from birth_date
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0
    
    # Average score across all subjects for this student
    average_score = fields.Float(string='Average Score', compute='_compute_average_score', store=True, digits=(6, 2), help='Average of all score values for this student' )
    @api.depends('score_ids.value')
    def _compute_average_score(self):
        for rec in self:
            values = rec.score_ids.mapped('value')
            rec.average_score = float(sum(values) / len(values)) if values else 0.0
