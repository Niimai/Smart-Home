import unittest

from domain.entities.habitacion import Habitacion


class TestHabitacion(unittest.TestCase):


    # Creación correcta
    def test_crear_habitacion_valida(self):

        habitacion = Habitacion("Dormitorio")

        self.assertEqual(habitacion.nombre, "Dormitorio")


    # Nombre vacío
    def test_nombre_vacio_lanza_error(self):

        with self.assertRaises(ValueError):

            Habitacion("")


    # Nombre espacios
    def test_nombre_espacios_lanza_error(self):

        with self.assertRaises(ValueError):

            Habitacion("   ")


    # Setter válido
    def test_modificar_nombre_valido(self):

        habitacion = Habitacion("Dormitorio")

        habitacion.nombre = "Salón"

        self.assertEqual(habitacion.nombre, "Salón")


    # Setter inválido
    def test_modificar_nombre_invalido(self):

        habitacion = Habitacion("Dormitorio")

        with self.assertRaises(ValueError):

            habitacion.nombre = ""


if __name__ == "__main__":
    unittest.main()