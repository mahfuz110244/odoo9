# -*- coding: utf-8 -*-
{
    'name': "booktrip",

    'summary': """
        Booking for oslobuss""",

    'description': """
        Booking for oslobuss
    """,

    'author': "Mahfuzur Rahman Khan, Brainstation-23 LTD",
    'website': "http://www.brainstation-23.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}