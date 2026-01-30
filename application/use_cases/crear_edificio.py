from domain.entities.edificio import Edificio


class CrearEdificioUseCase:
    def __init__(self, repo):
        self.repo = repo


    def ejecutar(self, nombre):
        edificio = Edificio(nombre)
        self.repo.guardar(edificio)
        return edificio