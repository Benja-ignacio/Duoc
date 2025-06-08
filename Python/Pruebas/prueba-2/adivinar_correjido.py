import random

minimo = int(input("Ingrese el inicio de la zona de búsqueda: "))
maximo = int(input("Ingrese el límite de la zona de búsqueda: "))
numero_aleatorio = random.randint(minimo, maximo)

intentos = 0
ultimo_intento = None

while intentos < 3:
    try:
        numero = int(input(f"Intento {intentos + 1}: Ingrese un número entre {minimo} y {maximo}: "))
        
        if numero < minimo or numero > maximo:
            print("¡Debes elegir un número dentro del rango!")
            continue  # no cuenta como intento válido
        
        intentos += 1
        ultimo_intento = numero

        if numero == numero_aleatorio:
            print("🎉 ¡Felicidades, adivinaste el número!")
            break
        elif numero > numero_aleatorio:
            print("🔻 El número ingresado es mayor que el número aleatorio.")
        else:
            print("🔺 El número ingresado es menor que el número aleatorio.")

    except ValueError:
        print("Formato inválido. Ingresa un número válido.")

if ultimo_intento != numero_aleatorio:
    print(f"❌ Perdiste. El número correcto era {numero_aleatorio}.")
