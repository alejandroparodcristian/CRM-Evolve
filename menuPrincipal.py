import insertar
import buscar
import operacionesFactura
continuar = True
while(continuar):
    print("""
    === SISTEMA CRM ===
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
          """)
    opcion = int(input("Introduzca una opción"))
    if(opcion == 7):
        continuar = False
    elif(opcion == 1):
        insertar.registrarUsuario()
    elif(opcion == 2):
        buscar.buscar()
    elif(opcion == 3):
        operacionesFactura.crearFactura()
    elif(opcion == 4):
        buscar.mostarUsuarios()
    elif(opcion == 5):
        operacionesFactura.facturasDeUsuario()
    elif(opcion == 6):
        operacionesFactura.resumenFinanciero()
    else:
        print("Introduzca una opcion válida")
        