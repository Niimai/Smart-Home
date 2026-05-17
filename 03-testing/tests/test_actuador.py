import unittest

from domain.entities.actuador import Actuador


class TestActuador(unittest.TestCase):

    # Estado inicial
    def test_estado_inicial_apagado(self):

        actuador = Actuador("Luz")

        self.assertFalse(actuador.estado)

    # Activar
    def test_activar_actuador(self):

        actuador = Actuador("Luz")

        actuador.activar()

        self.assertTrue(actuador.estado)


    # Desactivar
    def test_desactivar_actuador(self):

        actuador = Actuador("Luz")

        actuador.activar()

        actuador.desactivar()

        self.assertFalse(actuador.estado)

  
    # Nombre heredado
    def test_nombre_heredado(self):

        actuador = Actuador("Ventilador")

        self.assertEqual(actuador.nombre, "Ventilador")


if __name__ == "__main__":
    unittest.main()