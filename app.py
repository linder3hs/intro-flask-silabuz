from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Linder Hassinger"
    return render_template("index.html", nombre=nombre)


@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Nueva ruta sin html"


if __name__ == '__main__':
    app.run(debug=True)
