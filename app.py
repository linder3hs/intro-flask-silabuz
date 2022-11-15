from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    user = {
        "nombre" : "Linder",
        "apellido" : "Hassinger",
        "telefono" : "999999"
    }
    
    # return render_template("index.html", 
    #     nombre = user["nombre"],
    #     apellido = user["apellido"],
    #     telefono = user["telefono"]
    # )

    return render_template("index.html", **user)


@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Nueva ruta sin html"


@app.route('/ruta-nueva-1/nuevo-html')
def ruta_nueva_html():
    return render_template("nuevo.html")


if __name__ == '__main__':
    app.run(debug=True)
