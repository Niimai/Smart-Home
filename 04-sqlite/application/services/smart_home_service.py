from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase
from application.use_cases.agregar_sensor import AgregarSensorUseCase
from application.use_cases.agregar_actuador import AgregarActuadorUseCase

from application.use_cases.listar_habitaciones import ListarHabitacionesUseCase
from application.use_cases.listar_dispositivos import ListarDispositivosUseCase

from application.use_cases.activar_actuador import ActivarActuadorUseCase
from application.use_cases.desactivar_actuador import DesactivarActuadorUseCase
from application.use_cases.consultar_estado import ConsultarEstadoUseCase

from application.use_cases.eliminar_habitacion import (EliminarHabitacionUseCase)
from application.use_cases.eliminar_dispositivo import (EliminarDispositivoUseCase)


class ServicioSmartHome:

    def __init__(self, repo):

        self.agregar_habitacion_uc = AgregarHabitacionUseCase(repo)
        self.agregar_sensor_uc = AgregarSensorUseCase(repo)
        self.agregar_actuador_uc = AgregarActuadorUseCase(repo)

        self.listar_habitaciones_uc = ListarHabitacionesUseCase(repo)
        self.listar_dispositivos_uc = ListarDispositivosUseCase(repo)

        self.activar_actuador_uc = ActivarActuadorUseCase(repo)
        self.desactivar_actuador_uc = DesactivarActuadorUseCase(repo)

        self.consultar_estado_uc = ConsultarEstadoUseCase(repo)

        self.eliminar_habitacion_uc = (EliminarHabitacionUseCase(repo))
        self.eliminar_dispositivo_uc = (EliminarDispositivoUseCase(repo))


    # Habitaciones
    def agregar_habitacion(self, nombre):
        return self.agregar_habitacion_uc.ejecutar(nombre)

    def listar_habitaciones(self):
        return self.listar_habitaciones_uc.ejecutar()


    # Sensores
    def agregar_sensor(self, habitacion, nombre_sensor):
        return self.agregar_sensor_uc.ejecutar(habitacion, nombre_sensor)

    
    # Actuadores
    def agregar_actuador(self, habitacion, nombre_actuador):
        return self.agregar_actuador_uc.ejecutar(habitacion, nombre_actuador)

    def activar_actuador(self, habitacion, nombre_actuador):
        return self.activar_actuador_uc.ejecutar(habitacion, nombre_actuador)

    def desactivar_actuador(self, habitacion, nombre_actuador):
        return self.desactivar_actuador_uc.ejecutar(habitacion, nombre_actuador)


    # Dispositivos
    def listar_dispositivos(self, habitacion):
        return self.listar_dispositivos_uc.ejecutar(habitacion)

    def consultar_estado(self, habitacion):
        return self.consultar_estado_uc.ejecutar(habitacion)

    
    # Eliminar
    def eliminar_habitacion(self, nombre_habitacion):

        return self.eliminar_habitacion_uc.ejecutar(nombre_habitacion)

    def eliminar_dispositivo(self, nombre_habitacion, nombre_dispositivo):

        return self.eliminar_dispositivo_uc.ejecutar(nombre_habitacion, nombre_dispositivo)