# 🏗️ Arquitectura por Capas

## *Sistema de Gestión de una Casa Inteligente*

Este documento describe la arquitectura por capas utilizada en el
proyecto, siguiendo una separación clara entre lógica, datos y
presentación. El objetivo es lograr un sistema modular, mantenible y
extensible.

------------------------------------------------------------------------

# 📚 1. Visión General de la Arquitectura

El proyecto utiliza un **modelo de arquitectura por capas** dividido en:

1.  **Capa de Interfaces (UI/Interfaz de Usuario)**
2.  **Capa de Application (Controladores / Casos de Uso)**
3.  **Capa de Domain (Modelos / Lógica de Negocio)**
4.  **Capa de Infrastructure (Repositorios / Gestión interna de colecciones)**

Esta separación permite modificar cada capa sin afectar directamente a
las demás.

------------------------------------------------------------------------

# 🖥️ 2. Capa Interfaces

## (Interfaz de usuario por consola)

Responsable de la interacción directa con el usuario.

### **Funciones principales:**

-   Mostrar el menú principal.
-   Solicitar y validar entradas del usuario.
-   Mostrar resultados, errores o estados del sistema.
-   Invocar los métodos de la capa de aplicación.

### **Ejemplos dentro del proyecto:**

-   El archivo `main.py`.
-   Funciones que dibujan menús y capturan opciones.
-   Funciones que muestran el estado del edificio, habitaciones o
    dispositivos.

------------------------------------------------------------------------

# ⚙️ 3. Capa Application

## (Controladores o gestores del sistema)

Es el puente entre la interfaz de usuario y el dominio.

### **Responsabilidades:**

-   Coordina las acciones solicitadas por el usuario.
-   Llama a la lógica de negocio apropiada.
-   Valida operaciones de alto nivel.
-   Controla errores como nombres duplicados o inexistentes.

### **Ejemplos dentro del proyecto:**

-   Controlador del edificio.
-   Controlador de habitaciones.
-   Controlador de dispositivos.

------------------------------------------------------------------------

# 🧠 4. Capa Domain

## (Modelos y lógica de negocio)

Es el núcleo del sistema. Aquí se definen las reglas principales de
funcionamiento.

### **Incluye:**

### **Modelos del sistema**

-   Edificio
-   Habitación
-   Dispositivo (clase base)
-   Sensor (clases hijas)
-   Actuador (clases hijas)

### **Funciones clave:**

-   Comportamiento de sensores (lecturas simuladas).
-   Reglas automáticas:
    -   Activar luces ante movimiento.
    -   Ventilar por mala calidad del aire.
    -   Activar alarma ante valores críticos.
-   Gestión coherente de estados.
-   Simulación interna (variación de valores, detección de eventos,
    etc).

Esta capa es totalmente independiente de cómo se muestre la información
o cómo se organiza el sistema.

------------------------------------------------------------------------

# 🗂️ 5. Capa Infrastructure

## (Repositorios y almacenamiento simulado)

Maneja la estructura interna donde se guardan edificios, habitaciones y
dispositivos.

### **Características:**

-   No usa base de datos real (todo ocurre en memoria).
-   Utiliza listas o diccionarios para almacenar objetos.
-   Proporciona métodos para:
    -   Añadir, buscar y eliminar habitaciones.
    -   Añadir, buscar y eliminar dispositivos.
    -   Consultar estados globales.

### **Objetivo:**

Aislar la forma en la que se almacenan los datos del resto del sistema.

------------------------------------------------------------------------

# 🔗 6. Relación entre las capas

    +-----------------------------+
    |      Capa de Interfaces     |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |      Capa de Application    |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |        Capa de Domain       |
    +-----------------------------+
                  |
                  v
    +-----------------------------+
    |   Capa de Infrastructure    |
    +-----------------------------+

### **Flujo típico:**

1.  El usuario selecciona una acción desde el menú.
2.  La capa de presentación pasa esa acción a la capa de aplicación.
3.  La capa de aplicación usa el dominio para ejecutar la lógica.
4.  El dominio consulta o modifica datos en la capa de datos.
5.  Finalmente, los resultados vuelven a la capa de presentación.

------------------------------------------------------------------------

# 🧩 7. Ventajas de esta arquitectura

-   Código más limpio y organizado.
-   Facilidad para añadir nuevos dispositivos o sensores.
-   Posibilidad de reemplazar partes del sistema (por ejemplo, la UI)
    sin alterar el resto.
-   Mejor capacidad de pruebas y mantenimiento.
-   Modularidad y escalabilidad natural.

------------------------------------------------------------------------

# 🏁 8. Conclusión

La arquitectura por capas adoptada en este proyecto permite un
desarrollo estructurado y escalable.\
Cada componente tiene responsabilidades bien definidas y puede
evolucionar independientemente, manteniendo el proyecto organizado y
fácil de extender.
