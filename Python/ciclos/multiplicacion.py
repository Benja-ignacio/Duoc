multiplo = int(input("Ingrese la cantidad de multiplos: "))
tabla = int(input("Ingrese la tabla a multiplicar: "))

for i in range(multiplo):
    print(f"{i+1} x {tabla} = {(i + 1) * tabla}")