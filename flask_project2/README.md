# Estructura del Proyecto Flask

Este documento explica la función de cada archivo y directorio en este proyecto Flask. La estructura está diseñada para ser escalable y mantener el código organizado.

## Estructura de Archivos

```
flask_project/
├── run.py              # Punto de entrada para ejecutar la aplicación.
├── config.py           # Configuraciones de la aplicación.
├── requirements.txt    # Lista de dependencias de Python.
├── README.md           # Este archivo de explicación.
├── my_app/             # El paquete principal de la aplicación.
│   ├── __init__.py     # Inicializa la aplicación (Application Factory).
│   ├── routes.py       # Define las rutas/vistas de la aplicación.
│   ├── static/         # Archivos estáticos (CSS, JavaScript, imágenes).
│   │   └── css/
│   │       └── style.css
│   └── templates/      # Plantillas HTML.
│       └── index.html
└── venv/               # (Opcional) El entorno virtual.
```

---

## Descripción de Componentes

### Archivos en la Raíz

-   **`run.py`**
    -   **Propósito:** Es el script principal que se ejecuta para iniciar la aplicación.
    -   **Funcionamiento:** Importa la función `create_app` desde el paquete `my_app` y la utiliza para crear una instancia de la aplicación. Luego, inicia el servidor de desarrollo de Flask. Para ejecutar la aplicación, usarías el comando `python run.py`.

-   **`config.py`**
    -   **Propósito:** Almacena todas las configuraciones de la aplicación de forma centralizada.
    -   **Ejemplos:** Claves secretas (`SECRET_KEY`), configuraciones de la base de datos, y otras variables de entorno. Separar la configuración del código principal mejora la seguridad y la portabilidad.

-   **`requirements.txt`**
    -   **Propósito:** Lista todas las librerías de Python de las que depende el proyecto (como `Flask`).
    -   **Uso:** Permite a otros desarrolladores (o a ti mismo en otro entorno) instalar fácilmente todas las dependencias necesarias con un solo comando: `pip install -r requirements.txt`.

### El Paquete `my_app`

Este directorio contiene el núcleo de tu aplicación. Al incluir un archivo `__init__.py`, Python lo trata como un "paquete".

-   **`my_app/__init__.py`**
    -   **Propósito:** Contiene la "Application Factory" (fábrica de aplicaciones).
    -   **Funcionamiento:** La función `create_app()` se encarga de inicializar y configurar la aplicación Flask. Carga la configuración desde `config.py` y registra las rutas. Este patrón es muy útil para crear múltiples instancias de la aplicación (por ejemplo, para testing) y para evitar problemas de importación circular.

-   **`my_app/routes.py`**
    -   **Propósito:** Define las URLs de la aplicación y las funciones que se ejecutan cuando un usuario visita esas URLs.
    -   **Ejemplo:** `@current_app.route('/')` asocia la URL raíz con una función que renderiza la página de inicio. A medida que la aplicación crece, puedes tener múltiples archivos de rutas para diferentes secciones (usuarios, productos, etc.).

-   **`my_app/static/`**
    -   **Propósito:** Almacena archivos que no cambian, como hojas de estilo CSS, archivos de JavaScript, imágenes, fuentes, etc.
    -   **Acceso desde plantillas:** En el HTML, puedes acceder a estos archivos usando `url_for('static', filename='path/to/file')`. Por ejemplo: `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`.

-   **`my_app/templates/`**
    -   **Propósito:** Contiene las plantillas HTML que tu aplicación mostrará a los usuarios.
    -   **Funcionamiento:** Flask utiliza el motor de plantillas Jinja2, que te permite incrustar lógica de Python (como variables, bucles y condicionales) directamente en tu HTML. Las rutas en `routes.py` renderizan estas plantillas usando la función `render_template()`.
