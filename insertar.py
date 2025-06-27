import datetime 
import re
from modelos import usuario
from baseDatos import operacionesBD


def registrarUsuario():
    nombre = input("Introduzca el nombre : ")
    apellido1 = input("Introduzca el primer apellido : ")
    apellido2 = input("Introduzca el segundo apellido : ")
    email = input("Introduzca el correo : ")
    if not validarEmail(email):
        print("El email ingresado no es válido.")
        return
    telefono = input("Introduzca el telefono : ")
    direccion = input("Introduzca la dirección : ")
    fecha = datetime.date.today()
    
    u = usuario.Usuario(nombre, apellido1, apellido2, email, telefono, direccion, fecha)
    
    operacionesBD.insert(nombre, apellido1, apellido2, email, telefono, direccion)
    

def validarEmail(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

    
    
    
    
    

    
    

        
    
