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

