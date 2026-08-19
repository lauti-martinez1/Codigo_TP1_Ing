resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calculos(resultados):
    total_anotados = 0
    total_recibidos = 0

    for partido in resultados.items():
        total_anotados += partido[1][0]
        total_recibidos += partido[1][1]

    return total_anotados, total_recibidos


anotados, recibidos = calculos(resultados)
print("Anotados: " + str(anotados))
print("Recibidos: " + str(recibidos))