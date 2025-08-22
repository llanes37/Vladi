# Guía Avanzada para Crear un Proyecto Flask sobre Juegos

Esta guía continúa el proyecto básico y lo convierte en un material docente completo. Verás autenticación, relaciones en base de datos, manejo de errores, formularios seguros, buenas prácticas, pruebas y despliegue en Render. Cada bloque incluye explicación y código listo para usar en clase.

---

## 0) Preparativos (entorno y estructura)

- Python 3.10+ recomendado.
- Crea y activa un entorno virtual:
```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
```
- Instala dependencias mínimas:
```powershell
pip install Flask Flask-SQLAlchemy Flask-Login Flask-WTF
```
- Estructura sugerida:
```
proyecto_juegos/
├─ run.py
├─ config.py
├─ requirements.txt
└─ my_app/
   ├─ __init__.py
   ├─ models.py
   ├─ forms.py
   ├─ routes.py
   ├─ templates/
   └─ static/
```

Explicación rápida:
- run.py: arranque local de la app.
- config.py: variables de configuración (clave secreta, BD, etc.).
- my_app/: paquete con la lógica (app factory, modelos, rutas, formularios, vistas).

---

## 1) Autenticación de Usuarios (completa y explicada)

### ¿Qué resuelve?
- Identificar usuarios (registro/login)
- Recordar sesión (cookies seguras)
- Restringir acceso a páginas con `@login_required`

### 1.1 Configuración (config.py)
Usamos una clave secreta para sesiones/CSRF y una BD SQLite por defecto (cambia en producción):
```python
# config.py
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'cambia-esto-por-una-clave-larga-y-secreta')
# Soporte para Postgres en Render (DATABASE_URL) o SQLite local
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///juegos.db')
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql+psycopg2://', 1)

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Notas:
- SECRET_KEY debe venir de variable de entorno en producción.
- Render suele dar `DATABASE_URL` para Postgres.

### 1.2 Modelos (my_app/models.py)
```python
# my_app/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # almacenamos hash, no texto plano
    rol = db.Column(db.String(20), default='usuario')  # opcional: 'usuario' | 'admin'
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

class Juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    plataforma = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)
    propietario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))  # dueño del juego
    propietario = db.relationship('Usuario', backref='juegos')
```

Puntos clave:
- Nunca guardes contraseñas en texto plano: se usa hash seguro.
- Relacionamos Juego con Usuario para saber quién lo creó.

### 1.3 Application Factory (my_app/__init__.py)
```python
# my_app/__init__.py
from flask import Flask
from flask_login import LoginManager
from .models import db, Usuario

login_manager = LoginManager()
login_manager.login_view = 'login'  # a dónde redirigir si no hay sesión

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    login_manager.init_app(app)

    # Registro de rutas
    from .routes import register_routes
    register_routes(app)

    # Ejemplo de comando CLI para crear usuario admin rápido
    @app.cli.command('crear-admin')
    def crear_admin():
        from werkzeug.security import generate_password_hash
        if not Usuario.query.filter_by(username='admin').first():
            u = Usuario(username='admin', password=generate_password_hash('admin123'), rol='admin')
            db.session.add(u)
            db.session.commit()
            print('Admin creado: admin / admin123')
        else:
            print('Ya existe admin')

    return app
```

Qué hace:
- Crea la app (patrón factory)
- Inicializa BD y LoginManager
- Registra rutas
- Añade un comando CLI para crear un admin de ejemplo

### 1.4 Formularios (my_app/forms.py)
```python
# my_app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistroForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class JuegoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    genero = StringField('Género', validators=[DataRequired()])
    plataforma = StringField('Plataforma', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    submit = SubmitField('Guardar')
```

Notas:
- Flask-WTF añade CSRF automáticamente con `form.hidden_tag()` en la plantilla.

### 1.5 Rutas (my_app/routes.py)
Incluye registro, login, logout, perfil y CRUD de juegos básico protegido.
```python
# my_app/routes.py
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, Usuario, Juego
from .forms import RegistroForm, LoginForm, JuegoForm

# Pequeño registrador de rutas para mantener __init__ limpio

def register_routes(app):
    # Inicio
    @app.route('/')
    def index():
        juegos = Juego.query.order_by(Juego.id.desc()).all()
        return render_template('index.html', juegos=juegos)

    # Registro
    @app.route('/registro', methods=['GET', 'POST'])
    def registro():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistroForm()
        if form.validate_on_submit():
            if Usuario.query.filter_by(username=form.username.data).first():
                flash('El usuario ya existe. Elige otro nombre.', 'warning')
                return render_template('registro.html', form=form)
            hashed = generate_password_hash(form.password.data)
            nuevo = Usuario(username=form.username.data, password=hashed)
            db.session.add(nuevo)
            db.session.commit()
            flash('Usuario registrado. Inicia sesión.', 'success')
            return redirect(url_for('login'))
        return render_template('registro.html', form=form)

    # Login
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
            u = Usuario.query.filter_by(username=form.username.data).first()
            if u and check_password_hash(u.password, form.password.data):
                login_user(u, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('index'))
            flash('Usuario o contraseña incorrectos', 'danger')
        return render_template('login.html', form=form)

    # Logout
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Has cerrado sesión.', 'info')
        return redirect(url_for('login'))

    # Perfil protegido
    @app.route('/perfil')
    @login_required
    def perfil():
        return render_template('perfil.html')

    # CRUD Juegos
    @app.route('/nuevo', methods=['GET', 'POST'])
    @login_required
    def nuevo_juego():
        form = JuegoForm()
        if form.validate_on_submit():
            j = Juego(
                nombre=form.nombre.data,
                genero=form.genero.data,
                plataforma=form.plataforma.data,
                descripcion=form.descripcion.data,
                propietario=current_user
            )
            db.session.add(j)
            db.session.commit()
            flash('Juego creado', 'success')
            return redirect(url_for('index'))
        return render_template('nuevo_juego.html', form=form)

    @app.route('/editar/<int:id>', methods=['GET', 'POST'])
    @login_required
    def editar_juego(id):
        j = Juego.query.get_or_404(id)
        if j.propietario != current_user:
            flash('No puedes editar un juego que no es tuyo.', 'warning')
            return redirect(url_for('index'))
        form = JuegoForm(obj=j)
        if form.validate_on_submit():
            j.nombre = form.nombre.data
            j.genero = form.genero.data
            j.plataforma = form.plataforma.data
            j.descripcion = form.descripcion.data
            db.session.commit()
            flash('Juego actualizado', 'success')
            return redirect(url_for('index'))
        return render_template('editar_juego.html', form=form)

    @app.route('/eliminar/<int:id>', methods=['POST'])
    @login_required
    def eliminar_juego(id):
        j = Juego.query.get_or_404(id)
        if j.propietario != current_user:
            flash('No puedes eliminar un juego que no es tuyo.', 'warning')
            return redirect(url_for('index'))
        db.session.delete(j)
        db.session.commit()
        flash('Juego eliminado', 'info')
        return redirect(url_for('index'))
```

Detalles didácticos:
- `remember=True` mantiene sesión entre cierres del navegador.
- `next` permite volver a la ruta original tras login.
- Autorización básica: solo el propietario edita/borra.

### 1.6 Plantillas esenciales (my_app/templates)
- base.html: layout y mensajes flash.
```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{% block title %}Proyecto Juegos{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
<nav>
  <a href="{{ url_for('index') }}">Inicio</a>
  {% if current_user.is_authenticated %}
    <a href="{{ url_for('perfil') }}">Perfil</a>
    <a href="{{ url_for('logout') }}">Salir</a>
  {% else %}
    <a href="{{ url_for('login') }}">Entrar</a>
    <a href="{{ url_for('registro') }}">Registro</a>
  {% endif %}
</nav>
{% with messages = get_flashed_messages(with_categories=True) %}
  {% if messages %}
  <ul class="flashes">
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
{% endwith %}
<main>
  {% block content %}{% endblock %}
</main>
</body>
</html>
```

- index.html (listado):
```html
{% extends 'base.html' %}
{% block title %}Inicio{% endblock %}
{% block content %}
<h1>Mis Juegos</h1>
<p><a href="{{ url_for('nuevo_juego') }}">Añadir Juego</a></p>
<ul>
  {% for j in juegos %}
  <li>
    <strong>{{ j.nombre }}</strong> ({{ j.genero }}) - {{ j.plataforma }}
    {% if current_user.is_authenticated and j.propietario_id == current_user.id %}
      <a href="{{ url_for('editar_juego', id=j.id) }}">Editar</a>
      <form action="{{ url_for('eliminar_juego', id=j.id) }}" method="post" style="display:inline">
        <button type="submit">Eliminar</button>
      </form>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

- registro.html / login.html / perfil.html / nuevo_juego.html / editar_juego.html similares a la guía básica, incluyendo `{{ form.hidden_tag() }}` para CSRF.

---

## 2) Relaciones adicionales: Reseñas por Juego (uno-a-muchos)

Modelo y uso básico para que cada juego tenga múltiples reseñas.
```python
# my_app/models.py (añadir)
class Resena(db.Model):  # sin tilde en nombre de clase/tablas por convención
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text, nullable=False)
    juego_id = db.Column(db.Integer, db.ForeignKey('juego.id'), nullable=False)
    juego = db.relationship('Juego', backref='resenas')
```

Sugerencias:
- Crear `ResenaForm` y rutas `/juego/<id>/resenas/nueva` siguiendo el patrón de Juego.
- Mostrar `j.resenas` en la ficha del juego.

---

## 3) Manejo de errores y seguridad básica

- Páginas personalizadas:
```python
# en register_routes(app) o en un blueprint de errores
@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_servidor(e):
    return render_template('500.html'), 500
```
- CSRF: ya activo con Flask-WTF (usa `form.hidden_tag()`).
- Contraseñas: usa siempre `generate_password_hash` y `check_password_hash`.
- Autorización: verifica propietario/rol antes de modificar datos.

---

## 4) Migraciones con Flask-Migrate (opcional pero recomendado)

Permite versionar cambios en la BD sin borrar datos.
```powershell
pip install Flask-Migrate
```
```python
# my_app/__init__.py
from flask_migrate import Migrate
# dentro de create_app()
Migrate(app, db)
```
Comandos típicos:
```powershell
flask db init
flask db migrate -m "crear tablas"
flask db upgrade
```

---

## 5) Testing mínimo con pytest

Instalación y prueba rápida de ruta protegida.
```powershell
pip install pytest
```
Ejemplo de test (tests/test_auth.py):
```python
import pytest
from my_app import create_app
from my_app.models import db

def test_perfil_redirige_si_no_logado(tmp_path):
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{tmp_path}/test.db"
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
    c = app.test_client()
    r = c.get('/perfil', follow_redirects=False)
    assert r.status_code == 302  # redirige a login
```

---

## 6) Despliegue en Render (con notas de base de datos)

### 6.1 requirements.txt
Incluye todo lo usado; si usas Postgres añade `psycopg2-binary`:
```
Flask
Flask-SQLAlchemy
Flask-Login
Flask-WTF
Flask-Migrate
gunicorn
psycopg2-binary
```

### 6.2 start.sh
```bash
#!/bin/bash
gunicorn run:app
```

### 6.3 Pasos en Render
- Sube el repo a GitHub.
- En Render: New + > Web Service > conecta el repo.
- Build Command: `pip install -r requirements.txt`
- Start Command: `./start.sh`
- Variables de entorno: `SECRET_KEY` y si usas Postgres, `DATABASE_URL`.

Importante: El disco de Render es efímero. Para datos persistentes usa Postgres gestionado por Render y configura `DATABASE_URL` (ya soportado en config.py).

---

## 7) Puesta en marcha local

- Inicializa la BD:
```python
from my_app import create_app
from my_app.models import db
app = create_app()
with app.app_context():
    db.create_all()
```
- Ejecuta en desarrollo (run.py):
```python
# run.py
from my_app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 8) Próximos pasos sugeridos para clase

- Recuperación de contraseña por email (Flask-Mail).
- Paginación y búsqueda (query.paginate, filtros).
- Roles/Permisos (decoradores por rol).
- Subida de imágenes para juegos (validación de extensión/tamaño).
- Blueprints para modularizar (auth, juegos, api).

---

Con esta guía tienes un recorrido completo y explicativo para construir, asegurar, probar y desplegar tu app de juegos con Flask, listo para enseñar paso a paso.
