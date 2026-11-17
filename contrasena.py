
from utilidades import comprobar_numero

contrasena = "Hola1234"

def comprobar_longitud(contrasena):
    if len(contrasena) >= 12:
        return True
    else:
        return False

def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False

print(comprobar_longitud(contrasena))
print(comprobar_numero(contrasena))
print(comprobar_mayuscula(contrasena))
