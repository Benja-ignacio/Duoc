datos_videojuegos = {
    "juegos":[
        {
        "id":123,
        "nombre":"test",
        "anio":"hola"
        }
    ]
}

def guardar_datos():
    import json
    while True:
        opciones = int(input())
        # Nombre del archivo
        if opciones == 1:
            nombre_archivo = input()
            
            # Contenido del archivo
            contenido = datos_videojuegos["juegos"]

            # Abrir el archivo en modo escritura y escribe el contenido
            with open(nombre_archivo, 'w') as file:
                file.write(str(contenido))

            print(f"file {nombre_archivo} creada.")
            input("\nPresione enter para volver al menu principal: ")
            return
        elif opciones == 2:
            nombre_archivo = input()
            with open(nombre_archivo, "w") as json_file:
                json.dump(datos_videojuegos["juegos"], json_file)
            print("Archivo Json creado correctamente!")
            input("\nPresione enter para volver al menu principal: ")
            return

guardar_datos()