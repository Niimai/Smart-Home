class MenuCLI:
    def __init__(
        self,
        agregar_habitacion_uc,
        agregar_sensor_uc,
        agregar_actuador_uc,
        listar_habitaciones_uc,
        listar_dispositivos_uc
    ):
        self.agregar_habitacion_uc = agregar_habitacion_uc
        self.agregar_sensor_uc = agregar_sensor_uc
        self.agregar_actuador_uc = agregar_actuador_uc
        self.listar_habitaciones_uc = listar_habitaciones_uc
        self.listar_dispositivos_uc = listar_dispositivos_uc

    def mostrar(self):
        while True:
            print("\n--- MENÚ CASA INTELIGENTE ---")
            print("1. Agregar habitación")
            print("2. Agregar sensor")
            print("3. Agregar actuador")
            print("4. Listar habitaciones")
            print("5. Listar dispositivos de una habitación")
            print("0. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                nombre = input("Nombre habitación: ")
                try:
                    h = self.agregar_habitacion_uc.ejecutar(nombre)
                    print(f"Habitación '{h.nombre}' agregada.")
                except Exception as e:
                    print("Error:", e)

            elif opcion == "2":
                hab = input("Habitación: ")
                nombre = input("Nombre del sensor: ")
                try:
                    s = self.agregar_sensor_uc.ejecutar(hab, nombre)
                    print(f"Sensor '{s.nombre}' agregado.")
                except Exception as e:
                    print("Error:", e)

            elif opcion == "3":
                hab = input("Habitación: ")
                nombre = input("Nombre del actuador: ")
                try:
                    a = self.agregar_actuador_uc.ejecutar(hab, nombre)
                    print(f"Actuador '{a.nombre}' agregado.")
                except Exception as e:
                    print("Error:", e)

            elif opcion == "4":
                habitaciones = self.listar_habitaciones_uc.ejecutar()
                if not habitaciones:
                    print("No hay habitaciones.")
                else:
                    for h in habitaciones:
                        print(f"- {h.nombre}")

            elif opcion == "5":
                hab = input("Habitación: ")
                try:
                    dispositivos = self.listar_dispositivos_uc.ejecutar(hab)
                    if not dispositivos:
                        print("No hay dispositivos.")
                    else:
                        for d in dispositivos:
                            print(f"- {d}")
                except Exception as e:
                    print("Error:", e)

            elif opcion == "0":
                print("Saliendo...")
                return

            else:
                print("Opción inválida")