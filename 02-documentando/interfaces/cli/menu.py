class MenuCLI:
    def __init__(
        self,
        agregar_habitacion_uc,
        agregar_sensor_uc,
        agregar_actuador_uc,
        listar_habitaciones_uc,
        listar_dispositivos_uc,
        activar_actuador_uc,
        desactivar_actuador_uc,
        consultar_estado_uc
    ):
        self.agregar_habitacion_uc = agregar_habitacion_uc
        self.agregar_sensor_uc = agregar_sensor_uc
        self.agregar_actuador_uc = agregar_actuador_uc
        self.listar_habitaciones_uc = listar_habitaciones_uc
        self.listar_dispositivos_uc = listar_dispositivos_uc
        self.activar_actuador_uc = activar_actuador_uc
        self.desactivar_actuador_uc = desactivar_actuador_uc
        self.consultar_estado_uc = consultar_estado_uc

    def mostrar(self):
        while True:
            print("\n--- MENÚ CASA INTELIGENTE ---")
            print("1. Agregar habitación")
            print("2. Agregar sensor")
            print("3. Agregar actuador")
            print("4. Listar habitaciones")
            print("5. Listar dispositivos")
            print("6. Activar actuador")
            print("7. Desactivar actuador")
            print("8. Consultar estado dispositivos")
            print("0. Salir")

            opcion = input("Opción: ")

            try:
                if opcion == "1":
                    nombre = input("Nombre habitación: ")
                    self.agregar_habitacion_uc.ejecutar(nombre)

                elif opcion == "2":
                    hab = input("Habitación: ")
                    nombre = input("Sensor: ")
                    self.agregar_sensor_uc.ejecutar(hab, nombre)

                elif opcion == "3":
                    hab = input("Habitación: ")
                    nombre = input("Actuador: ")
                    self.agregar_actuador_uc.ejecutar(hab, nombre)

                elif opcion == "4":
                    for h in self.listar_habitaciones_uc.ejecutar():
                        print(h.nombre)

                elif opcion == "5":
                    hab = input("Habitación: ")
                    for d in self.listar_dispositivos_uc.ejecutar(hab):
                        print(d)

                elif opcion == "6":
                    hab = input("Habitación: ")
                    act = input("Actuador: ")
                    self.activar_actuador_uc.ejecutar(hab, act)

                elif opcion == "7":
                    hab = input("Habitación: ")
                    act = input("Actuador: ")
                    self.desactivar_actuador_uc.ejecutar(hab, act)

                elif opcion == "8":
                    hab = input("Habitación: ")
                    for d in self.consultar_estado_uc.ejecutar(hab):
                        print(d)

                elif opcion == "0":
                    print("Saliendo...")
                    return

                else:
                    print("Opción inválida")

            except Exception as e:
                print("Error:", e)