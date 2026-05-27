# Arquitectura por Capas

El proyecto sigue una arquitectura por capas inspirada en Clean Architecture.

## Capas

### Domain
Contiene las entidades y reglas de negocio.

### Application
Contiene los casos de uso y coordinación de la lógica.

### Infrastructure
Implementa detalles técnicos como repositorios.

### Interfaces
Gestiona interacción con el usuario mediante CLI.

## Dependencias

Las capas externas dependen de las internas.
