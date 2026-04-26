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

        dispositivos = self.repo.listar_dispositivos(hab)

        # ✔ Dominio decide duplicados
        edificio.validar_dispositivo_no_duplicado(nombre_sensor, dispositivos)

        sensor = Sensor(nombre_sensor)
        self.repo.agregar_dispositivo(hab, sensor)
        return sensor