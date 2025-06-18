# Catalogo de videojuegos

datos_videojuegos = {
    "juegos":[]
}

def validar_entero(mensaje:str, maximo=None, minimo=None)->int:
    """Validar Entero"""
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if  minimo is not None and maximo is not None:
            if not minimo < entero < maximo:
                print(f"El numero ingresado debe estar dentro del rango permitido. {(minimo,maximo)}")
                continue
        if minimo is not None:
            if not entero > minimo:
                print(f"Debes ingresar un numero mayor o igual al minimo. (minimo = {minimo})")
                continue
        if maximo is not None:
            if not entero < maximo:
                print(f"Debes ingresar un numero menor o igual al maximo. (maximo = {maximo})")
                continue
        return entero

def validar_string(mensaje:str)->str:
    """Validar string"""
    while True:
        caracteres_permitidos = "qwertyuiopñlkjhgfdsazxcvbnm: QWERTYUIOPÑLKJHGFDSAZXCVBNM1234567890"
        string = input(mensaje)

        for i in string:
            if i not in caracteres_permitidos:
                print("El nombre solo debe contener letras, numeros.")
                continue
        if not 3 < len(string) < 64:
            print("El nombre debe estar dentro del rango de caracteres permitidos. (3 - 64)")
            continue
        return string

        