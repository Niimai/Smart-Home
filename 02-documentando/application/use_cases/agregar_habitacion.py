from domain.entities.habitacion import Habitacion

class AgregarHabitacionUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion):
        edificio = self.repo.obtener_edificio()
        if not edificio:
            raise Exception("El edificio no está inicializado.")

        # Validación de duplicados en dominio
        nombres_existentes = [h.nombre for h in self.repo.listar_habitaciones()]
        edificio.validar_nombre_unico(nombre_habitacion, nombres_existentes)

        habitacion = Habitacion(nombre_habitacion)
        self.repo.agregar_habitacion(habitacion)
        return habitacion