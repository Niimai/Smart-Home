class MenuCLI:

    def __init__(self, servicio):
        self.servicio = servicio

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
                    self.servicio.agregar_habitacion(nombre)

                elif opcion == "2":

                    hab = input("Habitación: ")
                    nombre = input("Sensor: ")

                    self.servicio.agregar_sensor(hab, nombre)

                elif opcion == "3":

                    hab = input("Habitación: ")
                    nombre = input("Actuador: ")

                    self.servicio.agregar_actuador(hab, nombre)

                elif opcion == "4":

                    habitaciones = self.servicio.listar_habitaciones()

                    for h in habitaciones:
                        print(h.nombre)

                elif opcion == "5":

                    hab = input("Habitación: ")

                    dispositivos = self.servicio.listar_dispositivos(hab)

                    for d in dispositivos:
                        print(d)

                elif opcion == "6":

                    hab = input("Habitación: ")
                    act = input("Actuador: ")

                    self.servicio.activar_actuador(hab, act)

                elif opcion == "7":

                    hab = input("Habitación: ")
                    act = input("Actuador: ")

                    self.servicio.desactivar_actuador(hab, act)

                elif opcion == "8":

                    hab = input("Habitación: ")

                    dispositivos = self.servicio.consultar_estado(hab)

                    for d in dispositivos:
                        print(d)

                elif opcion == "0":

                    print("Saliendo...")
                    return

                else:
                    print("Opción inválida")

            except Exception as e:
                print("Error:", e)