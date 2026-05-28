# Ejecución

## Requisitos

- Python 3.10 o superior

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Crear base de datos

```bash
python crear_bd.py
```

## Ejecutar Flask

```bash
python -m interfaces.web.app
```

## Ejecutar tests

```bash
python -m unittest
```

## Acceso navegador

```text
http://127.0.0.1:5000
```

# API REST

| Ruta | Método | Descripción |
|---|---|---|
| /api/habitaciones | GET | Lista habitaciones |
| /api/habitaciones/<nombre> | GET | Detalle habitación |

## Ejemplo colección

```text
GET /api/habitaciones
```

## Ejemplo detalle

```text
GET /api/habitaciones/Dormitorio
```

## Error API

```json
{
  "error": "Habitación 'NO_EXISTE' no encontrada"
}
```

## Flash messages

La aplicación usa:

```python
flash(...)
```

para mostrar mensajes tras redirects POST.

# Rutas GET

| Ruta | Método | Descripción |
|---|---|---|
| / | GET | Inicio |
| /habitaciones | GET | Listar habitaciones |
| /dispositivos/<habitacion> | GET | Listar dispositivos |
| /ayuda | GET | Mostrar rutas |
| /habitaciones/crear | GET | Formulario crear habitación |
| /sensor/crear | GET | Formulario crear sensor |
| /actuador/crear | GET | Formulario crear actuador |
| /habitaciones/eliminar/<nombre> | GET | Confirmar eliminación habitación |
| /dispositivo/eliminar/<habitacion>/<nombre> | GET | Confirmar eliminación dispositivo |

# Rutas POST

| Ruta | Método | Descripción |
|---|---|---|
| /habitaciones/crear | POST | Crear habitación |
| /sensor/crear | POST | Crear sensor |
| /actuador/crear | POST | Crear actuador |
| /habitaciones/eliminar/<nombre> | POST | Eliminar habitación |
| /dispositivo/eliminar/<habitacion>/<nombre> | POST | Eliminar dispositivo |
| /actuador/activar/<habitacion>/<nombre> | POST | Activar actuador |
| /actuador/desactivar/<habitacion>/<nombre> | POST | Desactivar actuador |

## Plantillas

Las plantillas HTML están en:

```text
interfaces/web/templates/
```

y extienden de:

```text
base.html
```

## Ruta ayuda

```text
/ayuda
```

muestra dinámicamente todas las rutas registradas.

## Logging

Las peticiones HTTP se registran en:

```text
smarthome.log
```