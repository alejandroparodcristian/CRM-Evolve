import sqlite3

def conexion():
    Conexion = sqlite3.connect("CRM_Evolve.db")
    return Conexion

con = conexion()

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR NOT NULL,
        apellido1 VARCHAR NOT NULL,
        apellido2 VARCHAR NOT NULL,
        email VARCHAR NOT NULL UNIQUE,
        telefono VARCHAR,
        direccion VARCHAR,
        fecha_registro DATE DEFAULT CURRENT_DATE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS factura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        numFactura VARCHAR NOT NULL UNIQUE,
        fechaEmision DATE DEFAULT CURRENT_DATE,
        descripcion VARCHAR NOT NULL UNIQUE,
        montoTotal INTEGER,
        estado VARCHAR(20) NOT NULL CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')),
        FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id)
    )
''')

con.commit()
con.close()
