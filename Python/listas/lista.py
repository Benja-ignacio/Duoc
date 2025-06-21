lista = [1,2,3,4,5]


def test(nombre):
    for i in lista:
        if i == nombre:
            return True
    return False

print(test(7))    