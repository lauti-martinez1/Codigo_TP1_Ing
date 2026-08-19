ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def funcion_ventas(ventas):
    cantidad = len(ventas)
    total = 0

    for venta in ventas:
        total += venta

    promedio = total / cantidad

    return total, promedio


total,promedio = funcion_ventas(ventas_diarias)

print("Total de ventas:", total)
print("Promedio de ventas:", promedio)