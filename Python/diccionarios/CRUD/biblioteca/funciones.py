import biblioteca, validaciones

from time import sleep as pausa
from colorama import Fore, Style
import re, json


def pedir_string(mensaje, formato):
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        continue


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar numeros enteros.")
            continue
        
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe estar dentro del rango de {minimo, maximo}.")
                continue
        elif minimo is not None:
            if entero < minimo:
                print(f"EL numero debe ser mayor o igual a {minimo}.")
                continue
        elif maximo is not None:
            if entero > maximo:
                print(f"EL numero debe ser menor o igual a {maximo}.")
                continue
        return entero

def libro_estado():
    while True:
        estado = input("Ingrese el estado del libro (Disponible/Prestado): ").lower()
        if estado == "disponible":
            return estado
        elif estado == "prestado":
            return estado
        print("Debes ingresar Disponible o Prestado.")
        continue

def pedir_id(usuario_id):
    while True:
        usuario_id = input(usuario_id)

        if validaciones.existe_usuario(usuario_id):
            for i in biblioteca['usuarios']:
                if i['id'] == usuario_id:
                    return usuario_id
        print("Id de usuario no encontrado.")
        continue

def pedir_libro_id():
    while True:
        libro_id = input("Ingrese el ID: ")
        if not re.fullmatch(libro_id, r"[A-Z/D]{4,10}"):
            print("El ID debe tener 1 letra, un numero, solo letras mayusculas y un minimo de 4 caracteres y maximo 10.")
            continue



        if validaciones.existe_libro_id(libro_id):
            print("El ID ingresado se encuentra en uso.\nVuelva a intentarlo.")
            continue
        return libro_id


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
            "id":pedir_libro_id(),
            "nombre":,
            "autor":,
            "titulo":,
        }