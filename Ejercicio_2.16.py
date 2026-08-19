def crear_perfil(**kwargs):   # ** le dice que los argumentos con nombre que reciba los junte en un diccionario, puede ser kwargs o cualquier cosa no importa el nombre
    return kwargs

print(crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")) #no es tupla esto, es un diccionario escrito de otra forma (la tupla no tiene keys)

