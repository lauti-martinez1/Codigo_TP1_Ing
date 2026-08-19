paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def viajes(paquetes):
    diccionario = {}
    for paquete in paquetes:
        diccionario[paquete[0]] = paquete[1]*paquete[2]

    return diccionario


print(viajes(paquetes))