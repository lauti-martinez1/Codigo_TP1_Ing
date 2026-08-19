inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inventario, ventas):
    for i in range(len(inventario)):
        inventario[i] -= ventas[i]

    return inventario

print(actualizar_inventario(inventario, ventas))