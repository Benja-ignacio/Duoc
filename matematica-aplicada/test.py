estudiantes = [16.43, 19.31, 10.25, 18.63, 17.85, 19.76, 26.64, 21.94,21.3, 22.67, 16.48]

bajo_peso = []
peso_normal = []
sobre_peso = []
obesidad = []

categorias = [bajo_peso, peso_normal, sobre_peso, obesidad]


def categorias_imc(imc):
        if imc < 18.5:
            bajo_peso.append(imc)
        elif 18.5 <= imc <= 24.9:
            peso_normal.append(imc)
        elif 25 <= imc <= 29.9:
            sobre_peso.append(imc)
        else:
            obesidad.append(imc)

# contador = 0

# for i in estudiantes:
#     categorias_imc(i)

# print(f"Estudiante numero: {contador} Sobrepeso: {sobre_peso}"

for indice, valor in enumerate(estudiantes):
    print(f"Estudiante {indice}: IMC {valor} Categoria: {categorias}")
    categorias_imc(valor)
