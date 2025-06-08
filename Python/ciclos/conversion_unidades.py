# conversion unidades 

print("--- Conversor de unidades ---")
while True:
    print("*** OPCIONES *** \n")
    print("1) Metros a Centimetros\n2) Kilogramas a Gramos\n3) Celcius a Fahrenheit\n4) Salir")
    try:
        opcion = int(input("\nIngrese una opcion\n: "))
        if opcion <= 0 or opcion > 4:
            print("Debes ingresar una opcion valida. (1-4)")
            continue
        elif opcion == 1:
            print("*** METROS A CENTIMETROS ***")
            while True:
                try:
                    cantidad_metros = int(input("Ingrese la cantidad de metros\n: "))
                    if cantidad_metros <=0:
                        print("Debes ingresar un numero entero mayor a 0.")
                    else:
                        print(f"{cantidad_metros} en centimetros es = {cantidad_metros * 100}/mts")
                except ValueError:
                    print("Debes ingresar un numero entero mayor a 0.")
                    continue
                try:
                    preguntar = int(input("\nDesea seguir o volver al menu principal?\n1) Volver al menu\n2) Seguir\n: "))
                    if preguntar <= 0 or preguntar > 2:
                        print("Debes ingresar una opcion valida. (1-2)")
                        continue
                    elif preguntar == 1:
                        break
                    else:
                        continue
                except ValueError:
                    print("Debe ingresar una opcion valida. (1-2)")
                    continue
        elif opcion == 2:
            print("*** KILOGRAMOS A GRAMOS ***")
            while True:
                try:
                    cantidad_kilogramos = int(input("Ingrese la cantidad de kilogramos\n: "))
                    if cantidad_kilogramos <=0:
                        print("Debes ingresar un numero entero mayor a 0.")
                    else:
                        print(f"{cantidad_kilogramos} kilogramos  = {cantidad_kilogramos * 1000}g")
                except ValueError:
                        print("Debes ingresar un numero entero mayor a 0.")
                        continue
                try:
                    preguntar = int(input("\nDesea seguir o volver al menu principal?\n1) Volver al menu\n2) Seguir\n: "))
                    if preguntar <= 0 or preguntar > 2:
                        print("Debes ingresar una opcion valida. (1-2)")
                        continue
                    elif preguntar == 1:
                        break
                    else:
                        continue
                except ValueError:
                    print("Debe ingresar una opcion valida. (1-2)")
                    continue
        elif opcion == 3:
            print("*** CELSIUS A FAHRENHEIT ***")
            while True:
                try:
                    cantidad_celsius = int(input("Ingrese la cantidad de celsius\n: "))                   
                    print(f"{cantidad_celsius}°C  = {(cantidad_celsius * 1.8) + 32}°F")
                except ValueError:
                        print("Debes ingresar un numero entero")
                        continue
                try:
                    preguntar = int(input("\nDesea seguir o volver al menu principal?\n1) Volver al menu\n2) Seguir\n: "))
                    if preguntar <= 0 or preguntar > 2:
                        print("Debes ingresar una opcion valida. (1-2)")
                        continue
                    elif preguntar == 1:
                        break
                    else:
                        continue
                except ValueError:
                    print("Debe ingresar una opcion valida. (1-2)")
                    continue
        elif opcion == 4:
            break

    except ValueError:
        print("Debe ingresar una opcion valida. (1-4)")