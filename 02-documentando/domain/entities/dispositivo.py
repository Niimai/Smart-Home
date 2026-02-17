class Dispositivo:
    def __init__(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre de un dispositivo no puede estar vacío.")
        self.nombre = nombre

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}"