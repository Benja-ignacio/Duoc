""" Beneficios para Nuevos Empleados en una Empresa Tecnológica

Una empresa de tecnología ofrece distintos beneficios económicos a sus nuevos empleados en función de su rendimiento en el proceso de selección y la ciudad desde la cual provienen. El rendimiento se evalúa con una nota de 1.0 a 7.0, y las ciudades están agrupadas en tres zonas: Zona Norte, Zona Centro y Zona Sur.

Los beneficios se otorgan sobre el bono anual, que corresponde a $2.500.000. A continuación, se muestran las condiciones y descuentos aplicables al bono:

Evaluación de ingreso	Zona de origen	Descuento sobre bono
Nota mayor a 6.0	Zona Sur	25% de descuento
Nota mayor a 6.0	Zona Centro	20% de descuento
5.0 a 6.0	Zona Sur	15% de descuento
4.0 a 5.0	Zona Centro	10% de descuento

Además:

Todos los empleados provenientes de Zona Norte obtienen automáticamente un descuento del 12% sobre el bono.

Si el empleado es de la Zona Norte y obtuvo nota mayor o igual a 5.5, se le otorga un descuento adicional del 5%.

El programa debe solicitar al usuario:

Nota obtenida en la evaluación de ingreso.

Zona de origen (Norte, Centro o Sur). """



# ENTRADA. PEDIRLE AL USUARIO QUE INGRESE LA NOTA OBTENIDA Y LA ZONA DE ORIGEN

nota_obtenida = float(input("Ingrese la nota obtenida: ")) # ahora lo que el usuario escriba quedara guardado en las variables
zona = input("Ingrese la zona de origen: ").lower() # la funcion lower convierte todo lo que el usuario escriba a minuscula
bono_anual = 2500000 


# SALIDA/LOGICA/IF's

if zona == "sur":
    if nota_obtenida > 6.0 and nota_obtenida <= 7.0:
        print(f"EL bono a recibir con el descuento aplicado de (25%) es de: {bono_anual - (bono_anual * 0.25)}")
    if nota_obtenida >= 5.0 and nota_obtenida <= 6.0:
        print(f"El bono a recibir con el descuento aplicado de (15%) es de: {bono_anual - (bono_anual * 0.15)}")

if zona == "centro":
    if nota_obtenida > 6.0 and nota_obtenida <= 7.0:
        print(f"El bono a recibir con el descuento aplicado de (20%) es de: {bono_anual - (bono_anual * 0.20)}")
    if nota_obtenida >= 4.0 and nota_obtenida <= 5.0:
        print(f"El bono a recibir con el descuento aplicado de (10%) es de: {bono_anual - (bono_anual * 0.10)}")

if zona == "norte":
    if nota_obtenida >= 5.5 and nota_obtenida <= 7.0:
        print(f"El bono a recibir con el descuento aplicado de (17%) es de: {bono_anual - (bono_anual * 0.17)}")
    else:
        print(f"El bono a recibir con el descuento aplicado de (12%) es de: {bono_anual - (bono_anual * 0.12)}")


