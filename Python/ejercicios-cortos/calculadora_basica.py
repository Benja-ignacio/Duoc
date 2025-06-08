# Programa que pide dos numeros y permite sumarlos, multiplicarlos, dividirlos, y restarlos

def calc_basica():

    """ 'Interfaz' de la calculadora."""
    print("***Calculadora Basica***\n\nElija una opcion de la Calculadora.")
    """OPCIONES"""
    print("\n**Opciones**")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")

    while True:    
        try:
            userinput = int(input("\nIngrese su Opcion: "))

            if userinput < 1 or userinput > 4:
               print("Por favor, Ingrese solo las opciones posibles(1-4).")
            else:
                break
        except ValueError:
            print("Por favor, Ingrese solo las opciones posibles(1-4)")
   
    while True:      
        try:
           num1 = int(input("Ingrese su primer Numero: "))
           num2 = int(input("Ingrese su segundo Numero: "))
           break
        except ValueError: # Verifica si el valor ingresado es correcto
            print("Por favor Ingrese solo numeros enteros.")
    
    
    # verifica la entrada del usuario y devuelve la operacion segun la opcion escodida 
    if userinput == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
    elif userinput == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
    elif userinput == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
    elif userinput == 4:
            print(f"{num1} / {num2} = {num1 / num2}")

calc_basica()