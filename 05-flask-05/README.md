# Smart Home

Proyecto académico desarrollado en Python siguiendo principios de Clean Architecture, SQLite y Flask.

## Características

- Gestión de habitaciones
- Gestión de sensores
- Gestión de actuadores
- Arquitectura por capas
- Persistencia SQLite
- API Flask
- Plantillas Jinja2
- Formularios HTML
- Logging HTTP
- Manejo global de errores
- Tests unitarios
- Coverage

## Tecnologías

- Python
- Flask
- SQLite
- Jinja2
- unittest
- coverage

## Estructura

- domain/
- application/
- docs/
- infrastructure/
- interfaces/
- tests/

## Estructura Web

```text
interfaces/
└── web/
    ├── app.py
    └── templates/
        ├── base.html
        ├── index.html
        ├── habitaciones.html
        ├── dispositivos.html
        ├── ayuda.html
        └── error.html
```

## Ejecución

### Crear base de datos

```bash
python crear_bd.py
```

### Ejecutar Flask

```bash
python -m interfaces.web.app
```

## Plantillas

La aplicación usa plantillas Jinja2 con herencia desde:

```text
base.html
```

Todas las páginas comparten navegación común.


## Escrituras HTTP

Las operaciones que modifican estado:

- utilizan POST
- NO utilizan GET
- aplican PRG (Post/Redirect/Get)
- usan confirmación para eliminaciones


## Navegación

La aplicación incluye enlaces y botones HTML para navegar sin escribir URLs manualmente.


## Logging

Las peticiones se registran en:

smarthome.log


## Ruta ayuda

La aplicación incluye:

/ayuda
