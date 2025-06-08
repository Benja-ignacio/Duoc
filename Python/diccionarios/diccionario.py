diccionario = {"nombre": "cesar huispe",
               "fonos": [
                   973837892,
                   984035842,
                   934574722,
               ]}

# Búsqueda
print("Nombre:", diccionario["nombre"])
print("Segundo teléfono:", diccionario["fonos"][1])

# Inserción
diccionario["email"] = "cesar.huispe@example.com"
diccionario["fonos"].append(123456789)

# Actualización
diccionario["activo"] = False
diccionario["fonos"][0] = 999999999

# Eliminación
del diccionario["activo"]
diccionario["fonos"].pop(2)
print(diccionario)