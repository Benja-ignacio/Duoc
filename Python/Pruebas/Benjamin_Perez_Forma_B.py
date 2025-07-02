from time import sleep as pausa
from colorama import Fore, Style

# CARACTERES PERMITIDOS
mayusculas = "QWERTYUIOPÑLKJHGFDSAZXCVBNM"
letras = 'qwertyuiopñlkjhgfdsazxcvbnm'
numeros = "1234567890"

#CARACTERES NO PERMITIDOS
caracter_especial = "~=/.,= -'~`!@#$%^&*()_+][><?;:"

datos = {
    "entradas":[
        {
            "id":"abc1",
            "nombre":"Benjamin",
            "tipo":"G" # o V
        }
    ]
}

def  menu_principal():
    limpiar()
    while True:
        limpiar()
        print(Fore.LIGHTWHITE_EX + " *** GESTION DE ENTRADAS CONCIERTO ***\n", Style.RESET_ALL)
        print(Fore.MAGENTA + "1. Registrar entrada", Style.RESET_ALL)
        print(Fore.LIGHTBLUE_EX + "2. Consultar comprador", Style.RESET_ALL)
        print(Fore.GREEN + "3. Cancelar compra", Style.RESET_ALL)
        print(Fore.YELLOW + "4. Salir", Style.RESET_ALL)

        opcion = pedir_numero("\nIngrese una opcion: ", 1, 4)

        if opcion == 1:
            limpiar()
            registrar_entrada()
        elif opcion == 2:
            limpiar()
            buscar_comprador("Ingrese el nombre del vendedor: ")
        elif opcion == 3:
            limpiar()
            cancelar_reserva()
        elif opcion == 4:
            limpiar()
            print("Programa terminado...")
            pausa(1.5)
            break


def pedir_numero(mensaje:str, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensaje))
        except ValueError:
            print(Fore.RED + "Debes ingresar un numero entero", Style.RESET_ALL)
            continue
        
        if minimo is not None and maximo is not None:
            if not minimo <= numero <= maximo:
                print(Fore.RED + f"El numero debe estar entre {minimo} y {maximo}.", Style.RESET_ALL)
                continue
        if minimo is not None:
            if numero < minimo:
                print(Fore.RED+ f"El numero debe ser igual o mayor a {minimo}.", Style.RESET_ALL)
                continue
        if maximo is not None:
            if numero > maximo:
                print(Fore.RED + f"El numero debe ser igual o menor a {maximo}.", Style.RESET_ALL)
                continue
        return numero
    
def pedir_id(mensaje:str):
    while True:
        id_usuario = input(mensaje).strip()
        if not 6 <= len(id_usuario) <= 10:
            limpiar()
            print(Fore.RED + "El codigo debe tener minimo 6 caracteres y maximo 10.", Style.RESET_ALL)
            continue

        # CARACTERES PERMITIDOS
        tiene_mayuscula = any(c in mayusculas for c in id_usuario)
        tiene_numero = any(c in numeros for c in id_usuario)
        tiene_minusculas = all(c in letras for c in id_usuario)

        # CARACTERES NO PERMITIDOS 
        caracteres_invalidos = any(c in caracter_especial for c in id_usuario)
        
        if caracteres_invalidos:
            print(Fore.RED + "El id NO puede llevar caracteres especiales", Style.RESET_ALL)
            continue
        if tiene_minusculas:
            pass
        if tiene_mayuscula and tiene_numero:
            return id_usuario
        limpiar()
        print(Fore.RED + "El Codigo debe contener al menos una letra mayuscula y un numero.", Style.RESET_ALL)

def validar_id():
    while True:
        id_usuario = pedir_id("Ingrese el codigo de confirmacion: ")
        if any(i['id'] == id_usuario for i in datos["entradas"]):
            print(Fore.RED + "El id ingresado esta en uso. Intente de nuevo.", Style.RESET_ALL)
            continue
        return id_usuario

def tipo_entrada(mensaje:str):
    while True:
        tipo_entrada = input(mensaje).upper().strip()
        if tipo_entrada == "V" or tipo_entrada == "G": 
            return tipo_entrada
        limpiar()
        print(Fore.RED + "Tipo de entrada invalida. Debe ingresar 'G' para general o 'V' para vip.", Style.RESET_ALL)
    
def validar_nombre(mensaje):
    while True:
        nombre = input(mensaje).capitalize().strip()

        if not 3 <= len(nombre) <= 52:
            limpiar()
            print(Fore.RED + "El nombre debe tener minimo 3 caracteres y maximo 52.", Style.RESET_ALL)
            continue
        
        if any(i['nombre'].lower() == nombre.lower() for i in datos["entradas"]):
            limpiar()
            print(Fore.RED + "El nombre ingresado ya esta en uso. Intente nuevamente.", Style.RESET_ALL)
            continue
        
        if all(c in letras for c in nombre):
            return nombre
        limpiar()
        print(Fore.RED + "El nombre solo debe llevar letras.", Style.RESET_ALL)

def registrar_entrada():
    while True:
        nueva_entrada = {
            "id":validar_id(),
            "nombre":validar_nombre("Ingrese el nombre: "),
            "tipo":tipo_entrada("Ingrese el tipo de entrada: ")
        }

        datos["entradas"].append(nueva_entrada)
        input("\nEntrada registrada exitosamente!!\nPresione enter para volver al menu principal: ")
        return

def buscar_comprador(mensaje:str):
    if not hay_datos():
        return
    while True:
        nombre = input(mensaje).strip().capitalize()
        for i in datos["entradas"]:
            if i['nombre'] == nombre:
                print(Fore.LIGHTWHITE_EX + " *** DATOS DE LA RESERVA ***", Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX + f"Tipo de entrada: {i['tipo']}\nCodigo de confirmacion: {i['id']}\nNombre: {i['nombre']}", Style.RESET_ALL)
                input("\nPresione enter para volver al menu principal: ")
                return
        limpiar()
        print(Fore.RED + "El comprador no se encontro.", Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + "\nSi desea salir escriba 'salir'.\n", Style.RESET_ALL)
        if nombre == 'salir':
            return

def cancelar_reserva():
    if not hay_datos():
        return
    while True:
        nombre = input("Ingrese el nombre de la reserva a cancelar: ").capitalize().strip()
        limpiar()
        for i in datos["entradas"]:
            if i['nombre'] == nombre:
                datos["entradas"].remove(i)
                print(Fore.LIGHTWHITE_EX + "Reserva cancelada correctamente!", Style.RESET_ALL)
                input("Presione enter para volver al menu principal: ")
                return
        if nombre == 'Salir':
            return
        print(Fore.RED + "Nombre no encontrado. Intente nuevamente.", Style.RESET_ALL)
        print(Fore.RED + "\nSi desea salir al menu pricipal escriba 'salir'", Style.RESET_ALL)


def hay_datos():
    if not datos["entradas"]:
        print(Fore.LIGHTWHITE_EX + "No existen datos registrados.\nVolviendo al menu principal...", Style.RESET_ALL)
        pausa(1.5)
        return False
    return True

def limpiar():
    import os

    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')  

menu_principal()
        