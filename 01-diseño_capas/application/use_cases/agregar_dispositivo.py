from domain.entities.sensor import Sensor
from domain.entities.actuador import Actuador


class AgregarDispositivoUseCase:
    def __init__(self, repo):
        self.repo = repo


    def ejecutar(self, nombre_habitacion, tipo, nombre_dispositivo):
        edificio = self.repo.obtener()
        if edificio is None:
            raise Exception("No hay un edificio creado.")


        # Buscar habitación
        hab = next((h for h in edificio.habitaciones if h.nombre == nombre_habitacion), None)
        if hab is None:
            raise Exception("La habitación no existe.")


        # Crear dispositivo según tipo
        if tipo == "sensor":
            dispositivo = Sensor(nombre_dispositivo, "sensor")
        elif tipo == "actuador":
            dispositivo = Actuador(nombre_dispositivo, "actuador")
        else:
            raise Exception("Tipo de dispositivo no válido.")


        hab.agregar_dispositivo(dispositivo)
        return dispositivo