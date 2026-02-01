class Habitacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []


    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)