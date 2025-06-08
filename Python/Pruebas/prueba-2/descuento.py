# EJERCICIOS PRUEBA 2 / PROGRAMACION

promedio_final = float(input("Ingrese su promedio final: "))
decil = int(input("Ingrese al decil al que pertenece(1-10): "))

arancel = 2_200_000
matricula = 95_000
descuento = 0 
descuento_matricula = 0

if decil == 1 or decil == 2:
    if promedio_final > 6.5 and promedio_final <= 7.0:
        descuento += .25
        descuento_matricula += .17
    
    elif promedio_final >= 1 and promedio_final < 6.0:
        descuento += .15
        descuento_matricula += .12
    
    elif promedio_final <= 6.5 and promedio_final <= 7.0:
        descuento += .15
        descuento_matricula += .12

if decil == 3:
    if promedio_final > 6.5 and promedio_final <= 7.0:
        descuento += .18
        descuento_matricula += .17
    
    elif promedio_final >= 6.0 and promedio_final <= 6.5:
        descuento += .12
        descuento_matricula += .17

    elif promedio_final >= 1 and promedio_final < 6:
        descuento += .12
        descuento_matricula += .12 

if decil == 4:
    if promedio_final > 6.5 and promedio_final <= 7.0:
        descuento += .18
    
    elif promedio_final > 1.0 and promedio_final <= 6.5:
        descuento += .12


arancel_final = int(2_200_000 * (1 - descuento))
matricula_final = int(95_000 * (1 - descuento_matricula))

if decil == 1 or decil == 2 or decil == 3:
   print(f"El precio final del arancel con un descuento de {descuento*100:.0f}% es: ${arancel_final:,} ")        
   print(f"El precio final de la matricula con un descuento de {descuento_matricula*100:.0f}% es: ${matricula_final:,}")
else:
    print(f"El precio final del arancel con un descuento de {descuento*100:.0f}% es: ${arancel_final:,}")
    print(f"No aplicas para ningun descuento. El precio final de la matricula es: ${matricula_final:,}")
