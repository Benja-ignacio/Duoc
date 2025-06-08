print("     ***** LIGA DE LA JUSTICIA ***** ")

elite = 0
novatos = 0

while True:
    try:
        cantidad_heroes = int(input("Ingrese la cantidad de heroes que desea registrar: "))
        if cantidad_heroes <=0 or cantidad_heroes >10:
            print("No puedes elegir un numero igual o menor a 0. Debes elegir dentro del rango(1-10)")
            continue
        else:
            break
    except ValueError:
        print("Debe ingresar un numero valido:")

for i in range(0,cantidad_heroes):
    while True:
        nombres = input(f"Ingrese el nombre del heroe ({i+1}): ").strip()
        if len(nombres) <=0 or len(nombres) <=3 or len(nombres) > 16:
            print("El nombre debe estar dentro de los caracteres permitidos. (4 Minimo, 16 maximo`)")
            continue
        if any(char.isdigit() for char in nombres):
            print("El nombre no debe llevar Numeros")
            continue
        if not nombres:
            print("No ingresaste ningun nombre.")
            continue
        else:
            break
    
    while True:
        try:
            edad = int(input("Ingrese la edad del Heroe: ").strip())
            if edad <=0 or edad > 200:
                print("Debes ingresar una edad valida dentro del rango maximo. (1-200)")
                continue
            elif edad <= 60:
                novatos += 1
                break
            else:
                elite += 1
                break
        except ValueError:
            print("Debes ingresar una edad valida.")

print(f"La Cantidad de Heroes de Clase Elite es: {elite}")
print(f"La Cantidad de Heroes de Clase Novatos es: {novatos}")
print(f"La cantidad de Heroes total es: {cantidad_heroes}")


