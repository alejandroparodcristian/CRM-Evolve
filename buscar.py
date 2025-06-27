from baseDatos import operacionesBD

def buscar():
    nombre = input("Introduzca el nombre del usuario que busca: \n")
    lista = operacionesBD.buscarNombre(nombre)
    for u in lista:
        print(f""" 
Nombre : {u.nombre}
Primer Apellido : {u.apellido1}
Segundo Apellido : {u.apellido2}
Correo : {u.email}
Telefono : {u.telefono}
Dirección : {u.direccion}
Fecha Registro : {u.fechaRegistro}
""")
        
def buscarEmail():
    email = input("Introduzca el email del usuario que busca: \n")
    usuario = operacionesBD.buscarPorEmail(email)
    nombre = usuario["nombre"]
    print(f""" 
Nombre : {nombre}
Primer Apellido : {usuario["apellido1"]}
Segundo Apellido : {usuario["apellido2"]}
Correo : {usuario["email"]}
Telefono : {usuario["telefono"]}
Dirección : {usuario["direccion"]}
Fecha Registro : {usuario["fechaRegistro"]}
""")
        
    
def mostarUsuarios():
    lista = operacionesBD.todosLosUsuarios()
    for i in lista:
        print(f"{i[0], i[1], i[2]}")