precios_diarios = [100, 105, 102, 110, 108]

operaciones = [
    ("compra", 0),
    ("venta", 3),
    ("compra", 2),
    ("venta", 4)
]

def simular_mercado(precios, operaciones):
    beneficio = 0

    for operacion, dia in operaciones:
        if operacion == "compra":
            beneficio -= precios[dia]
        elif operacion == "venta":
            beneficio += precios[dia]

    return beneficio


print(simular_mercado(precios_diarios, operaciones))