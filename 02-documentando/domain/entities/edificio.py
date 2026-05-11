class Edificio:

    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del edificio no puede estar vacío.")

        self._nombre = valor

    def validar_habitacion_no_duplicada(self, nombre, habitaciones):
        if any(h.nombre == nombre for h in habitaciones):
            raise ValueError("La habitación ya existe.")

    def validar_dispositivo_no_duplicado(self, nombre, dispositivos):
        if any(d.nombre == nombre for d in dispositivos):
            raise ValueError("El dispositivo ya existe.")

    def buscar_habitacion(self, nombre_habitacion, habitaciones):
        for h in habitaciones:
            if h.nombre == nombre_habitacion:
                return h

        return None

    def __str__(self):
        return self.nombre