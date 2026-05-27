import unittest
import sqlite3
from pathlib import Path

from infrastructure.repositories.edificio_repository_sqlite import (
    EdificioRepositorySQLite
)

from domain.entities.habitacion import Habitacion
from domain.entities.sensor import Sensor

from infrastructure.errores import (
    HabitacionYaExisteError,
    DispositivoYaExisteError
)


class TestRepositorySQLite(unittest.TestCase):

    DB_PATH = "test_smarthome.db"

    def setUp(self):

        ruta = Path(self.DB_PATH)

        if ruta.exists():
            ruta.unlink()

        conn = sqlite3.connect(self.DB_PATH)

        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.executescript("""

        CREATE TABLE habitaciones (

            nombre TEXT PRIMARY KEY
        );

        CREATE TABLE dispositivos (

            nombre TEXT NOT NULL,
            habitacion_nombre TEXT NOT NULL,
            tipo TEXT NOT NULL,
            estado INTEGER,

            PRIMARY KEY (habitacion_nombre, nombre),

            FOREIGN KEY (habitacion_nombre)
                REFERENCES habitaciones(nombre)
                ON DELETE CASCADE
        );

        """)

        conn.commit()
        conn.close()

        self.repo = EdificioRepositorySQLite(
            self.DB_PATH
        )

    def tearDown(self):

        ruta = Path(self.DB_PATH)

        if ruta.exists():
            ruta.unlink()


    # Habitaciones
    def test_agregar_habitacion(self):

        habitacion = Habitacion("Dormitorio")

        self.repo.agregar_habitacion(habitacion)

        habitaciones = self.repo.listar_habitaciones()

        self.assertEqual(
            len(habitaciones),
            1
        )

    def test_habitacion_duplicada(self):

        habitacion = Habitacion("Dormitorio")

        self.repo.agregar_habitacion(habitacion)

        with self.assertRaises(
            HabitacionYaExisteError
        ):

            self.repo.agregar_habitacion(habitacion)


    # Dispositivos
    def test_agregar_sensor(self):

        habitacion = Habitacion("Dormitorio")

        self.repo.agregar_habitacion(habitacion)

        sensor = Sensor("Sensor1")

        self.repo.agregar_dispositivo(
            habitacion,
            sensor
        )

        dispositivos = self.repo.listar_dispositivos(
            habitacion
        )

        self.assertEqual(
            len(dispositivos),
            1
        )

    def test_sensor_duplicado(self):

        habitacion = Habitacion("Dormitorio")

        self.repo.agregar_habitacion(habitacion)

        sensor = Sensor("Sensor1")

        self.repo.agregar_dispositivo(
            habitacion,
            sensor
        )

        with self.assertRaises(
            DispositivoYaExisteError
        ):

            self.repo.agregar_dispositivo(
                habitacion,
                sensor
            )


if __name__ == "__main__":
    unittest.main()