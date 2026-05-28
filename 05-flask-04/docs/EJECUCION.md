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

## Carpeta de plantillas

Las plantillas HTML Flask se encuentran en:

```text
interfaces/web/templates/
```

## Plantilla base

La aplicación utiliza:

```text
base.html
```

como plantilla principal compartida.

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