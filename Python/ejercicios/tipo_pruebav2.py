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
        nombre = input(mensaje).capitalize().strip()
        if not re.fullmatch(r"^[A-Z][a-z ]{2,28}$", nombre):
            print("Solo debe llevar letras y tener minimo 3 caracteres y maximo 28.")
            continue
        if any(estudiante["nombre"] == nombre for estudiante in datos_estudiantes["estudiantes"]):
            print("El nombre ingresado se encuentra en uso.")
            continue
        return nombre
def validar_promedio(mensaje:str)->float:
    while True:
        try:
            promedio = float(input(mensaje))       
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
            print("EL codigo solo debe llevar letras/numeros y debe tener 6 caracteres.")
            continue
        return codigo
    
def verificar_si_existen_registros_de_estudiantes()->bool:    
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
def buscar_estudiante(mensaje:str)->str:
    while True:
        codigo_o_id = input(mensaje)
        for i in datos_estudiantes["estudiantes"]:
            if i["id"] == codigo_o_id or i["nombre"] == codigo_o_id:
                print(f"ID: {i['id']}\nNombre: {i['nombre']}\nEdad: {i['edad']}\nGenero: {i['genero']}\nPromedio: {i['promedio']}")
                input("\nPresione enter para volver al menu principal... ")
                return
            print("El Id/Nombre ingresado no coincide con ningun estudiante.")
def modificar_estudiante():
    while True:
        codigo = validar_codigo("Ingrese el codigo del estudiante que desea modificar: ")
        if any(estudiante['id'] == codigo for estudiante in datos_estudiantes["estudiantes"]):
            while True:
                try:
                    opcion = int(input("1. Modificar Edad\n2. Modificar Promedio\n3. Modificar genero\n4. Salir"))
                except ValueError:
                    print("Debes elegir una opcion valida. (1-3)")
                    continue
                if opcion == 1:
                    nueva_edad = validar_entero("Ingrese la nueva edad del estudiante: ", minimo=12, maximo=80)
                    for i in datos_estudiantes["estudiantes"]:
                        if i["id"] == codigo:
                            i["edad"] = nueva_edad
                    print("La nueva edad se ha modificado correctamente.")
                    continue
                elif opcion == 2:
                    nuevo_promedio = validar_promedio("Ingrese el nuevo promedio del estudiante ")
                    for i in datos_estudiantes["estudiantes"]:
                        if i["id"] == codigo:
                            i["promedio"] = nuevo_promedio
                    print("El nuevo promedio se ha modificado correctamente.")
                    continue
                elif opcion == 3:
                    nuevo_genero = validar_genero()
                    for i in datos_estudiantes["estudiantes"]:
                        if i["id"] == codigo:
                            i["genero"] = nuevo_genero
                    print("El nuevo genero se ha modificado correctamente")
                    continue
                elif opcion == 4:
                    return
def eliminar_estudiante():
    while True:
        codigo = validar_codigo("Ingrese el id del estudiante a eliminar: ")
        for i in datos_estudiantes["estudiantes"]:
            if i["id"] == codigo:
                datos_estudiantes["estudiantes"].remove(i)
                print("El estudiante ha sido eliminado correctamente.")
                input("\nPresione enter para volver al menu principal... ")
                return
        print("No se encontro ningun estudiante que coincida con el id ingresado.")
        continue
def mostrar_estudiantes():
    for i in datos_estudiantes["estudiantes"]:
        print(f"ID: {i['id']}\nNombre: {i['nombre']}\nEdad: {i['edad']}\nGenero: {i['genero']}\nPromedio: {i['promedio']}")
        input("\nPresione enter para volver al menu principal... ")

while True:
    print("*** Bienvenido al registro de estudiantes! ***")
    print("\n1. Registrar estudiante\n2. Buscar estudiante\n3. Modificar datos de estudiante\n4. ELiminar estudiante\n5. Mostrar todos los estudiantes\n6. Salir")
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
    elif opcion == 2:
        if not verificar_si_existen_registros_de_estudiantes():
            continue
        buscar_estudiante("Ingrese el Nombre o ID del estudiante: ")
    elif opcion == 3:
        if not verificar_si_existen_registros_de_estudiantes():
            continue
        modificar_estudiante()
    elif opcion == 4:
        if not verificar_si_existen_registros_de_estudiantes():
            continue
        eliminar_estudiante()
    elif opcion == 5:
        if not verificar_si_existen_registros_de_estudiantes():
            continue
        mostrar_estudiantes()
    elif opcion == 6:
        break
