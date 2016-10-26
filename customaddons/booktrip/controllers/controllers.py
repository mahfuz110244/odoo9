# -*- coding: utf-8 -*-
from openerp import http

# class Booktrip(http.Controller):
#     @http.route('/booktrip/booktrip/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booktrip/booktrip/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booktrip.listing', {
#             'root': '/booktrip/booktrip',
#             'objects': http.request.env['booktrip.booktrip'].search([]),
#         })

#     @http.route('/booktrip/booktrip/objects/<model("booktrip.booktrip"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booktrip.object', {
#             'object': obj
#         })