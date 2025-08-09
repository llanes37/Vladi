import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-dificil'
    DEBUG = True
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///juegos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False