class Edificio:
    def __init__(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del edificio no puede estar vacío.")
        self.nombre = nombre

    def validar_habitacion_no_duplicada(self, nombre, habitaciones):
        if any(h.nombre == nombre for h in habitaciones):
            raise ValueError("La habitación ya existe.")

    def validar_dispositivo_no_duplicado(self, nombre, dispositivos):
        if any(d.nombre == nombre for d in dispositivos):
            raise ValueError("El dispositivo ya existe.")

    def buscar_habitacion(self, nombre, habitaciones):
        return next((h for h in habitaciones if h.nombre == nombre), None)