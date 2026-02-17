from domain.repositories.edificio_repository import EdificioRepository

class EdificioRepositoryMemory(EdificioRepository):
    def __init__(self):
        self.edificio = None
        self.habitaciones = []  
        self.dispositivos = {}  

    # Edificio
    
    def guardar_edificio(self, edificio):
        self.edificio = edificio

    def obtener_edificio(self):
        return self.edificio

    # Habitaciones
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        self.dispositivos[habitacion.nombre] = []

    def listar_habitaciones(self):
        return self.habitaciones

    def buscar_habitacion(self, nombre):
        return next((h for h in self.habitaciones if h.nombre == nombre), None)

    # Dispositivos
    
    def agregar_dispositivo(self, habitacion, dispositivo):
        self.dispositivos[habitacion.nombre].append(dispositivo)

    def listar_dispositivos(self, habitacion):
        return self.dispositivos.get(habitacion.nombre, [])