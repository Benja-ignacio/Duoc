# Programa que cuenta caracteres 


def contar_caracteres():

    print("***   PROGRAMA QUE IMPRIME CUANTOS CARACTERES TIENE EL TEXTO INGRESADO   *****")


    userinput = input("Ingrese un texto/numero: ")
    contador = len(userinput.replace(" ",""))
    print(f"El numero total de caracteres de '{userinput}' es: {contador}")

contar_caracteres()

