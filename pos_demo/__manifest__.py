# -*- coding: utf-8 -*-
{
    'name': "POS demo",
    'summary': "Point of sale demo module",
    'description': """Long description""",
    'author': "Parth Gajjar",
    'website': "https://www.odoo.com",
    'category': 'Point of Sale',
    'version': '14.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets.xml'
    ],
    'qweb': [
        'static/src/xml/pos_demo.xml'
    ]
}