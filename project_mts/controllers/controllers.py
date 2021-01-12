# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectMts(http.Controller):
#     @http.route('/project_mts/project_mts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_mts/project_mts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_mts.listing', {
#             'root': '/project_mts/project_mts',
#             'objects': http.request.env['project_mts.project_mts'].search([]),
#         })

#     @http.route('/project_mts/project_mts/objects/<model("project_mts.project_mts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_mts.object', {
#             'object': obj
#         })
