import json

# Datos de ejemplo
datos = {
    "entradas": [
        {"id": "abc1", "nombre": "Benjamin", "tipo": "G"}
    ]
}

# Guardar archivo
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent=4)

# Leer archivo
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
