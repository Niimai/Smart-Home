class Dispositivo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo


    def __str__(self):
        return f"{self.tipo}: {self.nombre}"