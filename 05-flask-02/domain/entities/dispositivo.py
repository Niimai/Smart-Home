from domain.exceptions import NombreInvalidoError


class Dispositivo:

    def __init__(self, nombre):

        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        if not valor or valor.strip() == "":

            raise NombreInvalidoError(
                "El nombre del dispositivo no puede estar vacío."
            )

        self._nombre = valor

    def __str__(self):

        return f"{self.__class__.__name__}: {self.nombre}"