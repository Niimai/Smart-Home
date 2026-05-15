import sqlite3
from pathlib import Path


ruta_bd = Path("smarthome.db")

if ruta_bd.exists():
    ruta_bd.unlink()


conn = sqlite3.connect(ruta_bd)

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.executescript("""

CREATE TABLE IF NOT EXISTS habitaciones (

    nombre TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS dispositivos (

    nombre TEXT NOT NULL,
    habitacion_nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    estado INTEGER,

    PRIMARY KEY (habitacion_nombre, nombre),

    FOREIGN KEY (habitacion_nombre)
        REFERENCES habitaciones(nombre)
        ON DELETE CASCADE
);

""")


# Habitaciones iniciales

cursor.executemany(

    "INSERT INTO habitaciones (nombre) VALUES (?)",

    [
        ("Dormitorio",),
        ("Salón",)
    ]
)


# Dispositivos iniciales

cursor.executemany(

    """
    INSERT INTO dispositivos
    (nombre, habitacion_nombre, tipo, estado)

    VALUES (?, ?, ?, ?)
    """,

    [
        ("SensorDormitorio", "Dormitorio", "SENSOR", None),
        ("ActuadorDormitorio", "Dormitorio", "ACTUADOR", 0),

        ("SensorSalon", "Salón", "SENSOR", None),
        ("ActuadorSalon", "Salón", "ACTUADOR", 0)
    ]
)

conn.commit()

conn.close()

print("Base de datos creada correctamente.")