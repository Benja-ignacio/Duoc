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
    
def pedir_string(mensaje, formato):
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        print("Formato Incorrecto!")

def pedir_id():
    id_usuario = input("El id debe contener por lo menos:\n- 1 letra y un numero.\n- minimo 4 caracteres y maximo 10.\n- Solo se permiten letras mayusculas.\nIngrese el id: ")
    if not re.fullmatch(r"[A-ZÑ0-9]{6,10}", id_usuario):
        return False
    
    tiene_letra = re.search(r"[A-ZÑ]", id_usuario)
    tiene_numero = re.search(r"[/d]", id_usuario)
    if tiene_letra and tiene_numero:
        return id_usuario



