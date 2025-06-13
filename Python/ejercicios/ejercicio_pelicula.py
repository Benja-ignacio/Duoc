from time import sleep as pausa

datos_peliculas = {
    "peliculas":[]
}

def validar_entero(mensaje, minimo=None,maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero")
            continue

        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"Debes ingresar un número entre {minimo} y {maximo}.")
                continue

        if minimo is not None and entero < minimo:
            print(f"Debes ingresar un número mayor o igual a {minimo}.")
            continue

        if maximo is not None and entero > maximo:
            print(f"Debes ingresar un número menor o igual a {maximo}.")
            continue

        return entero

def validar_string(mensaje):
    """Validar string"""
    while True:
        string = input(mensaje).strip().capitalize()
        if not 3 <= len(string) <= 60:
            print("El titulo debe estar dentro de los caracteres permitidos. (3-60)")
            continue
        caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 :"
        for i in string:
            if i not in caracteres_validos:
                print("El titulo ingresado solo puede llevar letras y numeros.")
                break
        else:
            return string

def validar_estado(mensaje):
    while True:
        estado_pelicula = input(mensaje).lower()
        if estado_pelicula == "vista" or estado_pelicula == "no vista":
            return estado_pelicula
        else:
            print("Debes ingresar vista o no vista.")
            continue

def mostrar_peliculas():
    for i in datos_peliculas["peliculas"]:
        print(f"'Titulo: {i['titulo']}")
        print(f"Año: {i['año']}")
        print(f"Genero: {i['genero']}")
        print(f"Estado: {i['estado']}\n")

def buscar_pelicula(mensaje):
    while True:
        buscar_pelicula = input(mensaje).capitalize()
        encontrado = False
        for i in datos_peliculas["peliculas"]:
            if i["titulo"] == buscar_pelicula:
                print(f"Titulo: {i['titulo']}")
                print(f"Año: {i['año']}")
                print(f"Genero: {i['genero']}")
                print(f"Estado: {i['estado']}\n")
                encontrado = True
        if encontrado == True:
            break
        else:
            print("El titulo ingresado no coincide con ninguna pelicula.")
            continue

def eliminar_pelicula(mensaje):
    while True:
        encontrado = False
        eliminar_pelicula = validar_entero(mensaje, minimo=0)
        for i in datos_peliculas["peliculas"]:
            if i["id"] == eliminar_pelicula:
                datos_peliculas["peliculas"].remove(i)
                print("la pelicula ha sido eliminada correctamente.\nVolviendo al menu principal...")
                pausa(1.5)
                encontrado = True
                break
        if encontrado == True:
            break
        else:
            print("El id ingresado no coincide con ninguno.")
            continue


def validar_si_existen_datos():
    while True:
        if len(datos_peliculas["peliculas"]) == 0:
            print("No hay registros de peliculas ingresados.\nVolviendo al menu principal...")
            pausa(1)
            return False
        return True
    

def validar_pelicula():
        while True:
            id_pelicula = validar_entero("Ingrese el id de la pelicula: ", minimo=0,)
            if any(pelicula["id"] == id_pelicula for pelicula in datos_peliculas["peliculas"]):
                print("El ID ingresado ya esta en uso")
                continue
            break
        while True:
            titulo_pelicula = validar_string("Ingrese el titulo de la pelicula: ")
            if any(pelicula["titulo"] == titulo_pelicula for pelicula in datos_peliculas["peliculas"]):
                print("El titulo ya se encuentra ingresado.")
                continue
            anio_pelicula = validar_entero("Ingrese el año de la pelicula: ", minimo=1800, maximo=2025)
            genero_pelicula = validar_string("Ingrese el genero de la pelicula: ")
            estado_pelicula = validar_estado("Ingrese el estado de la pelicula (vista / no vista): ")

            agregar_pelicula = {
                "id":id_pelicula,
                "titulo":titulo_pelicula,
                "año":anio_pelicula,
                "genero":genero_pelicula,
                "estado":estado_pelicula
            }
            
            datos_peliculas["peliculas"].append(agregar_pelicula)
            print("Pelicula agregada!")
            pausa(1.5)
            break


while True:
    print("*****Menu*****")
    try:
        opcion = int(input("1) Agregar una pelicula\n2) Mostrar todas las peliculas\n3) Buscar una pelicula por su titulo\n4) Eliminar una pelicula\n5) Salir\n: "))
    except ValueError:
        print("Debes ingresar una opcion valida. (1-5)")
        continue

    if opcion == 1:
        validar_pelicula()

    
    elif opcion == 2:
        if not validar_si_existen_datos():
            continue
        mostrar_peliculas()
        input("Presione enter para volver al menu principal...")
    
    elif opcion == 3:
        if not validar_si_existen_datos():
            continue
        buscar_pelicula("Ingrese el titulo de la pelicula : ")
        input("Presione enter para volver al menu principal...")

    
    elif opcion == 4:
        if not validar_si_existen_datos():
            continue
        eliminar_pelicula("Ingrese el id de la pelicula a eliminar: ")
    
    elif opcion == 5:
        print("Saliendo...")
        pausa(1.5)
        break


    