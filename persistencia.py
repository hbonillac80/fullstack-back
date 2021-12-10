# Autor: Hugo Bonilla C.
# Módulo: Fundamentos Full Stack
# Tarea: Actividad 1 - Final Flask

def guardar_pedido(nombre, apellidos):
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("Graba pedido de: " + nombre + " " + apellidos + "\n")
        file.close()