from flask import Flask, request, redirect
# Importa módulo que hace el grabado del registro en archivo
from persistencia import guardar_pedido
app = Flask (__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    nombre = request.form.get("p1_nombre")
    apellido = request.form.get("p2_apellidos")
    print("El solicitante del pedido es: "+ nombre + " " + apellido)

    # Crea y limpia el fichero pedidos.txt
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    guardar_pedido(nombre,apellido)

    return redirect("http://localhost/solicita_pedido.html", code=302)