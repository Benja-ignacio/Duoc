estudiantes = [16.43, 19.31, 10.25, 18.63, 17.85, 19.76, 26.64, 21.94,21.3, 22.67, 16.48]

categorias = ["Bajo peso", "Peso normal", "Sobrepeso", "Obesidad"]

def categorias_imc(imc):
        if imc < 18.5:
            return categorias[0]
        elif 18.5 <= imc <= 24.9:
            return categorias[1] 
        elif 25 <= imc <= 29.9:
            return categorias[2]
        else:
            return categorias[3]


for indice, valor in enumerate(estudiantes, start=1):
    categoria = categorias_imc(valor)
    print(f"Estudiante {indice}: IMC {valor} Categoria {categoria}")
