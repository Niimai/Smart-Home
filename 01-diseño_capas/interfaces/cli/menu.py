class MenuCLI:
    def __init__(self, crear_edificio_uc, agregar_habitacion_uc, agregar_dispositivo_uc, edificio_repo):
        self.crear_edificio_uc = crear_edificio_uc
        self.agregar_habitacion_uc = agregar_habitacion_uc
        self.agregar_dispositivo_uc = agregar_dispositivo_uc
        self.edificio_repo = edificio_repo


    def mostrar(self):
        while True:
            print("--- MENÚ CASA INTELIGENTE ---")
            print("1. Crear edificio")
            print("2. Agregar habitación")
            print("3. Agregar dispositivo a una habitación")
            print("4. Listar habitaciones")
            print("5. Listar dispositivos de una habitación")
            print("0. Salir")


            opcion = input("Selecciona una opción: ")


            if opcion == "1":
                nombre = input("Nombre del edificio: ")
                edificio = self.crear_edificio_uc.ejecutar(nombre)
                print(f"Edificio '{edificio.nombre}' creado.")


            elif opcion == "2":
                nombre = input("Nombre de la habitación: ")
                try:
                    hab = self.agregar_habitacion_uc.ejecutar(nombre)
                    print(f"Habitación '{hab.nombre}' agregada.")
                except Exception as e:
                    print(f"Error: {e}")


            elif opcion == "3":
                nombre_hab = input("Nombre de la habitación: ")
                tipo = input("Tipo de dispositivo (sensor/actuador): ")
                nombre_disp = input("Nombre del dispositivo: ")
                try:
                    disp = self.agregar_dispositivo_uc.ejecutar(nombre_hab, tipo, nombre_disp)
                    print(f"Dispositivo '{disp.nombre}' agregado.")
                except Exception as e:
                    print(f"Error: {e}")


            elif opcion == "4":
                edificio = self.edificio_repo.obtener()
                if edificio is None:
                    print("Aún no hay un edificio creado.")
                else:
                    for h in edificio.habitaciones:
                        print(f"- {h.nombre}")


            elif opcion == "5":
                edificio = self.edificio_repo.obtener()
                if edificio is None:
                    print("No hay edificio.")
                    continue
                nombre_hab = input("Nombre de la habitación: ")
                hab = next((h for h in edificio.habitaciones if h.nombre == nombre_hab), None)
                if hab is None:
                    print("Habitación no encontrada.")
                else:
                    if not hab.dispositivos:
                        print("No hay dispositivos.")
                    else:
                        for d in hab.dispositivos:
                            print(f"- {d}")


            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")