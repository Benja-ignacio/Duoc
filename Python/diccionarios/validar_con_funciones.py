datos = {
    "estudiantes": []
}

def validar(nombre, edad, curso):
    if not nombre.strip():
        print("Nombre inválido.")
        return False
    if edad < 5 or edad > 100:
        print("Edad fuera de rango.")
        return False
    if not curso.strip():
        print("Curso inválido.")
        return False
    return True

def agregar():
    while True:
        nombre = input("Ingrese su nombre: ")
        try:
            edad = int(input("Ingrese su edad: "))
        except ValueError:
            print("Edad inválida. Debe ser un número.")
            continue
        curso = input("Ingrese su curso: ")

        if validar(nombre, edad, curso):
            datos["estudiantes"].append({
                "nombre": nombre,
                "edad": edad,
                "curso": curso
            })
            print("Estudiante agregado correctamente.")
            break  # salir del bucle si todo está bien
        else:
            print("Por favor, intente nuevamente.\n")

agregar()
