from flask import render_template, flash, redirect, url_for
from app import create_app
from app.forms import SalonesForm
from app.db import db

from app.models.salones import Salon

app = create_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    salones_form = SalonesForm()

    if salones_form.validate_on_submit():
        salon = Salon(
            salones_form.aula.data,
            salones_form.hora_entrada.data
        )

        db.session.add(salon)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template(
        "salones.html",
        salones_form=salones_form
    )


@app.route('/salones')
def salones():
    salones = Salon.query.all()

    return render_template("lista-salones.html", salones=salones)


@app.route('/ruta-nueva-1')
def ruta_nueva():
    return "Nueva ruta sin html"


@app.route('/ruta-nueva-1/nuevo-html')
def ruta_nueva_html():
    return render_template("nuevo.html")


db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
