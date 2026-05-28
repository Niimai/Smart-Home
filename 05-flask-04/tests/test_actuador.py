import unittest

from domain.entities.actuador import Actuador

from domain.exceptions import (
    NombreInvalidoError
)


class TestActuador(unittest.TestCase):

    def test_estado_inicial_apagado(self):

        actuador = Actuador("Luz")

        self.assertFalse(
            actuador.estado
        )

    def test_activar_actuador(self):

        actuador = Actuador("Luz")

        actuador.activar()

        self.assertTrue(
            actuador.estado
        )

    def test_desactivar_actuador(self):

        actuador = Actuador("Luz")

        actuador.activar()

        actuador.desactivar()

        self.assertFalse(
            actuador.estado
        )

    def test_nombre_heredado(self):

        actuador = Actuador("Ventilador")

        self.assertEqual(
            actuador.nombre,
            "Ventilador"
        )

    def test_nombre_invalido(self):

        with self.assertRaises(
            NombreInvalidoError
        ):

            Actuador("")


if __name__ == "__main__":
    unittest.main()