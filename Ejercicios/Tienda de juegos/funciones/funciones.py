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
        for i in videojuegos['juegos']:
            if videojuegos['juegos'][i][0].lower() == userinput.lower():
                juego_encontrado = videojuegos['juegos'][i]
                juego_encontrado.insert(0,i)
                print(juego_encontrado)
                input('\nPresione enter para volver al menu principal: ')
                return
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




