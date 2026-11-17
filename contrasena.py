
contrasena = "Hola1234"

def comprobar_longitud(contrasena):
    if len(contrasena) >= 8:
        return True
    else:
        return False

def comprobar_mayuscula(contrasena):
    for caracter in contrasena:
        if caracter.isupper():
            return True
    return False

print(comprobar_longitud(contrasena))
print(comprobar_mayuscula(contrasena))
