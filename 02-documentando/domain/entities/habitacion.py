class Habitacion:
    def __init__(self, nombre):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre de una habitación no puede estar vacío.")
        self.nombre = nombre