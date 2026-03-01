from domain.entities.actuador import Actuador

class AgregarActuadorUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_actuador):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        hab = edificio.buscar_habitacion(nombre_habitacion, habitaciones)
        if not hab:
            raise ValueError("La habitación no existe.")

        dispositivos = [d.nombre for d in self.repo.listar_dispositivos(hab)]
        edificio.validar_nombre_unico(nombre_actuador, dispositivos)

        actuador = Actuador(nombre_actuador)
        self.repo.agregar_dispositivo(hab, actuador)
        return actuador