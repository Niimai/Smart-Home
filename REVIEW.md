# REVISIONES PROYECTO

## REVISIÓN FASE 03 - 2026-03-02 — Nota: 0/10

> No entregado.

---

## REVISIÓN FASE 02 - 2026-03-02 — Nota: 4/10

> Revisión realizada sobre: `Smart-Home/02-documentando/`

### Resuelto desde la revisión anterior

- Se han añadido `ARQUITECTURA_POR_CAPAS.md`, `CASOS_DE_USO.md` y `EJECUCION.md` a la carpeta `docs/`.
- `casa_inteligente.md` renombrado correctamente a `DESCRIPCION_Y_ALCANCE.md`.

### Lo que está bien

- Los documentos nuevos tienen buena extensión y estructura clara.
- `ARQUITECTURA_POR_CAPAS.md` describe bien las responsabilidades de cada capa y el flujo entre ellas.
- La descripción general del proyecto en `DESCRIPCION_Y_ALCANCE.md` está bien redactada.

### Aspectos a mejorar

- [ ] [IMPORTANTE] `CHANGELOG.md` sigue sin existir. Es un fichero obligatorio en la raíz del paquete que registra los cambios por versión. Mira el modelo en `modelo/cepy_pd4/proyecto/02-documentando/expendedora/CHANGELOG.md` para ver el formato esperado.

- [ ] [IMPORTANTE] Faltan en `docs/` los siguientes ficheros obligatorios: `README.md` (índice de la documentación), `REGLAS_DE_NEGOCIO.md`, `MODELO_DE_DOMINIO.md`, `CONTRATO_REPOSITORIO.md`, `DATOS_INICIALES.md`, `TESTS_Y_PASOS.md` y `TROUBLESHOOTING.md`. Consulta el modelo para ver el contenido esperado de cada uno.

- [ ] [IMPORTANTE] No hay **docstrings en ningún fichero** del proyecto: ni en módulos, ni en clases, ni en métodos. Todos los ficheros `.py` carecen de ellos. Añade docstring de módulo al inicio de cada fichero (describe qué contiene), docstring de clase (describe qué representa) y docstring en cada método público (describe qué hace, qué recibe y qué devuelve).

- [ ] [IMPORTANTE] La documentación describe funcionalidades que **no están implementadas en el código actual**, lo que crea una desalineación entre docs y realidad:
  - `CASOS_DE_USO.md` lista 11 casos de uso (CU-02 eliminar habitación, CU-05 eliminar dispositivo, CU-07 lecturas de sensores, CU-08 activar/desactivar actuadores, CU-10 estado del edificio, etc.), pero el menú en `interfaces/cli/menu.py` solo tiene **5 opciones funcionales**.
  - `ARQUITECTURA_POR_CAPAS.md:88-95` describe "lecturas simuladas", "reglas automáticas" y "comportamiento de sensores" que no existen en el código.
  - `DESCRIPCION_Y_ALCANCE.md` describe "distintos tipos de sensores", "lecturas de sensores", "lógica automática" que tampoco están implementados.
  - `EJECUCION.md:44` dice que el sistema "cargará una simulación del edificio sin habitaciones iniciales", pero en el código actual `_cargar_datos_iniciales()` crea 2 habitaciones y 4 dispositivos al arrancar. También lista opciones del menú (consultar sensores, activar actuadores, ver estado del edificio) que no existen.

  La documentación debe reflejar lo que el programa **realmente hace ahora**, no lo que se planea hacer. Ajusta los casos de uso y descripciones para que coincidan con las 5 opciones actuales del menú.

- [ ] [SUGERENCIA] `README.md` (`02-documentando/README.md`) está en inglés y no incluye enlace a la carpeta `docs/` ni a `CHANGELOG.md`. Añade un apartado de documentación con los enlaces.

- [ ] [SUGERENCIA] Las reglas de negocio del dominio no tienen comentarios. Por ejemplo, en `domain/entities/edificio.py:3-4` valdría añadir `# El nombre del edificio no puede estar vacío ni contener solo espacios` y en `domain/entities/actuador.py:6` explicar que `estado = False` significa "apagado por defecto". El lector no debería tener que deducirlo.

## REVISIÓN FASE 01 - 2026-03-02 — Nota: 7/10

> Revisión realizada sobre: `Smart-Home/02-documentando/`

### Resuelto desde la revisión anterior

- Datos precargados implementados en `infrastructure/repositories/edificio_repository_memory.py` mediante `_cargar_datos_iniciales()`. El programa arranca con 2 habitaciones y 4 dispositivos sin necesidad de crearlos a mano.
- `buscar_habitacion` movida al dominio: `domain/entities/edificio.py:13`.
- El menú ya **no recibe ni usa el repositorio** directamente.
- Habitaciones y dispositivos gestionados a través del repositorio (`agregar_habitacion`, `agregar_dispositivo`).
- Casos de uso separados por tipo de dispositivo: `AgregarSensorUseCase` y `AgregarActuadorUseCase`.
- Persistencia correcta: los use cases llaman a `repo.agregar_habitacion()` y `repo.agregar_dispositivo()`.

### Lo que está bien

- La estructura de capas está bien definida y respetada.
- Herencia aplicada correctamente: `Sensor` y `Actuador` heredan de `Dispositivo`.
- El contrato de repositorio (`EdificioRepository`) con métodos abstractos está bien planteado.
- La validación de nombre vacío está en el dominio (`Dispositivo.__init__`, `Edificio.__init__`, `Habitacion.__init__`).

### Aspectos a mejorar

- [ ] [IMPORTANTE] Los atributos `nombre` de las entidades son públicos (`self.nombre = nombre`) sin usar `@property`. Esto significa que desde fuera se puede hacer `habitacion.nombre = ""` sin que se valide nada. Aplica el patrón de getter/setter con `@property` para el atributo `nombre` en al menos `Edificio` y `Habitacion`, de forma que la validación del `__init__` también proteja las modificaciones posteriores.

- [ ] [SUGERENCIA] El menú (`interfaces/cli/menu.py:2-14`) recibe **5 casos de uso como parámetros separados**. Como ya se indicó en la revisión anterior, considera crear un `ServicioSmartHome` en `application/` que agrupe todos los casos de uso y sea el único objeto que el menú necesite. Así el menú solo tendría una dependencia en lugar de cinco, y añadir nuevas funcionalidades no requeriría cambiar la firma del constructor del menú.

- [ ] [SUGERENCIA] La clase `Sensor` (`domain/entities/sensor.py:3-4`) solo contiene `pass` y no aporta ningún comportamiento propio más allá de heredar de `Dispositivo`. Para que la herencia tenga sentido, `Sensor` debería tener al menos algún método o atributo específico que lo diferencie (por ejemplo, un método `leer()` que devuelva un valor, aunque sea fijo o aleatorio).

# REVISIÓN DEL PROYECTO

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
- [ ] En `menu.py` (línea 2) estás pasando `repo` al `MenuCLI` y en las opciones `4` y `5` lees `repo.obtener()` y navegas por `edificio.habitaciones`.
  **Comentario:** el menú sigue leyendo directamente del repo para consultas.
- [ ] **Mueve la búsqueda de habitación al dominio**: no deberías incluir `next((h for h in edificio.habitaciones...` en casos de uso o en el menú. Añade algo como `Edificio.buscar_habitacion(nombre)` en `edificio.py` y úsalo desde application.
  **Comentario:** Sin implementar
- [x] Las habitaciones del edificio y los dispositivos de la habitación se debería almacenar en **repo**, no en listas en el propio objeto..
- [ ]**Añade reglas/validaciones en el dominio**: evita desde el dominio: nombres vacíos, habitaciones duplicadas, tipos inválidos. Actalmente esas validaciones están fuera (o no existen). Ponlas en Edificio/Habitacion y **haz que application solo coordine** y no aplique reglas de negocio.
  **Comentario:** parcialmente resuelto; aún hay parte de validación de negocio preparada en application.
- [x] **Evita que application decida strings de tipo**: AgregarDispositivoUseCase decide tipo == "sensor"/"actuador". Crea clases concretas cada una con su método para agregar y que sean invocadas desde el menu y que este llame al servicio/caso de uso correspondiente.
- [x] **Después de modificar el edificio, guarda en el repositorio**: en `agregar_habitacion.py` (línea 10) y `agregar_dispositivo.py` (línea 11) obtienes el edificio, lo modificas y devuelves, pero no haces `repo.guardar(edificio)`. Ahora funciona porque el repo en memoria guardas en el objeto en una lista, pero deberías hacerlo en el repositorio y tener en el objeto una referencia al repositorio como indico más arriba.
  **Comentario:** Evidencia: en `agregar_habitacion.py` (line 17), `agregar_sensor.py` (line 17) y `agregar_actuador.py` (line 17) se persiste mediante métodos específicos del repositorio (`agregar_habitacion`, `agregar_dispositivo`),

