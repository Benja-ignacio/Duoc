def multiplicacion():
    print("Multiplicacion de dos Numeros.")
    try:
        num1 = int(input("Ingrese el Primer Numero: "))
        num2 = int(input("Ingrese el Segundo Numero: "))
        return num1 * num2
    except ValueError:
        raise ValueError("Los valores ingresados deben ser numeros enteros.")
    
print(multiplicacion())