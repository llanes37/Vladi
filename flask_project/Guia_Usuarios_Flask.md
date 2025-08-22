# 🧭 Guía Avanzada — Sistema de Usuarios en Flask

Este documento explica de forma **clara, completa y paso a paso** cómo crear un sistema de **usuarios** en Flask:  
registro, inicio/cierre de sesión y perfil de usuario. Está diseñado para ser **copiable y pegable** en un proyecto real.

---

## 1. Instalación de dependencias

Ejecuta en tu terminal:

```bash
pip install flask flask-sqlalchemy flask-wtf flask-login email-validator werkzeug
```

---

## 2. Estructura del proyecto

Se recomienda organizar el proyecto así:

```
flask_project/
├─ run.py
├─ config.py
└─ my_app/
   ├─ __init__.py
   ├─ models.py
   ├─ forms.py
   ├─ routes.py
   ├─ auth/
   │  ├─ __init__.py
   │  └─ routes.py
   ├─ templates/
   │  ├─ base.html
   │  ├─ index.html
   │  ├─ auth/
   │  │  ├─ login.html
   │  │  └─ registro.html
   │  └─ usuario/
   │     └─ perfil.html
   └─ static/
```

---

## 3. Configuración base

### `config.py`
```python
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Redirección por defecto de Flask-Login
LOGIN_VIEW = "auth.login"
```

### `my_app/__init__.py`
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = app.config["LOGIN_VIEW"]

    # Registrar blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    # Crear tablas en desarrollo
    with app.app_context():
        from . import models
        db.create_all()

    return app
```

### `run.py`
```python
from my_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 4. Modelo de Usuario

### `my_app/models.py`
```python
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, login_manager

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    nombre = db.Column(db.String(120))
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Helpers de contraseña
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Usuario {self.username}>"

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
```

---

## 5. Formularios

### `my_app/forms.py`
```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class RegistroForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=40)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirmar", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Crear cuenta")

class LoginForm(FlaskForm):
    username = StringField("Usuario o Email", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember = BooleanField("Recordarme")
    submit = SubmitField("Entrar")

class PerfilForm(FlaskForm):
    nombre = StringField("Nombre", validators=[Optional(), Length(max=120)])
    bio = TextAreaField("Bio", validators=[Optional(), Length(max=500)])
    submit = SubmitField("Guardar cambios")
```

---

## 6. Rutas de Autenticación

### `my_app/auth/__init__.py`
```python
from flask import Blueprint
auth_bp = Blueprint("auth", __name__, template_folder="../templates")
```

### `my_app/auth/routes.py`
```python
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from ..forms import RegistroForm, LoginForm
from ..models import Usuario
from .. import db
from . import auth_bp

# Registro
@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegistroForm()
    if form.validate_on_submit():
        # Verificar si existe
        if Usuario.query.filter((Usuario.username == form.username.data) | (Usuario.email == form.email.data)).first():
            flash("El usuario o email ya existe.", "danger")
            return render_template("auth/registro.html", form=form)

        user = Usuario(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Cuenta creada. Ya puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))
    return render_template("auth/registro.html", form=form)

# Login
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        q = form.username.data.strip()
        user = Usuario.query.filter((Usuario.username == q) | (Usuario.email == q)).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Bienvenido 👋", "success")
            next_url = request.args.get("next")
            return redirect(next_url or url_for("main.index"))
        flash("Credenciales inválidas.", "danger")
    return render_template("auth/login.html", form=form)

# Logout
@auth_bp.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Sesión cerrada.", "info")
    return redirect(url_for("auth.login"))
```

---

## 7. Rutas principales (perfil)

### `my_app/routes.py`
```python
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import PerfilForm
from . import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/perfil", methods=["GET", "POST"])
@login_required
def perfil():
    form = PerfilForm(obj=current_user)
    if form.validate_on_submit():
        current_user.nombre = form.nombre.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash("Perfil actualizado.", "success")
        return redirect(url_for("main.perfil"))
    return render_template("usuario/perfil.html", form=form)
```

---

## 8. Plantillas mínimas

### `templates/base.html`
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Proyecto Flask</title>
</head>
<body>
    <nav>
        <a href="{{ url_for('main.index') }}">Inicio</a>
        {% if current_user.is_authenticated %}
            <a href="{{ url_for('main.perfil') }}">Perfil</a>
            <a href="{{ url_for('auth.logout') }}">Cerrar sesión</a>
        {% else %}
            <a href="{{ url_for('auth.login') }}">Login</a>
            <a href="{{ url_for('auth.registro') }}">Registro</a>
        {% endif %}
    </nav>
    <hr>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul>
        {% for category, message in messages %}
          <li><strong>{{ category }}:</strong> {{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    {% block content %}{% endblock %}
</body>
</html>
```

### `templates/index.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>Bienvenido al Proyecto Flask</h2>
<p>Esta es la página principal.</p>
{% endblock %}
```

### `templates/auth/login.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>Iniciar Sesión</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username }}<br>
  {{ form.password.label }} {{ form.password }}<br>
  {{ form.remember }} Recordarme<br>
  {{ form.submit }}
</form>
{% endblock %}
```

### `templates/auth/registro.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>Registro</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username }}<br>
  {{ form.email.label }} {{ form.email }}<br>
  {{ form.password.label }} {{ form.password }}<br>
  {{ form.confirm_password.label }} {{ form.confirm_password }}<br>
  {{ form.submit }}
</form>
{% endblock %}
```

### `templates/usuario/perfil.html`
```html
{% extends "base.html" %}
{% block content %}
<h2>Mi Perfil</h2>
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.nombre.label }} {{ form.nombre }}<br>
  {{ form.bio.label }} {{ form.bio }}<br>
  {{ form.submit }}
</form>
{% endblock %}
```

---

## ✅ Conclusión

Con este módulo tienes un sistema de usuarios **completo** en Flask:

- Registro ✔  
- Login / Logout ✔  
- Perfil editable ✔  
- Protección de rutas con `@login_required` ✔  

El siguiente paso puede ser añadir recuperación de contraseña o roles de usuario.
