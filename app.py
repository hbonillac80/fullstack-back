""" Programa principal - Author: Hugo Bonilla C. - Tarea: Actividad Final """
from flask import Flask, request, redirect, Response
# Importa módulo que hace el grabado del registro en archivo
from persistencia import guardar_pedido
app = Flask (__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    """ Programa para solicitar Pizza """
    nombre = request.form.get("p1_nombre")
    apellido = request.form.get("p2_apellidos")
    print("El solicitante del pedido es: "+ nombre + " " + apellido)

    # Crea y limpia el fichero pedidos.txt
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    guardar_pedido(nombre,apellido)

    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get("p6_list_tampizza")
    if size=="S":
        mensaje = "No Disponible"
    else:
        mensaje = "Disponible"

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
