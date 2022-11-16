from app.db import db


class Salon(db.Model):
    __tablename__ = "salones"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    aula = db.Column(db.String(20))
    horaEntrada = db.Column(db.Time)
    # alumnos = db.relationship('Alumno', backref='salon', lazy="dynamic")

    def __init__(self, aula, horaEntrada):
        self.aula = aula
        self.horaEntrada = horaEntrada
        # self.alumnos = alumnos
