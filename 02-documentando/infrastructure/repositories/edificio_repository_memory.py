from domain.repositories.edificio_repository import EdificioRepository
from domain.entities.habitacion import Habitacion
from domain.entities.sensor import Sensor
from domain.entities.actuador import Actuador


class EdificioRepositoryMemory(EdificioRepository):
    def __init__(self):
        self.edificio = None
        self.habitaciones = []  
        self.dispositivos = {}  

        # Carga datos iniciales
        self._cargar_datos_iniciales()


    # Carga inicial
    
    def _cargar_datos_iniciales(self):
        
        dormitorio = Habitacion("Dormitorio")
        salon = Habitacion("Salón")

        self.habitaciones.extend([dormitorio, salon])

        self.dispositivos[dormitorio.nombre] = [
            Sensor("SensorDormitorio"),
            Actuador("ActuadorDormitorio")
        ]

        self.dispositivos[salon.nombre] = [
            Sensor("SensorSalon"),
            Actuador("ActuadorSalon")
        ]
        

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