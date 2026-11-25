from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS = {
    "juan": {"clave": "admin", "mensaje": "Bienvenido administrador juan"},
    "pepe": {"clave": "user", "mensaje": "Bienvenido usuario pepe"},
}


def calcular_descuento(edad):
    if edad > 30:
        return 0.25
    elif edad >= 18:
        return 0.15
    else:
        return 0.0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        tarros = int(request.form["tarros"])

        total_sin_descuento = tarros * PRECIO_TARRO
        descuento = total_sin_descuento * calcular_descuento(edad)
        total_a_pagar = total_sin_descuento - descuento

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento,
            "total_a_pagar": total_a_pagar,
        }
    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario in USUARIOS and USUARIOS[usuario]["clave"] == clave:
            mensaje = USUARIOS[usuario]["mensaje"]
        else:
            mensaje = "Usuario o contraseña incorrectos"
    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
