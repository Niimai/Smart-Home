import sqlite3

from domain.repositories.edificio_repository import (
    EdificioRepository
)

from domain.entities.habitacion import Habitacion
from domain.entities.sensor import Sensor
from domain.entities.actuador import Actuador

from infrastructure.errores import (
    HabitacionYaExisteError,
    HabitacionNoEncontradaError,
    DispositivoYaExisteError,
    ErrorPersistencia
)


class EdificioRepositorySQLite(EdificioRepository):

    def __init__(self, db_path="smarthome.db"):

        self._db_path = db_path

    
    # Conexión
    def _conectar(self):

        conn = sqlite3.connect(self._db_path)

        conn.execute("PRAGMA foreign_keys = ON")

        return conn


    # Habitaciones
    def agregar_habitacion(self, habitacion):

        conn = self._conectar()

        try:

            with conn:

                cursor = conn.cursor()

                cursor.execute(

                    """
                    INSERT INTO habitaciones (nombre)
                    VALUES (?)
                    """,

                    (habitacion.nombre,)
                )

        except sqlite3.IntegrityError as e:

            raise HabitacionYaExisteError(
                f"La habitación '{habitacion.nombre}' ya existe."
            ) from e

        except sqlite3.OperationalError as e:

            raise ErrorPersistencia(
                f"Error al guardar habitación: {e}"
            ) from e

        finally:
            conn.close()

    def listar_habitaciones(self):

        conn = self._conectar()

        try:

            cursor = conn.cursor()

            cursor.execute(
                "SELECT nombre FROM habitaciones"
            )

            habitaciones = []

            for fila in cursor.fetchall():

                habitaciones.append(
                    Habitacion(fila[0])
                )

            return habitaciones

        except sqlite3.OperationalError as e:

            raise ErrorPersistencia(
                f"Error al listar habitaciones: {e}"
            ) from e

        finally:
            conn.close()


    # Dispositivos
    def agregar_dispositivo(self, habitacion, dispositivo):

        if isinstance(dispositivo, Sensor):

            tipo = "SENSOR"
            estado = None

        elif isinstance(dispositivo, Actuador):

            tipo = "ACTUADOR"
            estado = 1 if dispositivo.estado else 0

        else:

            raise ValueError(
                "Tipo de dispositivo desconocido."
            )

        conn = self._conectar()

        try:

            with conn:

                cursor = conn.cursor()

                cursor.execute(

                    """
                    INSERT INTO dispositivos
                    (nombre, habitacion_nombre, tipo, estado)

                    VALUES (?, ?, ?, ?)
                    """,

                    (
                        dispositivo.nombre,
                        habitacion.nombre,
                        tipo,
                        estado
                    )
                )

        except sqlite3.IntegrityError as e:

            raise DispositivoYaExisteError(
                f"El dispositivo '{dispositivo.nombre}' ya existe."
            ) from e

        except sqlite3.OperationalError as e:

            raise ErrorPersistencia(
                f"Error al guardar dispositivo: {e}"
            ) from e

        finally:
            conn.close()

    def listar_dispositivos(self, habitacion):

        conn = self._conectar()

        try:

            cursor = conn.cursor()

            cursor.execute(

                """
                SELECT nombre, tipo, estado
                FROM dispositivos

                WHERE habitacion_nombre = ?
                """,

                (habitacion.nombre,)
            )

            dispositivos = []

            for nombre, tipo, estado in cursor.fetchall():

                if tipo == "SENSOR":

                    dispositivos.append(
                        Sensor(nombre)
                    )

                elif tipo == "ACTUADOR":

                    actuador = Actuador(nombre)

                    actuador.estado = (
                        bool(estado)
                        if estado is not None
                        else False
                    )

                    dispositivos.append(actuador)

            return dispositivos

        except sqlite3.OperationalError as e:

            raise ErrorPersistencia(
                f"Error al listar dispositivos: {e}"
            ) from e

        finally:
            conn.close()


    # Actualizar estado actuador
    def actualizar_estado_actuador(
        self,
        habitacion,
        actuador
    ):

        conn = self._conectar()

        try:

            with conn:

                cursor = conn.cursor()

                cursor.execute(

                    """
                    UPDATE dispositivos

                    SET estado = ?

                    WHERE habitacion_nombre = ?
                    AND nombre = ?
                    """,

                    (
                        1 if actuador.estado else 0,
                        habitacion.nombre,
                        actuador.nombre
                    )
                )

        except sqlite3.OperationalError as e:

            raise ErrorPersistencia(
                f"Error al actualizar actuador: {e}"
            ) from e

        finally:
            conn.close()