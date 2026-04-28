# Guía de rutas Flask — Smart-Home: Casa Inteligente (API REST completa)

> Documento de acompañamiento para la actividad **ut4e1** — exposición como routes Flask de toda la API del dominio Smart-Home.
> Fecha: 2026-04-24

---

## Estructura actual del proyecto

El proyecto sigue el patrón de **arquitectura por capas** con cuatro carpetas en `02-documentando/` (la subcarpeta más avanzada):

```
02-documentando/
├── domain/
│   ├── entities/          ← Edificio, Habitacion, Dispositivo, Sensor, Actuador
│   └── repositories/      ← EdificioRepository (contrato / interfaz abstracta)
├── application/
│   └── use_cases/         ← AgregarHabitacionUseCase, AgregarSensorUseCase,
│                             AgregarActuadorUseCase, ListarHabitacionesUseCase,
│                             ListarDispositivosUseCase
├── infrastructure/
│   └── repositories/      ← EdificioRepositoryMemory (implementación en memoria)
├── interfaces/
│   └── cli/               ← MenuCLI (interfaz por consola)
└── main.py                ← Punto de entrada: inicializa repo, use cases y lanza el menú
```

La capa `interfaces/cli/` es la que se reemplaza en ut4e1 por `interfaces/api/` con Flask. Las capas `domain`, `application` e `infrastructure` **no cambian**.

> Desviacion relevante respecto a la estructura estandar: la capa de presentacion se llama `interfaces/` (no `presentation/`). Flask se añade como una nueva subcarpeta `interfaces/api/`, en paralelo a `interfaces/cli/`.

---

## Inventario completo del menu/entrypoints

### Operaciones implementadas en el CLI (menu real — `interfaces/cli/menu.py`)

| # | Opcion en el menu | Tipo | Use case que invoca | Parametros |
|---|---|---|---|---|
| 1 | Agregar habitacion | Accion | `AgregarHabitacionUseCase.ejecutar(nombre)` | nombre (str) |
| 2 | Agregar sensor | Accion | `AgregarSensorUseCase.ejecutar(habitacion, nombre)` | nombre_habitacion, nombre_sensor |
| 3 | Agregar actuador | Accion | `AgregarActuadorUseCase.ejecutar(habitacion, nombre)` | nombre_habitacion, nombre_actuador |
| 4 | Listar habitaciones | Lectura | `ListarHabitacionesUseCase.ejecutar()` | — |
| 5 | Listar dispositivos de una habitacion | Lectura | `ListarDispositivosUseCase.ejecutar(habitacion)` | nombre_habitacion |
| 0 | Salir | Transicion | — | — |

### Operaciones documentadas en casos de uso pero NO implementadas en el CLI

Segun `docs/CASOS_DE_USO.md`, el dominio prevé las siguientes operaciones adicionales que aun no tienen use case ni opcion en el menu:

| CU | Operacion | Tipo | Estado |
|---|---|---|---|
| CU-02 | Eliminar habitacion | Accion | Sin use case ni metodo en repo |
| CU-05 | Eliminar dispositivo | Accion | Sin use case ni metodo en repo |
| CU-07 | Consultar lecturas simuladas de sensores | Lectura | Sin implementar en Sensor |
| CU-08 | Activar/desactivar actuador manualmente | Transicion | `Actuador.activar()` / `Actuador.desactivar()` existen; sin use case |
| CU-09 | Ejecutar logica automatica | Transicion | No implementada |
| CU-10 | Mostrar estado general del edificio | Lectura | Sin use case |

> Nota critica (recogida en REVIEW.md Fase 02): la documentacion describe funcionalidades que no estan implementadas. Para ut4e1 se expone como API **lo que existe en el codigo real**, no lo que describe la documentacion.

---

## Rutas sugeridas (toda la API)

Los parametros de creacion/modificacion se pasan como segmentos de URL. El repositorio en memoria es el unico disponible en esta fase.

### Habitaciones

| Ruta Flask | Metodo del servicio | Descripcion |
|------------|---------------------|-------------|
| `/habitaciones` | `ListarHabitacionesUseCase.ejecutar()` | Lista todas las habitaciones |
| `/habitaciones/nueva/<nombre>` | `AgregarHabitacionUseCase.ejecutar(nombre)` | Crea una habitacion nueva |
| `/habitaciones/<nombre>/eliminar` | *(use case pendiente — ver seccion "Metodos a anadir")* | Elimina una habitacion |

### Dispositivos (sensores y actuadores)

| Ruta Flask | Metodo del servicio | Descripcion |
|------------|---------------------|-------------|
| `/habitaciones/<nombre>/dispositivos` | `ListarDispositivosUseCase.ejecutar(nombre)` | Lista dispositivos de una habitacion |
| `/habitaciones/<nombre>/sensores/nuevo/<nombre_sensor>` | `AgregarSensorUseCase.ejecutar(nombre, nombre_sensor)` | Agrega un sensor a una habitacion |
| `/habitaciones/<nombre>/actuadores/nuevo/<nombre_actuador>` | `AgregarActuadorUseCase.ejecutar(nombre, nombre_actuador)` | Agrega un actuador a una habitacion |
| `/habitaciones/<nombre_hab>/dispositivos/<nombre_disp>/eliminar` | *(use case pendiente)* | Elimina un dispositivo de una habitacion |

### Actuadores — estado

| Ruta Flask | Metodo del servicio | Descripcion |
|------------|---------------------|-------------|
| `/habitaciones/<nombre_hab>/actuadores/<nombre>/activar` | `CambiarEstadoActuadorUseCase.ejecutar(...)` | Activa un actuador *(use case a crear — ver "Metodos a anadir")* |
| `/habitaciones/<nombre_hab>/actuadores/<nombre>/desactivar` | `CambiarEstadoActuadorUseCase.ejecutar(...)` | Desactiva un actuador *(use case a crear — ver "Metodos a anadir")* |

### Edificio

| Ruta Flask | Metodo del servicio | Descripcion |
|------------|---------------------|-------------|
| `/edificio` | `EdificioRepository.obtener_edificio()` | Devuelve nombre del edificio y resumen |

### Codigos de estado HTTP a usar

| Situacion | Codigo |
|---|---|
| Operacion OK con datos devueltos | `200 OK` |
| Recurso creado correctamente | `201 Created` |
| Body invalido o campo vacio | `400 Bad Request` |
| Habitacion o dispositivo no existe | `404 Not Found` |
| Nombre duplicado | `409 Conflict` |

### Ejemplo: cómo quedaría `app.py` con dos rutas ya hechas

El siguiente fragmento muestra la estructura mínima de `app.py` con dos rutas implementadas
para que puedas tomar el patrón y aplicarlo al resto:

```python
from flask import Flask
from domain.entities.edificio import Edificio
from infrastructure.repositories.edificio_repository_memory import EdificioRepositoryMemory
from application.use_cases.listar_habitaciones import ListarHabitacionesUseCase
from application.use_cases.agregar_habitacion import AgregarHabitacionUseCase

app = Flask(__name__)

repo     = EdificioRepositoryMemory()
edificio = Edificio("Mi Casa Inteligente")
repo.guardar_edificio(edificio)

listar_habitaciones_uc  = ListarHabitacionesUseCase(repo)
agregar_habitacion_uc   = AgregarHabitacionUseCase(repo)
# (instanciar aquí el resto de use cases que se necesiten)


@app.route("/")
def bienvenida():
    habitaciones = listar_habitaciones_uc.ejecutar()
    return (
        "Bienvenido a Smart Home\n"
        f"  Habitaciones registradas: {len(habitaciones)}\n"
        "  /habitaciones                        → lista todas las habitaciones\n"
        "  /habitaciones/<nombre>/dispositivos  → lista dispositivos de una habitacion\n"
    )


@app.route("/habitaciones")
def listar_habitaciones():
    habitaciones = listar_habitaciones_uc.ejecutar()
    if not habitaciones:
        return "No hay habitaciones registradas."
    return "\n".join(h.nombre for h in habitaciones)


if __name__ == "__main__":
    app.run(debug=True)
```

**Lo que hace cada parte:**

- El repositorio y los use cases se crean **una sola vez** fuera de las vistas, al arrancar la
  aplicación. Así todas las rutas comparten el mismo estado en memoria.
- Cada función de vista llama al método `ejecutar()` del use case correspondiente y devuelve
  texto plano.
- Para rutas con `ValueError` puedes devolver una tupla `(mensaje, código)`:
  `return "No encontrado", 404` o `return "Ya existe", 409`.

---

## Metodos a anadir

| Que crear | Donde | Para que |
|---|---|---|
| `EliminarHabitacionUseCase` | `application/use_cases/eliminar_habitacion.py` | Ruta `/habitaciones/<nombre>/eliminar`; también requiere `eliminar_habitacion()` en el contrato del repo y su implementacion en memoria |
| `EliminarDispositivoUseCase` | `application/use_cases/eliminar_dispositivo.py` | Ruta `/habitaciones/<nombre_hab>/dispositivos/<nombre_disp>/eliminar`; mismo patron que el anterior |
| `CambiarEstadoActuadorUseCase` | `application/use_cases/cambiar_estado_actuador.py` | Rutas `/activar` y `/desactivar`; localiza el actuador en la habitacion y llama a `Actuador.activar()` / `Actuador.desactivar()`. No llamar al metodo del dominio directamente desde el route |

---

## Advertencias

### Particularidades del proyecto de paco

1. **El repositorio en memoria ya precarga datos.** `_cargar_datos_iniciales()` en `EdificioRepositoryMemory` crea 2 habitaciones (Dormitorio, Salon) y 4 dispositivos al arrancar. Flask arrancara con esos datos disponibles desde el primer `/habitaciones`.

2. **El edificio es un objeto único compartido por toda la aplicación.** Solo existe un edificio en el sistema. El repositorio no soporta multiples edificios. La ruta `/edificio` devuelve siempre el mismo objeto.

3. **`Edificio` tiene una funcion discutible.** Como se senala en REVIEW.md, la clase `Edificio` actualmente solo sirve para validar nombres y buscar habitaciones. No almacena habitaciones directamente (el repo las guarda en una lista separada). Tener esto en cuenta al serializar: `Edificio` no tiene lista de habitaciones, hay que pedirlas al repo.

4. **Los actuadores mutan en memoria.** Al llamar `Actuador.activar()`, el objeto en `self.dispositivos[hab.nombre]` cambia de estado porque Python guarda referencias. No es necesario persistir explicitamente con el repo en memoria. En SQLite (fase siguiente) si sera necesario.

5. **`Sensor` no tiene atributos adicionales.** La clase `Sensor` es solo `pass` heredando de `Dispositivo`. No hay lecturas simuladas implementadas. La ruta `/habitaciones/<nombre>/sensores/<nombre>/lectura` no es posible hasta que se implemente.

6. **Validacion de nombre duplicado lanza `ValueError`.** Los use cases llaman a `edificio.validar_nombre_unico()` que lanza `ValueError("El nombre ya existe.")`. En Flask hay que capturar ese `ValueError` y devolver `409 Conflict`.

7. **Busqueda de habitacion devuelve `None`.** `edificio.buscar_habitacion()` devuelve `None` si no existe. Los use cases lanzan `ValueError("La habitacion no existe.")`. En Flask → `404 Not Found`.

8. **No hay servicio de aplicacion (facade).** El menu (y por extension Flask) recibe 5 use cases separados. REVIEW.md sugiere crear un `ServicioSmartHome`. Para ut4e1 se puede trabajar directamente con los use cases; el refactor puede hacerse en ut4e2.

9. **Capas `domain` e `infrastructure` sin `presentation/`.** La capa de interfaz de usuario se llama `interfaces/`, no `presentation/`. Al anadir Flask se respeta esa convencion del alumno.
