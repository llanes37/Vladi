from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(10), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    plataforma = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nombre_completo = db.Column(db.String(120), nullable=True)  # Nuevo campo
    edad = db.Column(db.Integer, nullable=True)                 # Nuevo campo

class Reseña(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    calificacion = db.Column(db.Integer, nullable=False)  # 1-10
    __table_args__ = (
        db.CheckConstraint('calificacion >= 1 AND calificacion <= 10', name='check_calificacion_1_10'),
    )
    texto_reseña = db.Column(db.Text, nullable=False)
    juego_id = db.Column(db.Integer, db.ForeignKey('juego.id'), nullable=False)

    juego = db.relationship('Juego', backref=db.backref('reseñas', lazy=True))