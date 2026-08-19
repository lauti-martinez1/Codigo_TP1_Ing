encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def analizar_encuestas(encuestas):
    resultados = {}

    for pregunta, respuestas in encuestas.items():
        frecuencias = {}

        for respuesta in respuestas:
            if respuesta in frecuencias:
                frecuencias[respuesta] += 1  #se le suma 1 al numero asignado a la key 5:1 -> 5:2
            else:
                frecuencias[respuesta] = 1  #se agrega la respuesta como key

        resultados[pregunta] = frecuencias

    return resultados


resultado = analizar_encuestas(encuestas)
print(resultado)