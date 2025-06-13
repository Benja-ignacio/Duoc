import sys
from time import sleep as sp
sys.path.append("C:/Users/Admin/Documents/Duoc/Duoc/Python/")
from funciones import validaciones

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
        id_estudiante = validaciones.validar_id("Ingrese el id del estudiante: ")
        nombre_estudiante = validaciones.validar_nombre("Ingrese el nombre del estudiante: ")
        apellido_estudiante = validaciones.validar_apellido("Ingrese el apellido del estudiante: ")
        edad_estudiante = validaciones.validar_edad("Ingrese la edad del estudiante: ")
        carrera_estudiante = validaciones.validar_carrera("Ingrese la carrera del estudiante: ")
        agregar_estudiante = {
            "id":id_estudiante,
            "nombre":nombre_estudiante,
            "apellido":apellido_estudiante,
            "edad":edad_estudiante,
            "carrera":carrera_estudiante,
        }
        datos_estudiantes["estudiantes"].append(agregar_estudiante)
        print(f"El estudiante {nombre_estudiante} ha sido agregado correctamente!")
        sp(1.5)

    if opcion == 2:
        if len(datos_estudiantes["estudiantes"]) <=0:
            print("No hay estudiantes registrandos\nVolviendo al menu principal...")
            sp(1.5)
        else:
            for i in datos_estudiantes["estudiantes"]:
                print(f"ID: {i["id"]}")
                print(f"Nombre: {i["nombre"]}")
                print(f"Apellido: {i["apellido"]}")
                print(f"Edad: {i["edad"]}")
                print(f"Carrera: {i["carrera"]}")
    if opcion == 3:
        if len(datos_estudiantes["estudiantes"]) <=0:
            print("No hay estudiantes registrados\nVolviendo al menu principal...")
            sp(1.5)
        else:
            while True:                    
                id_estudiante = validaciones.validar_id("Ingrese el id del estudiante actualizar: ")
                if any (estudiante["id"] == id_estudiante for estudiante in datos_estudiantes["estudiantes"]):
                    while True:
                        try:
                            actualizar = int(input("1) Actualizar nombre\n2) Actualizar apellido\n3) Actualizar edad\n4) Actualizar carrera\n5) Volver al menu principal\n: "))
                            if actualizar == 1:
                                nuevo_nombre = validaciones.validar_nombre("Ingrese el nuevo nombre: ")
                                for i in datos_estudiantes["estudiantes"]:
                                    i["nombre"] = nuevo_nombre
                                print(f"Estudiante actualizado! El nuevo nombre es: {nuevo_nombre}")
                            elif actualizar == 2:
                                nuevo_apellido = validaciones.validar_apellido("Ingrese el nuevo apellido: ")
                                for i in datos_estudiantes["estudiantes"]:
                                    i["apellido"] = nuevo_apellido
                                print(f"Estudiante actualizado! El nuevo apellido es: {nuevo_apellido}")
                            elif actualizar == 3:
                                nueva_edad = validaciones.validar_edad("Ingrese la nueva edad: ")
                                for i in datos_estudiantes["estudiantes"]:
                                    i["edad"] = nueva_edad
                                print(f"Estudiante actualizado! La nueva edad es: {nueva_edad}")
                            elif actualizar == 4:
                                nueva_carrera = validaciones.validar_carrera("Ingrese la nueva carrera: ")
                                for i in datos_estudiantes["estudiantes"]:
                                    i["carrera"] = nueva_carrera
                                print(f"Estudiante actualizado! La nueva carrera es: {nueva_carrera}")
                            elif actualizar == 5:
                                break
                        except ValueError:
                            print("Debes ingresar una opcion valida. (1-5)")
                            continue
                if actualizar == 5:
                    break
                else:
                    print("El id ingresado no coincide con ninguno.")
                    continue
    if opcion == 4:
        if len(datos_estudiantes["estudiantes"]) <= 0:
            print("No hay estudiantes registradosn\nVolviendo al menu principal")
            sp(1.5)
        while True:
            estudiante_a_eliminar = validaciones.validar_id("Ingrese el id del estudiante a eliminar: ")

            for estudiante in datos_estudiantes["estudiantes"]:
                if estudiante["id"] == estudiante_a_eliminar:
                    datos_estudiantes["estudiantes"].remove(estudiante)
                    print(f"El estudiante {estudiante['nombre']} ha sido eliminado.")
                    sp(1.5)
                    break  # rompe el for
            else:
                print("El id ingresado no coincide con ningún estudiante.")
                continue  # vuelve al while para pedir otro ID
            break  # rompe el while si se eliminó correctamente



