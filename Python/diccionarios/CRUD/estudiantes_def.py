from time import sleep as pausa

def validar_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Valor ingresado invalido. Debes ingresar un numero entero.")
            continue

        if minimo is not None and maximo is not None:
            if not minimo < entero < maximo:
                print(f"Debes ingresar un numero dentro del rango permitido. ({minimo},{maximo})")
                continue

        
        elif minimo is not None:
            if entero < minimo:
                print(f"Debes ingresar un numero entero dentro del rango permitido. ({minimo} - infinito)")
                continue
        
        elif maximo is not None:
            if entero > maximo:
                print(f"Debes ingresar un numero menor o igual al maximo. (maximo:{maximo})")
                continue
        return entero

def validar_string(mensaje):
    while True:
        string = input(mensaje).strip().capitalize()
        caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzñáéíóúüABCDEFGHIJKLMNOPQRSTUVWXYZÑÁÉÍÓÚÜ0123456789 :@"
        for i in string:
            if i not in caracteres_permitidos:
                print("Solo puedes ingresar numeros y letras.")
                break
        if not 3 < len(string) < 48:
            print("Debe estar dentro del rango de los caracteres permitidos. (3-48)")
            continue
        return string

def listar_estudiantes():
    while True:
        for i in datos_estudiantes["estudiantes"]:
            print(f"ID: {i["id"]}")
            print(f"Nombre: {i['nombre']}")
            print(f"Apellido: {i['apellido']}")
            print(f"Edad: {i['edad']}")
            print(f"Carrera: {i['carrera']}")
        break

def validar_si_existen_estudiantes():
    while True:
        if len(datos_estudiantes["estudiantes"]) == 0:
            print("No hay datos de estudiantes registrados\nVolviendo al menu principal...")
            pausa(1.5)
            return False
        return True

def crear_estudiante():
    while True:
        id_estudiante = validar_entero("Ingrese el id del estudiante: ", minimo=0)
        if any(estudiante["id"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
            print("EL id ingresado ya se encuentra registrado. Ingrese otro id.")
            continue
        break
    nombre = validar_string("Ingrese el nombre del estudiante: ").strip().capitalize()
    apellido = validar_string("Ingrese el apellido del estudiante: ").strip().capitalize()
    edad = validar_entero("Ingrese la edad del estudiante: ", minimo=16, maximo=80)
    carrera = validar_string("Ingrese la carrera del estudiante: ").strip().capitalize()

    agregar_estudiante = {
        "id":id_estudiante,
        "nombre":nombre,
        "apellido":apellido,
        "edad":edad,
        "carrera":carrera
    }
    datos_estudiantes["estudiantes"].append(agregar_estudiante)

    print("\nEstudiante agregado!")
    input("Presione enter para volver al menu principal... ")

def actualizar_estudiantes():
    while True:
        id_estudiante = validar_entero("Ingrese el id del estudiante: ", minimo=0)
        if id_estudiante == any(estudiante["id"] for estudiante in datos_estudiantes["estudiantes"]):
            nuevo_nombre = validar_string("Ingrese el nuevo nombre: ")
            nuevo_apellido = validar_string("Ingrese el nuevo apellido: ")
            nueva_edad = validar_entero("Ingrese la nueva edad: ", minimo=16, maximo=80)
            nueva_carrera = validar_string("Ingrese la nueva carrera: ")
        else:
            print("EL id ingresado no coincide con ningun estudiante.")
            continue
        for i in datos_estudiantes["estudiantes"]:
            i["nombre"] = nuevo_nombre
            i["apellido"] = nuevo_apellido
            i["edad"] = nueva_edad
            i["carrera"] = nueva_carrera
        print("Estudiante actualizado!\nVolviendo al menu principal...")
        pausa(1.5)
        break

def eliminar_estudiante():
    while True:
        id_estudiante = validar_entero("Ingrese el id del estudiante: ", minimo=0)
        encontrado = False
        for i in datos_estudiantes["estudiantes"]:
            if i["id"] == id_estudiante:
                datos_estudiantes["estudiantes"].remove(i)
                print("El estudiante ha sido eliminado\nVolviendo al menu principal...")
                pausa(1.5)
                encontrado = True
                break
        if encontrado == True:
            break
        elif encontrado == False:
            print("El id ingresado no coincide con ningun estudiante.")
            continue
            

datos_estudiantes = {
    "estudiantes":[]
}

while True:
    print("REGISTRO DE ESTUDIANTES")
    try:
        opcion = int(input("1) Crear estudiantes\n2) Listar estudiantes\n3) Actualizar estudiantes\n4) ELiminar estudiante\n5) Salir\n: "))
    except ValueError:
        print("Debes ingresar una opcion valida. (1-5)")
        continue

    if opcion == 1:
        crear_estudiante()

    if opcion == 2:
        if not validar_si_existen_estudiantes():
            continue
        listar_estudiantes()
        input("\nPresione enter para volver al menu principal...")
    
    if opcion == 3:
        if not validar_si_existen_estudiantes():
            continue
        actualizar_estudiantes()
    
    if opcion == 4:
        if not validar_si_existen_estudiantes():
            continue
        eliminar_estudiante()
    
    if opcion == 5:
        print("Saliendo...")
        pausa(1.5)
        break