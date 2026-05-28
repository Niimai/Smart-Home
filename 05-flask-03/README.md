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

## Logging

Las peticiones se registran en:

smarthome.log

## Ruta ayuda

La aplicación incluye:

/ayuda
