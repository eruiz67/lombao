# lombao

Usando la versión Odoo 13:
    • Instalar los módulos:
        ◦ Project (El oficial de Odoo)
        ◦ Project Milestones  
        ◦ Project Task Stage Closed  
        ◦ Add State field to Project Stages
        ◦ Project Status
        ◦ Project Task Timer  
        ◦ Project timeline  
        ◦ Project Timeline - Timesheet 
 https://github.com/OCA/project/tree/13.0/project_milestone
    • Crear un proyecto llamado “Proyecto de Prueba”
    • Agregar 2 hitos:
        ◦ Diseño
        ◦ Desarrollo
    • Crear 4 tareas:
        ◦ Tarea 1 (Duración 2 horas) 
        ◦ Tarea 2 (Duración 4 horas)
        ◦ Tarea 3 (Duración 3 horas)
        ◦ Tarea 4 (Duración 7 horas)
    • Asociar las Tarea 1 y 2 al hito Diseño.
    • Asociar las Tarea 3 y 4 al hito Desarrollo.
Con esta configuración realizada, se debe ver en el listado de proyectos algo parecido a esto:
    1- Editar el proyecto:

    2- Ir a la pestaña Hitos

Debe ver algo como esto:

LA PRUEBA CONSISTE EN:
Crear un módulo llamado “Project Milestones Time Summary” que muestre una columna llamada “Time Summary” o “Horas planeadas” en la página, como se muestra a continuación:

En esta columna por cada hito se debe mostrar la sumatoria de los tiempos definidos en las tareas asociadas al hito.
Se espera que envíe el módulo. Se probará instalando el módulo en un ambiente completamente estéril y en uno ya funcionando con otros módulos.
