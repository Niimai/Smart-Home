from domain.entities.edificio import Edificio

from infrastructure.repositories.edificio_repository_memory import (
    EdificioRepositoryMemory
)

from application.services.smart_home_service import ServicioSmartHome

from interfaces.cli.menu import MenuCLI


def main():

    repo = EdificioRepositoryMemory()

    edificio = Edificio("Mi Casa Inteligente")

    repo.guardar_edificio(edificio)

    # Servicio de aplicación
    servicio = ServicioSmartHome(repo)

    # Menú
    menu = MenuCLI(servicio)

    menu.mostrar()


if __name__ == "__main__":
    main()