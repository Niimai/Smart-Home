class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []


    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)


    def listar_habitaciones(self):
        return self.habitaciones