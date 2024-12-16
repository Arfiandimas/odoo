# -*- coding: utf-8 -*-
# from odoo import http


# class Arfian(http.Controller):
#     @http.route('/arfian/arfian', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arfian/arfian/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arfian.listing', {
#             'root': '/arfian/arfian',
#             'objects': http.request.env['arfian.arfian'].search([]),
#         })

#     @http.route('/arfian/arfian/objects/<model("arfian.arfian"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arfian.object', {
#             'object': obj
#         })

