estudiantes = {
    101: {
          "nombre": "Ana",
          "edad": 16,
          "calificaciones": {
              "matemáticas": 85, "ciencias": 90
          }
    },

    102: {
        "nombre": "Luis",
        "edad": 17,
        "calificaciones": {
            "matemáticas": 78, "ciencias": 88
        }
    }
}


def promedio(estudiantes, id):
    estudiante = estudiantes[id]
    promedio = (estudiante["calificaciones"]["matemáticas"] + estudiante["calificaciones"]["ciencias"]) / 2

    return promedio

print(promedio(estudiantes, 101))