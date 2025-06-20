import re
while True:
    nombre = input("nombre: ").capitalize()
    if not re.fullmatch(r"^[A-Z][a-z ]{2,24}$", nombre):
        print("El nombre solo debe llevar letras minusculas, espacios y debe estar dentro del rango de caracteres permitidos. (3,24).")
        continue
    else:
        print(nombre)

