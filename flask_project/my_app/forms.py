from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, DataRequired, Length, EqualTo, Optional, NumberRange

class JuegoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=3, max=20)])
    genero = StringField('Género', validators=[DataRequired()])
    plataforma = StringField('Plataforma', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Guardar')

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class EditarPerfilForm(FlaskForm):
    nombre_completo = StringField('Nombre completo', validators=[Optional(), Length(max=120)])
    edad = IntegerField('Edad', validators=[Optional(), NumberRange(min=1, max=120)])
    submit = SubmitField('Guardar cambios')

class ReseñaForm(FlaskForm):
    calificacion = IntegerField('Calificación', validators=[DataRequired(), NumberRange(min=1, max=10)])
    texto_reseña = TextAreaField('Reseña', validators=[DataRequired(), Length(min=3, max=500)])
    submit = SubmitField('Añadir reseña')