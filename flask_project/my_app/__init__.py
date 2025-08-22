# my_app/__init__.py
from flask import Flask
from flask_login import LoginManager
from config import Config
from my_app.models import db, Usuario


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'  # nombre de la vista de login

    with app.app_context():
        db.create_all()  # Crear tablas
        from .routes import register_routes
        register_routes(app)  # Registrar rutas

    return app


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))