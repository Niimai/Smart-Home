# 📘 Casos de Uso

## *Sistema de Gestión de una Casa Inteligente*

Este documento describe los **casos de uso principales** del sistema,
basados en cómo el usuario interactúa con la aplicación y cómo se
comportan los sensores y actuadores dentro del entorno simulado.

------------------------------------------------------------------------

# 👤 1. Actores del Sistema

### **Actor principal:**

-   **Usuario**\
    Interactúa con la aplicación mediante la interfaz por consola para
    gestionar habitaciones, sensores y actuadores.

### **Actores secundarios (internos):**

-   **Sistema de Simulación**\
    Genera valores automáticos de sensores y aplica reglas de actuación.

-   **Sensores y Actuadores**\
    Objetos internos del sistema que detectan condiciones y reaccionan
    según la lógica implementada.

------------------------------------------------------------------------

# 📂 2. Lista de Casos de Uso

1.  **CU-01 -- Crear habitación**
2.  **CU-02 -- Eliminar habitación**
3.  **CU-03 -- Listar habitaciones**
4.  **CU-04 -- Añadir dispositivo a una habitación**
5.  **CU-05 -- Eliminar dispositivo de una habitación**
6.  **CU-06 -- Consultar dispositivos de una habitación**
7.  **CU-07 -- Consultar lecturas simuladas de sensores**
8.  **CU-08 -- Activar o desactivar actuadores manualmente**
9.  **CU-09 -- Ejecutar lógica automática del sistema**
10. **CU-10 -- Mostrar estado general del edificio**
11. **CU-11 -- Salir de la aplicación**

------------------------------------------------------------------------

# 📝 3. Detalle de Casos de Uso

------------------------------------------------------------------------

## **CU-01 -- Crear habitación**

**Actor:** Usuario\
**Flujo principal:** 1. El usuario selecciona la opción "Crear
habitación". 2. Introduce un nombre. 3. El sistema valida que no exista
ya una habitación con ese nombre. 4. Si es válido, la habitación se crea
y se almacena en la capa de datos.

**Excepciones:** - El nombre ya existe → se muestra un mensaje de error.

------------------------------------------------------------------------

## **CU-02 -- Eliminar habitación**

**Flujo principal:** 1. El usuario selecciona "Eliminar habitación". 2.
Escribe el nombre de la habitación. 3. El sistema verifica su
existencia. 4. La elimina, junto con los dispositivos asociados.

**Excepciones:** - Habitación inexistente → mensaje de error.

------------------------------------------------------------------------

## **CU-03 -- Listar habitaciones**

**Flujo principal:** 1. El usuario selecciona "Listar habitaciones". 2.
El sistema muestra una lista con todas las habitaciones registradas.

**Resultado:** - Lista ordenada con nombres y número de dispositivos.

------------------------------------------------------------------------

## **CU-04 -- Añadir dispositivo a una habitación**

**Flujo principal:** 1. El usuario selecciona "Añadir dispositivo". 2.
Elige una habitación existente. 3. Selecciona tipo de dispositivo
(sensor o actuador). 4. Introduce un nombre. 5. El dispositivo se crea y
se asigna a la habitación.

**Excepciones:** - Habitación no existe. - Nombre duplicado dentro de la
misma habitación.

------------------------------------------------------------------------

## **CU-05 -- Eliminar dispositivo**

**Flujo principal:** 1. El usuario selecciona "Eliminar dispositivo". 2.
Indica la habitación y el dispositivo. 3. El sistema valida nombres y
elimina el dispositivo.

**Excepciones:** - Habitación inexistente. - Dispositivo inexistente.

------------------------------------------------------------------------

## **CU-06 -- Consultar dispositivos de una habitación**

**Flujo principal:** 1. El usuario selecciona "Ver dispositivos". 2.
Elige una habitación. 3. El sistema muestra los sensores y actuadores
con su estado actual.

------------------------------------------------------------------------

## **CU-07 -- Consultar lecturas simuladas de sensores**

**Flujo principal:** 1. El usuario selecciona "Consultar sensores". 2.
Elige habitación o dispositivo concreto. 3. El sistema genera lecturas
simuladas (temperatura, movimiento, humedad, etc.) 4. Se muestran en
pantalla.

**Resultado adicional:** - Puede activar reglas automáticas (ej.
movimiento → luz ON).

------------------------------------------------------------------------

## **CU-08 -- Activar o desactivar actuadores manualmente**

**Flujo principal:** 1. El usuario elige un actuador. 2. El sistema
muestra su estado actual. 3. El usuario elige activarlo o desactivarlo.

------------------------------------------------------------------------

## **CU-09 -- Ejecutar lógica automática**

Caso interno del sistema.

**Descripción:** - Cada vez que se consultan sensores o se actualiza el
estado del edificio, el sistema: - Procesa las lecturas. - Evalúa reglas
configuradas. - Activa/desactiva actuadores automáticamente.

**Ejemplos:** - Activar ventilación si la calidad del aire supera un
umbral. - Encender luces si hay movimiento. - Activar alarma si los
valores son críticos.

------------------------------------------------------------------------

## **CU-10 -- Mostrar estado global del edificio**

**Flujo principal:** 1. El usuario selecciona "Estado del edificio". 2.
El sistema muestra: - Número de habitaciones. - Total de sensores y
actuadores. - Estados generales relevantes.

------------------------------------------------------------------------

## **CU-11 -- Salir del programa**

**Flujo principal:** 1. El usuario selecciona "Salir". 2. El sistema
cierra la aplicación limpiamente.

------------------------------------------------------------------------

# 🧩 4. Reglas Automáticas del Sistema (Resumen)

-   Movimiento detectado → activar iluminación.
-   Mala calidad del aire → activar ventilación.
-   Valores extremos → activar alarma.
-   Lecturas normales → restablecer estados automáticos.

------------------------------------------------------------------------

# 🏁 5. Conclusión

Este documento resume todas las interacciones posibles entre el usuario
y el sistema.\
Los casos de uso ayudan a estructurar la lógica, facilitar el desarrollo
y verificar el funcionamiento completo del sistema.
