from domain.entities.edificio import Edificio
from infrastructure.repositories.edificio_repository_memory import EdificioRepositoryMemory

from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase
from application.use_cases.agregar_sensor import AgregarSensorUseCase
from application.use_cases.agregar_actuador import AgregarActuadorUseCase

from interfaces.cli.menu import MenuCLI


def main():
    # Repositorio en memoria
    repo = EdificioRepositoryMemory()

    # Crear edificio automáticamente AL INICIAR
    edificio = Edificio("Mi Casa Inteligente")
    repo.guardar_edificio(edificio)

    # Casos de uso
    agregar_habitacion_uc = AgregarHabitacionUseCase(repo)
    agregar_sensor_uc = AgregarSensorUseCase(repo)
    agregar_actuador_uc = AgregarActuadorUseCase(repo)

    # Interfaz de usuario (menú)
    menu = MenuCLI(
        agregar_habitacion_uc,
        agregar_sensor_uc,
        agregar_actuador_uc,
        repo   # el menú solo LEE datos, no aplica reglas
    )

    # Iniciar aplicación
    menu.mostrar()


if __name__ == "__main__":
    main()