from modelos import usuario
from baseDatos.crearTablas import conexion as crear_conexion


con = crear_conexion()
cursor = con.cursor()

def insert(nombre, apellido1, apellido2, email, telefono, direccion):
    
    cursor.execute(""" 
    Insert into usuarios (nombre, apellido1, apellido2, email, telefono, direccion) 
    VALUES ( ? , ? , ? , ?, ?, ?)                   
                   """, (nombre, apellido1, apellido2, email, telefono, direccion))
    
    con.commit()    


def buscarNombre(nombre):
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
    resultados = cursor.fetchall()

    lista_usuarios = []
    for fila in resultados:
        u = usuario.Usuario(
            fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]
        )
        lista_usuarios.append(u)
    return lista_usuarios

def buscarPorEmail(email):
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    fila = cursor.fetchone()
    if fila:
        return {
            "usuario_id": fila[0],
            "nombre": fila[1],
            "apellido1": fila[2],
            "apellido2": fila[3],
            "email": fila[4],
            "telefono": fila[5],
            "direccion": fila[6],
            "fechaRegistro": fila[7]
        }
    return None


def todosLosUsuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()


def generarIdFactura():
    cursor.execute("SELECT MAX(id) FROM factura")
    resultado = cursor.fetchone()
    ultimo_id = resultado[0] if resultado[0] is not None else 0
    nuevo_id = ultimo_id + 1
    return f"FAC{nuevo_id}"

def insertarFactura(usuario_id, numFactura, descripcion, monto, estado):
    cursor.execute("""
        INSERT INTO factura (usuario_id, numFactura, descripcion, montoTotal, estado)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario_id, numFactura, descripcion, monto, estado))
    con.commit()


def facturasPorUsuario(usuario_id):
    cursor.execute("""
        SELECT numFactura, fechaEmision, descripcion, montoTotal, estado
        FROM factura WHERE usuario_id = ?
    """, (usuario_id,))
    return cursor.fetchall()

def obtenerResumenFinanciero():
    cursor.execute("""
        SELECT u.nombre, u.email,
            COUNT(f.id) as total_facturas,
            SUM(f.montoTotal) as total,
            SUM(CASE WHEN f.estado = 'Pagada' THEN f.montoTotal ELSE 0 END) as pagado,
            SUM(CASE WHEN f.estado = 'Pendiente' THEN f.montoTotal ELSE 0 END) as pendiente
        FROM usuarios u
        LEFT JOIN factura f ON u.usuario_id = f.usuario_id
        GROUP BY u.usuario_id
    """)
    return cursor.fetchall()