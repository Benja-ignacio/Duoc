# Sistema de Biblioteca con usuarios y prestamos
#NOTE GUARDAR LOS DATOS EN UN ARCHIVO BIBLIOTECA.JSON
import funciones

biblioteca = {
    "libros":[
        {
            "id": "L001",
            "titulo": "1984",
            "autor": "George Orwell",
            "estado": "prestado"
        }
    ],
    "usuarios":[
        {
            "id": "U001", 
            "nombre": "Benjamin"
        }
    ],
    "prestamos":[
        {
            "usuario_id": "U001", 
            "Libro_id": "L001"
        }
    ]
}

def menu_principal():
    while True:
        print("*** SISTEMA DE BIBLIOTECA ***\n")
        opciones = funciones.pedir_entero("1. Registrar libro\n2. Registrar usuario\n3. Prestar libro\n4. Devolver libro\n5. Ver libros prestados\n6. Ver libros disponibles\n7. salir\n: ",1, 7)
        if opciones == 1:
            print("opc")
        elif opciones == 2:
            print("opc")
        elif opciones == 3:
            print("opc1")
        elif opciones == 4:
            print("opc1")
        elif opciones == 5:
            print("opc1")
        elif opciones == 6:
            print("opc2")
        elif opciones == 7:
            return
        else:
            print("Debes ingresar una opcion valida. (1-6)")
            continue
    




