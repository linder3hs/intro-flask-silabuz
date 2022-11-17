from app.db import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    password = db.Column(db.String(300))
    sobre_mi = db.Column(db.String(100))
    miembro_desde = db.Column(db.DateTime(), default=func.now())

    def __init__(self, nombre, apellido, correo, password, sobre_mi):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.sobre_mi = sobre_mi
