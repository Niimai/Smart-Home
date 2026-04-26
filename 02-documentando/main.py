from domain.entities.edificio import Edificio
from infrastructure.repositories.edificio_repository_memory import EdificioRepositoryMemory

from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase
from application.use_cases.agregar_sensor import AgregarSensorUseCase
from application.use_cases.agregar_actuador import AgregarActuadorUseCase
from application.use_cases.listar_habitaciones import ListarHabitacionesUseCase
from application.use_cases.listar_dispositivos import ListarDispositivosUseCase
from application.use_cases.activar_actuador import ActivarActuadorUseCase
from application.use_cases.desactivar_actuador import DesactivarActuadorUseCase
from application.use_cases.consultar_estado import ConsultarEstadoUseCase

from interfaces.cli.menu import MenuCLI


def main():
    repo = EdificioRepositoryMemory()
    edificio = Edificio("Mi Casa Inteligente")
    repo.guardar_edificio(edificio)

    menu = MenuCLI(
        AgregarHabitacionUseCase(repo),
        AgregarSensorUseCase(repo),
        AgregarActuadorUseCase(repo),
        ListarHabitacionesUseCase(repo),
        ListarDispositivosUseCase(repo),
        ActivarActuadorUseCase(repo),
        DesactivarActuadorUseCase(repo),
        ConsultarEstadoUseCase(repo)
    )

    menu.mostrar()


if __name__ == "__main__":
    main()