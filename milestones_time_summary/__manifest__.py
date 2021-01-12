# -*- coding: utf-8 -*-
{
    'name': "Project Milestones Time Summary",

    'summary': """
        Agrega la columna hotas planeadas a los hitos""",

    'description': """
        Crear un módulo llamado “Project Milestones Time Summary” que muestre una columna llamada “Time Summary” o “Horas planeadas” en la página
        En esta columna por cada hito se debe mostrar la sumatoria de los tiempos definidos en las tareas asociadas al hito.
    """,

    'author': "Ernesto Ruiz Rodriguez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project_milestone', 'project_task_timer'],

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
