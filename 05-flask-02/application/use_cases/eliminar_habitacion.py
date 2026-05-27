class EliminarHabitacionUseCase:

    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):

        habitaciones = self.repo.listar_habitaciones()

        habitacion = next(

            (
                h for h in habitaciones
                if h.nombre == nombre_habitacion
            ),

            None
        )

        if not habitacion:
            raise ValueError("La habitación no existe.")

        self.repo.eliminar_habitacion(habitacion)