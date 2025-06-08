notas = []
while True:
    try:
        agregar_nota = float(input("Ingrese su nota: "))
        if agregar_nota < 1.0 or agregar_nota > 7.0:
            print("Debes ingresar una nota valida. (1.0 - 7.0)")
            continue
        else:
            notas.append(agregar_nota)
            print(f"La nota {agregar_nota} ha sido añadida.")
    except ValueError:
        print("Debes ingresar una nota valida. (1.0 - 7.0)")
        continue
    while True:
        preguntar = input("Desea agregar mas notas o imprimir las estadisticas?\n1. Agregar mas notas\n2. Imprimir las estadisticas\n: ")
        if preguntar < "1" or preguntar > "2":
            print("Debes ingresar una opcion valida. (1-2) )")
            continue
        if preguntar == "1":
            break
        else:
            break
    if preguntar == "2":
        promedio_final = sum(notas) / len(notas)
        print(f"Notas: {notas}")
        print(f"Total de notas: {len(notas)}")
        print(f"Promedio final: {promedio_final}")
        break