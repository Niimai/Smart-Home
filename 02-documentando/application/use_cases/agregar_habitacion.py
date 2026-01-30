from domain.entities.habitacion import Habitacion


class AgregarHabitacionUseCase:
    def __init__(self, repo):
        self.repo = repo


    def ejecutar(self, nombre_habitacion):
        edificio = self.repo.obtener()
        if edificio is None:
            raise Exception("No hay un edificio creado todavía.")


        habitacion = Habitacion(nombre_habitacion)
        edificio.agregar_habitacion(habitacion)
        return habitacion