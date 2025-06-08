# PROGRAMA QUE PIDE UN TEXTO Y ELIMINA LAS VOCALES MINUSCULAS

userinput = input("Ingrese un texto: ")
for letra in "aeiou":
    userinput = userinput.replace(letra, "")

print(userinput)