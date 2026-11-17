
contrasena = "Hola1234"

def comprobar_longitud(contrasena):
    if len(contrasena) >= 8:
        return True
    else:
        return False

print(comprobar_longitud(contrasena))
