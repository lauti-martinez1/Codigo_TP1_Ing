biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}


def libros_despues_2000(biblioteca):
    libros = []

    for titulo, informacion in biblioteca.items():
        if informacion["año"] > 2000:
            libros.append(titulo)

    return libros


resultado = libros_despues_2000(biblioteca)
print(resultado)