# Sistema de Biblioteca con usuarios y prestamos
#NOTE GUARDAR LOS DATOS EN UN ARCHIVO BIBLIOTECA.JSON
import re, json
from time import sleep as pausa
from colorama import Fore, Style

biblioteca = {
    "libros":[
        {
            "id": "L001",
            "titulo": "1984",
            "autor": "George Orwell",
            "prestado": False
        }
    ],
    "usuarios":[
        {
            "id": "U001", 
            "nombre": "Benjamin"
        }
    ],
    "prestamos":[
        {
            "usuario_id": "U001", 
            "Libro_id": "L001"
        }
    ]
}

def menu_principal():
    while True:
        print("*** SISTEMA DE BIBLIOTECA ***\n")
        try:
            opciones = int(input("1. Registrar libro\n2. Registrar usuario\n3. Prestar libro\n4. Devolver libro\n5. Ver libros prestados y disponibles\n6. salir\n: "))
        except ValueError:
            print("Debes ingresar una opcion valida. 1-6")
            continue
        if opciones == 1:
            print("opc1")
        elif opciones == 2:
            print("opc1")
        elif opciones == 3:
            print("opc1")
        elif opciones == 4:
            print("opc1")
        elif opciones == 5:
            print("opc1")
        elif opciones == 6:
            return
        else:
            print("Debes ingresar una opcion valida. (1-6)")
            continue
    
def pedir_string(mensaje, formato,error:str):
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        print(error)
        continue

def pedir_id():
    while True:
        limpiar()
        print(Fore.LIGHTWHITE_EX + "El id debe contener por lo menos: ", Style.RESET_ALL, Fore.RED + "\n- 1 letra y un numero.\n- minimo 4 caracteres y maximo 10.\n- Solo se permiten letras mayusculas.", Style.RESET_ALL)
        id_usuario = input("\nIngrese el id: ")
        if not re.fullmatch(r"[A-ZÑ0-9]{4,10}", id_usuario):
            limpiar()
            print(Fore.RED + "El id ingresado no es valido.", Style.RESET_ALL)
            input("Presione enter para volver a intentarlo: ")
            continue
        tiene_letra = re.search(r"[A-ZÑ]", id_usuario)
        tiene_numero = re.search(r"[\d]", id_usuario)
        if tiene_letra and tiene_numero:
            return id_usuario


def validar_id_libro():
    while True:
        id_libro = pedir_id()
        if any(i['id'] == id_libro for i in biblioteca["libros"]):
            print("El id ingresado se encuentra en uso. Intente de nuevo.")
            continue
        return id_libro

def validar_id_usuario():
    while True:
        id_usuario = pedir_id()
        if any(i['id'] == id_usuario for i in biblioteca["usuarios"]):
            print("El id ingresado se encuentra en uso. Intente de nuevo.")
            continue
        return id_usuario

def limpiar():
    import os
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/macOS

def libro_estado():
    while True:
        estado = input("Ingrese el estado del libro (Disponible/Prestado): ").lower()
        if estado == "disponible":
            return estado
        elif estado == "prestado":
            return estado
        print("Debes ingresar Disponible o Prestado.")
        continue

def registrar_libro():
    while True:
        nuevo_libro = {
            "id":validar_id_libro(),
            "titulo":pedir_string("Ingrese el titulo: ", r"[a-zA-Z \d.:@\-;]{2,100}", "Debes ingresar un titulo valido.").capitalize(),
            "autor":pedir_string("Ingrese el autor: ", r"[a-zA-Z ]{6,100}", "Solo se permiten letras y minimo 6 caracteres.").capitalize(),
            "estado":libro_estado()
        }
        biblioteca["libros"].append(nuevo_libro)
        print("Libro agregado correctamente!")
        input("\nPresione enter para volver al menu principal: ")
        return


def hay_datos():
    limpiar()
    if not biblioteca["libros"]:
        print("No hay Libros registrados. Volviendo al menu principal...")
        pausa(1.5)
        return False
    return True