class ListarHabitacionesUseCase:
    def __init__(self, repo):
        self.repo = repo

    def ejecutar(self):
        return self.repo.listar_habitaciones()