import logging

from flask import (
    Flask,
    redirect,
    url_for,
    jsonify,
    request
)

from application.services.smart_home_service import (
    ServicioSmartHome
)

from infrastructure.repositories.edificio_repository_sqlite import (
    EdificioRepositorySQLite
)

from domain.exceptions import (
    NombreInvalidoError,
    DispositivoDuplicadoError
)

from infrastructure.errores import (
    HabitacionYaExisteError,
    HabitacionNoEncontradaError,
    DispositivoYaExisteError
)


# LOGGING
logging.basicConfig(

    filename="smarthome.log",

    level=logging.INFO,

    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)


# APP
app = Flask(__name__)

repo = EdificioRepositorySQLite()

servicio = ServicioSmartHome(repo)


# BEFORE REQUEST
@app.before_request
def log_request():

    logging.info(
        f"{request.method} {request.path}"
    )


# ERROR HANDLERS
@app.errorhandler(404)
def error_404(error):

    return """

    <h1>404 - Página no encontrada</h1>

    <p>
        La ruta solicitada no existe.
    </p>

    <a href="/">
        Volver al inicio
    </a>

    """, 404


@app.errorhandler(500)
def error_500(error):

    return """

    <h1>500 - Error interno</h1>

    <p>
        Ha ocurrido un error inesperado.
    </p>

    <a href="/">
        Volver al inicio
    </a>

    """, 500


# AYUDA
@app.route("/ayuda")
def ayuda():

    rutas = []

    for rule in app.url_map.iter_rules():

        if rule.endpoint != "static":

            rutas.append({

                "ruta": str(rule),

                "metodos":
                    list(rule.methods)
            })

    return jsonify(rutas)


# HOME
@app.route("/")
def home():

    return {

        "mensaje": "Bienvenido a Smart Home API",

        "rutas_principales": {

            "ayuda":
                "/ayuda",

            "habitaciones":
                "/habitaciones",

            "crear_habitacion":
                "/habitaciones/crear/<nombre>",

            "eliminar_habitacion":
                "/habitaciones/eliminar/<nombre>",

            "dispositivos":
                "/dispositivos/<habitacion>",

            "crear_sensor":
                "/sensor/crear/<habitacion>/<nombre>",

            "crear_actuador":
                "/actuador/crear/<habitacion>/<nombre>"
        }
    }


# HABITACIONES
@app.route("/habitaciones")
def listar_habitaciones():

    habitaciones = servicio.listar_habitaciones()

    return jsonify([

        {
            "nombre": h.nombre
        }

        for h in habitaciones
    ])


@app.route("/habitaciones/crear/<nombre>")
def crear_habitacion(nombre):

    try:

        servicio.agregar_habitacion(nombre)

        return redirect(
            url_for("listar_habitaciones")
        )

    except NombreInvalidoError as e:

        return {"error": str(e)}, 400

    except HabitacionYaExisteError as e:

        return {"error": str(e)}, 409


@app.route("/habitaciones/eliminar/<nombre>")
def eliminar_habitacion(nombre):

    try:

        servicio.eliminar_habitacion(nombre)

        return redirect(
            url_for("listar_habitaciones")
        )

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404


# DISPOSITIVOS
@app.route("/dispositivos/<habitacion>")
def listar_dispositivos(habitacion):

    try:

        dispositivos = servicio.listar_dispositivos(
            habitacion
        )

        return jsonify([

            {
                "tipo":
                    d.__class__.__name__,

                "nombre":
                    d.nombre,

                "estado":
                    getattr(d, "estado", None)
            }

            for d in dispositivos
        ])

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404


# SENSOR
@app.route("/sensor/crear/<habitacion>/<nombre>")
def crear_sensor(habitacion, nombre):

    try:

        servicio.agregar_sensor(
            habitacion,
            nombre
        )

        return redirect(

            url_for(
                "listar_dispositivos",
                habitacion=habitacion
            )
        )

    except NombreInvalidoError as e:

        return {"error": str(e)}, 400

    except (
        DispositivoDuplicadoError,
        DispositivoYaExisteError
    ) as e:

        return {"error": str(e)}, 409

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404



# ACTUADOR
@app.route("/actuador/crear/<habitacion>/<nombre>")
def crear_actuador(habitacion, nombre):

    try:

        servicio.agregar_actuador(
            habitacion,
            nombre
        )

        return redirect(

            url_for(
                "listar_dispositivos",
                habitacion=habitacion
            )
        )

    except NombreInvalidoError as e:

        return {"error": str(e)}, 400

    except (
        DispositivoDuplicadoError,
        DispositivoYaExisteError
    ) as e:

        return {"error": str(e)}, 409

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404


@app.route(
    "/actuador/activar/<habitacion>/<nombre>"
)
def activar_actuador(habitacion, nombre):

    try:

        servicio.activar_actuador(
            habitacion,
            nombre
        )

        return redirect(

            url_for(
                "listar_dispositivos",
                habitacion=habitacion
            )
        )

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404


@app.route(
    "/actuador/desactivar/<habitacion>/<nombre>"
)
def desactivar_actuador(habitacion, nombre):

    try:

        servicio.desactivar_actuador(
            habitacion,
            nombre
        )

        return redirect(

            url_for(
                "listar_dispositivos",
                habitacion=habitacion
            )
        )

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404


# ELIMINAR DISPOSITIVO
@app.route(
    "/dispositivo/eliminar/<habitacion>/<nombre>"
)
def eliminar_dispositivo(habitacion, nombre):

    try:

        servicio.eliminar_dispositivo(
            habitacion,
            nombre
        )

        return redirect(

            url_for(
                "listar_dispositivos",
                habitacion=habitacion
            )
        )

    except HabitacionNoEncontradaError as e:

        return {"error": str(e)}, 404



# RUTA TEMPORAL ERROR 500
@app.route("/error")
def provocar_error():

    raise Exception(
        "Error de prueba"
    )


# MAIN
if __name__ == "__main__":

    app.run()