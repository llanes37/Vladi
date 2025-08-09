from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class JuegoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    genero = StringField('Género', validators=[DataRequired()])
    plataforma = StringField('Plataforma', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    submit = SubmitField('Guardar')