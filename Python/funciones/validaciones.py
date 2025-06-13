def validar_id(mensaje:int)->int:
    while True:
        """Valida IDs ingresados"""
        try:
            id = int(input(mensaje))
        except ValueError:
            print("El id debe ser un numero entero mayor a 0.")
            continue
        if id <=0:
            print("El id debe ser un numero entero mayor a 0.")
            continue
        return id

def validar_nombre(mensaje:str)->str:
    """Valida nombres ingresados"""
    while True:
        nombre = input(mensaje).strip().capitalize()
        if not nombre or " " in nombre:
            print("El nomnbre no debe llevar espacios ni puede estar vacio.")
            continue
        if not 3 <= len(nombre) <= 24:
            print("El nombre debe estar dentro del rango de caracteres permitidos. (3-24)")
            continue
        if not nombre.isalpha():
            print("El nombre no debe llevar caracteres especiales.")
            continue
        
        return nombre
    
def validar_apellido(mensaje:str)->str:
    """Valida apellidos ingresados"""
    while True:
        apellido = input(mensaje).strip().capitalize()
        if not all((char.isalpha() or char==' ') for char in apellido):
            print("El apellido solo puede llevar caracteres y/o espacios. ")
            continue
        if not 3 <= len(apellido) <= 24:
            print("El apellido debe estar dentro del rango de caracteres permitidos. (3-24)")
            continue

        return apellido
    
def validar_edad(mensaje:int)->int:
    while True:
        """Valida edad ingresada"""
        try:
            edad = int(input(mensaje))
        except ValueError:
            print("la edad ser un numero entero mayor a 0.")
            continue
        if not 17 <= edad <= 80:
            print("la edad debe estar dentro del rango permitido. (1-80)")
            continue
      
        return edad

def validar_carrera(mensaje:str)->str:
    """Valida carreras ingresados"""
    while True:
        carrera = input(mensaje).strip().capitalize()
        if not all((char.isalpha() or char==' ') for char in carrera):
            print("la carrera solo puede llevar caracteres y/o espacios. ")
            continue
        if not 3 <= len(carrera) <= 32:
            print("la carrera debe estar dentro del rango de caracteres permitidos. (3-32)")
            continue
        
        return carrera
