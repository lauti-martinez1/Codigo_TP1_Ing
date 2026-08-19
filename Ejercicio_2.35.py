rutas = [
    ("Madrid", "Barcelona", 620),
    ("Madrid", "Valencia", 350),
    ("Barcelona", "Valencia", 350)
]

distancias_max = [600, 400, 500]


def rutas_validas(rutas, distancias_max):
    resultado = []

    for i in range(len(rutas)):
        if rutas[i][2] <= distancias_max[i]:
            resultado.append(rutas[i])

    return resultado


print(rutas_validas(rutas, distancias_max))