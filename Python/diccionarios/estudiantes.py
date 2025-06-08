from time import sleep as sp

def clear():
    import os

    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/macOS

datos_estudiantes = {
    "estudiantes":[
    ]
}
while True:
    print("REGISTRO DE ESTUDIANTES")
    try:
        opcion = int(input("1) Crear estudiantes\n2) Listar estudiantes\n3) Actualizar estudiantes\n4) ELiminar estudiante\n5) Salir\n: "))
    except ValueError:
        clear()
        print("Debes ingresar una opcion valida. (1-5)")
        continue
    if opcion <= 0 or opcion > 5:
        clear()
        print("Debes ingresar una opcion dentro del rango. (1-5)")
        continue
        
    if opcion == 1:
        clear()
        print("CREAR ESTUDIANTES")

        while True:    
            try:
                id_estudiante = int(input("Ingrese el id del estudiante: "))
            except ValueError:
                print("Debes ingresar un numero valido mayor a 0.")
                continue
            if id_estudiante <=0:
                clear()
                print("Debes escojer un id mayor a 0.")
                continue
            if any(estudiante["id_estudiante"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
                clear()
                print("Ese id esta en uso, vuelva a ingresar un id.")
                continue
            break

        while True:
                nombre = input("Ingrese el nombre del estudiante: ").strip().capitalize()
                if not nombre.isalpha():
                    clear()
                    print("No debe llevar numeros ni caracteres especiales.")
                    continue
                if not 3 <= len(nombre) <=24:
                    clear()
                    print("El nombre debe estar dentro del rango de caracteres permitidos. (3-24)") 
                    continue
                break

        while True:
                apellido = input("Ingrese el apellido del estudiante: ").strip().capitalize()
                if not apellido.isalpha():
                    clear()
                    print("No debe llevar numeros ni caracteres especiales.")
                    continue
                if not 3 <= len(apellido) <=24:
                    clear()
                    print("El apellido debe estar dentro del rango de caracteres (3-24).")
                    continue
                break
        
        while True:
            try:
                edad = int(input("Ingrese la edad del estudiante: "))
            except ValueError:
                clear()
                print("Debes ingresar una edad valida. (17-100)")
                continue
            if not 17 <= edad <= 100:
                    clear()
                    print("Debes ingresar una edad valida. (17-100)")
                    continue
            break

        while True:
            carrera = input("Ingrese la carrera del estudiante: ").strip().capitalize()
            if not 3 <= len(carrera) <=40:
                clear()
                print("Debe estar dentro del rango permitido. (3-40)")
                continue
            if not all((char.isalpha() or char==' ') for char in carrera):
                clear()
                print("Solo debe llevar letras y espacios.")
                continue
            break
        estudiante_agregar = {
            "id_estudiante":id_estudiante,
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad,
            "carrera":carrera
        }
        datos_estudiantes["estudiantes"].append(estudiante_agregar)
        print("Estudiante agregado.")
        sp(1.5)
        
    if opcion == 2:
        clear()
        if len(datos_estudiantes["estudiantes"]) == 0:
            print("No hay estudiantes registrados.")
            sp(1.5)
            continue
        for estudiantes in datos_estudiantes["estudiantes"]:
            print(f"ID del estudiante: {estudiantes["id_estudiante"]}\nNombre: {estudiantes["nombre"]}\nApellido: {estudiantes["apellido"]}\nEdad: {estudiantes["edad"]}\nCarrera: {estudiantes["carrera"]}\n")
        input("Presiona enter para volver al menu: ")

    if opcion == 3:        
        if len(datos_estudiantes["estudiantes"]) <= 0:
            clear()
            print("No hay estudiantes registrados")
            sp(1.5)
            continue
        print("ACTUALIZAR ESTUDIANTES")
        while True:
            try:
                id_estudiante = int(input("Ingrese el id del estudiante: "))
            except ValueError:
                clear()
                print("Debes ingresar un numero mayor a 0.")
                continue
            if id_estudiante <= 0:
                clear()
                print("Debes ingresar un numero mayor a 0.")
                continue
            if not any(estudiante["id_estudiante"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
                clear()
                print("El id ingresado no coindice con ninguno.")
                continue
            if any(estudiante["id_estudiante"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
                while True:
                    try:
                        actualizar = int(input("1) Editar nombre\n2) Editar apellido\n3) Editar edad\n4) Editar carrera\n5) Volver al menu principal\n:  "))
                    except ValueError:
                        clear()
                        print("Debes ingresar una opcion valida. (1-4)")
                        continue
                    if not 1 <= actualizar <= 5:
                        clear()
                        print("Debes ingresar una opcion valida. (1-4)")
                        continue
                
                    elif actualizar == 1:
                        clear()
                        while True:
                            nombre = input("Ingrese el nombre: ")
                            if not nombre.isalpha():
                                clear()
                                print("No debe llevar numeros ni caracteres especiales.")
                                continue
                            if not 3 <= len(nombre) <=24:
                                clear()
                                print("El nombre debe estar dentro del rango de caracteres permitidos. (3-24)") 
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"El nombre nuevo sera {nombre}, estas seguro?\n1) Estoy seguro.\n2) Volver a editar el nombre.\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                else:
                                    break
                            if preguntar == 1:
                                for i in datos_estudiantes["estudiantes"]:
                                    i["nombre"] = nombre
                                break
                            else:
                                continue
                    
                    elif actualizar == 2:
                        clear()
                        while True:                        
                            apellido = input("Ingrese el apellido: ").strip().capitalize()
                            if not apellido.isalpha():
                                clear()
                                print("No debe llevar numeros ni caracteres especiales.")
                                continue
                            if not 3 <= len(apellido) <=24:
                                clear()
                                print("El apellido debe estar dentro del rango de caracteres (3-24).")
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"El apellido nuevo sera {apellido}, estas seguro?\n1) Estoy seguro.\n2) Volver a editar el apellido.\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                break
                            if preguntar == 1:
                                for i in datos_estudiantes["estudiantes"]:
                                    i["apellido"] = apellido
                                break
                            else:
                                continue

                    elif actualizar == 3:
                        clear()
                        while True:
                            try:
                                edad = int(input("Ingrese la edad: "))
                            except ValueError:
                                clear()
                                print("Debes ingresar una edad valida. (17-100)")
                                continue
                            if not 17 <= edad <= 100:
                                clear()
                                print("Debes ingresar una edad valida. (17-100)")
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"La edad nueva sera {edad}, estas seguro?\n1) Estoy seguro.\n2) Volver a editar la edad.\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar un opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                break
                            if preguntar == 1:
                                for i in datos_estudiantes["estudiantes"]:
                                    i["edad"] = edad
                                break
                            else:
                                continue

                    elif actualizar == 4:
                        clear()
                        while True:
                            carrera = input("Ingrese la carrera del estudiante: ").strip().capitalize()
                            if not 3 <= len(carrera) <=40:
                                clear()
                                print("Debe estar dentro del rango de caracteres permitido. (3-40)")
                                continue
                            if not all((char.isalpha() or char==' ') for char in carrera):
                                clear()
                                print("Solo debe llevar letras y espacios.")
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"La carrera nueva sera {carrera}, estas seguro?\n1) Estoy seguro.\n2) Volver a editar la carrera.\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                break
                            if preguntar == 1:
                                for i in datos_estudiantes["estudiantes"]:
                                    i["carrera"] = carrera
                                break
                            else:
                                continue
                    elif actualizar == 5:
                        break
                if actualizar == 5:
                    break                    

    if opcion == 4:
        if len(datos_estudiantes["estudiantes"]) == 0:
            clear()
            print("No hay estudiantes registrados.")
            sp(1)
            continue
        clear()
        print("ELIMINAR ESTUDIANTES")
        while True:
            try:
                id_estudiante = int(input("Ingrese el id del estudiante: "))
            except ValueError:
                clear()
                print("Debes ingresar un id valido mayor a 0.")
                continue
            if id_estudiante <= 0:
                clear()
                print("Debes ingresar id mayor a 0.")
                continue
            encontrado = False
            for i in datos_estudiantes["estudiantes"]:
                if i["id_estudiante"] == id_estudiante:
                    datos_estudiantes["estudiantes"].remove(i)
                    print("El estudiante ha sido eliminado correctamente ")
                    encontrado = True
                    sp(1.5)
                    break
            if encontrado == True:
                break
            else:
                clear()
                print("El id ingresado no coincide con ninguno ")
                continue
    if opcion == 5:
        clear()
        print("Saliendo... ")
        sp(1.5)
        break
