import sys
sys.path.append("/home/benjamin/Documents/duoc/Python")
from funciones import validacion
from time import sleep as sp
# Registro de libros en una biblioteca 

meses = {
    1:"enero",2:"febrero" ,3:"marzo",4:"abril",5:"mayo",6:"junio",7:"julio",8:"agosto",9:"septiembre",10:"octubre",11:"noviembre",12:"diciembre"
}

mes_dias = {
    "enero":31,"febrero":28,"marzo":31,"abril":30,"mayo":31,"junio":30,"julio":31,"agosto":31,"septiembre":30,"octubre":31,"noviembre":30,"diciembre":31
}


datos_biblioteca = {
    "libros":[
    ]
}
print(   " Bienvenido al registro de libros.")
while True:
    clear()
    print("   ***MENU***")
    opcion = int(input("1) Crear libro\n2) Listar libros\n3) Actualizar libro\n4) ELiminar libro\n5) Salir\n: "))
    if opcion == 1:
        while True:
            try:
                libro_id = int(input("Id del libro: "))
            except ValueError:
                print("Debes ingresar un id valido.")
                continue
            if libro_id <0:
                print("Debes ingresar un id mayor o igual a 0.")
                continue
            if any(libro["id"] == libro_id for libro in datos_biblioteca["libros"]):
                print("El id ingresado esta en uso.")
                continue
            break

        while True:
            titulo = input("Titulo del libro: ").strip().capitalize()
            if not all((char.isalpha() or char==' ') for char in titulo):
                print("El titulo no debe llevar caracteres especiales, ni numeros.")
                continue
            if not 3 < len(titulo) <= 34:
                print("El titulo debe estar dentro del rango de caracteres permitidos. (3-34)")
                continue
            break

        while True:
            autor = input("Autor del libro: ").strip().capitalize()
            if not all((char.isalpha() or char==' ') for char in titulo):
                print("El nombre de autor no debe llevar caracteres especiales, ni numeros.")
                continue
            if not 3 < len(titulo) <= 26:
                print("El nombre del autor debe estar dentro del rango de caracteres permitidos. (3-26)")
                continue
            break

        while True:
            try:
                anio_de_publicacion = int(input("Ingrese el año de publicacion del libro: "))
            except ValueError:
                print("Debes ingresar un año valido.")
                continue
            if not 1800 <= anio_de_publicacion <= 2025:
                print("Debes ingresar un año dentro del rango permitido. (1800-2025)")
                continue
            break
        while True:
                mes_nombre = None
                mes_de_publicacion = input("Ingrese el mes de publicacion del libro (numero o escrito): ").strip().lower()
                
                if mes_de_publicacion.isdigit():
                    mes_de_publicacion = int(mes_de_publicacion)
                    if 1 <= mes_de_publicacion <= 12:
                        mes_nombre = meses[mes_de_publicacion]
                    else:
                        print("Debes ingresar un numero entre 1 y 12.")
                        continue
                elif mes_de_publicacion in meses.values():
                    mes_nombre = mes_de_publicacion
                else:
                    print("Nombre invalido, debes ingresar un mes valido.")
                    
                meses_invertido = {v: k for k, v in meses.items()}
                numero_mes = meses_invertido[mes_nombre]
                dias_en_el_mes = mes_dias[mes_nombre]

                if mes_de_publicacion == meses[2]:
                    if (anio_de_publicacion % 4 == 0 and anio_de_publicacion % 100 != 0) or (anio_de_publicacion % 400 == 0):
                        mes_dias["febrero"] += 1
                break
        
        while True:
                try:
                    dia_de_publicacion = int(input("Ingrese el dia de publicacion del libro: "))
                    if 1 <= dia_de_publicacion <= dias_en_el_mes:
                        break
                    else:
                        print("Dia del fuera del rango permitido")
                        continue
                except ValueError:
                    print("Debes ingresar un dia valido del mes escogido.")
                    continue
                


        while True:
            disponibilidad = input("Disponibilidad del libro (si/no): ").strip().lower()
            if disponibilidad == "si":
                disponibilidad = True
                break
            elif disponibilidad == "no":
                disponibilidad = False
                break
            else:
                print("Debes ingresar una opcion valida. (si/no)")
                continue
        
        fecha = (dia_de_publicacion,numero_mes,anio_de_publicacion)
        libro_agregar ={
            "id":libro_id,
            "titulo":titulo,
            "autor":autor,
            "fecha":fecha,
            "disponible":disponibilidad
        }   
        datos_biblioteca["libros"].append(libro_agregar)
        print("Libro agregado.")

    if opcion == 2:
        if len(datos_biblioteca["libros"]) == 0:
            clear()
            print("No hay libros registrados.\nVolviendo al menu principal...")
            sp(1.5)
            continue
        for i in datos_biblioteca["libros"]:  
            print(f'\nID: {i["id"]}\nTitulo: {i["titulo"]}\nAutor: {i["autor"]}')
            
            dia_de_publicacion,numero_mes,anio_de_publicacion = i["fecha"]
            print(f"Fecha de publicacion: {dia_de_publicacion:02d}/{numero_mes:02d}/{anio_de_publicacion}")
            if i["disponible"] == True:
                print("Disponibilidad: Libro disponible.")
            else:
                print("Disponibilidad: Libro no disponible.")

        input("\nPresione enter para volver al menu: ")
        clear()
    
    if opcion == 3:
        if len(datos_biblioteca["libros"]) == 0:
            clear()
            print("No hay libros registrados\nVolviendo al menu principal...")
            sp(1.5)
            continue
        while True:
            try:
                ingresar_id = int(input("Ingrese el id del libro: "))
            except ValueError:
                print("Debes ingresar un id valido.")
                continue
            if ingresar_id < 0:
                print("Debes ingresar un id mayor o igual a 0")
                continue
            if not any(libro["id"] == ingresar_id for libro in datos_biblioteca["libros"]):
                clear()
                print("El id ingresado no coindice con ninguno.")
                continue

            if any(libro["id"] == ingresar_id for libro in datos_biblioteca["libros"]):
                while True:
                    try:
                        actualizar = int(input("1) Editar titulo\n2) Editar autor\n3) Editar fecha\n4) Editar disponibilidad\n5) Volver al menu principal\n:  "))
                    except ValueError:
                        clear()
                        print("Debes ingresar una opcion valida. (1-5)")
                        continue
                    if not 1 <= actualizar <= 5:
                        clear()
                        print("Debes ingresar una opcion valida. (1-5)")
                        continue
                    if actualizar == 1:
                        while True:
                            nuevo_titulo = input("Titulo del libro: ").strip().capitalize()
                            if not all((char.isalpha() or char==' ') for char in titulo):
                                print("El titulo no debe llevar caracteres especiales, ni numeros.")
                                continue
                            if not 3 < len(titulo) <= 34:
                                print("El titulo debe estar dentro del rango de caracteres permitidos. (3-34)")
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"El titulo nuevo sera {nuevo_titulo}, estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                else:
                                    break
                            if preguntar == 1:
                                for i in datos_biblioteca["libros"]:
                                    i["titulo"] = nuevo_titulo
                                break
                            else:
                                continue

                    if actualizar == 2:
                        while True:
                            nuevo_autor = input("Autor del libro: ").strip().capitalize()
                            if not all((char.isalpha() or char==' ') for char in titulo):
                                print("El nombre de autor no debe llevar caracteres especiales, ni numeros.")
                                continue
                            if not 3 < len(titulo) <= 26:
                                print("El nombre del autor debe estar dentro del rango de caracteres permitidos. (3-26)")
                                continue
                            while True:
                                try:
                                    clear()
                                    preguntar = int(input(f"El nuevo autor sera {nuevo_autor}, estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                else:
                                    break
                            if preguntar == 1:
                                for i in datos_biblioteca["libros"]:
                                    i["autor"] = nuevo_autor
                                break
                            else:
                                continue

                    if actualizar == 3:
                        while True:
                            try:
                                preguntar = int(input("1) Editar año\n2) Editar mes\n3) Editar dia\n4) Salir: "))
                            except ValueError:
                                print("Debes ingresar una opcion valida. (1-5)")
                            if not 1 <= preguntar <= 5:
                                print("Debes seleccionar una opcion valida. (1-5)")
                            if preguntar == 1:
                                while True:
                                    try:
                                        nuevo_anio_de_publicacion = int(input("Ingrese el nuevo año de publicacion del libro: "))
                                    except ValueError:
                                        print("Debes ingresar un año valido.")
                                        continue
                                    if not 1800 <= nuevo_anio_de_publicacion <= 2025:
                                        print("Debes ingresar un año dentro del rango permitido. (1800-2025)")
                                        continue
                                    while True:
                                        try:
                                            clear()
                                            preguntar = int(input(f"El nuevo año de publicacion sera {nuevo_anio_de_publicacion}, estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                        except ValueError:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        if not 1 <= preguntar <= 2:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        else:
                                            break
                                    if preguntar == 1:
                                        for i in datos_biblioteca["libros"]:
                                            if i["id"] == ingresar_id:
                                                fecha = list(i["fecha"])
                                                fecha[2] = nuevo_anio_de_publicacion
                                                i["fecha"] = tuple(fecha)
                                        break
                                    else:
                                        continue

                            if preguntar == 2:
                                while True:
                                    mes_nombre = None
                                    nuevo_mes_de_publicacion = input("Ingrese el nuevo mes de publicacion del libro (numero o escrito): ").strip().lower()
                                    
                                    if nuevo_mes_de_publicacion.isdigit():
                                        nuevo_mes_de_publicacion = int(nuevo_mes_de_publicacion)
                                        if 1 <= nuevo_mes_de_publicacion <= 12:
                                            mes_nombre = meses[nuevo_mes_de_publicacion]
                                        else:
                                            print("Debes ingresar un numero entre 1 y 12.")
                                            continue
                                    elif nuevo_mes_de_publicacion in meses.values():
                                        mes_nombre = nuevo_mes_de_publicacion
                                    else:
                                        print("Nombre invalido, debes ingresar un mes valido.")
                                        
                                    meses_invertido = {v: k for k, v in meses.items()}
                                    numero_mes = meses_invertido[mes_nombre]
                                    dias_en_el_mes = mes_dias[mes_nombre]

                                    if numero_mes == meses[2]:
                                        for libro in datos_biblioteca["libros"]:
                                            if libro["id"] == ingresar_id:
                                                anio = libro["fecha"][2]
                                                break
                                        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                                            mes_dias["febrero"] += 1
                                        else:
                                            mes_dias["febrero"] 
                                    while True:
                                        try:
                                            clear()
                                            preguntar = int(input(f"El nuevo mes de publicacion sera {nuevo_mes_de_publicacion}, estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                        except ValueError:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        if not 1 <= preguntar <= 2:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        else:
                                            break
                                    if preguntar == 1:
                                        for i in datos_biblioteca["libros"]:
                                            if i["id"] == ingresar_id:
                                                fecha = list(i["fecha"])
                                                fecha[1] = nuevo_mes_de_publicacion
                                                i["fecha"] = tuple(fecha)
                                        break
                                    else:
                                        continue
                            if preguntar == 3:
                                while True:
                                    try:
                                        nuevo_dia_de_publicacion = int(input("Ingrese el dia de publicacion del libro: "))
                                    except ValueError:
                                        if 1 <= nuevo_dia_de_publicacion <= dias_en_el_mes:
                                            pass
                                        else:
                                            print("Dia del fuera del rango permitido")
                                            continue
                                        print("Debes ingresar un dia valido del mes escogido.")
                                        continue
                                    while True:
                                        try:
                                            clear()
                                            preguntar = int(input(f"El nuevo dia de publicacion sera: {nuevo_dia_de_publicacion}, estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                        except ValueError:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        if not 1 <= preguntar <= 2:
                                            clear()
                                            print("Debes ingresar una opcion valida. (1-2)")
                                            continue
                                        else:
                                            break
                                    if preguntar == 1:
                                        for i in datos_biblioteca["libros"]:
                                            if i["id"] == ingresar_id:
                                                fecha = list(i["fecha"])
                                                fecha[0] = nuevo_dia_de_publicacion
                                                i["fecha"] = tuple(fecha)
                                        break
                                    else:
                                        continue
                            if preguntar == 4:
                                break
                    if actualizar == 4:
                        while True:
                            nueva_disponibilidad = input("Ingrese la nueva disponibilidad del libro (si/no): ").strip().lower()
                            if disponibilidad == "si":
                                disponibilidad = True
                            elif disponibilidad == "no":
                                disponibilidad = False
                            else:
                                print("Debes ingresar una opcion valida. (si/no)")
                                continue
                            while True:
                                try:
                                    clear()
                                    if disponibilidad == True:
                                        print("La nueva disponibilidad sera: Libro No disponible.", end=" ")
                                    else:
                                        print("La nueva disponibilidad sera: Libro disponible.", end=" ")
                                    preguntar = int(input(f"estas seguro?\n1) Estoy seguro\n2) Volver a editar el titulo\n: "))
                                except ValueError:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                if not 1 <= preguntar <= 2:
                                    clear()
                                    print("Debes ingresar una opcion valida. (1-2)")
                                    continue
                                else:
                                    break
                            if preguntar == 1:
                                for i in datos_biblioteca["libros"]:
                                    i["disponibilidad"] = nueva_disponibilidad
                                    break
                            else:
                                continue
                    if actualizar == 5:
                        break
            if actualizar == 5:
                break        
    if opcion == 4:
        if len(datos_biblioteca["libros"]) == 0:
            clear()
            print("No hay libros a eliminar\nVolviendo al menu principal...")
            sp(1.5)
            continue
        ingresar_id = int(input("Ingrese el id del libro a eliminar: "))
        libro_a_eliminar = None
        for libro in datos_biblioteca["libros"]:
            if libro["id"] == ingresar_id:
                libro_a_eliminar = ingresar_id
        if libro_a_eliminar:
            datos_biblioteca["libros"].remove(libro)
        else:
            print("El id ingresado no coincide con ningun libro.")
            continue
        print(f"El libro {libro['titulo']} ha sido eliminado.")
        input("Presione enter para volver al menu principal. ")
        
    if opcion == 5:
        print("Saliendo...")
        sp(1.5)
        break    
