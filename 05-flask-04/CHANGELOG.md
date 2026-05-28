# Changelog

## v1.0.0

- Implementación inicial del proyecto Smart Home
- Arquitectura por capas
- Gestión de habitaciones
- Gestión de sensores y actuadores
- Persistencia en memoria
- Menú por consola


## v2.0.0

- Añadidos tests unitarios
- Añadida documentación
- Añadido soporte coverage
- Refactorización Clean Architecture


## v3.0.0

- Integración SQLite
- Persistencia
- CRUD completo

## v4.0.0

- Integración Flask
- API REST
- Rutas para dispositivos


## v4.1.0

- Añadidos handlers 404 y 500
- Añadida ruta /ayuda
- Añadido logging HTTP
- Añadido before_request
- Añadido smarthome.log
- Añadido .gitignore para logs


## v4.2.0

- Integradas plantillas Jinja2
- Añadida herencia de plantillas con base.html
- Añadida navegación común en todas las páginas
- Sustituido HTML inline por render_template()
- Añadidas plantillas para habitaciones, ayuda y errores
- Añadida plantilla común error.html para errores 404 y 500
- Integrado uso de url_for() en plantillas
- Añadida carpeta templates para vistas Flask
