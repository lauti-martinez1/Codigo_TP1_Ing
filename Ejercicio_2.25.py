
def analizar_finanzas(**kwargs):
    balance_final = 0
    for valor in kwargs:
        balance_final += kwargs[valor]

    return balance_final


resultado = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(resultado)