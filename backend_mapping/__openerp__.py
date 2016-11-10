# -*- coding: utf-8 -*-
{
    'name': "backend_mapping",
    'summary': """
         Anbindung der Access Datenbank an Odoo""",

    'description': """
        Die Access Tabellen werden an das Odoo-Framework angebunden. 
    """,

    'author': "HiYa Coding LTD",
    'website': "http://www.hiyacoding.co.uk",
    'icon': "/felix1de_backend/static/description/backend.png",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'felix1de',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'#views/views.xml',
        #'#views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}