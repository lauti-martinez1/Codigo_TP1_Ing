suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    if usuario in suscripciones:
        suscripciones[usuario].append(suscripcion)
    else:
        suscripciones[usuario] = [suscripcion]

    return suscripciones


print(actualizar_suscripcion(
    usuario="Luis",
    suscripcion="mensual",
    auto_renovacion=True
))