from infrastructure.repositories.edificio_repository_memory import EdificioRepositoryMemory
from application.use_cases.crear_edificio import CrearEdificioUseCase
from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase
from application.use_cases.agregar_dispositivo import AgregarDispositivoUseCase
from interfaces.cli.menu import MenuCLI


def main():
    repo = EdificioRepositoryMemory()
    crear_edificio_uc = CrearEdificioUseCase(repo)
    agregar_habitacion_uc = AgregarHabitacionUseCase(repo)
    agregar_dispositivo_uc = AgregarDispositivoUseCase(repo)


    menu = MenuCLI(crear_edificio_uc, agregar_habitacion_uc, agregar_dispositivo_uc, repo)
    menu.mostrar()


if __name__ == "__main__":
    main()