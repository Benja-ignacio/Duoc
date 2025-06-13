def validar_entero(mensaje, minimo=None,maximo=None):
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero")
            continue

        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"Debes ingresar un número entre {minimo} y {maximo}.")
                continue

        if minimo is not None and entero < minimo:
            print(f"Debes ingresar un número mayor o igual a {minimo}.")
            continue

        if maximo is not None and entero > maximo:
            print(f"Debes ingresar un número menor o igual a {maximo}.")
            continue

        return entero


