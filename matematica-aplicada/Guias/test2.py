datos = []

def cantidad_datos(segundos):
    megabits_por_segundo = 100
    datos = segundos * megabits_por_segundo
    return datos


contador = 0
incremento = 100

while contador < 1001:
    resultado = cantidad_datos(contador)
    datos.append(resultado)
    print(datos)    
    contador += 100
