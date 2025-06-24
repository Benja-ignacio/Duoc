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

tipo, precio = tipo_habitacion()
print(tipo, precio)