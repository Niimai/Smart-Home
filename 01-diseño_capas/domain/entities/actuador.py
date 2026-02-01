from domain.entities.dispositivo import Dispositivo


class Actuador(Dispositivo):
    def __init__(self, nombre, tipo, estado=False):
        super().__init__(nombre, tipo)
        self.estado = estado


    def activar(self):
        self.estado = True


    def desactivar(self):
        self.estado = False