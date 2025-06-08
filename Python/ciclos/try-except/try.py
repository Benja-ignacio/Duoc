# Try - Except
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print(f"Tienes {edad} años")
        print(f"El siguiente año tendras {edad + 1} años.")

    except ValueError:
        print(f"Debe ingresar su edad en enteros (Ej: Edad = 10)")
    else:
        break