from domain.repositories.edificio_repository import EdificioRepository


class EdificioRepositoryMemory(EdificioRepository):
    def __init__(self):
        self.edificio = None


    def guardar(self, edificio):
        self.edificio = edificio


    def obtener(self):
        return self.edificio