class Edificio:
    def __init__(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del edificio no puede estar vacío.")
        self.nombre = nombre

    # El repo se encargará de almacenar habitaciones y dispositivos

    def validar_nombre_unico(self, nombre_nuevo, nombres_existentes):
        if nombre_nuevo in nombres_existentes:
            raise ValueError("Ya existe un elemento con ese nombre.")