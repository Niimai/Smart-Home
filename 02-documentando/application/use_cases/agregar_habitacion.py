from domain.entities.habitacion import Habitacion


class AgregarHabitacionUseCase:

    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):

        habitaciones = self.repo.listar_habitaciones()

        if any(h.nombre == nombre_habitacion for h in habitaciones):
            raise ValueError("La habitación ya existe.")

        habitacion = Habitacion(nombre_habitacion)

        self.repo.agregar_habitacion(habitacion)

        return habitacion