from time import sleep as pausa
# Caracteres permitidos
letras = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numeros = "1234567890"

datos_hotel = {
    "reservas":[
        {
            "id":"abc1",
            "nombre":"benja",
            "habitacion":101,
            "tipo":"individual", # doble, suite
            "dias":1 # 1 minimo
        }
    ]
}

# Precios por tipo de habitación
precios_habitacion = {
    "individual": 50,
    "doble": 80,
    "suite": 120
}

def menu_principal():
    while True:
        print("***Gestion de reservas de hotel***\n")
        opcion = pedir_entero("1. Registrar nueva reserva\n2. Buscar reserva\n3. Modificar reserva\n4. Cancelar reserva\n5. Mostrar todas las reservas\n6. Salir\n: ", 1, 6)
        if opcion == 1:
            registrar_nueva_reserva()
        elif opcion == 2:
            buscar_reserva()
        elif opcion == 3:
            modificar_reserva()
        elif opcion == 4:
            cancelar_reserva()
        elif opcion == 5:
            mostrar_reservas()
        elif opcion == 6:
            break


def pedir_id(mensaje):
    while True:
        id_usuario = input(mensaje)
        if not 2 <= len(id_usuario) <= 12:
            print("El ID debe tener minimo 2 caracteres y maximo 12.")
            continue
        tiene_letra =  any(c in letras for c in id_usuario)
        tiene_numero = any(c in numeros for c in id_usuario)
        if tiene_letra and tiene_numero:
            return id_usuario
        print("El ID debe llevar almenos una letra y un numero.")

def validar_id():
    while True:
        id_usuario = pedir_id("Ingrese el id: ")
        if any(i['id'] == id_usuario for i in datos_hotel["reservas"]):
            print("El id ingresado esta en uso.")
            continue
        return id_usuario


def pedir_entero(mensaje:str, minimo=None, maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue

        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe estar dentro del rango permitido {minimo}, {maximo}.")
                continue
        elif minimo is not None:
            if entero < minimo:
                print(f"El numero debe ser mayor o igual a {minimo}.")
                continue
        elif maximo is not None:
            if entero > maximo:
                print(f"El numero debe ser menor o igual a {maximo}.")
                continue
        return entero

def validar_numero_habitacion():
    while True:
        numero_habitacion = pedir_entero("Ingrese el numero de habitacion (101 - 999): ", 101, 999)
        if any(i['habitacion'] == numero_habitacion for i in datos_hotel["reservas"]):
            print(f"La habitacion {numero_habitacion} esta en uso.")
            continue
        return numero_habitacion

def tipo_habitacion():
    while True:
        tipo_habitacion = input("Ingrese el tipo de habitacion (Individual/Doble/Suite): ").lower()
        if tipo_habitacion == "individual":
                precio = 50
                return tipo_habitacion, precio
        elif tipo_habitacion == "doble":
            precio = 80
            return tipo_habitacion, precio
        elif tipo_habitacion == "suite":
            precio = 120
            return tipo_habitacion, precio
        print("La habitacion debe ser tipo individual, doble o suite.")


def validar_nombre(mensaje:str):
    while True:
        nombre_huesped = input(mensaje)
        if not 3 <= len(nombre_huesped) <= 52:
            print("El nombre del huesped debe tener minimo 3 caracteres y maximo 52")
            continue
        if all(caracter in letras for caracter in nombre_huesped):
            return nombre_huesped
        print("El nombre huesped debe contener solo letras. A-Z")

def registrar_nueva_reserva():
    tipo, precio = tipo_habitacion()
    nueva_reserva = {
        "id":validar_id(),
        "nombre":validar_nombre("Ingrese el nombre del huesped: "),
        "habitacion":validar_numero_habitacion(),
        "tipo":tipo,
        "dias":pedir_entero("Ingrese la cantidad de dias que desea reservar: ", 1, 30)
    }
    datos_hotel['reservas'].append(nueva_reserva)
    print(f"\nEl precio total de la reserva es ${precio * nueva_reserva['dias']}")
    input("\nPresione enter para volver al menu principal: ")

def buscar_reserva():
    if not hay_datos():
        pausa(1.5)
        return
    
    while True:
        id_reserva = pedir_id("Ingrese el id de la reserva: ")
        for i in datos_hotel["reservas"]:
            if i["id"] == id_reserva:
                print(f"\nID: {i['id']}\nNombre: {i['nombre']}\nNumero de habitacion: {i['habitacion']}\nTipo de habitacion: {i['tipo']}\nCantidad de dias: {i['dias']}")
                input("\nPresione enter para volver al menu principal: ")
                return
        print("No se encontro reserva con el id ingresado.")

def modificar_reserva():
    if not hay_datos():
        pausa(1.5)
        return
    while True:
        id_reserva = pedir_id("Ingrese el id de la reserva: ")
        for i in datos_hotel["reservas"]:
            if i['id'] == id_reserva:
                while True:
                    opcion = pedir_entero("1. Modificar nombre: \n2. Modificar numero de habitacion\n3. Modificar Tipo de habitacion\n4. Modificar cantidad de dias\n5. Salir\n: ", 1,5)
                    if opcion == 1:
                        nuevo_nombre = validar_nombre("Ingrese el nuevo nombre: ")
                        i["nombre"] = nuevo_nombre
                        input("Se ha modificado el nombre correctamente!\nPresione enter para volver al menu: ")
                    elif opcion == 2:
                        nuevo_num_habitacion = validar_numero_habitacion()
                        i["habitacion"] = nuevo_num_habitacion
                        input("Se ha modificado el numero de habitacion correctamente!\nPresione enter para volver al menu:")
                    elif opcion == 3:
                        nuevo_tipo_habitacion, _ = tipo_habitacion()
                        i["tipo"] = nuevo_tipo_habitacion
                        input("Se ha modificado el tipo de habitacion correctamente!\nPresione enter para volver al menu: ")
                    elif opcion == 4:
                        nuevos_dias_reserva = pedir_entero("Ingrese la cantidad de dias de reserva: ", 1, 30)
                        i["dias"] = nuevos_dias_reserva
                        input("Se ha modificado la cantidad de dias correctamente!\nPresione enter para volver al menu: ")
                    elif opcion == 5:
                            tipo_actual = i['tipo']
                            dias_actuales = i['dias']
                            precio_final = precios_habitacion.get(tipo_actual) * dias_actuales
                            print(f"El precio final de la reserva es: ${precio_final}")
                            input("Presione enter para volver al menu principal: ")
                            return
        print("El id ingresado no coincide con ninguna reserva.")
        continue

def cancelar_reserva():
    if not hay_datos():
        pausa(1.5)
        return
    
    while True:
        id_reserva = pedir_id("Ingrese el id de la reserva: ")
        for i in datos_hotel['reservas']:
            if i["id"] == id_reserva:
                datos_hotel["reservas"].remove(i)
                input("\nReserva cancelada correctamente!\nPresione enter para volver al menu principal: ")
                return
        print("No se encontro ninguna reserva.")

def mostrar_reservas():
    if not hay_datos():
        pausa(1.5)
        return
    for i in datos_hotel["reservas"]:
        print(f"\nID: {i['id']}\nNombre: {i['nombre']}\nNumero de habitacion: {i['habitacion']}\nTipo de habitacion: {i['tipo']}\nCantidad de dias: {i['dias']}")
    input("\nPresione enter para volver al menu principal: ")

def hay_datos():
    if not datos_hotel["reservas"]:
        print("No hay datos registrados\nVolviendo al menu principal...")
        return False
    return True

menu_principal()


