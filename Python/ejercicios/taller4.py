# Sistema de gestion de reservas de hotel 

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
# $ por dia
habitaciones = {
    "precios":
    {
        "suite":120,
        "doble":80,
        "individual":50
    }
}

def validar_entero(mensaje:str, minimo=None, maximo=None)->int:
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe ser mayor o igual a {minimo} y menor o igual a {maximo}")
                continue
        elif minimo is not None and entero < minimo:
            print(f"El numero debe ser mayor o igual = {minimo}")
            continue
        elif maximo is not None and entero > maximo:
            print(f"EL numero debe ser menor o igual = {maximo}")
            continue
        return entero

def validar_id(mensaje:str):
    while True:
        id_reserva = input(mensaje)
        numeros = "1234567890"
        letras = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM"
        tiene_letra = False
        tiene_numero = False
        if not 2 <= len(id_reserva) <= 10:
            print("Debe tener almenos una letra y un numero. minimo 2 y maximo 10 caracteres.")
            continue
        for i in id_reserva:
            if i in letras:
                tiene_letra = True 
            elif i in numeros:
                tiene_numero = True

        if tiene_numero and tiene_letra:
            return id_reserva
        else:
            print("El id debe llevar al menos una letra y un numero.")
            continue

def validar_string(mensaje:str):
    while True:        
        letras = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM "
        string = input(mensaje).strip().capitalize()
        if not 3 <= len(string) <= 32:
            print("Debe tener minimo 3 y maximo 32 caracteres.")
            continue
        for i in string:
            if i in letras:
                return string
        else:
            print("Entrada invalida, intente nuevamente.")
            continue

def tipo_habitacion(mensaje:str):
    while True:
        habitacion_tipo = input(mensaje).lower().strip()
        if habitacion_tipo in habitaciones["precios"]:
            return habitacion_tipo, habitaciones["precios"][habitacion_tipo]
        print("Debes ingresar un tipo de habitacion. Individual - Doble - Suite")
        continue
    
while True:
    print("***Gestion de reservas de hotel***")
    opcion = validar_entero("1. Registrar nueva reserva\n2. Buscar reserva\n3. Modificar reserva\n4. Cancelar reserva\n5. Mostrar todas las reservas\n6. Salir\n: ")

    if opcion == 1:
        tipo, precio = tipo_habitacion("Ingrese el tipo de habitacion: ")
        nueva_reserva = {
            "id":validar_id("Ingrese el ID: "),
            "nombre_huesped":validar_string("Ingrese el nombre del huesped: ").capitalize(),
            "numero_habitacion":validar_entero("Ingrese el numero de habitacion: ", 101, 999),
            "tipo":tipo,
            "dias_estadia":validar_entero("Ingrese los dias de estadia: ", 1, 30)
        }
        print("La reserva se ha registrado correctamente.")
        print(f"\nEl precio total de la reserva es: ${precio * nueva_reserva['dias_estadia']} ")
        input("Presione enter para volver al menu: ")
