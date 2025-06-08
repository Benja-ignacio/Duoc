# PRUEBA 2 / PROGRAMACION

import random

minimo = int(input("Ingrese el inicio de la zona de busqueda: "))
maximo = int(input("Ingrese el limite de la zona de busqueda: "))
intentos = 0
numero_aleatorio = random.randint(minimo,maximo)

while intentos <= 3:

    try:
      #intento 1
        intento1 = int(input("Ingrese un numero dentro de la zona escojida: ")) # Intento 1    
    
       # Validacion numero escojido dentro del rango   
        if intento1 < minimo or intento1 > maximo:
           print("!Debes elejir un numero del rango escogido: ")
           intento1 = int(input("Vuelve a intentarlo: ")) # Intento 1
        intentos = intentos + 1
 

        if intento1 == numero_aleatorio:
           print("Felicidades pudiste adivinar!")
        elif intento1 > numero_aleatorio:
            print("El numero ingresado es mayor que el numero aleatorio!")
        else:
            print("El numero ingresado es menor que el numero aleatorio!")
    
        intento2 = int(input("Vuelve a intentarlo: ")) # Intento 2
    
        # Validacion numero escojido dentro del rango   
        if intento2 < minimo or intento2 > maximo:
           print("!Debes elejir un numero del rango escogido: ")
           intento2 = int(input("Vuelve a intentarlo: ")) # Intento 2 
        intentos = intentos + 1

    
        # intento 2 
        if intento2 == numero_aleatorio:
           print("Felicidades pudiste adivinar! ")
        elif intento2 > numero_aleatorio:
           print("El numero ingresado es mayor que el numero aleatorio!")
        else:
           print("El numero escojido es menor que el numero aleatorio!")

        distancia1 = abs(intento1 - numero_aleatorio)
        distancia2 = abs(intento2 - numero_aleatorio)
        if distancia1 > distancia2:
           print("El segundo intento estuvo mas cerca.")
        elif distancia1 < distancia2:
           print("El primer intento estuvo mas cerca.") 
        else:
           print("Los dos intentos estuvieron igual de cerca. ")
    
        # Intento 3 
        numero_escogido = int(input("Vuelva a intentarlo: ")) # Intento 3

        # Validacion numero escojido dentro del rango   
        if numero_escogido < minimo or numero_escogido > maximo:
           print("!Debes elejir un numero del rango escogido: ")
           numero_escogido = int(input("Vuelve a intentarlo: ")) # Intento 3

        if numero_escogido == numero_aleatorio:
           print("Felicidades pudiste adivinar!")
        else:
           print("Perdiste!!")
        intentos = intentos + 1
    except ValueError:
       print("Formato invalido.")

