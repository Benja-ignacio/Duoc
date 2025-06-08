heroes = ['spiderman','batman']
edad = [60, 70]
clase = ['novato', 'elite']
combinados = list(zip(heroes,edad, clase))
for nombre , edad, clase in combinados:
    print(f"Nombre: {nombre} - Edad: {edad} Clase: {clase} ")

""" Output: Nombre: spiderman - Edad: 60 Clase: novato 
            Nombre: batman - Edad: 70 Clase: elite    """