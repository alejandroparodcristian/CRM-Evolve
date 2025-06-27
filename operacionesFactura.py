from baseDatos import operacionesBD

def crearFactura():
    email = input("Ingrese el email del usuario: ")
    usuario = operacionesBD.buscarPorEmail(email)

    if not usuario:
        print("Usuario no encontrado.")
        return

    descripcion = input("Ingrese descripción del servicio/producto: ")
    
    try:
        montoTotal = float(input("Ingrese el monto total: "))
        if montoTotal <= 0:
            raise ValueError
    except ValueError:
        print("El monto debe ser un número positivo.")
        return

    e = int(input("""
Seleccione el estado:
1. Pendiente
2. Pagada
3. Cancelada
          """))
    if(e == 1):
        estado = "Pendiente"
    elif(e == 2):
        estado = "Pagada"
    elif(e == 3):
        estado = "Cancelada"
    else:
        print("Opción de estado no válida.")
        return

    numFactura = operacionesBD.generarIdFactura()
    operacionesBD.insertarFactura(usuario["usuario_id"], numFactura, descripcion, montoTotal, estado)

    print(f"""
Factura creada exitosamente.
Número: {numFactura}
Cliente: {usuario['nombre']} {usuario['apellido1']}
Descripción: {descripcion}
Monto: ${montoTotal}
Estado: {estado}
""")
    
def facturasDeUsuario():
    email = input("Ingrese el email del usuario: ")
    usuario = operacionesBD.buscarPorEmail(email)
    if not usuario:
        print("Usuario no encontrado.")
        return

    facturas = operacionesBD.facturasPorUsuario(usuario["usuario_id"])
    if not facturas:
        print("No hay facturas registradas para este usuario.")
        return

    print(f"\n--- FACTURAS DE {usuario['nombre']} {usuario['apellido1']} ---")
    for i in facturas:
        print(f"""
        Numero de factura : {i[0]}, 
        Fecha : {i[1]},
        Descripcion : {i[2]},
        Monto Total : {i[3]}, 
        Estado : {i[4]}""")


def resumenFinanciero():
    resumen = operacionesBD.obtenerResumenFinanciero()
    if not resumen:
        print("No hay datos financieros disponibles.")
        return

    print("\n=== RESUMEN FINANCIERO POR USUARIO ===")
    for r in resumen:
        print(f"""
Usuario: {r[0]} ({r[1]})
- Total facturas: {r[2]}
- Monto total: ${r[3]}
- Pagado: ${r[4]}
- Pendiente: ${r[5]}
""")

    
    