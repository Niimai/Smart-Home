# 🏠 Ejecución del Proyecto

## *Sistema de Gestión de una Casa Inteligente*

Este documento explica cómo ejecutar la aplicación y cómo interactuar
con el sistema de simulación domótica desde la consola.

------------------------------------------------------------------------

## ✅ 1. Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado:

### **Software necesario**

-   **Python 3.8 o superior**
-   No se requieren librerías externas adicionales.

### **Estructura esperada del proyecto**

El proyecto debe incluir al menos: - Módulos con las clases del sistema
(sensores, actuadores, habitaciones, edificio). - Archivo **`main.py`**
como punto de entrada. - Directorios organizados por componentes.

------------------------------------------------------------------------

## ▶️ 2. Cómo ejecutar la aplicación

1.  Abre una terminal o consola.
2.  Ve al directorio raíz del proyecto.
3.  Ejecuta:

``` bash
python3 main.py
```

En Windows:

``` bash
python main.py
```

Al iniciarse, el sistema mostrará un menú principal y cargará una
simulación del edificio sin habitaciones iniciales.

------------------------------------------------------------------------

## 🖥️ 3. Interfaz de Usuario

La aplicación funciona mediante un **menú interactivo por consola**.

### Opciones típicas del menú

-   Listar habitaciones.
-   Crear o eliminar habitaciones.
-   Añadir o quitar dispositivos.
-   Consultar sensores.
-   Activar/desactivar actuadores.
-   Ver estado del edificio.
-   Salir del programa.

------------------------------------------------------------------------

## 🔄 4. Simulación del Sistema

El sistema **no utiliza hardware real**.\
Todas las lecturas son generadas automáticamente.

### **Sensores simulados**

-   Sensor de temperatura → variación gradual.\
-   Sensor de movimiento → activación aleatoria.\
-   Sensor de humedad o calidad del aire → valores dinámicos.\
-   Sensor de consumo energético → fluctuaciones simuladas.

### **Lógica automática**

El sistema puede activar actuadores según reglas simples, por ejemplo: -
Encender luces si hay movimiento. - Activar ventilación si la calidad
del aire es mala. - Lanzar alarma ante valores críticos.

------------------------------------------------------------------------

## 📌 5. Flujo de Uso Recomendada

1.  Crear una o varias habitaciones.
2.  Añadir sensores y actuadores a cada habitación.
3.  Consultar las lecturas de los sensores.
4.  Observar la reacción automática de los actuadores.
5.  Gestionar manualmente los dispositivos si es necesario.
6.  Eliminar habitaciones o dispositivos cuando ya no se requieran.

------------------------------------------------------------------------

## ⚠️ 6. Manejo de Errores

El sistema: - No permite nombres duplicados. - Informa cuando una
habitación o dispositivo no existe. - Evita acciones inválidas. -
Muestra mensajes claros en cada situación.

------------------------------------------------------------------------

## ⏹️ 7. Cierre del Programa

Para cerrar la aplicación, selecciona **Salir** desde el menú principal.

------------------------------------------------------------------------

## 📝 8. Notas Finales

-   El programa no crea archivos ni bases de datos externas.
-   Todo ocurre en memoria durante la ejecución.
-   Puede ampliarse con nuevos sensores, actuadores o reglas
    automáticas.
