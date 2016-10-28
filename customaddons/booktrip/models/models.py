# -*- coding: utf-8 -*-

from openerp import models, fields, api
import random

class booktrip(models.Model):
    _inherit = 'crm.lead'

    name = fields.Char('Opportunity', required=False)
    travel_from = fields.Char("Travel From")
    travel_to = fields.Char("Travel To")
    round_trip = fields.Boolean("Round Trip")
    single_trip = fields.Boolean("Single Trip")
    trip_status = fields.Char("Trip Status")
    bus_availability = fields.Boolean("Bus Availability")
    travel_date = fields.Char("Travel Date")
    travel_time = fields.Char("Travel Time")
    return_date = fields.Char("Return Date")
    return_time = fields.Char("Return Time")
    no_of_passengers = fields.Integer("No of Passengers")
    catering = fields.Boolean("Want Cheap Catering")
    price_estimation = fields.Float(compute='_compute_price', string='Price Estimation')

    @api.one
    def _compute_price(self):
        # self.price_estimation = 1000
        # print self.price_estimation
        product_id = random.randint(1, 68)
        # product_line_obj = self.pool.get('product.template')
        product_line_obj = self.env['product.template']
        # product_line_ids = product_line_obj.search(self.cr, self.uid, [('id', '=', product_id)])
        product_line_ids = product_line_obj.browse([product_id])
        # product_line_ids = product_line_obj.search(self.cr, self.uid, [('id', '=', product_id)])
        print product_line_ids
        print product_line_ids.list_price
        self.price_estimation = product_line_ids.list_price