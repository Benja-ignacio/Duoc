def es_par(mensaje:str)->list:
    """Validar si es par o no"""
    pares = []
    impares = []
    while True:
        lista_de_numeros = input(mensaje)
        lista_de_numeros = ",".join(lista_de_numeros.split())
        lista_de_numeros = lista_de_numeros.split(",")
        numeros_lista = []
        try:
            for i in lista_de_numeros:
                numeros_lista.append(int(i))
        except ValueError:
            print("Debes ingresar un numero entero mayor a 0.")
            continue

        if any(i <=0 for i in numeros_lista):
            print("Debes ingresar un numero positivo mayor a 0.")
            continue
        
        for i in numeros_lista:
            if i % 2 == 0:
                pares.append(i)
            else:
                impares.append(i)
        return pares, impares
    
pares, impares = es_par("Ingrese numeros: ")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")