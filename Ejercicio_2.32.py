def simular_ventas(*args):
    total = 0

    for producto, cantidad, precio in args:
        total += cantidad * precio

    return total


resultado = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print(resultado)