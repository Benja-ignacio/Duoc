from dbAPi import db_api
print(db_api["items"][1])

# for elementos in db_api:
#     print(elementos[0]["name"])

for personaje in db_api["items"]:
    print(f"Nombre: {personaje["name"]}, ki: {personaje["ki"]} ")