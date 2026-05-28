import logging

from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    flash,
    jsonify
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

app.secret_key = "smart-home-secret"

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

    return render_template(

        "error.html",

        codigo=404,

        mensaje="Página no encontrada"
    ), 404


@app.errorhandler(500)
def error_500(error):

    return render_template(

        "error.html",

        codigo=500,

        mensaje="Error interno del servidor"
    ), 500


# AYUDA
@app.route("/ayuda")
def ayuda():

    rutas = []

    for rule in app.url_map.iter_rules():

        if rule.endpoint != "static":

            rutas.append({

                "ruta": str(rule),

                "metodos":
                    ", ".join(rule.methods)
            })

    return render_template(

        "ayuda.html",

        rutas=rutas
    )


# HOME
@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# HABITACIONES
@app.route("/habitaciones")
def listar_habitaciones():

    habitaciones = servicio.listar_habitaciones()

    return render_template(

        "habitaciones.html",

        habitaciones=habitaciones
    )


@app.route("/habitaciones/crear", methods=["GET", "POST"])
def crear_habitacion():

    error = None

    nombre = ""

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        )

        try:

            servicio.agregar_habitacion(
                nombre
            )

            flash("Habitación creada correctamente", "exito")

            return redirect(
                url_for(
                    "listar_habitaciones"
                )
            )

        except NombreInvalidoError as e:

            error = str(e)

            return render_template(

                "crear_habitacion.html",

                error=error,

                nombre=nombre

            ), 400

        except HabitacionYaExisteError as e:

            error = str(e)

            return render_template(

                "crear_habitacion.html",

                error=error,

                nombre=nombre

            ), 409

    return render_template(

        "crear_habitacion.html",

        error=error,

        nombre=nombre
    )


@app.route("/habitaciones/eliminar/<nombre>", methods=["GET", "POST"])
def eliminar_habitacion(nombre):

    if request.method == "POST":

        try:

            servicio.eliminar_habitacion(
                nombre
            )

            flash("Habitación eliminada correctamente", "info")

            return redirect(

                url_for(
                    "listar_habitaciones"
                )
            )

        except HabitacionNoEncontradaError as e:

            return render_template(

                "error.html",

                codigo=404,

                mensaje=str(e)

            ), 404

    return render_template(

        "confirmar_eliminar_habitacion.html",

        nombre=nombre
    )


# DISPOSITIVOS
@app.route("/dispositivos/<habitacion>")
def listar_dispositivos(habitacion):

    try:

        dispositivos = servicio.listar_dispositivos(
            habitacion
        )

        return render_template(

            "dispositivos.html",

            habitacion=habitacion,

            dispositivos=dispositivos
        )

    except HabitacionNoEncontradaError as e:

        return render_template(

            "error.html",

            codigo=404,

            mensaje=str(e)

        ), 404


# SENSOR
@app.route("/sensor/crear", methods=["GET", "POST"])
def crear_sensor():

    error = None

    nombre = ""

    habitacion = ""

    habitaciones = servicio.listar_habitaciones()

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        )

        habitacion = request.form.get(
            "habitacion",
            ""
        )

        try:

            servicio.agregar_sensor(

                habitacion,

                nombre
            )

            flash("Sensor creado correctamente", "exito")

            return redirect(

                url_for(

                    "listar_dispositivos",

                    habitacion=habitacion
                )
            )

        except Exception as e:

            error = str(e)

            return render_template(

                "crear_sensor.html",

                error=error,

                nombre=nombre,

                habitacion_actual=habitacion,

                habitaciones=habitaciones

            ), 400

    return render_template(

        "crear_sensor.html",

        error=error,

        nombre=nombre,

        habitacion_actual=habitacion,

        habitaciones=habitaciones
    )


# ACTUADOR
@app.route("/actuador/crear", methods=["GET", "POST"])
def crear_actuador():

    error = None

    nombre = ""

    habitacion = ""

    habitaciones = servicio.listar_habitaciones()

    if request.method == "POST":

        nombre = request.form.get(
            "nombre",
            ""
        )

        habitacion = request.form.get(
            "habitacion",
            ""
        )

        try:

            servicio.agregar_actuador(

                habitacion,

                nombre
            )

            flash("Actuador creado correctamente", "exito")

            return redirect(

                url_for(

                    "listar_dispositivos",

                    habitacion=habitacion
                )
            )

        except Exception as e:

            error = str(e)

            return render_template(

                "crear_actuador.html",

                error=error,

                nombre=nombre,

                habitacion_actual=habitacion,

                habitaciones=habitaciones

            ), 400

    return render_template(

        "crear_actuador.html",

        error=error,

        nombre=nombre,

        habitacion_actual=habitacion,

        habitaciones=habitaciones
    )


@app.route("/actuador/activar/<habitacion>/<nombre>", methods=["POST"])
def activar_actuador(

    habitacion,

    nombre
):

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

@app.route("/actuador/desactivar/<habitacion>/<nombre>", methods=["POST"])
def desactivar_actuador(

    habitacion,

    nombre
):

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


# ELIMINAR DISPOSITIVO
@app.route("/dispositivo/eliminar/<habitacion>/<nombre>", methods=["GET", "POST"])
def eliminar_dispositivo(

    habitacion,

    nombre
):

    if request.method == "POST":

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

    return render_template(

        "confirmar_eliminar_dispositivo.html",

        habitacion=habitacion,

        nombre=nombre
    )


# API REST
@app.route("/api/habitaciones")
def api_habitaciones():

    habitaciones = servicio.listar_habitaciones()

    resultado = []

    for habitacion in habitaciones:

        resultado.append({

            "nombre":
                habitacion.nombre
        })

    return jsonify(resultado)
    

@app.route(
    "/api/habitaciones/<nombre>"
)
def api_habitacion_detalle(nombre):

    try:

        habitaciones = servicio.listar_habitaciones()

        for habitacion in habitaciones:

            if habitacion.nombre == nombre:

                dispositivos = servicio.listar_dispositivos(
                    nombre
                )

                return jsonify({

                    "nombre":
                        habitacion.nombre,

                    "dispositivos": [

                        {

                            "nombre":
                                d.nombre,

                            "tipo":
                                d.__class__.__name__,

                            "estado":
                                getattr(
                                    d,
                                    "estado",
                                    None
                                )

                        }

                        for d in dispositivos
                    ]
                })

        raise HabitacionNoEncontradaError(
            f"Habitación '{nombre}' no encontrada"
        )

    except HabitacionNoEncontradaError as e:

        return jsonify({

            "error":
                str(e)

        }), 404    


# MAIN
if __name__ == "__main__":

    app.run()