inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(tienda, **kwargs):
    for producto, cantidad in kwargs.items():
        inventario[tienda][producto] += cantidad

    return inventario

print(actualizar_inventario( tienda="Tienda A", producto_1=10, producto_2=-5 ))