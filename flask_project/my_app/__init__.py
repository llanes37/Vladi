# my_app/__init__.py
from flask import Flask
from config import Config
from my_app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        from .routes import register_routes
        register_routes(app)  # ← ESTO ES CLAVE

    return app
