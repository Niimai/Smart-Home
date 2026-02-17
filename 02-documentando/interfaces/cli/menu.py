class MenuCLI:
    def __init__(self, agregar_habitacion_uc, agregar_sensor_uc, agregar_actuador_uc, repo):
        self.agregar_habitacion_uc = agregar_habitacion_uc
        self.agregar_sensor_uc = agregar_sensor_uc
        self.agregar_actuador_uc = agregar_actuador_uc
        self.repo = repo  # solo lectura, NO reglas

    def mostrar(self):
        while True:
            print("--- MENÚ CASA INTELIGENTE ---")
            print("1. Agregar habitación")
            print("2. Agregar sensor")
            print("3. Agregar actuador")
            print("4. Listar habitaciones")
            print("5. Listar dispositivos de habitación")
            print("0. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                nombre = input("Nombre de la habitación: ")
                try:
                    hab = self.agregar_habitacion_uc.ejecutar(nombre)
                    print(f"Habitación '{hab.nombre}' agregada.")
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
                for h in self.repo.listar_habitaciones():
                    print(f"- {h.nombre}")

            elif opcion == "5":
                hab = input("Habitación: ")
                h = self.repo.buscar_habitacion(hab)
                if not h:
                    print("Habitación no encontrada.")
                else:
                    dispositivos = self.repo.listar_dispositivos(h)
                    if not dispositivos:
                        print("No hay dispositivos.")
                    for d in dispositivos:
                        print(f"- {d}")

            elif opcion == "0":
                print("Saliendo...")
                return  # Cerrar correctamente el menú y volver a main()
                print("Saliendo...")