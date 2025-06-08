total = 0 
num_validos = 0

while num_validos < 5:
    try:
        num = int(input(f"Ingrese el numero {num_validos + 1}: "))
        if num <= 0:
            print("El numero debe ser mayor a 0.")
            continue
        
        total += num
        num_validos += 1
    except ValueError:
        print("Error!, Debe ingresar un valor numerico valido!")

print(f"El total de los numeros ingresados es {total}")

    