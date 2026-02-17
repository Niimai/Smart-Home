from domain.entities.actuador import Actuador

class AgregarActuadorUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_actuador):
        hab = self.repo.buscar_habitacion(nombre_habitacion)
        if not hab:
            raise ValueError("La habitación no existe.")

        dispositivos = [d.nombre for d in self.repo.listar_dispositivos(hab)]
        edificio = self.repo.obtener_edificio()
        edificio.validar_nombre_unico(nombre_actuador, dispositivos)

        actuador = Actuador(nombre_actuador)
        self.repo.agregar_dispositivo(hab, actuador)
        return actuador