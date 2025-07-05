from . import validaciones


from time import sleep as pausa
from colorama import Fore, Style
import re, json

def menu_principal(biblioteca):
    while True:
        print("*** SISTEMA DE BIBLIOTECA ***\n")
        opciones = pedir_entero("1. Registrar libro\n2. Registrar usuario\n3. Prestar libro\n4. Devolver libro\n5. Ver libros prestados\n6. Ver libros disponibles\n7. salir\n: ",1, 7)
        if opciones == 1:
            registrar_libro(biblioteca)
        elif opciones == 2:
            print("opc")
        elif opciones == 3:
            print("opc1")
        elif opciones == 4:
            print("opc1")
        elif opciones == 5:
            print("opc1")
        elif opciones == 6:
            print("opc2")
        elif opciones == 7:
            return
        else:
            print("Debes ingresar una opcion valida. (1-6)")
            continue
    

def pedir_string(mensaje, formato):
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        print("Formato de texto invalido. asegurese de ingresar caracteres validos.")
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

def pedir_id(usuario_id, biblioteca):
    while True:
        usuario_id = input(usuario_id)

        if validaciones.existe_usuario(usuario_id):
            for i in biblioteca['usuarios']:
                if i['id'] == usuario_id:
                    return usuario_id
        print("Id de usuario no encontrado.")
        continue

def pedir_libro_id(biblioteca):
    while True:
        libro_id = input("Ingrese el ID: ").strip()

        tiene_letra = re.search(r"[A-Z]", libro_id)
        tiene_numero = re.search(r"\d", libro_id) 
        if not re.fullmatch(r"[A-Z\d]{4,10}", libro_id):
            print("El ID debe tener 1 letra, un numero, solo letras mayusculas y un minimo de 4 caracteres y maximo 10.")
            continue
        if validaciones.existe_libro_id(libro_id, biblioteca):
            print("El ID ingresado se encuentra en uso.\nVuelva a intentarlo.")
            continue
        if tiene_letra and tiene_numero:
            return libro_id
        print("El ID debe tener 1 letra, un numero, solo letras mayusculas y un minimo de 4 caracteres y maximo 10.")

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

def registrar_libro(biblioteca):
    while True:
        nuevo_libro = {
            "id":pedir_libro_id(biblioteca),
            "nombre":pedir_string("Ingrese el titulo del libro: ", r"^[A-Za-z \d.:-@,]{2,100}").capitalize(),
            "autor":pedir_string("Ingrese el nombre del autor: ", r"^[A-Za-z \d]{6,64}").capitalize(),
            "estado":libro_estado(),
        }
        biblioteca['libros'].append(nuevo_libro)
        input("Libro agregado correctamente!\nPresione enter para volver al menu principal: ")
        return