# Sistema de gestion de estudiantes 
from time import sleep as pausa

datos_estudiantes = {
    "estudiantes":[]
}

def validar_entero(mensaje:str, minimo=None, maximo=None)->int:
    """Validar entero"""
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe estar dentro el rango permitido. {minimo,maximo}")
                continue
        if minimo is not None:
            if not entero >= minimo:
                print(f"El numero debe ser mayor o igual al minimo. (minimo: {minimo})")
                continue
        if maximo is not None:
            if not entero <= maximo:
                print(f"El numero debe ser menor o igual al maximo. (maximo: {maximo})")
                continue
        return entero

def validar_string(mensaje:str)->str:
    while True:
        string = input(mensaje).strip()
        if not string.isalpha():
            print("no debe llevar numeros ni caracteres especiales")
            continue
        if not 3 <= len(string) <= 48:
            print("Debe estar dentro del rango de los caracteres permitidos. (3 - 48)")
            continue
        return string

def validar_genero()->str:
    while True:
        genero = input("Ingrese su genero (F/M): ").strip().upper()
        if genero == "F" or genero == "M":
            return genero
        else:
            continue

def validar_nombre()->str:
    while True:
        nombre_estudiante = validar_string("Ingrese el nombre del estudiante: ")
        if  any(nombre["nombre"] == nombre_estudiante for nombre in datos_estudiantes["estudiantes"]):
            print("El nombre ya se encuentra en uso.")
            continue
        return nombre_estudiante

def validar_promedio_notas()->float:
    while True:
        try:
            promedio_notas = float(input("Ingrese el promedio de las notas: "))
        except ValueError:
            print("Debes ingresar un valor dentro del rango de notas. (1.0 - 7.0)")
            continue
        if not 1.0 <= promedio_notas <= 7.0:
            print("El promedio debe estar dentro del rango de notas. (1.0 - 7.0)")
            continue
        return promedio_notas

def validar_id()->str:
    while True:
        caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ0123456789"
        codigo_estudiante = input("Ingrese el id del estudiante (Deben ser 6 caracteres alfanumericos): ").strip()
        for i in codigo_estudiante:
            if i not in caracteres_permitidos:
                print("El codigo de estudiante solo debe llevar caracteres alfanumericos. (Letras y Numeros)")
                continue
        if any(estudiante["id"] == codigo_estudiante for estudiante in datos_estudiantes["estudiantes"]):
            print("El id ingresado ya se encuentra en uso.")
            continue
        if len(codigo_estudiante) == 6:
            return codigo_estudiante
        else:
            print("El codigo del estudiante debe llevar 6 caracteres alfanumericos.")
            continue

def agregar_estudiante():
    nombre_estudiante = validar_nombre()
    edad_estudiante = validar_entero("Ingrese la edad del estudiante: ", minimo=12, maximo=80)
    genero_estudiante = validar_genero()
    id_estudiante = validar_id()
    promedio_estudiante = validar_promedio_notas()

    agregar_estudiante = {
        "id":id_estudiante,
        "nombre":nombre_estudiante,
        "edad":edad_estudiante,
        "genero":genero_estudiante,
        "promedio":promedio_estudiante
    }
    datos_estudiantes["estudiantes"].append(agregar_estudiante)
    print("Estudiante creado!\nVolviendo al menu principal...")
    pausa(1)

def mostrar_todos_los_estudiante():
    for i in datos_estudiantes["estudiantes"]:
        print(f"ID = {i["id"]}")
        print(f"Nombre = {i["nombre"].capitalize()}")
        print(f"Edad = {i["edad"]}")
        print(f"Genero = {i["genero"]}")
        print(f"Promedio = {i["promedio"]}")
    input("\nPresione enter para volver al menu principal: ")

def buscar_estudiante():
    while True:
        buscar = input("Ingrese el id o nombre del estudiante: ")
        for i in datos_estudiantes["estudiantes"]:
            if i["id"] == buscar or i["nombre"] == buscar:
                    print(f"ID = {i["id"]}")
                    print(f"Nombre = {i["nombre"].capitalize()}")
                    print(f"Edad = {i["edad"]}")
                    print(f"Genero = {i["genero"]}")
                    print(f"Promedio = {i["promedio"]}")
                    input("\nPresione enter para volver al menu principal: ")
                    return
        else:
            print("Estudiante no encontrado.")
            pausa(1)
            break

def eliminar_estudiante():
    while True:
        id_estudiante = input("Ingrese el id del estudiante: ")
        if any(estudiante["id"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
            for estudiante in datos_estudiantes["estudiantes"]:
                if estudiante["id"] == id_estudiante:
                    datos_estudiantes["estudiantes"].remove(id_estudiante)
            print("\nEl estudiante ha sido eliminado.")
            input("Presione enter para volver al menu principal...")
            return
        else:
            print("Estudiante no encontrado.")
            continue


def modificar_estudiante():
    while True:
        caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ0123456789"
        codigo_estudiante = input("Ingrese el id del estudiante (Deben ser 6 caracteres alfanumericos): ").strip()
        for i in codigo_estudiante:
            if i not in caracteres_permitidos:
                print("El codigo de estudiante solo debe llevar caracteres alfanumericos. (Letras y Numeros)")
                continue
        if not len(codigo_estudiante) == 6:
            print("El codigo de estudiante debe llevar 6 caracteres.")
            continue
        if any(estudiante["id"] == codigo_estudiante for estudiante in datos_estudiantes["estudiantes"]):
            print("1. Modificar Edad")
            print("2. Modificar Promedio")
            print("3. Modificar Genero")
            print("4. Salir")
            
            opcion = validar_entero("Ingrese una opcion: ", minimo=1, maximo=4)
            if not 1 <= opcion <= 4:
                print("Debes elegir una opcion valida.")
                continue
            if opcion == 1:
                nueva_edad = validar_entero("Ingrese la nueva edad: ", minimo=12, maximo=80)
                for i in datos_estudiantes["estudiantes"]:
                    if i["edad"] == codigo_estudiante:
                        i["edad"] = nueva_edad
                print("Edad actualizada!")
                pausa(1)
                continue
            elif opcion == 2:
                nuevo_promedio = validar_promedio_notas()
                for i in datos_estudiantes["estudiantes"]:
                    if i["edad"] == codigo_estudiante:
                        i["promedio"] = nuevo_promedio
                print("Promedio actualizado!")
                pausa(1)
                continue
            elif opcion == 3:
                nuevo_genero = validar_genero()
                for i in datos_estudiantes["estudiantes"]:
                    if i["edad"] == codigo_estudiante:
                        i["genero"] = nuevo_genero
                print("Genero actualizado!")
                pausa(1)
                continue
            elif opcion == 4:
                break

def verificar_si_hay_estudiantes():
    if len(datos_estudiantes["estudiantes"]) == 0:
        print("No hay estudiantes registrados\nVolviendo al menu principal...")
        pausa(1.5)
        return False
    return True
while True:
    print("*** SISTEMA DE GESTION DE ESTUDIATES ***")
    opcion = int(input("Opciones\n1. Registrar estudiante\n2. Buscar estudiante\n3. Modificar datos de estudiante\n4. Eliminar estudiante\n5) Mostrar todos los estudiantes\n6. Salir\n: "))
    if not 1 <= opcion <= 6:
        print("Debes escoger una opcion valida. (1-6)")
        continue
    if opcion == 1:
        agregar_estudiante()
    elif opcion == 2:
        if not verificar_si_hay_estudiantes():
            continue
        buscar_estudiante()
    elif opcion == 3:
        if not verificar_si_hay_estudiantes():
            continue
        modificar_estudiante()
    elif opcion == 4:
        if not verificar_si_hay_estudiantes():
            continue
        eliminar_estudiante()
    elif opcion == 5:
        if not verificar_si_hay_estudiantes():
            continue
        mostrar_todos_los_estudiante()
    elif opcion == 6:
        break

    
    
     
