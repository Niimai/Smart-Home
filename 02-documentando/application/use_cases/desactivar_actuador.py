from domain.entities.actuador import Actuador

class DesactivarActuadorUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_actuador):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        hab = edificio.buscar_habitacion(nombre_habitacion, habitaciones)
        if not hab:
            raise ValueError("La habitación no existe.")

        dispositivos = self.repo.listar_dispositivos(hab)

        for d in dispositivos:
            if isinstance(d, Actuador) and d.nombre == nombre_actuador:
                d.desactivar()
                return d

        raise ValueError("Actuador no encontrado.")