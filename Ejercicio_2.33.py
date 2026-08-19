reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hotel(reservas):
    nueva_reserva = ("Lautaro",103,180)
    nueva_fecha="2024-08-15"

    fecha_existente = False
    habitacion_disponible = True

    for fecha in reservas:
        if fecha == nueva_fecha:
            fecha_existente = True
            break

    if fecha_existente:
        for fecha in reservas:
            if nueva_fecha == fecha:
                for reserva in reservas[fecha]:
                    if nueva_reserva[1] == reserva[1]:
                        habitacion_disponible = False
                        break

        if habitacion_disponible:
            reservas[nueva_fecha].append(nueva_reserva)
        else:
            print("La habitacion " + str(nueva_reserva[1]) + " no disponible en la fecha: " + str(nueva_fecha))



    else:
        reservas[nueva_fecha] = [nueva_reserva]


    return reservas


print(hotel(reservas))


