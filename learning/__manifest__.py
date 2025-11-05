# -*- coding: utf-8 -*-
{
    'name': "learning",

    'summary': "Modulo para gestionar alumnos",

    'description': """
Modulo para gestionar alumnos
    """,

    'author': "Vinicius Maruyama",
    'website': "https://www.edyma.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '18.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/course_views.xml',
        'views/menu_itens.xml'
    ],
    # only loaded in demonstration mode
}

