datos = {
    "juegos":[
        {
            "id":"abc1",
            "nombre":"Counter:Strike",
            "año":2011,
            "genero":"FPS"
        }
    ]
}

# Caracteres permitidos
letras = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
numeros = "1234567890"

def menu_principal():
    while True:
        print(" *** Bienvenido al gestionador de juegos!! ***")
        print("\n *** MENU PRINCIPAL ***")
        opcion = pedir_entero("1. Agregar juego\n2. Mostrar juegos\n3. Buscar juego\n4. Eliminar juego\n5. Salir\n: ", 1, 5)
        if opcion == 1:
            agregar_juego()
        elif opcion == 2:
            mostrar_datos()
        elif opcion == 3:
            buscar_juego()
        elif opcion == 4:
            eliminar_juego()
        elif opcion == 5:
            break

def pedir_id(id_usuario:str):
    """Pide ID hasta que sea valido"""
    while True:
        id_user = input(id_usuario)
        if not 2 <= len(id_user) <= 12:
            print("El ID debe tener minimo 2 y maximo 12 caracteres.")
            continue
        tiene_letra = any(caracter in letras for caracter in id_user)
        tiene_numero = any(caracter in numeros for caracter in id_user)
        if tiene_letra and tiene_numero:
            return id_user
        print("El Id debe contener al menos una letra y un numero.")

def validar_id():
    """Valida si el ID esta repetido"""
    while True:
        id_usuario  = pedir_id("Ingrese el id: ")
        if any(i['id'] == id_usuario for i in datos["juegos"]):
            print("El id ingresado se encuentra en uso.")
            continue
        return id_usuario

def mostrar_datos():
    if not hay_datos():
        return
    
    for i in datos["juegos"]:
        print(f"\nID: {i['id']}\nNombre: {i['nombre']}\nAño: {i['año']}\nGenero: {i['genero']}")
    input("\nPresione enter para volver al menu principal: ")

def hay_datos():
    if not datos["juegos"]:
        print("No hay datos registrados. Volviendo al menu principal...")
        return False
    return True

def eliminar_juego():
    if not hay_datos():
        return
    while True:
        juego_a_eliminar = pedir_id("Ingrese el id del juego a eliminar: ")
        for i in datos["juegos"]:
            if i['id'] == juego_a_eliminar:
                datos["juegos"].remove(i)
                input(f"\nEl juego ({i['nombre']}) ha sido eliminado correctamente.\nPresione enter para volver al menu: ")
                return
        print("El id ingresado no se encontro. Vuelva a intentar.")

def pedir_entero(mensaje:str, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero ingresado debe estar entre {minimo}, {maximo}")
                continue
        if minimo is not None:
            if entero < minimo:
                print(f"El numero ingresado debe ser mayor o igual al minimo, {minimo}")
                continue
        if maximo is not None:
            if entero > maximo:
                print(f"El numero ingresado debe ser menor o igual al maximo, {maximo}")
                continue
        return entero

def buscar_juego():
    if not hay_datos():
        return
    while True:
        juego_a_mostrar = pedir_id("Ingrese el id del juego: ")
        for i in datos["juegos"]:
            if i['id'] == juego_a_mostrar:
                print(f"\nID: {i['id']}\nNombre: {i['nombre']}\nAño: {i['año']}\nGenero: {i['genero']}")
                input("\nPresione enter para volver al menu principal: ")
                return
        print("El ID ingresado no se encontro. Vuelva a intentar.")

def validar_nombre_juego(mensaje:str):
    while True:
        caracteres_permitidos = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890 :@-."
        nombre_juego = input(mensaje)
        if any(i['nombre'].lower() == nombre_juego.lower() for i in datos["juegos"]):
            print("El nombre de juego esta en uso.")
            continue
        if all(caracter in caracteres_permitidos for caracter in nombre_juego):
            return nombre_juego
        print(f"El nombre solo debe tener caracteres permitidos.\nCaracteres permitidos: {caracteres_permitidos}")

def validar_genero_juego(mensaje:str):
    while True:
        caracteres_permitidos = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM "
        genero = input(mensaje).capitalize()
        if not 3 <= len(genero) <= 64:
            print("El genero debe tener minimo 3 caracteres y  maximo 64.")
            continue
        if all(caracter in caracteres_permitidos for caracter in genero):
            return genero
        print("Debes ingresar un genero de juego valido.")

def agregar_juego():
    while True:
        agregar_juego = {
            "id":validar_id(),
            "nombre":validar_nombre_juego("Ingrese el nombre del juego: "),
            "año":pedir_entero("Ingrese el año de publicacion del juego: ", 1800, 2025),
            "genero":validar_genero_juego("Ingrese el genero del juego: ")
        }

        datos["juegos"].append(agregar_juego)
        print("Juego agregado correctamente!")
        input("Presione enter para volver al menu principal: ")
        return

menu_principal()