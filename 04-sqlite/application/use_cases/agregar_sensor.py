from domain.entities.sensor import Sensor


class AgregarSensorUseCase:

    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_sensor):

        habitaciones = self.repo.listar_habitaciones()

        habitacion = next(
            (h for h in habitaciones if h.nombre == nombre_habitacion), None)

        if not habitacion:
            raise ValueError("La habitación no existe.")

        dispositivos = self.repo.listar_dispositivos(habitacion)

        habitacion.validar_dispositivo_no_duplicado(
            nombre_sensor, dispositivos)

        sensor = Sensor(nombre_sensor)

        self.repo.agregar_dispositivo(habitacion, sensor)

        return sensor