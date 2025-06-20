import re
from time import sleep as pausa

datos_estudiantes = {
    "estudiantes":[]
}

# Validar estudiante
def validar_entero(mensaje:str, minimo=None, maximo=None)->int:
    """Validar el entero ingresado"""
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe estar dentro del rango permitido. {minimo,maximo}")
                continue
        elif minimo is not None:
            if entero < minimo:
                print(f"EL numero debe ser mayor o igual al minimo. minimo: {minimo}")
                continue
        elif maximo is not None:
            if entero > maximo:
                print(f"El numero debe ser mayor o igual que el maximo. maximo: {maximo}")
                continue
        return entero
def validar_genero()->str:
    while True:
        genero = input("Ingrese el genero del estudiante (F/M): ").upper()
        if genero == "F" or genero == "M":
            return genero
        else:
            print("Debes ingresar un genero valido.")
            continue
def validar_nombre(mensaje:str)->str:
    while True:
        nombre = input(mensaje).capitalize()
        if not re.fullmatch(r"^[A-Z][a-z ]{2,28}$", nombre):
            print("Solo debe llevar letras y tener minimo 3 caracteres y maximo 28.")
            continue
        if any(estudiante["nombre"] == nombre for estudiante in datos_estudiantes["estudiantes"]):
            print("El nombre ingresado se encuentra en uso.")
            continue
        return nombre
def validar_promedio(mensaje:str)->bool:
    while True:
        try:
            promedio = bool(input(mensaje))       
        except ValueError:
            print("El promedio debe estar dentro del rango. (1.0 - 7.0)")
            continue
        if not 1.0 <= promedio <= 7.0:
            print("El promedio debe estar dentro del rango. (1.0 - 7.0)")
            continue
        return promedio
def validar_codigo(mensaje:str)->str:
    while True:
        codigo = input(mensaje)
        if not re.fullmatch(r"^[a-zA-Z\d]{6}$", codigo):
            print("EL codigo solo debe llevar letras y numeros y debe tener 6 caracteres.")
            continue
        return codigo

def verificar_si_registros_de_estudiantes()->bool:    
    """Verifica si hay datos existentes"""
    if len(datos_estudiantes["estudiantes"]) == 0:
        print("No hay datos de estudiantes registrados\nVolviendo al menu principal...")
        return False
    return True

def registrar_estudiantes():
    id_estudiante = validar_codigo("Ingrese el codigo del estudiante.\nDebe contener 6 caracteres y solo se aceptan letras y numeros.\n: ")
    nombre = validar_nombre("Ingrese el nombre del estudiante: ")
    edad = validar_entero("Ingrese la edad del estudiante: ", minimo=12, maximo=80)
    genero = validar_genero()
    promedio = validar_promedio("Ingrese el promedio del estudiante: ")
    
    agregar_estudiante = {
        "id":id_estudiante,
        "nombre":nombre,
        "edad":edad,
        "genero":genero,
        "promedio":promedio
    }
    datos_estudiantes["estudiantes"].append(agregar_estudiante)
    print("Estudiante Agregado!")
    input("Presione enter para volver al menu principal... ")

while True:
    print("*** Bienvenido al registro de estudiantes! ***")
    print("Opciones\n1. Registrar estudiante\n2. Buscar estudiante\n3. Modificar datos de estudiante\n4. ELiminar estudiante\n5. Mostrar todos los estudiantes\n6. Salir")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Debes ingresar una opcion valida. (1-6)")
        continue
    if not 1 <= opcion <= 6:
        print("Debes ingresar una opcion valida. (1-6)")
        continue
    if opcion == 1:
        registrar_estudiantes()