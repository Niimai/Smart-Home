from domain.entities.dispositivo import Dispositivo

class Actuador(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.estado = False

    def activar(self):
        self.estado = True

    def desactivar(self):
        self.estado = False

    def __str__(self):
        estado = "ENCENDIDO" if self.estado else "APAGADO"
        return f"Actuador: {self.nombre} ({estado})"