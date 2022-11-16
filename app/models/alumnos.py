from app.db import db


class Alumno(db.Model):
    __tablename__ = "alumnos"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(100))
    idAula = db.Column(db.Integer, db.ForeignKey(
        'salones.id'), primary_key=True)

    def __init__(self, nombre, apellido, email, idAula):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.idAula = idAula
