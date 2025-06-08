print("***** LIGA DE LA JUSTICIA *****")

novatos = 0
elite = 0
while True:
    try:
        can_heroes = int(input("Ingrese la cantadidad de heroes que desea: "))
        if can_heroes <= 0:
            print("La cantidad no puede ser menor a 0.")
            continue
        else:
            break
    except ValueError:
        print("Error! Debe ingresar un numero entero mayor a 0.")
        continue
    

for i in range(0, can_heroes):
    while True:
        nombre_heroes = input(f"Ingrese el nombre del heroe ({i+1}): ")
        if not nombre_heroes.strip():
            print("No ingresaste ningun heroe.")
            continue
        if len(nombre_heroes) <=0 or len(nombre_heroes) <4 or len(nombre_heroes) >24:
            print("El nombre del heroe debe estar dentro del rango minimo. (Minimo: 4, Maximo: 24)")
            continue
        if any(char.isdigit() for char in nombre_heroes):
            print("El nombre del heroe no puede llevar numeros.")
            continue
        else:
            break

    try:
        while True:
            edad = int(input("Ingrese la edad del superheroe: "))
            if edad <=0 or edad > 200:
                print("La edad no puede ser igual o menor a 0 y debe estar dentro del rango permitido. (1-200)")
                continue
            elif edad >0 and edad <=60:
                novatos += 1
                break
        
            elif edad > 60:
                elite += 1 
                break
    except ValueError:
        print("Debes ingresar una edad valida.")

print("")
print(F"La cantidad de heroes novatos es: {novatos}")
print(f"La cantidad de heroes de Elite es: {elite}")
