productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

def inventario (productos):

    mas_caro = 0
    producto_caro = ()

    for x in productos:
        if x[1] > mas_caro:
            mas_caro = x[1]
            producto_caro = x

    return producto_caro

print(inventario(productos))
