from domain.entities.sensor import Sensor

class AgregarSensorUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_sensor):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        hab = edificio.buscar_habitacion(nombre_habitacion, habitaciones)
        if not hab:
            raise ValueError("La habitación no existe.")

        dispositivos = [d.nombre for d in self.repo.listar_dispositivos(hab)]
        edificio.validar_nombre_unico(nombre_sensor, dispositivos)

        sensor = Sensor(nombre_sensor)
        self.repo.agregar_dispositivo(hab, sensor)
        return sensor