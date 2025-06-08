datos = {
    "productos":[
        {
            "id_producto":1,
            "nombre":"parlante",
            "precio":500,
            "cantidad":10,
        },
        {
            "id_producto":2,
            "nombre":"chicle",
            "precio":250,
            "cantidad":5,
        }
    ]
}

for nombre in datos["productos"]:
    print(f"{nombre["nombre"]}")

while True:
    print("1 = Agregar Producto")
    print("2 = Listar Producto")
    print("3 = Editar producto Producto")
    print("4 = Eliminar Producto")
    print("5 = Salir")

    opcion = int(input("Seleccione una opcion\n: "))

    if opcion == 1:
        id_producto = int(input("Ingrese el id del producto: "))
        nombre = int(input("Ingrese el nombre del producto: "))
        precio = int(input("Ingrese el pecio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
    
        producto_agregar = {
            "id_producto":id_producto,
            "nombre":nombre,
            "precio":precio,
            "cantidad":cantidad
        }

        datos["productos"].append(producto_agregar)
        print("Producto agregado!")

    elif opcion == 2:
        for elementos in datos["productos"]:
            print(f"ID: {elementos["id_producto"]}\nNombre: {elementos["nombre"]}\nPrecio: {elementos["precio"]}\nCantidad: {elementos["cantidad"]}: ")    
            break
    
    elif opcion == 3:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if id_producto == i["productos"]:
                nombre = input("Ingrese el nombre: ")
                precio = input("Ingrese el precio: ")
                cantidad = input("Ingrese la cantidad: ")
                i["nombre"] = nombre
                i["precio"] = precio
                i["cantidad"] = cantidad
                print("Producto actualizado correctamente!")

    elif opcion == 4:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if i["id_producto"] == id_producto:
                datos["productos"].remove(i)
                print("Producto eliminado correctamente.")

    elif opcion == 5:
        break    