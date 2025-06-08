# Pide edades y muestra el promedio
total_edades = 0
while True:
    try:
        edades = int(input("Ingrese el numero de edades: ")) 
        if edades <= 0:
            print("La edad debe ser mayor a 0.")
            continue
        for i in range(0, edades):
            while True:
                total = int(input("Ingrese las edades: "))
                if total <= 0:
                    print("Error! El numero debe ser mayor a 0.")
                    continue
                else:
                    total_edades += total 
                    break
            
        promedio = total_edades / edades
        print(f"El promedio de las edades ingresadas es: {promedio}")
        break

    
    except ValueError:
        print("Error! Entrada no valida, Ingrese un numero mayor a 0.")
    