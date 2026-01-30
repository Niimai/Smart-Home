class MenuCLI:
    def __init__(self, crear_edificio_uc, agregar_habitacion_uc, edificio_repo):
        self.crear_edificio_uc = crear_edificio_uc
        self.agregar_habitacion_uc = agregar_habitacion_uc
        self.edificio_repo = edificio_repo


    def mostrar(self):
        while True:
            print("\n--- MENÚ CASA INTELIGENTE ---")
            print("1. Crear edificio")
            print("2. Agregar habitación")
            print("3. Listar habitaciones")
            print("0. Salir")


            opcion = input("Selecciona una opción: ")


            if opcion == "1":
                nombre = input("Nombre del edificio: ")
                edificio = self.crear_edificio_uc.ejecutar(nombre)
                print(f"Edificio '{edificio.nombre}' creado.")


            elif opcion == "2":
                nombre = input("Nombre de la habitación: ")
                try:
                    habitacion = self.agregar_habitacion_uc.ejecutar(nombre)
                    print(f"Habitación '{habitacion.nombre}' agregada.")
                except Exception as e:
                    print(f"Error: {e}")


            elif opcion == "3":
                edificio = self.edificio_repo.obtener()
                if edificio is None:
                    print("Aún no hay un edificio creado.")
                else:
                    habitaciones = edificio.listar_habitaciones()
                    if not habitaciones:
                        print("El edificio no tiene habitaciones.")
                    else:
                        print("Habitaciones:")
                        for h in habitaciones:
                            print(f"- {h.nombre}")


            elif opcion == "0":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")