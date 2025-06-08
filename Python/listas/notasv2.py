notas = []
clear = "\n" * 7
while True:
    try:
        agregar_nota = input("Ingrese su nota: ").lower()
        if agregar_nota == "salir":
            break
        agregar_nota = float(agregar_nota)
        if agregar_nota < 1.0 or agregar_nota > 7.0:
            print("Debes ingresar una nota valida. (1.0 - 7.0)")
            continue
        else:
            print(clear)
            notas.append(agregar_nota)
            print(f"La nota {agregar_nota} ha sido añadida.\n\nPara salir y ver sus estadisticas debe escribir 'salir'")
    except ValueError:
        print(clear)
        print("Debes ingresar una nota valida. (1.0 - 7.0)")
        continue
    
try:
    promedio_final = sum(notas) / len(notas)
    print(f"\nNotas: {notas}")
    print(f"Total de notas: {len(notas)}")
    print(f"Promedio final: {promedio_final:.2f}")
except ZeroDivisionError:
    print("No ingresaste ninguna nota")