class ConsultarEstadoUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):
        edificio = self.repo.obtener_edificio()
        habitaciones = self.repo.listar_habitaciones()

        hab = edificio.buscar_habitacion(nombre_habitacion, habitaciones)
        if not hab:
            raise ValueError("La habitación no existe.")

        return self.repo.listar_dispositivos(hab)