import re

def string(mensaje, formato):
    while True:
        texto = input(mensaje).strip()
        if re.fullmatch(formato, texto):
            return texto
        print("Formato Incorrecto!")

# Ejemplos 

# Solo letras minusculas
t1 = string("Test: ", r"^[a-z]+$").capitalize()
print(t1)

# Letras minusculas + mayusculas
t2 = string("test: ", r"^[a-zA-Z]+$")
print(t2)

# Letras minusculas + mayusculas + espacios + numeros
t3 = string("test: ", r"^[a-zA-Z \d]+$")
print(t3)

# minimo y maximo de caracteres
t4 = string("test: ", r"^[a-zA-Z]{3,24}+$") # minimo 3 y maximo de 24
t5 = string("test", r"^[a-zA-Z]{24}+$") # maximo 24

# Solo permite ingresar una letra sea minuscula o mayuscula.
t6 = string("test", r"^[a-zA-Z]$")
t6 = string("test", r"^[a-zA-Z]+$") # Permite solo letras minusculas y mayusculas, sin limite ya que no lo especifique
#                                     #NOTE En re.fullmatch no es necesario el $ que significa fin del texto, ya que en fullmatch exige que todo el string coincida.

#  Primera letra debe ser mayuscula
#NOTE sin el + al final solo acepta 2 letras
t7 = string("test: ", r"^[A-Z][a-z \d]")
print(t7)
# Esto significa que la primera letra debe ser mayuscula y las demas minusculas o numeros.
t7 = string("test: ", r"^[A-Z][a-z \d]+")

# | Regex              | Significado                                 |
# | ------------------ | ------------------------------------------- |
# | `[a-z]{3}`         | exactamente 3 letras minúsculas             |
# | `\d{2,4}`          | entre 2 y 4 dígitos                         |
# | `[A-Z][a-z]{2,10}` | una mayúscula seguida de 2 a 10 minúsculas  |
# | `[a-zA-Z0-9]{6}`   | exactamente 6 letras o números              |
# | `[a-zA-Z0-9]{1,}`  | al menos una letra o número (como usar `+`) |

# re.fullmatch(r"^[A-Z][a-z]{2}[\d]{2}$", "Abc12")
# ✅ Coincide si:

# 1 mayúscula

# 2 minúsculas

# 2 dígitos

# Ej: "Abc12" ✅

# "Abe123" ❌ (tiene 3 dígitos)

# ✅ Resumen rápido de {}
# Símbolo	Significado	Ejemplo
# {n}	Exactamente n repeticiones	a{3} = "aaa"
# {n,}	Al menos n repeticiones	a{2,} = "aa" o más
# {n,m}	Entre n y m repeticiones	a{2,4} = "aa", "aaa", "aaaa"



            