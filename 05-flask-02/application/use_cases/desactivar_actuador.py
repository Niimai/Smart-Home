from domain.entities.actuador import Actuador


class DesactivarActuadorUseCase:

    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self, nombre_habitacion, nombre_actuador):

        habitaciones = self.repo.listar_habitaciones()

        habitacion = next(
            (h for h in habitaciones if h.nombre == nombre_habitacion), None)

        if not habitacion:
            raise ValueError("La habitación no existe.")

        dispositivos = self.repo.listar_dispositivos(habitacion)

        for d in dispositivos:

            if isinstance(d, Actuador) and d.nombre == nombre_actuador:

                d.desactivar()

                #Guardar en SQLITE
                self.repo.actualizar_estado_actuador(
                    habitacion, d)

                return d

        raise ValueError("Actuador no encontrado.")