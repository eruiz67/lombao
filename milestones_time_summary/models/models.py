# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MilestoneTimeSumary(models.Model):
    _inherit = "project.milestone"
    _description = 'Adiciona Horas planeadas al hito'


    time_summary = fields.Float(compute='_compute_time_summary', string='Horas Planeadas')
    
    @api.depends('project_task_ids')
    def _compute_time_summary(self):
        for rec in self:
            suma=0 
            for task in rec.project_task_ids:
                suma += task.planned_hours
            rec.time_summary=suma

# from odoo import models, fields, api


# class milestones_time_summary(models.Model):
#     _name = 'milestones_time_summary.milestones_time_summary'
#     _description = 'milestones_time_summary.milestones_time_summary'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
