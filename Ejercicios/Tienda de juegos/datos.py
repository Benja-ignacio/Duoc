videojuegos = {
    "juegos":
    {
        'GOW001': ['God of War', 'PSS', 'Aventura', 'M', 'Santa Monica Studio', 2022, 'Sony'],
        'ZEL002': ['The Legend of Zelda: Tears of the Kingdom', 'Switch', 'Aventura', 'E10+', 'Nintendo', 2023, 'Nintendo'],
        'ELD003': ['Elden Ring', 'Multiplataforma', 'RPG', 'M', 'FromSoftware', 2022, 'Bandai Namco'],
        'SPD004': ['Spider-Man 2', 'PS5', 'Acción-Aventura', 'T', 'Insomniac Games', 2023, 'Sony'],
        'MNC005': ['Minecraft', 'Multiplataforma', 'Sandbox', 'E', 'Mojang', 2011, 'Microsoft'],
        "FNF006": ["Five Nights at Freddy's: Security Breach", 'Multiplataforma', 'Terror', 'T', 'Steel Wool Studios', 2021, 'ScottGames'],
        'GT7007': ['Gran Turismo 7', 'PS5', 'Carreras', 'E', 'Polyphony Digital', 2022, 'Sony'],
        'HLY008': ['Hogwarts Legacy', 'Multiplataforma', 'RPG', 'T', 'Avalanche Software', 2823, 'Warner Bros']
    },
    "stock":
    {
        'GOW001': [59_990, 12],
        'ZEL002': [69_990, 8 ],
        'ELD003': [49_990, 15],
        'SPD004': [64_900, 5 ],
        'MNC005': [19_900, 30],
        'FNF006': [34_900, 7 ],
        'GT7007': [54_900, 10],
        'HLY008': [59_990, 6 ]
    }
}

# for i in videojuegos['juegos']:
#     juegos = videojuegos['juegos'][i]
#     juegos.insert(0,i)
# print(F"""
# ID: {juegos[0]}
# Nombre: {juegos[1]}
# Plataforma: {juegos[2]}
# Genero: {juegos[3]}
# Clasificacion: {juegos[4]}
# Desarrollador: {juegos[5]}
# Año de lanzamiento: {juegos[6]}
# Publicador: {juegos[7]}
# """)
                
for i in videojuegos['juegos']:
    print(i)