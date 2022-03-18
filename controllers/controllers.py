# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderAlbert(http.Controller):
#     @http.route('/booking_order_albert/booking_order_albert/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order_albert/booking_order_albert/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order_albert.listing', {
#             'root': '/booking_order_albert/booking_order_albert',
#             'objects': http.request.env['booking_order_albert.booking_order_albert'].search([]),
#         })

#     @http.route('/booking_order_albert/booking_order_albert/objects/<model("booking_order_albert.booking_order_albert"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order_albert.object', {
#             'object': obj
#         })
