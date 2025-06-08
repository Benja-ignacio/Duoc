import time

print("***** POKÉMON GAME SHOP *****\n¡Bienvenido al sistema de gestión de la tienda!") 

cantidad_stock = 50
while True:
    try:
        opcion = int(input("1) Ver cartas disponibles en stock\n2) Vender cartas a un entrenador\n3) Agregar nuevas cartas al inventario\n4) Salir\nIngrese una opcion: "))
        if opcion <=0 or opcion >4:
            print("Debe elegir una opcion entre el rango disponible (1-4)")

        if opcion == 1:
            print("Haz Seleccionado\n Ver cartas Disponibles en stock\n\nCartas En Stock: 50")
            while True:
                try:
                    if cantidad_stock <= 0:
                        break
                    nombre_pokemon = input("Ingrese el nombre del pokemon que desea: ").strip()
                    if not nombre_pokemon:
                        print("El nombre del pokemon no puede estar vacio")
                        continue
                    if len(nombre_pokemon) <=0 or len(nombre_pokemon) <4:
                        print("El pokemon debe tener minimo 4 caracteres")
                        continue
                    if any(char.isdigit() for char in nombre_pokemon):
                        print("El nombre no puede llevar numeros.")
                    else:
                        while True:
                            try:
                                cantidad = int(input("Ingrese la cantidad de cartas que desea comprar: "))
                                if cantidad <= 0 or cantidad > 50:
                                    print("El numero debe estar entre el rango del stock disponible (1-50)")
                                    continue
                                if cantidad > cantidad_stock:
                                    print(f"No queda stock suficiente. Stock: {cantidad_stock} ")
                                    continue
                                print(f"Haz comprado ({cantidad}) cartas de {nombre_pokemon}.")
                                
                                cantidad_stock -= cantidad
                                time.sleep(1)
                                preguntar = int(input("Desea comprar mas cartas o volver al menu principal?\n1) Volver al menu principal \n2) Comprar mas cartas\nElija una opcion: "))
                                if preguntar <=0 or preguntar >2:
                                    print("Debe ingresar una opcion dentro del rango disponible(1-2)")
                                    continue
                                if preguntar == 1:
                                    break
                                else:
                                    if cantidad_stock <=0:
                                        print("No quedan cartas en stock")
                                        print("Volviendo al menu principal...")
                                        time.sleep(1)
                                        break
                                    else:
                                        continue
                            except ValueError:
                                print("Debes ingresar un numero valido.")

                except ValueError:
                    print("Debes ingresar un nombre valido.")


        
        if opcion == 2:
            print("Haz Seleccionado ---Vender cartas a un entrenedor---")
            try:
                cartas_total = int(input("Cuantas cartas tienes disponible para vender?: "))
                while True:
                    try:
                        if cartas_total == 0:
                            print("No tienes cartas para vender.\nVolviendo al menu principal...")
                            time.sleep(1)
                            break
                        vender_cartas = int(input("Cuantas cartas desea vender?: "))

                        
                        if vender_cartas > cartas_total:
                            print("No puedes vender mas cartas de las que tienes.")

                        print(f"Haz vendido {vender_cartas}")
                        cartas_total -= vender_cartas

                        preguntar = int(input("Desea vender mas cartas o volver al menu principal?\n1) Volver al menu principal: \n2) Vender mas cartas: "))
                        if preguntar <=0 or preguntar >2:
                            print("Debe ingresar una opcion dentro del rango disponible(1-2)")
                            continue
                        if preguntar == 1:
                            break
                        else:
                            continue
                    except ValueError:
                        print("Debe ingresar un numero valido mayor a 0.")
    
            except ValueError:
                print("Debes ingresar un numero entero.")

        if opcion == 3:
            print("Haz Seleccionado\n ---Agregar cartas al inventario---")
            while True:
                try:
                    agregar_stock = int(input("Cuantas cartas desea agregar al stock?: "))
                    if agregar_stock <=0:
                        print("No puedes agregar 0 de stock.")
                        continue
                    else:
                        print(f"Haz agregado {agregar_stock} cartas al stock")
                        print(f"Stock inicial: {cantidad_stock}")
                        print(f"Stock nuevo: {cantidad_stock + agregar_stock}")
                        cantidad_stock += agregar_stock
                        preguntar = int(input("Desea agregar mas cartas o volver al menu principal?\n1) Volver al menu principal: \n2) agregar mas cartas: \nElija una opcion: "))
                        if preguntar <=0 or preguntar >2:
                            print("Debe ingresar una opcion dentro del rango disponible(1-2)")
                            continue
                        if preguntar == 1:
                            break
                        else:
                            continue
                except ValueError:
                    print("Numero no valido. Debes ingresar un numero mayor a 0.")
        if opcion == 4:
            print("Saliendo...")
            time.sleep(1.5)
            break
    except ValueError:
        print("Debe ingresar un numero en el rango disponible (1-4)")
        


