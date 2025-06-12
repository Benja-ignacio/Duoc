numeros = "1 2 3 4 5 6      7                               8" 
numeros = ",".join(numeros.split())
numeros = numeros.split(",")
numeros_lista = []
for i in numeros:
    numeros_lista.append(int(i))
print(numeros_lista)
