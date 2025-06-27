from baseDatos import operacionesBD

def buscar():
    nombre = input("Introduzca el nombre del usuario que busca")
    lista = operacionesBD.buscarNombre(nombre)
    for u in lista:
        print(f"{u.nombre} {u.apellido1} ({u.email})")
    
def mostarUsuarios():
    lista = operacionesBD.todosLosUsuarios()
    for i in lista:
        print(f"{i[0], i[1], i[2]}")