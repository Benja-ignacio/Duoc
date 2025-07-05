# Sistema de Biblioteca con usuarios y prestamos
#NOTE GUARDAR LOS DATOS EN UN ARCHIVO BIBLIOTECA.JSON
from funciones import funciones, validaciones
from datos import biblioteca

def main():
    funciones.menu_principal(biblioteca)

if __name__ == "__main__":
    main()

