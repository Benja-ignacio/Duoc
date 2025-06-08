""" El Tesoro de la Isla Aleatoria
Una antigua leyenda pirata dice que hay un tesoro escondido en una isla dividida en varias
zonas numeradas. El jugador deberá elegir dos números que representen los límites de las
zonas de búsqueda (por ejemplo, 1 y 50). El sistema elegirá aleatoriamente una zona
donde se escondió el tesoro.
El objetivo es encontrar el tesoro antes de que el detector de metales se quede sin batería
(tienes 3 intentos).
Mecánica del juego:
• En cada intento, el jugador escoge una zona.
• Si acierta, gana el juego y se imprime: "¡Tesoro encontrado! ¡Felicidades, pirata!"
• Si no acierta:
o En el segundo intento, se le dirá si su intento anterior fue “muy cerca” (a
menos de 3 zonas de distancia) o “muy lejos”.
o En el tercer intento, si aún no acierta, pierde y se imprime: "El tesoro
seguirá perdido por siempre... """

import random

# ENTRADA

# Solicitamos al usuario el minimo y el maximo 
minimo = int(input("Ingrese el minimo de la zona de busqueda: "))
maximo = int(input("Ingrese el limite de la zona de busqueda: "))

# USAMOS RANDOM.RANDINT PARA GENERAR EL TESORO 
tesoro = random.randint(minimo, maximo)

# CREAMOS LA VARIABLE ADIVINAR DONDE SE GUARDARA EL NUMERO ESCODIGO
adivinar = int(input("Ingrese un numero dentro de la zona escogida: "))


# SALIDA/LOGICA/IF'S 

# iNTENTO 1 
if adivinar == tesoro:
    print("¡Tesoro encontrado! ¡Felicidades, pirata!")
else:
    adivinar = int(input("Vuelva a intentarlo: "))

# iNTENTO 2 
if adivinar == tesoro:
    print("¡Tesoro encontrado! ¡Felicidades, pirata!")
else:              
    if abs(adivinar - tesoro) <3: #NOTA CON LA FUNCION ABS SE PUEDE SABER LA DISTANCIA ENTRE EL TESORO Y ADIVINAR EJ: Si el tesoro está en la zona 10: Si el jugador dice 8 ➔ distancia = 2 (porque abs(8 - 10) = 2) Si dice 13 ➔ distancia = 3 (porque abs(13 - 10) = 3)
        print("Estas muy cerca!!")
    else:
        print("Muy lejos!!")
    adivinar = int(input("Vuelva a intentarlo: "))

# INTENTO 3 
if adivinar == tesoro:
    print("¡Tesoro encontrado! ¡Felicidades, pirata!")
else:
    print("El tesoro seguirá perdido por siempre...")
    print(f"El tesoro se encontraba en: {tesoro}.")

    