def calcular_promedio(*notas):
    total = 0
    for nota in notas:
        total += nota

    return total/len(notas)

print(calcular_promedio(85, 90, 78, 92))