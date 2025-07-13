# Caracteres permitidos ID 
letras = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
numeros = "1234567890"
caracteres_validos = "QWERTYUIOPASDFGHJKLÑZXCVBNM1234567890"
# Validaciones 



# funciones
def menu_principal(videojuegos):
    while True:
        print(" *** TIENDA DE VIDEOJUEGOS ***")
        print("""
    1. Vender juego (Disminuir stock)
    2. Mostrar todos los juegos
    3. Actualizar precio de un juego
    4. Filtrar juegos por año de lanzamiento
    5. Salir""")

        opcion = pedir_entero("\nIngrese una opcion: ", 1, 5)
        
        if opcion == 1:
            buscar_juego_por_nombre(videojuegos)
        elif opcion == 2:
            mostrar_juegos(videojuegos)
        elif opcion == 3:
            print("opc3")
        elif opcion == 4:
            print("opc4")
        elif opcion == 5:
            break

def buscar_juego_por_nombre(videojuegos):
    while True:
        userinput = input("Ingrese el nombre del juego: ")
        for id in videojuegos['juegos']:
            nombre = videojuegos['juegos'][id][0]
            if  nombre.lower() == userinput.lower():
                return True
        print("El nombre ingresado no existe.")
        continue

def mostrar_juegos(videojuegos):
    for i in videojuegos['juegos']:
        juegos = videojuegos['juegos'][i]
        juegos.insert(0,i)
        print(F"""
    ID: {juegos[0]}
    Nombre: {juegos[1]}
    Plataforma: {juegos[2]}
    Genero: {juegos[3]}
    Clasificacion: {juegos[4]}
    Desarrollador: {juegos[5]}
    Año de lanzamiento: {juegos[6]}
    Publicador: {juegos[7]}
    """)
    input("\nPresione enter para volver al menu principal:")

def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"Debes ingresar un numero entre {minimo},{maximo}")
                continue
        elif maximo is not None:
            if entero > maximo:
                print(f"El numero debe ser igual o menor a {maximo}")
                continue
        elif minimo is not None:
            if entero < minimo:
                print(f"El numero debe ser igual o mayor a {minimo}")
                continue
        return entero
    
def stock_disponible(videojuegos):
    while True:
        opcion = pedir_entero("1. Mostrar todos los stock disponibles.\n2. Buscar stock por nombre\n: ", 1,2)
        if opcion == 1:
            for id in videojuegos['juegos']:
                nombre = videojuegos['juegos'][id][0]
                stock = videojuegos['stock'][id][1]
                print(f"ID: {id} Nombre: {nombre}, Stock: {stock}")
            return
        elif opcion == 2:
            buscar_juego_por_nombre(videojuegos)

def pedir_id(videojuegos):
    while True:
        id = input("Ingrese el id: ")
        tiene_numero = any(c in numeros for c in id)
        es_valido = all(c in caracteres_validos for c in id)

        if not len(id) == 6:
            print("EL id debe tener 6 caracteres.")
            continue
        if tiene_numero and es_valido:
            return id 
        print("EL ID debe tener solo letras mayusculas y al menos un numero.")

def validar_id(videojuegos):
    while True:
        id = pedir_id(videojuegos)
        if any(juego[0] == id for juego in videojuegos['juegos']):
            print("El id ingresado se encuentra en uso.")
            continue
        return id
