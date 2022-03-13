# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderAlbertusDa(http.Controller):
#     @http.route('/booking_order__albertus_da/booking_order__albertus_da/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__albertus_da/booking_order__albertus_da/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__albertus_da.listing', {
#             'root': '/booking_order__albertus_da/booking_order__albertus_da',
#             'objects': http.request.env['booking_order__albertus_da.booking_order__albertus_da'].search([]),
#         })

#     @http.route('/booking_order__albertus_da/booking_order__albertus_da/objects/<model("booking_order__albertus_da.booking_order__albertus_da"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__albertus_da.object', {
#             'object': obj
#         })
