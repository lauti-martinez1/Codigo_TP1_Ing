temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def calculos(temperaturas):
    total = 0

    for x in temperaturas:

        total += x

    resultados = [total/len(temperaturas), max(temperaturas), min(temperaturas)]


    return resultados


print (calculos(temperaturas))