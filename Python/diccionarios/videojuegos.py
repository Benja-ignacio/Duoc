# Catalogo de videojuegos
import re
from time import sleep as pausa
datos_videojuegos = {"juegos":[]}

def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/macOS

def datos_repetidos(nuevo_juego):
    for i in datos_videojuegos["juegos"]:
        id_repetido = i['id'] == nuevo_juego['id']
        nombre_repetido = i["nombre"] == nuevo_juego['nombre']

        if id_repetido and nombre_repetido:
            print(f"\nNo se logro registrar el juego porque los suguientes datos se encuentran en uso: ID: {i["id"]}, Nombre: {i["nombre"]}\n")
            return True
        elif id_repetido:
            print(f"\nNo se logro registrar el juego porque el siguientes dato se encuentra en uso: {i["id"]}")
            return True
        elif nombre_repetido:
            print(f"\nNo se logro registrar el juego porque el siguiente dato se encuentra en uso: {i["id"]}")
            return True
    return False # Retorna falso si no se encontro nada repetido  

def validar_entero(mensaje:str, min=None, max=None)->int:
    """Validar Entero"""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            limpiar()
            print("Debes ingresar un numero entero.\n")
            continue
        if  min is not None and max is not None:
            if not min <= valor <= max:
                limpiar()
                print(f"El numero ingresado debe estar dentro del rango permitido. {(min,max)}\n")
                continue
        if min is not None and valor < min:
            limpiar()
            print(f"Debe ser >= al minimo. (min = {min})\n")
            continue
        if max is not None and valor > max:
            limpiar()
            print(f"Debe ser <= al maximo. (max = ({max})\n")
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
            break
        datos_videojuegos["juegos"].append(nuevo_juego)
        print(f"\nEl Videojuego {nuevo_juego["nombre"]} ha sido agregado correctamente!")
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
    limpiar()
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
        print("\nNo se encontro ningun juego con el nombre ingresado. Volviendo al menu principal...")
        pausa(2)
        break

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

def modificar_juego():
    if not hay_datos():
        return
    while True:
        id_juego = validar_string("Ingrese el id del juego que desea modificar: ", r"^[a-zA-Z\d]{6}")
        for i in datos_videojuegos["juegos"]:
            if i['id'] == id_juego:
                opcion = validar_entero("\n1. Modificar Nombre\n2. Modificar Plataforma\n3. Modificar año\n4. Salir\n: ", 1, 4)
                if opcion == 1:
                    modificar_nombre = validar_string("Ingrese el nuevo nombre: ", r"^[a-zA-Z\d:. ]{3,64}").capitalize()
                    i["nombre"] = modificar_nombre
                    input("El nombre se ha modificado correctamente!\nPresione enter para volver al menu: ")
                    
                if opcion == 2:
                    modificar_plataforma = validar_string("Ingrese la nueva plataforma del juego: ", r"^[a-zA-Z :.\d]{3,64}").capitalize()
                    i["plataforma"] = modificar_plataforma
                    input("La plataforma se ha modificado correctamente!\nPresione enter para volver al menu: ")
        
                if opcion == 3:
                    modificar_anio =validar_entero("Ingrese el nuevo año de de salida del juego: ", 1950, 2025)
                    i["anio"] = modificar_anio 
                    input("El año se ha modificado correctamente!\nPresione enter para volver al menu: ")
                    
                if opcion == "4":
                    return
        print("No se encontro ningun juego con el id ingresado.\nVolviendo al menu principal...")    
        pausa(1.5)
        break
while True:
    limpiar()
    print("  ***Administrador de juegos***\n")
    opciones = validar_entero("1. Agregar Juegos\n2. Listar los juegos\n3. Buscar por nombre\n4. Eliminar por id\n5. Modificar juego\n6. Salir\n: ", 1,6)
    if opciones == 1:
        agregar_juego()
    elif opciones == 2:
        limpiar()
        mostrar_datos()
    elif opciones == 3:
        limpiar()
        buscar_juego()
    elif opciones == 4:
        limpiar()
        eliminar_juego()
    elif opciones == 5:
        limpiar()
        modificar_juego()
    elif opciones == 6:
        break

