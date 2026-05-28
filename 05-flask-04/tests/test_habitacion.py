import unittest

from domain.entities.habitacion import Habitacion

from domain.exceptions import (
    NombreInvalidoError,
    DispositivoDuplicadoError
)


class DummyDispositivo:

    def __init__(self, nombre):
        self.nombre = nombre


class TestHabitacion(unittest.TestCase):

    def test_crear_habitacion_valida(self):

        habitacion = Habitacion("Dormitorio")

        self.assertEqual(
            habitacion.nombre,
            "Dormitorio"
        )

    def test_nombre_vacio_lanza_error(self):

        with self.assertRaises(NombreInvalidoError):

            Habitacion("")

    def test_nombre_espacios_lanza_error(self):

        with self.assertRaises(NombreInvalidoError):

            Habitacion("   ")

    def test_modificar_nombre_valido(self):

        habitacion = Habitacion("Dormitorio")

        habitacion.nombre = "Salón"

        self.assertEqual(
            habitacion.nombre,
            "Salón"
        )

    def test_modificar_nombre_invalido(self):

        habitacion = Habitacion("Dormitorio")

        with self.assertRaises(NombreInvalidoError):

            habitacion.nombre = ""

    def test_dispositivo_duplicado(self):

        habitacion = Habitacion("Dormitorio")

        dispositivos = [
            DummyDispositivo("Sensor1")
        ]

        with self.assertRaises(
            DispositivoDuplicadoError
        ):

            habitacion.validar_dispositivo_no_duplicado(
                "Sensor1",
                dispositivos
            )


if __name__ == "__main__":
    unittest.main()