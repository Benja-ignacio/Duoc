# Catalogo de videojuegos
import re
from time import sleep as pausa
datos_videojuegos = {"juegos":[]}

def datos_repetidos(nuevo_juego):
    for i in datos_videojuegos["juegos"]:
        id_repetido = i['id'] == nuevo_juego['id']
        nombre_repetido = i["nombre"] == nuevo_juego['nombre']

        if id_repetido and nombre_repetido:
            print(f"No se logro registrar el juego porque los suguientes datos se encuentran en uso: ID: {i["id"]}, Nombre: {i["nombre"]}\n")
            return True
        elif id_repetido:
            print(f"No se logro registrar el juego porque el siguientes dato se encuentra en uso: {i["id"]}")
            return True
        elif nombre_repetido:
            print(f"No se logro registrar el juego porque el siguiente dato se encuentra en uso: {i["id"]}")
            return True
    return False # Retorna falso si no se encontro nada repetido  

def validar_entero(mensaje:str, min=None, max=None)->int:
    """Validar Entero"""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if  min is not None and max is not None:
            if not min <= valor <= max:
                print(f"El numero ingresado debe estar dentro del rango permitido. {(min,max)}")
                continue
        if min is not None and valor < min:
            print(f"Debe ser >= al minimo. (min = {min})")
            continue
        if max is not None and valor > max:
            print(f"Debe ser <= al maximo. (max = ({max})")
            continue
        return valor

def validar_string(mensaje:str, formato)->str:
    """Validar string"""
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        print("Formato incorrecto!")

def agregar_juego():
    while True:
        nuevo_juego = {
            "id":validar_string("Ingrese el id del juego. Deben ser 6 caracteres alfanumericos: ", r"^[a-zA-Z\d]{6}"),
            "nombre":validar_string("Ingrese el nombre del juego: ", r"^[a-zA-Z\d:. ]{3,64}").capitalize(),
            "plataforma":validar_string("Ingrese la plataforma del juego: ", r"^[a-zA-Z :.\d]{3,64}").capitalize(),
            "anio":validar_entero("Ingrese el año de de salida del juego: ", 1950, 2025)
        }
        
        if datos_repetidos(nuevo_juego):
            continue
        datos_videojuegos["juegos"].append(nuevo_juego)
        print(f"El Videojuego {nuevo_juego["nombre"]} ha sido agregado correctamente!")
        input("Presione enter para volver al menu principal: ")
        break

def hay_datos():
    if not datos_videojuegos["juegos"]:
        print("No hay datos registrados. Volviendo al menu principal...")
        pausa(1.5)
        return False
    return True

def mostrar_datos():
    if not hay_datos():
        return
    for i in datos_videojuegos["juegos"]:
        print(f"ID: {i['id']}")
        print(f"Nombre: {i['nombre']}")
        print(f"Plataforma: {i['plataforma']}")
        print(f"Año: {i['anio']}\n")
    input("\nPresione enter para volver al menu: ")

def buscar_juego()->str:
    if not hay_datos():
        return
    while True:
        nombre = validar_string("Ingrese el nombre del juego: ", r"^[a-zA-Z\d:. ]{3,64}").capitalize()
        for i in datos_videojuegos["juegos"]:
            if i["nombre"] == nombre:
                print("Juego encontrado!... Mostrando datos")
                print(f"ID: {i["id"]}, Nombre: {i["nombre"]}, Plataforma: {i["plataforma"]}, Año: {i["anio"]}")
                input("\nPresione enter para volver al menu: ")
                return
        print("No se encontro ningun juego con el nombre ingresado.")
        continue

def eliminar_juego():
    if not hay_datos():
        return
    while True:
        id_juego = validar_string("Ingrese el id del juego. Deben ser 6 caracteres alfanumericos: ", r"^[a-zA-Z\d]{6}")
        for i in datos_videojuegos["juegos"]:
            if i["id"] == id_juego:
                datos_videojuegos["juegos"].remove(i) 
            print(f"El juego {i["nombre"]} ha sido eliminado correctamente.")
            input("Presione enter para volver al menu: ")
            return
        print("No se encontro ningun juego con el id ingresado.")
        continue

while True:
    print("***Administrador de juegos***")
    try:
        opciones = int(input("1. Agregar Juegos\n2. Listar los juegos\n3. Buscar por nombre\n4. Eliminar por id\n5. Salir\n: "))
    except ValueError:
        print("Debes ingresar una opcion valida. (1-5)")
        continue
    if not 1 <= opciones <= 5:
        print("Debes ingresar una opcion valida. (1-5)")
        continue
    if opciones == 1:
        agregar_juego()
    elif opciones == 2:
        mostrar_datos()
    elif opciones == 3:
        buscar_juego()
    elif opciones == 4:
        eliminar_juego()
    elif opciones == 5:
        break

