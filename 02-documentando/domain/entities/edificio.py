class Edificio:
    def __init__(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del edificio no puede estar vacío.")
        self.nombre = nombre

    # Validación de duplicados
    def validar_nombre_unico(self, nombre_nuevo, existentes):
        if nombre_nuevo in existentes:
            raise ValueError("El nombre ya existe.")

    # Búsqueda movida al dominio (como pidió el profesor)
    def buscar_habitacion(self, nombre_habitacion, lista_habitaciones):
        return next((h for h in lista_habitaciones if h.nombre == nombre_habitacion), None)