# -*- coding: utf-8 -*-
# © 2014-2016 Akretion (http://www.akretion.com)
#   @author Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Fast products quantity search',
    'summary': """Currently search product by quantity is verry slow. We this module search tieme is divided by ~ 200. When we
        have 80K product, search product by quantity take ~ 6.6 mn (400 second). So odoo, compute quantities for each product and make filter in python site. With this module product are filtred in one SQL request execute in 2 seconds. 
        Whe""",
    'version': '8.0.0.1.0',
    'author': "Akretion,Odoo Community Association (OCA)",
    'website': 'http://www.akretion.com',
    'category': 'Warehouse',
    'depends': [
        'stock',
        'product',
    ],
    'data': [
    ],
    'application': False,
    'installable': True,
}
