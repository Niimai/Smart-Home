class EdificioRepository:

    
    # Habitaciones
    def agregar_habitacion(self, habitacion):
        raise NotImplementedError

    def listar_habitaciones(self):
        raise NotImplementedError

    def eliminar_habitacion(self, habitacion):
        raise NotImplementedError

    # Dispositivos
    def agregar_dispositivo(self, habitacion, dispositivo):
        raise NotImplementedError

    def listar_dispositivos(self, habitacion):
        raise NotImplementedError

    def eliminar_dispositivo(
        self,
        habitacion,
        dispositivo
    ):
        raise NotImplementedError

    # Actuadores
    def actualizar_estado_actuador(
        self,
        habitacion,
        actuador
    ):
        raise NotImplementedError