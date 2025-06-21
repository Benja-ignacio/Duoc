# Catalogo de videojuegos
import re

datos_videojuegos = {"juegos":[]}

def validar_entero(mensaje:str, max=None, min=None)->int:
    """Validar Entero"""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if  min is not None and max is not None:
            if not min <= valor <= max:
                print(f"El numero ingresado debe estar dentro del rango permitido. {(min,max)}")
                continue
        if min is not None and valor < min:
            print(f"Debe ser >= al minimo. (min = {min})")
            continue
        if max is not None and valor > max:
            print(f"Debe ser <= al maximo. (max = ({max})")
            continue
        return valor

def validar_string(mensaje:str, formato)->str:
    """Validar string"""
    while True:
        texto = input(mensaje).strip().capitalize()
        if re.fullmatch(formato, texto):
            return texto
        print("Formato incorrecto!")

test = validar_string("test: ", r"^[A-Z][a-z \d]+$")