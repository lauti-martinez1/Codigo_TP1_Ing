puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def obtener_puntuacion(tupla):
    return tupla[1]

resultado = sorted(puntuaciones, key=obtener_puntuacion, reverse=True)
print(resultado)