# PROGRAMA QUE REMPLAZA TODAS LAS VOCALES POR * Y CAMBIA A MAYUSCULAS EL STRING

userinput = input("Ingrese un texto: ")
upper = userinput.upper()

for letra in "aeiouAEIOU":
    upper = upper.replace(letra, "*")

print(upper)

