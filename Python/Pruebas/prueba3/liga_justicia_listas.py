print("***** LIGA DE LA JUSTICIA *****")

clase = []
heroes = []
edad_heroes = []
novatos = 0
elite = 0
while True:
    try:
        can_heroes = int(input("Ingrese la cantadidad de heroes que desea: "))
        if can_heroes <= 0 or can_heroes >10:
            print("La cantidad no puede ser menor a 0 ni mayor a 10.")
            continue
    except ValueError:
        print("Error! Debe ingresar un numero entero mayor a 0.")
        continue
    
    
    for i in range(0, can_heroes):
            while True:  
                    nombre_heroes = input(f"Ingrese el nombre del Heroe({i+1}): ")
                    if not nombre_heroes.strip():
                        print("No ingresaste ningun heroe.")
                        continue
                    if len(nombre_heroes) <=0 or len(nombre_heroes) <=4 or len(nombre_heroes) >16:
                        print("El nombre del heroe debe tener mas de 4 caracteres y maximo 16.")
                        continue
                    if any(char.isdigit() for char in nombre_heroes):
                        print("El nombre de Heroe no puede tener numeros.")
                        continue
                    else:
                        heroes.append(nombre_heroes)
                        break
            while True:   
                try:            
                    edad = int(input("Ingrese la edad del heroe: "))
                    if edad <=0:
                        print("La edad no puede ser igual o menor a 0.")
                        continue
                    elif edad >0 and edad <=60:
                                edad_heroes.append(edad)
                                clase.append("Novato")
                                novatos +=1
                                break
                    else:
                            edad_heroes.append(edad)
                            clase.append("Elite")
                            elite +=1
                            break
                except ValueError:
                    print("Debes ingresar una edad valida.")

    combinados = list(zip(heroes,edad_heroes,clase))
    print("\n       ***Estadisticas*** ")
    for a, b, c in combinados:  
        print(f"Nombre: {a} edad: {b} Clase: {c}")
    
    print(f"\nTotal de Heroes de clase Novato: {novatos}\nTotal de Heroes de Clase Elite: {elite}")
    break


