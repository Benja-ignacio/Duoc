# Try= - Except 

try:
    num1 = 2
    num2 = 2
    resultado = num1 / num2
    print(resultado)
except ZeroDivisionError:
    print("Division por cero no es correcto.")
else:
    print("El codigo se ejecuto sin ningun problema.")
finally:
    print("test")