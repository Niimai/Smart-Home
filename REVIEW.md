# REVISIONES PROYECTO

## REVISIÓN FASE 03 - 2026-03-03 — Nota: 0/10

> No entregado.


## REVISIÓN FASE 02 - 2026-03-03 — Nota: 4/10

> Revisión realizada sobre: `Smart-Home/02-documentando/`

### Resuelto desde la revisión anterior

- Se han añadido `ARQUITECTURA_POR_CAPAS.md`, `CASOS_DE_USO.md` y `EJECUCION.md` a la carpeta `docs/`.
- `casa_inteligente.md` renombrado correctamente a `DESCRIPCION_Y_ALCANCE.md`.

### Lo que cumples

- La carpeta `docs/` existe y contiene cuatro documentos con buena extensión y estructura clara: `DESCRIPCION_Y_ALCANCE.md`, `ARQUITECTURA_POR_CAPAS.md`, `CASOS_DE_USO.md` y `EJECUCION.md`.
- `ARQUITECTURA_POR_CAPAS.md` describe bien las responsabilidades de cada capa y el flujo entre ellas.
- `DESCRIPCION_Y_ALCANCE.md` está bien redactado.

### Lo que no cumples

- [ ] **[IMPORTANTE] Falta `CHANGELOG.md`** en la raíz de `02-documentando/`. Es un fichero obligatorio para registrar los cambios del proyecto por versión. Consulta el modelo en `modelo/cepy_pd4/proyecto/02-documentando/expendedora/CHANGELOG.md` para ver el formato: encabezado con número de versión, fecha y lista de cambios añadidos, modificados y eliminados.

- [ ] **[IMPORTANTE] Faltan 7 ficheros obligatorios en `docs/`**: `README.md` (índice de la documentación), `REGLAS_DE_NEGOCIO.md`, `MODELO_DE_DOMINIO.md`, `CONTRATO_REPOSITORIO.md`, `DATOS_INICIALES.md`, `TESTS_Y_PASOS.md` y `TROUBLESHOOTING.md`. Consulta los equivalentes en `modelo/cepy_pd4/proyecto/02-documentando/expendedora/docs/` para ver el contenido esperado de cada uno.

- [ ] **[IMPORTANTE] No hay docstrings en ningún fichero Python del proyecto**: ni en módulos, ni en clases, ni en métodos. Todos los `.py` carecen de ellos. Añade:
  - Al inicio de cada módulo: una línea describiendo qué contiene (por ejemplo, `"""Módulo que define la entidad Habitacion."""`).
  - En cada clase: una descripción de qué representa.
  - En cada método público: qué hace, qué parámetros recibe y qué devuelve.

- [ ] **[IMPORTANTE] La documentación describe funcionalidades que no están implementadas**, lo que crea una desalineación entre docs y código:
  - `CASOS_DE_USO.md` lista 11 casos de uso, pero el menú (`interfaces/cli/menu.py`) solo tiene **5 opciones funcionales** (agregar habitación, agregar sensor, agregar actuador, listar habitaciones, listar dispositivos). Los casos CU-02, CU-05, CU-07, CU-08, CU-09 y CU-10 no están implementados.
  - `ARQUITECTURA_POR_CAPAS.md` (sección 4) describe "lecturas simuladas" y "reglas automáticas" que no existen en el código.
  - `DESCRIPCION_Y_ALCANCE.md` menciona "distintos tipos de sensores" y "lógica automática" que tampoco están implementados.
  - `EJECUCION.md` dice que el sistema arranca "sin habitaciones iniciales", pero `_cargar_datos_iniciales()` crea 2 habitaciones y 4 dispositivos al arrancar. También lista opciones del menú que no existen.

  **Cómo resolverlo:** la documentación debe reflejar lo que el programa **hace ahora**, no lo que planeas añadir. Ajusta cada documento para que el apartado **incluye** de `DESCRIPCION_Y_ALCANCE.md` coincida con las opciones reales del menú y lo no implementado que aparezca en el apartado **no incluye**. Actualiza si añades funcionalidades al menú. Te puedes guiar del mismo contenido en el proyecto modelo de la máquina expendedora.

- [ ] **[SUGERENCIA] `README.md` sin completar**. Usa como referencia para el mismo contenido en el proyecto modelo de la máquina expendedora
- [ ] **[SUGERENCIA] Las reglas de negocio del dominio no tienen comentarios.** Por ejemplo, en `domain/entities/edificio.py:3` añade `# El nombre no puede estar vacío ni contener solo espacios` y en `domain/entities/actuador.py:6` explica que `estado = False` significa "apagado por defecto". El lector no debería tener que deducirlo.


## REVISIÓN FASE 01 - 2026-03-03 — Nota: 6/10

> Revisión realizada sobre: `Smart-Home/02-documentando/`

### Resuelto desde la revisión anterior

- Datos precargados implementados en `infrastructure/repositories/edificio_repository_memory.py` mediante `_cargar_datos_iniciales()`. El programa arranca con 2 habitaciones y 4 dispositivos sin necesidad de crearlos a mano.
- `buscar_habitacion` movida al dominio: `domain/entities/edificio.py:13`.
- El menú ya **no recibe ni usa el repositorio** directamente.
- Habitaciones y dispositivos gestionados a través del repositorio (`agregar_habitacion`, `agregar_dispositivo`).
- Casos de uso separados por tipo de dispositivo: `AgregarSensorUseCase` y `AgregarActuadorUseCase`.
- Persistencia correcta: los use cases llaman a `repo.agregar_habitacion()` y `repo.agregar_dispositivo()`.

### Lo que cumples

- Repositorio creado y compartido con el profesor.
- `README.md` presente con instrucciones para ejecutar el proyecto.
- El proyecto está organizado en capas bien diferenciadas: `domain/`, `application/`, `infrastructure/` e `interfaces/` (equivalente a `presentation/`).
- La estructura de ficheros sigue las pautas de módulos, paquetes y subpaquetes Python (todos los directorios tienen `__init__.py`).
- POO aplicado correctamente: `Sensor` y `Actuador` heredan de `Dispositivo`.
- El contrato de repositorio (`domain/repositories/edificio_repository.py`) define métodos abstractos con `raise NotImplementedError`.
- Validación de nombre vacío en el dominio: `Dispositivo.__init__`, `Edificio.__init__`, `Habitacion.__init__`.
- La búsqueda de habitación está delegada al dominio (`Edificio.buscar_habitacion`).
- El menú no accede directamente al repositorio.
- Los 5 apartados del menú funcionan correctamente.
- Datos precargados en `infrastructure/repositories/edificio_repository_memory.py` mediante `_cargar_datos_iniciales()`: el programa arranca con 2 habitaciones y 4 dispositivos.
- Nombres de ficheros, clases y variables significativos y conformes a PEP8.

### Lo que no cumples

- [ ] **[IMPORTANTE] El menú no tiene opciones para la operativa básica de los dispositivos.** La clase `Actuador` (`domain/entities/actuador.py`) incluye `activar()` y `desactivar()`, pero ninguna opción del menú permite ejecutarlos. El usuario no puede interactuar con los actuadores más allá de crearlos: no puede encenderlos, apagarlos ni consultar su estado. De igual forma, `Sensor` existe como clase pero no hay ninguna opción para leer un sensor. 
- *Cómo resolverlo:* Añade al menú al menos una opción para activar/desactivar un actuador y otra para consultar el estado de los dispositivos de una habitación.

- [ ] **[SUGERENCIA] `obtener_edificio()` puede devolver `None`** si se llama antes de que `guardar_edificio()` haya sido invocado. Todos los use cases asumen que el resultado nunca es `None` y llaman directamente `edificio.validar_nombre_unico(...)` sin comprobarlo, lo que causaría un `AttributeError`. 
  - *Cómo resolverlo*: lanza un error claro si el edificio no ha sido inicializado o de momento no implementes esta clase.

- [ ] **[IMPORTANTE] Los atributos `nombre` de las entidades son públicos** (`self.nombre = nombre`) sin usar `@property`. Esto permite hacer `habitacion.nombre = ""` desde fuera sin que se valide nada. Aplica el patrón getter/setter con `@property` para `nombre` en al menos `Edificio` y `Habitacion`, de forma que la validación del `__init__` también proteja modificaciones posteriores.

- [ ] **[SUGERENCIA] El menú (`interfaces/cli/menu.py:2-14`) recibe 5 casos de uso como parámetros separados.** Considera crear un `ServicioSmartHome` en `application/` que agrupe todos los casos de uso y sea el único objeto que el menú necesite. Así el menú tendría una sola dependencia y añadir nuevas funcionalidades no requeriría cambiar la firma del constructor.

- [ ] **[SUGERENCIA] La clase `Sensor` (`domain/entities/sensor.py`) no está implementada**

- [ ] **[SUGERENCIA] eliminar o implementar correctamente la clase Edificio**: En el estado actual de la apliación usar la clase edificio no tiene sentido. Solo hay habitaciones con sensores y actuadores. La clase Edificio solo tiene sentido si la aplicación permite tener más de un edificio y gestionarlos y en ese caso cada uno debería contener una lista de aplicaciones con lo que el repo sería de edificios que a su vez contendría una lista de habitaciones como uno de sus atributos. Tener ahora mismo la clase edificio solo para buscar habitaciones que ni siquiera están guardadas en él no tiene sentido.


## REVISIÓN FASE 02 - 2026-02-25

### Incumplimientos detectados

- [ ] No existe `CHANGELOG.md`.
- [ ] En `docs/` faltan `README.md` (de docs), `REGLAS_DE_NEGOCIO.md`, `MODELO_DE_DOMINIO.md`, `CONTRATO_REPOSITORIO.md`, `DATOS_INICIALES.md`, `TESTS_Y_PASOS.md` (y `TROUBLESHOOTING.md` como opcional recomendado).
- [ ] `README.md` no sigue modelo de apuntes.
- [ ] Casos de uso documentados desalineados con funcionalidades realmente implementadas:
  - `docs/CASOS_DE_USO.md:32-42` lista 11 casos de uso. El documento describe operaciones no disponibles en la versión final actual: `interfaces/cli/menu.py:11-16` implementa 5 opciones funcionales + salida.
- [ ] La documentación de arquitectura sugiere capacidades no presentes en el código actual.
  - `docs/ARQUITECTURA_POR_CAPAS.md:88-95` menciona simulación de lecturas y reglas automáticas.
    - En `domain/entities/sensor.py:3-4` no hay lógica de lectura/simulación.
    - En `application/use_cases` solo hay altas (`agregar_*`).

## REVISIÓN DE FASE I - 2026-02-25

###  Comentarios / recomendaciones

- [ ] **Tener datos precargados** desde `infrastructure` que se usen cada vez que se ejecute el programa que permitan hacer pruebas sin tener que cargar datos cada vez que se ejecuta el menú. Mira en expendedora.
  **Comentario**: no se ha implementado y facilita las pruebas.
- **Añade un servicio de aplicación que haga de fachada de la misma**: en vez de pasar 3 use _cases sueltos al menú, crea un `ServicioSmartHome` en `application` que agrupe operaciones y sea el único objeto que usa la UI. Esto simplifica el menú y reduce acoplamiento (cantidad de dependencias del menú).
- El diseño que empleas ahora con un `main.py` de entrada que se encarga de llamar al `cli/menu.py` aunque es correcto la idea era usarlo más adelante al ver como empaquetar correctamente las aplicaciones. Si quieres puedes manternerlo, pero no está alineado con lo que hemos visto hasta ahora.

### PTE Arreglar

La aplicación no está siguiendo los principios del diseño por capas visto en clase en algunos aspectos. Deberías arreglar:

- [x] Dado que **solo usas un edificio** no tiene mucho sentido que desde el menú haya una opción para añadir edificio. No debería aparecer la opción en el menú y crearlo al inicializarlo. De hecho cada vez que seleccionas la opción de crear un edificio pierdes el edificio anterior y todo lo que le habías añadido. De esa forma además te ahorras usar el repositorio desde el menú que va contra los principios del diseño por capas:
- [x] En `menu.py` (línea 2) estás pasando `repo` al `MenuCLI` y en las opciones `4` y `5` lees `repo.obtener()` y navegas por `edificio.habitaciones`.
  **Comentario:** el menú sigue leyendo directamente del repo para consultas.
- [x] **Mueve la búsqueda de habitación al dominio**: no deberías incluir `next((h for h in edificio.habitaciones...` en casos de uso o en el menú. Añade algo como `Edificio.buscar_habitacion(nombre)` en `edificio.py` y úsalo desde application.
  **Comentario:** Sin implementar
- [x] Las habitaciones del edificio y los dispositivos de la habitación se debería almacenar en **repo**, no en listas en el propio objeto..
- [x]**Añade reglas/validaciones en el dominio**: evita desde el dominio: nombres vacíos, habitaciones duplicadas, tipos inválidos. Actalmente esas validaciones están fuera (o no existen). Ponlas en Edificio/Habitacion y **haz que application solo coordine** y no aplique reglas de negocio.
  **Comentario:** parcialmente resuelto; aún hay parte de validación de negocio preparada en application.
- [x] **Evita que application decida strings de tipo**: AgregarDispositivoUseCase decide tipo == "sensor"/"actuador". Crea clases concretas cada una con su método para agregar y que sean invocadas desde el menu y que este llame al servicio/caso de uso correspondiente.
- [x] **Después de modificar el edificio, guarda en el repositorio**: en `agregar_habitacion.py` (línea 10) y `agregar_dispositivo.py` (línea 11) obtienes el edificio, lo modificas y devuelves, pero no haces `repo.guardar(edificio)`. Ahora funciona porque el repo en memoria guardas en el objeto en una lista, pero deberías hacerlo en el repositorio y tener en el objeto una referencia al repositorio como indico más arriba.
  **Comentario:** Evidencia: en `agregar_habitacion.py` (line 17), `agregar_sensor.py` (line 17) y `agregar_actuador.py` (line 17) se persiste mediante métodos específicos del repositorio (`agregar_habitacion`, `agregar_dispositivo`),
