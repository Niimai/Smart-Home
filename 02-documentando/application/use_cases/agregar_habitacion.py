from domain.entities.habitacion import Habitacion

class AgregarHabitacionUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        # ✔ El dominio decide todo
        edificio.validar_habitacion_no_duplicada(nombre_habitacion, habitaciones)

        hab = Habitacion(nombre_habitacion)
        self.repo.agregar_habitacion(hab)
        return hab