class EdificioRepository:

    # Edificio
    def guardar_edificio(self, edificio):
        raise NotImplementedError

    def obtener_edificio(self):
        raise NotImplementedError

    # Habitaciones
    def agregar_habitacion(self, habitacion):
        raise NotImplementedError

    def listar_habitaciones(self):
        raise NotImplementedError

    # Dispositivos
    def agregar_dispositivo(self, habitacion, dispositivo):
        raise NotImplementedError

    def listar_dispositivos(self, habitacion):
        raise NotImplementedError