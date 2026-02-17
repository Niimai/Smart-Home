from domain.entities.sensor import Sensor

class AgregarSensorUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_sensor):
        hab = self.repo.buscar_habitacion(nombre_habitacion)
        if not hab:
            raise ValueError("La habitación no existe.")

        sensores = [d.nombre for d in self.repo.listar_dispositivos(hab)]
        edificio = self.repo.obtener_edificio()
        edificio.validar_nombre_unico(nombre_sensor, sensores)

        sensor = Sensor(nombre_sensor)
        self.repo.agregar_dispositivo(hab, sensor)
        return sensor