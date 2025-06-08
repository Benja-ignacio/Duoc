# Menu 
while True:
    try:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero:"))
        

        if num1 < 0 or num2  < 0:
            print("No puedo ingresar numeros negativos")
            continue
        break
    except ValueError:
        print("Solo debe ingresar numeros enteros.")
        continue
    


while True:
    print("---Menu---")
    print("[1] - Sumar")
    print("[2] - Restar")
    print("[3] - Multiplicar")
    print("[4] - Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Solo debe ingresar numeros enteros.")
        continue


    if opcion == 1:
        print(f"El resultado de la suma de {num1} + {num2} es: {num1 + num2}")
    elif opcion == 2:
        print(f"El resultado de la resta de {num1} - {num2} es: {num1 - num2}")
    elif opcion == 3:
        print(f"El resultado de la multiplicacion de {num1} * {num2} es: {num1 * num2}")
    elif opcion == 4:
        print("Salir.")
        break
    else:
        print("La opcion ingresada no es valida. Debe estar entre las opciones posibles (1 - 4) ")
    