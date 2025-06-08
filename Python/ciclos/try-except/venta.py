ingreso_total = 0
while True:
    try:
        venta_pasaje = int(input("Cuantos pasajes desea vender?\nIngrese la cantidad: "))
        if venta_pasaje <= 0:
            print("Debe ingresar un numero mayor a 0.")
            continue
        for i in range(0,venta_pasaje):
            while True:
                try:
                    precio_pasaje = float(input("Ingrese el precio de cada pasaje: "))
                    if precio_pasaje <= 0:
                        print("Debe ingresar un numero mayor a 0")
                        continue
                    ingreso_total += precio_pasaje
                    break
                except ValueError:
                    print("Debe ingresar un valor numerico valido.")
        print(f"El valor total de ingresos por la venta de pasajes es: {ingreso_total}")
        break

    except ValueError:
        print("Debe ingresar un valor numerico valido.")