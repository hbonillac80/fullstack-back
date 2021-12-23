""" Programa graba pedido - Author: Hugo Bonilla C. - Tarea: Actividad Final """
def guardar_pedido(nombre, apellidos):
    """ Programa para guardar pedido """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-" + nombre + " " + apellidos + "\n")
        file.close()
