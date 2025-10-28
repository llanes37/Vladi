from my_app.models import db, Usuario
from flask import Flask
from my_app.routes import register_routes

app = Flask(__name__)
app.config.from_object('config.Config')  # Corrijo para cargar la clase Config
register_routes(app)
db.init_app(app)

with app.app_context():
    db.create_all()  # Asegura que las tablas existan
    usuarios = Usuario.query.filter(Usuario.edad >= 18).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Usuario: {usuario.username}, Nombre: {usuario.nombre_completo}, Edad: {usuario.edad}")
