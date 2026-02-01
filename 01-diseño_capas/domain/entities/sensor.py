from domain.entities.dispositivo import Dispositivo


class Sensor(Dispositivo):
    def __init__(self, nombre, tipo, valor=0):
        super().__init__(nombre, tipo)
        self.valor = valor