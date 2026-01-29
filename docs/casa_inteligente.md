# Proyecto Casa Inteligente

### Título del proyecto

**Sistema de Gestión de una Casa Inteligente: Simulación de Sensores y Actuadores en un Entorno Domótico**

### Descripción general

El proyecto consiste en el diseño y desarrollo de una aplicación software que simula el funcionamiento básico de una casa inteligente, centrada en la gestión de sensores que monitorizan el entorno y actuadores que responden automáticamente ante determinados eventos.

El sistema modela un edificio compuesto por varias habitaciones o estancias, en las que se ubican distintos sensores y actuadores. Aunque el proyecto se inspira en escenarios reales de viviendas o edificios inteligentes, no se contempla la conexión con hardware físico real, sino que las lecturas de los sensores y los eventos del sistema se generan de forma completamente simulada.

Esta aproximación permite centrarse en el diseño lógico, la estructura del sistema y la interacción entre sus componentes, sin depender de dispositivos externos.


### Objetivos

* **Objetivo general**:
  Desarrollar un sistema modular que represente un edificio inteligente, capaz de gestionar de forma coherente sensores y actuadores distribuidos en diferentes estancias.

* **Objetivos específicos**:

  * Modelar dispositivos domóticos con comportamientos diferenciados según su tipo.
  * Simular situaciones habituales en una casa inteligente, como alertas por condiciones anómalas o reacciones automáticas ante determinados valores de sensores.
  * Permitir la gestión dinámica de habitaciones y dispositivos dentro del sistema.


### Características principales

#### Dispositivos de la casa inteligente

* Se definirá un conjunto de **dispositivos genéricos** que compartan propiedades comunes, como nombre, tipo y estado.
* Se implementarán **distintos tipos de sensores** (por ejemplo, temperatura, movimiento, calidad del aire, humedad o consumo energético) y **distintos tipos de actuadores** (como sistemas de climatización, puertas automáticas, iluminación o alarmas), cada uno con un comportamiento específico dentro de la simulación.

#### Gestión de ubicaciones

* El sistema modelará habitaciones o estancias que agrupan sensores y actuadores.
* Se permitirá añadir y eliminar habitaciones, así como asociar o desasociar dispositivos a cada una de ellas.
* Será posible obtener información agregada tanto a nivel de habitación como del edificio completo, mediante informes o estados generales simulados.

#### Interacción con el usuario

* El usuario dispondrá de una interfaz que permita realizar acciones como listar habitaciones, consultar dispositivos, visualizar lecturas simuladas, activar o desactivar actuadores y gestionar el alta o baja de habitaciones y dispositivos.
* Se gestionarán errores habituales de uso, mostrando mensajes claros cuando una habitación o dispositivo no exista o cuando una acción no sea válida.
* El sistema está diseñado para ser utilizado por un único usuario en una máquina local.

#### Simulación de lecturas y lógica automática

* Las lecturas de los sensores se generarán de forma simulada, imitando comportamientos realistas como variaciones de temperatura o detección de movimiento.
* El sistema implementará reglas automáticas simples, por ejemplo:

  * Activar un actuador ante la detección de movimiento en una zona.
  * Simular una alarma o la activación de un sistema de ventilación cuando la calidad del aire supere un determinado umbral.


### Alcance del proyecto

#### Incluye

* Modelado de un número significativo de clases que representen dispositivos, habitaciones y el edificio.
* Simulación de varios tipos de sensores y actuadores (al menos cuatro o cinco tipos en total).
* Implementación de una interfaz con múltiples opciones de gestión y consulta, incluyendo la creación y eliminación dinámica de habitaciones y dispositivos.
* Verificaciones básicas del funcionamiento del sistema, asegurando que no se permitan estados o valores incoherentes.

#### No incluye

* Conexión con dispositivos físicos reales ni integración con hardware, sensores externos o redes.
* Aspectos relacionados con la seguridad, autenticación de usuarios o despliegue en entornos de producción.


 
