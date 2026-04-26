from domain.entities.edificio import Edificio
from infrastructure.repositories.edificio_repository_memory import EdificioRepositoryMemory

from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase
from application.use_cases.agregar_sensor import AgregarSensorUseCase
from application.use_cases.agregar_actuador import AgregarActuadorUseCase
from application.use_cases.listar_habitaciones import ListarHabitacionesUseCase
from application.use_cases.listar_dispositivos import ListarDispositivosUseCase

from interfaces.cli.menu import MenuCLI


def main():
    repo = EdificioRepositoryMemory()

    edificio = Edificio("Mi Casa Inteligente")
    repo.guardar_edificio(edificio)

    # Casos de uso
    agregar_habitacion_uc = AgregarHabitacionUseCase(repo)
    agregar_sensor_uc = AgregarSensorUseCase(repo)
    agregar_actuador_uc = AgregarActuadorUseCase(repo)
    listar_habitaciones_uc = ListarHabitacionesUseCase(repo)
    listar_dispositivos_uc = ListarDispositivosUseCase(repo)

    menu = MenuCLI(
        agregar_habitacion_uc,
        agregar_sensor_uc,
        agregar_actuador_uc,
        listar_habitaciones_uc,
        listar_dispositivos_uc
    )

    menu.mostrar()


if __name__ == "__main__":
    main()