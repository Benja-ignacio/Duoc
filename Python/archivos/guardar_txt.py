# Guardar archivo como texto

# with open("test.txt", "w") as archivo:
#     archivo.write("Hola mundo!\n")
#     archivo.write("Otra linea")

guardar_input_usuario = input("Ingrese lo que desea guardar: ")
nombre_archivo = input("Ingrese el nombre del archivo: ") + ".txt"
print(nombre_archivo)

with open(nombre_archivo, "w") as archivo:
    archivo.write(guardar_input_usuario)

print(f"Se ha creado el archivo {nombre_archivo}")