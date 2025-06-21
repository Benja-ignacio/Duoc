import re

datos_estudiantes = {"estudiantes": []}

# ---------- Validadores ----------
def validar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and maximo is not None:
                if not minimo <= valor <= maximo:
                    print(f"Debe estar entre {minimo, maximo}.")
                    continue
            if minimo is not None and valor < minimo:
                print(f"Debe ser >= {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Debe ser <= {maximo}")
                continue
            return valor
        except ValueError:
            print("Debe ser un número entero.")

def validar_promedio(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if 1.0 <= valor <= 7.0:
                return valor
        except ValueError:
            pass
        print("Promedio inválido. (1.0 - 7.0)")

def validar_nombre(mensaje):
    while True:
        nombre = input(mensaje).strip().capitalize()
        if not re.fullmatch(r"[A-Z][a-z ]{2,28}", nombre):
            print("Debe comenzar con mayúscula y tener 3-29 letras.")
            continue
        if any(e["nombre"] == nombre for e in datos_estudiantes["estudiantes"]):
            print("El nombre ya está registrado.")
            continue
        return nombre

def validar_codigo(mensaje):
    while True:
        codigo = input(mensaje).strip()
        if re.fullmatch(r"[A-Za-z0-9]{6}", codigo):
            return codigo
        print("Debe tener 6 caracteres alfanuméricos.")

def validar_genero():
    while True:
        genero = input("Ingrese el género (F/M): ").strip().upper()
        if genero in ("F", "M"):
            return genero
        print("Debe ingresar F o M.")

# ---------- Utilidad ----------
def hay_estudiantes():
    if not datos_estudiantes["estudiantes"]:
        print("No hay estudiantes registrados.\n")
        return False
    return True

# ---------- Funciones principales ----------
def registrar_estudiante():
    estudiante = {
        "id": validar_codigo("Código (6 caracteres): "),
        "nombre": validar_nombre("Nombre: "),
        "edad": validar_entero("Edad (12-80): ", 12, 80),
        "genero": validar_genero(),
        "promedio": validar_promedio("Promedio: ")
    }
    datos_estudiantes["estudiantes"].append(estudiante)
    print("¡Estudiante registrado!\n")

def buscar_estudiante(mensaje):
    if not hay_estudiantes():
        return
    codigo_o_id = input(mensaje)
    for e in datos_estudiantes["estudiantes"]:
        if e["id"] == codigo_o_id or e["nombre"] == codigo_o_id:
            print(f"\nID: {e['id']}\nNombre: {e['nombre']}\nEdad: {e['edad']}\nGenero: {e['genero']}\nPromedio: {e['promedio']}")
            input("\nPresione enter para volver al menú principal... ")
            return
    print("El ID o nombre ingresado no coincide con ningún estudiante.")

def modificar_estudiante():
    if not hay_estudiantes():
        return
    codigo = validar_codigo("Ingrese el ID del estudiante: ")
    for e in datos_estudiantes["estudiantes"]:
        if e["id"] == codigo:
            while True:
                print("\n1. Modificar edad\n2. Modificar promedio\n3. Modificar género\n4. Volver al menú")
                opcion = validar_entero("Opción: ", 1, 4)
                if opcion == 1:
                    e["edad"] = validar_entero("Nueva edad: ", 12, 80)
                    print("Edad actualizada correctamente.\n")
                elif opcion == 2:
                    e["promedio"] = validar_promedio("Nuevo promedio: ")
                    print("Promedio actualizado correctamente.\n")
                elif opcion == 3:
                    e["genero"] = validar_genero()
                    print("Género actualizado correctamente.\n")
                elif opcion == 4:
                    return
            return
    print("No se encontró ningún estudiante con ese ID.")

def eliminar_estudiante():
    if not hay_estudiantes():
        return
    codigo = validar_codigo("Ingrese el ID a eliminar: ")
    for e in datos_estudiantes["estudiantes"]:
        if e["id"] == codigo:
            datos_estudiantes["estudiantes"].remove(e)
            print("Estudiante eliminado.")
            return
    print("No se encontró ningún estudiante con ese ID.")

def mostrar_estudiantes():
    if not hay_estudiantes():
        return
    for e in datos_estudiantes["estudiantes"]:
        print(f"\nID: {e['id']}\nNombre: {e['nombre']}\nEdad: {e['edad']}\nGenero: {e['genero']}\nPromedio: {e['promedio']}")
    input("\nPresione enter para volver al menú principal... ")

# ---------- Menú principal ----------
while True:
    print("\n*** Menú de estudiantes ***")
    print("1. Registrar estudiante\n2. Buscar estudiante\n3. Modificar estudiante\n4. Eliminar estudiante\n5. Mostrar todos\n6. Salir")
    opcion = validar_entero("Seleccione una opción (1-6): ", 1, 6)

    if opcion == 1:
        registrar_estudiante()
    elif opcion == 2:
        buscar_estudiante("Ingrese el ID o nombre del estudiante: ")
    elif opcion == 3:
        modificar_estudiante()
    elif opcion == 4:
        eliminar_estudiante()
    elif opcion == 5:
        mostrar_estudiantes()
    elif opcion == 6:
        print("¡Hasta luego!")
        break
