hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]

tendencias = [
    ("#verano", 120),
    ("#moda", 80),
    ("#tecnologia", 150)
]

def analizar_tendencias(hashtags, tendencias, minimo):
    resultado = []

    for hashtag, frecuencia in tendencias:
        if frecuencia > minimo:
            resultado.append(hashtag)

    return resultado


print(analizar_tendencias(hashtags, tendencias, 100))