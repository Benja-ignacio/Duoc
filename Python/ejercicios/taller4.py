# Sistema de gestion de reservas de hotel 
from time import sleep as pausa

datos_hotel = {
    "reservas":[
        {
            "id":"abc1",
            "nombre":"benja",
            "habitacion":101,
            "tipo":"individual", # doble, suite
            "dias":1 # 1 minimo
        }
    ],
    "precios":
    {
        "suite":120,
        "doble":80,
        "individual":50
    }
}
# $ por dia
habitaciones = {
    "precios":
    {
        "suite":120,
        "doble":80,
        "individual":50
    }
}

def hay_datos():
    if not datos_hotel["reservas"]:
        print("No hay datos registrados. Volviendo al menu principal")
        pausa(1.5)
        return False
    return True

def validar_entero(mensaje:str, minimo=None, maximo=None)->int:
    while True:
        try:
            entero = int(input(mensaje))
        except ValueError:
            print("Debes ingresar un numero entero.")
            continue
        if minimo is not None and maximo is not None:
            if not minimo <= entero <= maximo:
                print(f"El numero debe ser mayor o igual a {minimo} y menor o igual a {maximo}")
                continue
        elif minimo is not None and entero < minimo:
            print(f"El numero debe ser mayor o igual = {minimo}")
            continue
        elif maximo is not None and entero > maximo:
            print(f"EL numero debe ser menor o igual = {maximo}")
            continue
        return entero

def validar_id(mensaje:str):
    while True:
        id_reserva = input(mensaje)
        numeros = "1234567890"
        letras = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM"
        tiene_letra = False
        tiene_numero = False
        if not 2 <= len(id_reserva) <= 10:
            print("Debe tener almenos una letra y un numero. minimo 2 y maximo 10 caracteres.")
            continue
        if any(i["id"] == id_reserva for i in datos_hotel["reservas"]):
            print("El id ingresado esta en uso.")
            continue
        for i in id_reserva:
            if i in letras:
                tiene_letra = True 
            elif i in numeros:
                tiene_numero = True

        if tiene_numero and tiene_letra:
            return id_reserva
        else:
            print("El id debe llevar al menos una letra y un numero.")
            continue

def validar_string(mensaje:str):
    while True:        
        letras = "qwertyuiopñlkjhgfdsazxcvbnmQWERTYUIOPÑLKJHGFDSAZXCVBNM "
        string = input(mensaje).strip().capitalize()
        if not 3 <= len(string) <= 32:
            print("Debe tener minimo 3 y maximo 32 caracteres.")
            continue
        if all (i in letras for i in string):
            return string
        else:
            print("Entrada invalida, intente nuevamente.")


def tipo_habitacion(mensaje:str):
    while True:
        habitacion_tipo = input(mensaje).lower().strip()
        if habitacion_tipo in habitaciones["precios"]:
            return habitacion_tipo, habitaciones["precios"][habitacion_tipo]
        print("Debes ingresar un tipo de habitacion. Individual - Doble - Suite")
        continue

def buscar_reserva():
    while True:
        if not hay_datos():
            return
        id_reserva = input("Ingrese el id de la reserva: ")
        for i in datos_hotel["reservas"]:
            if i['id'] == id_reserva:
                print(f"\nID: {i['id']}\nNombre Del Huesped: {i['nombre']}\nNumero De Habitacion: {i['habitacion']}\nTipo De Habitacion: {i['tipo']}\nDias De Estadia: {i['dias']}")
                input("\nPresione enter para volver al menu: ")
                return
        print("No se encontro ninguna reserva con el id ingresado.")
        continue

def mostrar_reservas():
    if not hay_datos():
        return
    while True:
        for i in datos_hotel["reservas"]:
            print(f"\nID: {i['id']}\nNombre Del Huesped: {i['nombre']}\nNumero De Habitacion: {i['habitacion']}\nTipo De Habitacion: {i['tipo']}\nDias De Estadia: {i['dias']}")
        input("\nPresione enter para volver al menu principal: ")
        return 

def agregar_reserva():
        tipo, precio = tipo_habitacion("Ingrese el tipo de habitacion: ")
        nueva_reserva = {
            "id":validar_id("Ingrese el ID: "),
            "nombre":validar_string("Ingrese el nombre del huesped: "),
            "habitacion":validar_num_habitacion(),
            "tipo":tipo,
            "dias":validar_entero("Ingrese los dias de estadia: ", 1, 30)
        }
        datos_hotel["reservas"].append(nueva_reserva)
        print("La reserva se ha registrado correctamente.")
        print(f"\nEl precio total de la reserva es: ${precio * nueva_reserva['dias']} ")
        input("Presione enter para volver al menu: ")
    
def cancelar_reserva():
    if not hay_datos():
        return
    while True:
        id_reserva = input("Ingrese el id de la reserva: ")
        for i in datos_hotel["reservas"]:
            if i['id'] == id_reserva:
                datos_hotel["reservas"].remove(i)
                print("La reserva se ha cancelado correctamente!")
                input("\nPresione enter para volver al menu principal...")
                return
        print("No se encontro ninguna reserva con el id ingresado.")

def validar_num_habitacion():
    while True:            
        num_habitacion = validar_entero("Ingrese el numero de habitacion (101 - 999): ", 101, 999)
        if any(i["habitacion"] == num_habitacion for i in datos_hotel["reservas"]):
            print(f"La habitacion {num_habitacion} esta reservada.")
            continue
        return num_habitacion
def modificar_reserva():
    if not hay_datos():
        return
    while True:
        id_reserva = input("Ingrese el id de la reserva: ")
        for i in datos_hotel["reservas"]:
            if i['id'] == id_reserva:
                opcion = validar_entero("1. Modificar Nombre\n2. Modificar numero de habitacion\n3. Modificar tipo de habitacion\n4. Modificar dias de estadia\n5. Salir\n: ", 1, 6)
                if opcion == 1:
                    nuevo_nombre = validar_string("Ingrese el nuevo nombre del huesped: ")
                    i['nombre'] = nuevo_nombre
                    input("El nombre de huesped se ha modificado correctamente!\n\nPresione enter para volver al menu principal...")
                
                elif opcion == 2:
                    nuevo_num_habitacion = validar_num_habitacion()
                    i["habitacion"] = nuevo_num_habitacion
                    input("El numero de habitacion se ha modificado correctamente!\n\nPresione enter para volver al menu principal...")
                
                elif opcion == 3:
                    nuevo_tipo_habitacion, _ = tipo_habitacion("Ingrese el tipo de habitacion")
                    i['tipo'] = nuevo_tipo_habitacion
                    input("El tipo de habitacion se ha modificado correctamente!\n\nPresione enter para volver al menu principal...")
                
                elif opcion == 4:
                    dias_estadia = validar_entero("Ingrese los dias de estadia: ", 1, 30)
                    i['dias'] = dias_estadia
                    input("Los dias de estadia se han modificado correctamente!\n\nPresione enter para volver al menu principal...")
        print("El id ingresado no coincide con ninguna reserva.")
        continue
while True:
    print("***Gestion de reservas de hotel***\n")
    opcion = validar_entero("1. Registrar nueva reserva\n2. Buscar reserva\n3. Modificar reserva\n4. Cancelar reserva\n5. Mostrar todas las reservas\n6. Salir\n: ", 1, 6)
    if opcion == 1:
        agregar_reserva()
    elif opcion == 2:
        buscar_reserva()
    elif opcion == 3:
        modificar_reserva()
    elif opcion == 4:
        cancelar_reserva()
    elif opcion == 5:
        mostrar_reservas()
    elif opcion == 6:
        print("Saliendo...")
        pausa(1.5)
        break

# SUGERENCIAS PARA MEJORAR EL CÓDIGO DE GESTIÓN DE RESERVAS DE HOTEL

# 1. USO DE FUNCIONES PARA ORDENAR EL CÓDIGO
# - Extraer el menú principal a una función `menu_principal()` para mantener limpio el script principal.

# 2. OPTIMIZAR VALIDACIÓN DE STRINGS
# - En `validar_string`, se puede mejorar la validación usando `all()` para asegurarse de que todos los caracteres sean válidos:
#   if all(c in letras for c in string): ...

# 3. EVITAR REPETICIÓN DE INPUT EN BUCLES INNECESARIOS
# - En funciones como `modificar_reserva`, después de modificar un campo, se puede salir del bucle si no se desea seguir modificando más campos.
# - También considerar usar un submenú dentro de la modificación por si el usuario quiere hacer varios cambios sin tener que volver al menú principal.

# 4. USO DE `str.lower()` EN COMPARACIONES
# - Para evitar errores por mayúsculas/minúsculas, normaliza el input de ID o strings al comparar:
#   if i['id'].lower() == id_reserva.lower():

# 5. EVITAR DUPLICACIÓN DE LÓGICA EN CADA FUNCIÓN
# - Algunas funciones como `buscar_reserva`, `modificar_reserva`, y `cancelar_reserva` comparten la lógica de buscar una reserva por ID.
#   Crear una función auxiliar: `obtener_reserva_por_id(id)` que retorne la reserva si existe.

# 6. MENSAJES DE USUARIO MÁS AMIGABLES
# - Usa mayúsculas bien aplicadas para que los mensajes sean más legibles. Ejemplo:
#   "El ID ingresado no se encontró." en lugar de "El id ingresado no coincide con ninguna reserva."

# 7. AGREGAR FUNCIÓN PARA MOSTRAR EL PRECIO TOTAL EN MODIFICACIONES
# - Si se cambia el número de días o el tipo de habitación, se puede recalcular el precio y mostrarlo.

# 8. AGREGAR OPCIÓN PARA CONFIRMAR ACCIONES IMPORTANTES
# - Por ejemplo, antes de cancelar una reserva, preguntar "¿Está seguro? (s/n)"

# 9. GUARDAR Y CARGAR DATOS DESDE ARCHIVO
# - Para hacer el sistema más útil a largo plazo, implementar funciones para guardar en JSON y cargar al iniciar.

# 10. TESTEO DE FUNCIONES DE FORMA AISLADA
# - Agregar pruebas pequeñas para cada función con inputs simulados para asegurar su correcto funcionamiento.

# FIN DE LAS SUGERENCIAS.
