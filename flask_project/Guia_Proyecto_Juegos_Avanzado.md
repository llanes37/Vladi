# Guía Avanzada para Crear un Proyecto Flask sobre Juegos

Esta guía es una continuación del proyecto básico de Flask sobre juegos. Aquí aprenderás a implementar funcionalidades avanzadas como autenticación, APIs RESTful, relaciones entre tablas, y despliegue en producción. Está diseñada para ser clara y detallada, ideal para enseñar en un entorno educativo.

---

## 1. Autenticación de Usuarios

### ¿Qué es la Autenticación?
La autenticación permite identificar a los usuarios que acceden a tu aplicación. Usaremos **Flask-Login** para manejar sesiones de usuario.

### Instalación de Flask-Login
Instala Flask-Login con el siguiente comando:
```bash
pip install flask-login
```

### Configuración Básica
1. **Crear un Modelo de Usuario**:
   En `my_app/models.py`, añade un modelo para los usuarios:
   ```python
   from flask_login import UserMixin

   class Usuario(db.Model, UserMixin):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
       password = db.Column(db.String(200), nullable=False)
   ```

2. **Configurar Flask-Login**:
   En `my_app/__init__.py`, configura Flask-Login:
   ```python
   from flask_login import LoginManager
   from my_app.models import Usuario

   login_manager = LoginManager()

   def create_app():
       app = Flask(__name__)
       app.config.from_object('config')
       db.init_app(app)
       login_manager.init_app(app)
       login_manager.login_view = 'login'
       return app

   @login_manager.user_loader
   def load_user(user_id):
       return Usuario.query.get(int(user_id))
   ```

3. **Crear Formularios de Registro e Inicio de Sesión**:
   En `my_app/forms.py`, añade formularios para el registro e inicio de sesión:
   ```python
   from flask_wtf import FlaskForm
   from wtforms import StringField, PasswordField, SubmitField
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
   ```

4. **Crear Rutas para Registro e Inicio de Sesión**:
   En `my_app/routes.py`, añade las rutas:
   ```python
   from flask import render_template, redirect, url_for, flash
   from flask_login import login_user, logout_user, login_required
   from my_app.models import db, Usuario
   from my_app.forms import RegistroForm, LoginForm
   from werkzeug.security import generate_password_hash, check_password_hash

   @app.route('/registro', methods=['GET', 'POST'])
   def registro():
       form = RegistroForm()
       if form.validate_on_submit():
           hashed_password = generate_password_hash(form.password.data, method='sha256')
           nuevo_usuario = Usuario(username=form.username.data, password=hashed_password)
           db.session.add(nuevo_usuario)
           db.session.commit()
           flash('Usuario registrado con éxito', 'success')
           return redirect(url_for('login'))
       return render_template('registro.html', form=form)

   @app.route('/login', methods=['GET', 'POST'])
   def login():
       form = LoginForm()
       if form.validate_on_submit():
           usuario = Usuario.query.filter_by(username=form.username.data).first()
           if usuario and check_password_hash(usuario.password, form.password.data):
               login_user(usuario)
               return redirect(url_for('index'))
           flash('Usuario o contraseña incorrectos', 'danger')
       return render_template('login.html', form=form)

   @app.route('/logout')
   @login_required
   def logout():
       logout_user()
       return redirect(url_for('login'))
   ```

5. **Proteger Rutas con Login**:
   Usa el decorador `@login_required` para proteger rutas:
   ```python
   @app.route('/perfil')
   @login_required
   def perfil():
       return render_template('perfil.html')
   ```

---

## 2. Crear una API RESTful

### ¿Qué es una API RESTful?
Una API RESTful permite que otras aplicaciones interactúen con tu aplicación a través de HTTP. Usaremos **Flask-RESTful** para crear una API.

### Instalación de Flask-RESTful
Instala Flask-RESTful con:
```bash
pip install flask-restful
```

### Configuración Básica
1. **Crear Recursos**:
   En `my_app/api.py`, define recursos para los juegos:
   ```python
   from flask_restful import Resource, Api
   from my_app.models import Juego

   class JuegoResource(Resource):
       def get(self):
           juegos = Juego.query.all()
           return [{'id': j.id, 'nombre': j.nombre, 'genero': j.genero, 'plataforma': j.plataforma} for j in juegos]
   ```

2. **Registrar Recursos**:
   En `my_app/__init__.py`, registra la API:
   ```python
   from flask_restful import Api
   from my_app.api import JuegoResource

   def create_app():
       app = Flask(__name__)
       api = Api(app)
       api.add_resource(JuegoResource, '/api/juegos')
       return app
   ```

---

## 3. Relaciones entre Tablas

### Crear un Modelo Relacionado
1. **Añadir Reseñas a los Juegos**:
   En `my_app/models.py`, crea un modelo para las reseñas:
   ```python
   class Reseña(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       contenido = db.Column(db.Text, nullable=False)
       juego_id = db.Column(db.Integer, db.ForeignKey('juego.id'), nullable=False)
       juego = db.relationship('Juego', backref='reseñas')
   ```

2. **Actualizar el Modelo de Juegos**:
   Añade una relación en el modelo de juegos:
   ```python
   class Juego(db.Model):
       # ... campos existentes ...
       reseñas = db.relationship('Reseña', backref='juego', lazy=True)
   ```

---

## 4. Despliegue en Producción

### ¿Por qué Desplegar?
El despliegue permite que tu aplicación esté disponible en internet para que otros puedan usarla.

### Despliegue en Heroku
1. **Instalar Heroku CLI**:
   Descarga e instala la CLI de Heroku desde [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).

2. **Crear un Archivo `Procfile`**:
   En la raíz del proyecto, crea un archivo llamado `Procfile` con el siguiente contenido:
   ```
   web: gunicorn run:app
   ```

3. **Subir el Proyecto a Heroku**:
   - Inicia sesión en Heroku:
     ```bash
     heroku login
     ```
   - Crea una nueva aplicación:
     ```bash
     heroku create nombre-de-tu-app
     ```
   - Sube el proyecto:
     ```bash
     git add .
     git commit -m "Preparar despliegue"
     git push heroku main
     ```

### Despliegue en Render
Render es una plataforma fácil de usar para desplegar aplicaciones web.

1. **Crear una Cuenta en Render**:
   - Ve a [https://render.com](https://render.com) y crea una cuenta.

2. **Configurar el Proyecto**:
   - Asegúrate de que tu proyecto esté en un repositorio de GitHub.
   - Crea un archivo `requirements.txt` si no lo tienes:
     ```
     flask
     flask-sqlalchemy
     flask-login
     flask-restful
     gunicorn
     ```
   - Crea un archivo `start.sh` en la raíz del proyecto:
     ```bash
     #!/bin/bash
     gunicorn run:app
     ```
   - Asegúrate de que el archivo `start.sh` sea ejecutable:
     ```bash
     chmod +x start.sh
     ```

3. **Desplegar en Render**:
   - Ve a tu cuenta de Render y selecciona "New + > Web Service".
   - Conecta tu repositorio de GitHub.
   - Configura los siguientes parámetros:
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `./start.sh`
   - Haz clic en "Create Web Service" y Render se encargará del despliegue.

4. **Configurar Variables de Entorno**:
   - En la configuración del servicio en Render, añade las variables de entorno necesarias, como `SECRET_KEY` o configuraciones de base de datos.

---

## 5. Próximos Pasos

- **Mejorar la Interfaz**: Usa Bootstrap o Tailwind CSS para un diseño más profesional.
- **Añadir Funcionalidades**: Implementa un sistema de favoritos o estadísticas.
- **Optimización**: Usa caché con Flask-Caching para mejorar el rendimiento.

---

¡Con esta guía avanzada, estarás listo para llevar tu proyecto Flask al siguiente nivel! 🚀
