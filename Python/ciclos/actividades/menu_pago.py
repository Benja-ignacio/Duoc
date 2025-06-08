import time

# CREDITO MAXIMO 500.000
deuda = 100_000
saldo = 400_000
while True:
    print("---Menu de Opciones---\n[1] - Pago de tarjeta de Credito.\n[2] - Simulacion de compras.\n[3] - Salir.")

    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion <= 0 or opcion > 3:
            print("Debes ingresar un numero dentro del rango disponible (1-3)")
            continue
    except ValueError:
        print("!Error! Debe ingresar un numero dentro de los valores permitidos (1 - 3)")
        continue

    if opcion == 1:
        print("Haz seleccionado [Pago de tarjeta de Credito]\n---Pago de Tarjeta de Credito---")
        print("---Recordatorio!!---\nTienes una deuda de 100.000$ ClP")
        print("Cupo disponible: 400.000CLP")
        while True:
            try:
                monto_pagar = int(input("Ingrese el monto a pagar: "))
                if monto_pagar > 0 and monto_pagar <= 100_000:
                    print(f"Haz pagado: {monto_pagar}$")
                    print(f"La deuda luego del pago es: {deuda - monto_pagar}$")
                    print(f"El cupo disponible luego de la compra es: {saldo + monto_pagar}$ ")
                    break

                if monto_pagar > 100000 or monto_pagar <=0:
                    print("Debes ingresar un numero mayor a 0 y menor a la deuda. ")
                    continue
            except ValueError:
                print("!Error! Debe Ingresar un numero valido.")
                continue
        continue

    if opcion == 2:
        print("Haz seleccionado [Simulador De Compras]\n---Simulador De Compras---\nSaldo actual = 400.000")
        while True:
            try:
                sim_compras = int(input("Ingrese el numero de compras que desea simular: "))
                if sim_compras <=0:
                    print("El numero de compras no puede ser 0.") 
                    continue
                else:
                    break
            except ValueError:
                print("Debes ingresar un numero valido mayor a 0.")
                continue

        # Opcion 2 
        precio_total = 0
        saldo = 400_000    

        for i in range(0, sim_compras):
                while True:
                    try:
                        
                        pago = int(input(f"Ingrese el precio de la compra [{i+ 1}]: "))
                        if pago <=0:
                            print("Debes ingresar un numero mayor a 0.")
                            continue
                        else:
                            precio_total += pago
                            print(f"El saldo total luego de la compra {i + 1} es: {saldo - pago}")
                            saldo -= pago
                    except ValueError:
                        print("Debes ingresar un numero valido mayor a 0")
        print(f"El precio a pagar con la cantidad de compras de [{sim_compras}] es: {precio_total}$")
        continue
    
    if opcion == 3:
        print("Saliendo...")
        time.sleep(1)
    break
