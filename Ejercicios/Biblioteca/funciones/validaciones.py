import funciones
from time import sleep as pausa


def existe_usuario(usuario_id, biblioteca):
    for i in biblioteca['usuarios']:
        if i['id'] == usuario_id:
            return True
    return False

def validar_id_usuario(mensaje):
    while True:
        usuario_id = input(mensaje)
        
        if not existe_usuario(usuario_id):
            return usuario_id
        print("El ID de usuario ingresado se encuentra en uso.")


def existe_libro_id(libro_id, biblioteca):
    for i in biblioteca['libros']:
        if i['id'] == libro_id:
            return True
    return False
    
def hay_datos(biblioteca):
    funciones.limpiar()
    if not biblioteca["libros"]:
        print("No hay Libros registrados. Volviendo al menu principal...")
        pausa(1.5)
        return False
    return True

