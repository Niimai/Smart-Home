class Habitacion:

    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre de una habitación no puede estar vacío.")

        self._nombre = valor

    def __str__(self):
        return self.nombre