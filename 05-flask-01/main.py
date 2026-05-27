from infrastructure.repositories.edificio_repository_sqlite import (
    EdificioRepositorySQLite
)

from application.services.smart_home_service import (
    ServicioSmartHome
)

from interfaces.cli.menu import MenuCLI


def main():

    repo = EdificioRepositorySQLite()

    servicio = ServicioSmartHome(repo)

    menu = MenuCLI(servicio)

    menu.mostrar()


if __name__ == "__main__":
    main()