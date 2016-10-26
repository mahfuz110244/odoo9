# -*- coding: utf-8 -*-

from openerp import models, fields, api

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