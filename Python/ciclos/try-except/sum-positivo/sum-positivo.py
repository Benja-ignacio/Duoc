# Pide al usuario 5 numeros. Solo suma los positivos y muestra el total. Si se ingresa un valor no numerico, pide el numero otra vez

total = 0

while True:
    try:
        for i in range(0, 5):
            nums = int(input("Ingrese 5 numeros: "))
            if nums <= 0:
                print("Debe ingresar un numero valido mayor a 0.")
                break
            total += nums
        print(f"El numero total de los 5 numeros elegidos es: {total}")
        break

    except ValueError:
        print("Error!, Debe ingresar un numero valido mayor a 0.")
