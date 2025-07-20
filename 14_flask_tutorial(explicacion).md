
# Flask: Guía Completa para Empezar desde Cero

Flask es un **framework de desarrollo web minimalista y ligero** para Python. Es ideal tanto para principiantes que quieren aprender a crear aplicaciones web simples como para desarrolladores avanzados que necesitan un control completo y flexibilidad en sus proyectos.

---

## **¿Qué es Flask?**

Flask es un framework que permite crear aplicaciones web de manera rápida y eficiente. Fue diseñado para ser sencillo de usar, pero altamente extensible gracias a un ecosistema de extensiones.

Algunas de sus principales características son:
- **Ligero y modular**: Flask tiene una base código reducida, permitiendo mayor flexibilidad.
- **Extensible**: Puedes agregar extensiones para manejo de bases de datos, autenticación, etc.
- **Compatible con WSGI**: Integra de manera eficiente aplicaciones con servidores web.

---

## **¿Cómo instalar Flask?**

### Paso 1: Crear un entorno virtual
Es una buena práctica usar un entorno virtual para evitar conflictos entre dependencias.

1. Abre tu terminal o línea de comandos.
2. Navega al directorio donde quieras crear tu proyecto.
3. Ejecuta el siguiente comando para crear un entorno virtual:

```bash
python -m venv env
```

4. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

### Paso 2: Instalar Flask

Con el entorno virtual activado, instala Flask ejecutando:

```bash
pip install flask
```

Puedes verificar que Flask está instalado ejecutando:

```bash
pip show flask
```

---

## **¿Cómo crear tu primera aplicación Flask?**

### Estructura del proyecto
Crea una estructura simple como esta:

```
mi_proyecto/
|-- app.py
|-- env/ (entorno virtual)
```

### Paso 1: Crear el archivo principal `app.py`

Crea un archivo llamado `app.py` y agrega el siguiente código:

```python
from flask import Flask  # Importamos la clase Flask

app = Flask(__name__)  # Creamos una instancia de Flask

@app.route("/")  # Definimos una ruta para la URL principal
def inicio():
    return "¡Hola, Mundo! Esta es mi primera aplicación Flask."

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación en modo debug
```

### Paso 2: Ejecutar la aplicación

1. En tu terminal, asegúrate de estar en el directorio donde se encuentra `app.py`.
2. Ejecuta el archivo:

```bash
python app.py
```

3. Verás un mensaje indicando que la aplicación está corriendo en `http://127.0.0.1:5000/`.
4. Abre tu navegador y visita esa URL. Deberías ver el mensaje `¡Hola, Mundo! Esta es mi primera aplicación Flask.`

---

## **Conceptos clave en Flask**

### 1. Rutas
Las rutas son URL que definen las distintas páginas o puntos de acceso de tu aplicación.

Ejemplo:

```python
@app.route("/about")
def about():
    return "Esta es la página Acerca de."
```

### 2. Templates
Flask permite usar archivos HTML para estructurar tus páginas web.

1. Crea un directorio `templates/` en tu proyecto.
2. Dentro de `templates/`, crea un archivo `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Principal</title>
</head>
<body>
    <h1>Bienvenido a mi aplicación Flask</h1>
</body>
</html>
```

3. Modifica tu archivo `app.py` para usar este template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")  # Renderiza el archivo HTML
```

### 3. Manejo de datos con formularios
Puedes capturar datos de formularios HTML con Flask.

Ejemplo:

1. Crea un archivo `formulario.html` en el directorio `templates/`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
</head>
<body>
    <form action="/procesar" method="post">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre">
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

2. Modifica `app.py` para manejar el formulario:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form["nombre"]  # Captura el dato del formulario
    return f"Hola, {nombre}!"
```

---

## **Recursos adicionales**

- [Documentación oficial de Flask](https://flask.palletsprojects.com/)
- [Flask en GitHub](https://github.com/pallets/flask)

Con esto, ya tienes los conceptos básicos para empezar a usar Flask. Desde aquí, puedes explorar temas avanzados como autenticación, bases de datos o despliegue en servidores.
