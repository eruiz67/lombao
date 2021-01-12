# -*- coding: utf-8 -*-
# from odoo import http


# class MilestonesTimeSummary(http.Controller):
#     @http.route('/milestones_time_summary/milestones_time_summary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/milestones_time_summary/milestones_time_summary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('milestones_time_summary.listing', {
#             'root': '/milestones_time_summary/milestones_time_summary',
#             'objects': http.request.env['milestones_time_summary.milestones_time_summary'].search([]),
#         })

#     @http.route('/milestones_time_summary/milestones_time_summary/objects/<model("milestones_time_summary.milestones_time_summary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('milestones_time_summary.object', {
#             'object': obj
#         })
