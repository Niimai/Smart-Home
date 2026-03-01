from domain.entities.habitacion import Habitacion

class AgregarHabitacionUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        # Validación en dominio
        nombres = [h.nombre for h in habitaciones]
        edificio.validar_nombre_unico(nombre_habitacion, nombres)

        hab = Habitacion(nombre_habitacion)
        self.repo.agregar_habitacion(hab)
        return hab