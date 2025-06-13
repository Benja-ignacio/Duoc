import sys
sys.path.append("/home/benjamin/Documents/Duoc-repo/Python")
from funciones import validacion

datos_estudiantes = {
    "estudiantes":[
    ]
}
while True:
    print("REGISTRO DE ESTUDIANTES")
    try:
        opcion = int(input("1) Crear estudiantes\n2) Listar estudiantes\n3) Actualizar estudiantes\n4) ELiminar estudiante\n5) Salir\n: "))
    except ValueError:
        print("Debes ingresar una opcion valida. (1-5)")
        continue
    if opcion == 1:
        crear_id = validacion.validar_entero("Ingrese el id del estudiante: ", minimo=0)
        print(crear_id)

