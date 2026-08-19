empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def salarios(empleados,salario):
    empleados_mejor_salario = {}
    for id,empleado in empleados.items():
        if (empleado[2] >= salario):
            empleados_mejor_salario[id] = empleado

    return empleados_mejor_salario


print(salarios(empleados,3000))