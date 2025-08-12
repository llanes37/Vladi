# Guía Completa para Crear un Proyecto Flask sobre Juegos

Esta guía está diseñada para enseñar paso a paso cómo construir una aplicación web usando Flask. El objetivo es crear un proyecto donde puedas gestionar información sobre tus juegos favoritos. Aprenderás a usar bases de datos, formularios y a crear un CRUD (Crear, Leer, Actualizar, Eliminar). Esta guía está pensada para ser clara y educativa, ideal para enseñar a alguien que está aprendiendo.

---

## 1. ¿Qué es Flask?
Flask es un framework de Python que te permite crear aplicaciones web de manera sencilla. Es muy flexible y fácil de aprender, lo que lo hace perfecto para proyectos educativos.

---

## 2. Configuración Inicial

### Estructura del Proyecto
Tu proyecto tendrá la siguiente estructura básica:

```
flask_project/
├── run.py              # Punto de entrada para ejecutar la aplicación.
├── config.py           # Configuraciones de la aplicación.
├── requirements.txt    # Lista de dependencias de Python.
├── my_app/             # El paquete principal de la aplicación.
│   ├── __init__.py     # Inicializa la aplicación (Application Factory).
│   ├── routes.py       # Define las rutas/vistas de la aplicación.
│   ├── models.py       # Define los modelos de la base de datos.
│   ├── forms.py        # Define los formularios de la aplicación.
│   ├── static/         # Archivos estáticos (CSS, JavaScript, imágenes).
│   └── templates/      # Plantillas HTML.
```

### Instalación de Dependencias
Antes de empezar, asegúrate de tener Python instalado. Luego, instala Flask y otras dependencias necesarias. Si tienes un archivo `requirements.txt`, puedes instalar todo con:
```bash
pip install -r requirements.txt
```
Si no tienes el archivo, instala Flask manualmente:
```bash
pip install flask
```

---

## 3. Añadir una Base de Datos

### ¿Qué es una Base de Datos?
Una base de datos es un lugar donde puedes guardar información de manera organizada. En este proyecto, usaremos SQLite, que es una base de datos ligera y fácil de usar.

### Instalar Flask-SQLAlchemy
SQLAlchemy es una herramienta que te permite trabajar con bases de datos de manera sencilla. Instálalo con:
```bash
pip install flask-sqlalchemy
```

### Configurar la Base de Datos
En el archivo `config.py`, añade la configuración para usar SQLite:
```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///juegos.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### Crear el Modelo de Datos
Un modelo es una representación de cómo se verá tu información en la base de datos. En `my_app/models.py`, define un modelo para los juegos:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    plataforma = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
```

### Inicializar la Base de Datos
En `my_app/__init__.py`, inicializa SQLAlchemy:
```python
from flask import Flask
from my_app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    return app
```

Para crear la base de datos, ejecuta este script:
```python
from my_app import create_app
from my_app.models import db

app = create_app()
with app.app_context():
    db.create_all()
```
Este script crea un archivo llamado `juegos.db` donde se guardará toda la información.

---

## 4. Crear un CRUD para Juegos

### ¿Qué es un CRUD?
CRUD significa Crear, Leer, Actualizar y Eliminar. Es un conjunto de operaciones básicas que puedes realizar en una base de datos.

### Crear Formularios
Los formularios permiten a los usuarios ingresar información. En `my_app/forms.py`, define un formulario para los juegos:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class JuegoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    genero = StringField('Género', validators=[DataRequired()])
    plataforma = StringField('Plataforma', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    submit = SubmitField('Guardar')
```

### Crear Rutas
Las rutas son las direcciones que los usuarios visitan en tu aplicación. En `my_app/routes.py`, añade las rutas para el CRUD:
```python
from flask import render_template, redirect, url_for, request
from my_app.models import db, Juego
from my_app.forms import JuegoForm

@app.route('/')
def index():
    juegos = Juego.query.all()
    return render_template('index.html', juegos=juegos)

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo_juego():
    form = JuegoForm()
    if form.validate_on_submit():
        juego = Juego(
            nombre=form.nombre.data,
            genero=form.genero.data,
            plataforma=form.plataforma.data,
            descripcion=form.descripcion.data
        )
        db.session.add(juego)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('nuevo_juego.html', form=form)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_juego(id):
    juego = Juego.query.get_or_404(id)
    form = JuegoForm(obj=juego)
    if form.validate_on_submit():
        juego.nombre = form.nombre.data
        juego.genero = form.genero.data
        juego.plataforma = form.plataforma.data
        juego.descripcion = form.descripcion.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_juego.html', form=form)

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_juego(id):
    juego = Juego.query.get_or_404(id)
    db.session.delete(juego)
    db.session.commit()
    return redirect(url_for('index'))
```

### Crear Plantillas
Las plantillas son los archivos HTML que se muestran a los usuarios. Crea las plantillas en `my_app/templates/`:

- **`index.html`**:
```html
<h1>Mis Juegos</h1>
<a href="{{ url_for('nuevo_juego') }}">Añadir Juego</a>
<ul>
    {% for juego in juegos %}
    <li>
        <strong>{{ juego.nombre }}</strong> ({{ juego.genero }}) - {{ juego.plataforma }}
        <a href="{{ url_for('editar_juego', id=juego.id) }}">Editar</a>
        <form action="{{ url_for('eliminar_juego', id=juego.id) }}" method="post" style="display:inline;">
            <button type="submit">Eliminar</button>
        </form>
    </li>
    {% endfor %}
</ul>
```

- **`nuevo_juego.html`** y **`editar_juego.html`**:
```html
<h1>{% if form.nombre.data %}Editar{% else %}Nuevo{% endif %} Juego</h1>
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.nombre.label }} {{ form.nombre }}<br>
    {{ form.genero.label }} {{ form.genero }}<br>
    {{ form.plataforma.label }} {{ form.plataforma }}<br>
    {{ form.descripcion.label }} {{ form.descripcion }}<br>
    {{ form.submit }}
</form>
```

---

## 5. Próximos Pasos

- **Mejorar la Interfaz**: Usa Bootstrap para hacer que la aplicación se vea más profesional.
- **Autenticación**: Añade un sistema de usuarios con Flask-Login.
- **Despliegue**: Sube tu aplicación a un servidor como Heroku o PythonAnywhere.

---

¡Diviértete creando tu proyecto de juegos y aprendiendo Flask! 🚀
