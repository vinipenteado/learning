from odoo import models, fields, api

class Score(models.Model):
    _name = 'learning.score'
    _description = 'Score'

    value = fields.Float(string='Score Value', required=True)
    student_id = fields.Many2one('learning.student', string='Student', required=True)
    
    # link to subject: each score must be assigned to one subject
    subject_id = fields.Many2one('learning.subject', string='Subject', required=True)
