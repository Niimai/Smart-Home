class EliminarDispositivoUseCase:

    def __init__(self, repo):
        self.repo = repo

    def ejecutar(
        self,
        nombre_habitacion,
        nombre_dispositivo
    ):

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

        dispositivos = self.repo.listar_dispositivos(habitacion)

        dispositivo = next(

            (
                d for d in dispositivos
                if d.nombre == nombre_dispositivo
            ),

            None
        )

        if not dispositivo:
            raise ValueError("El dispositivo no existe.")

        self.repo.eliminar_dispositivo(
            habitacion,
            dispositivo
        )