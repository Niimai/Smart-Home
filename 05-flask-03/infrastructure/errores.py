class ErrorRepositorio(Exception):
    """Clase base para errores del repositorio."""
    pass


class HabitacionYaExisteError(ErrorRepositorio):
    pass


class HabitacionNoEncontradaError(ErrorRepositorio):
    pass


class DispositivoYaExisteError(ErrorRepositorio):
    pass


class ErrorPersistencia(ErrorRepositorio):
    pass