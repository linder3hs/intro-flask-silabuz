from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    correo = StringField("Correo", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    sobre_mi = StringField("Sobre mi", validators=[DataRequired()])
    submit = SubmitField("Crear cuenta")


class SalonesForm(FlaskForm):
    aula = StringField("Aula", validators=[DataRequired()])
    hora_entrada = StringField("Hora de Entrada", validators=[DataRequired()])
    submit = SubmitField("Enviar")


class AlumnosForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    id_aula = StringField("Id Aula", validators=[DataRequired()])
