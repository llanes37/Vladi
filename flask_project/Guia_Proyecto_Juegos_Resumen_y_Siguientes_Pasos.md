# Proyecto Juegos (Flask) — Resumen y Siguientes Pasos

Este documento resume lo que ya implementaste en el proyecto y marca un camino claro (paso a paso) para continuar y usarlo en clase.

---

## 1) Qué tenemos hecho

Tecnologías principales: Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Jinja2.

Estructura real (carpeta `flask_project/`):
- `run.py`: arranque local de la app.
- `requirements.txt`: dependencias.
- `config.py`: configuración (SECRET_KEY, conexión a BD).
- `instance/juegos.db`: base de datos SQLite creada en runtime.
- `my_app/`
  - `__init__.py`: Application Factory; inicializa BD y login, registra rutas.
  - `models.py`: modelos SQLAlchemy (Usuario, Juego; relación propietario ↔ juegos).
  - `forms.py`: formularios (RegistroForm, LoginForm, JuegoForm) con validación y CSRF.
  - `routes.py`: vistas (registro, login, logout, índice, creación de juegos, etc.).
  - `templates/`: HTML con Jinja (index, login, registro, nuevo_juego, about …).
  - `static/css/style.css`: estilos básicos.

Funcionalidad:
- Autenticación: registro (hash de contraseña), login/logout, ruta protegida (perfil si la añades).
- Juegos: listado y creación mediante formulario (edición/eliminación se añaden en los siguientes pasos si faltan).
- Seguridad: CSRF en formularios, `@login_required` en rutas sensibles.

---

## 2) Cómo ejecutar en local (Windows PowerShell)

```powershell
# 1) Activar entorno (si lo usas)
# python -m venv venv
# .\venv\Scripts\Activate.ps1

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Ejecutar la app
python run.py
```

Abre en el navegador: http://127.0.0.1:5000

Tip: si cambias modelos, recrea tablas rápidamente:
```python
from my_app import create_app
from my_app.models import db
app = create_app()
with app.app_context():
    db.create_all()
```

---

## 3) Plan de clase (ruta de aprendizaje)

Sesión 1 — Arquitectura Flask
- App factory, paquetes, templates, static, config.

Sesión 2 — Modelos y BD
- SQLAlchemy, crear tablas, relaciones Usuario↔Juego.

Sesión 3 — Formularios y validación
- Flask-WTF, CSRF, validadores, mensajes flash.

Sesión 4 — Autenticación
- Registro, login, logout, protección de rutas, autorización básica.

Sesión 5 — CRUD de juegos completo
- Crear, listar, editar y eliminar, con control de propietario.

Sesión 6 — Plantillas y estilo
- Layout base, bloques, componentes, Bootstrap opcional.

Sesión 7 — Errores y logging
- Páginas 404/500, buenas prácticas de manejo de errores.

Sesión 8 — Migraciones
- Flask-Migrate, `flask db migrate/upgrade`.

Sesión 9 — Testing
- pytest: pruebas de rutas públicas y protegidas.

Sesión 10 — Despliegue en Render
- Variables de entorno, Postgres gestionado, `start.sh` y `requirements.txt`.

---

## 4) Siguientes pasos concretos (checklist)

- [ ] Añadir plantilla `perfil.html` y ruta protegida `/perfil` si no está.
- [ ] Completar CRUD: crear `editar_juego.html` y acción de eliminar por POST.
- [ ] Añadir búsqueda y paginación en el listado de juegos.
- [ ] Reseñas por juego (modelo `Reseña/Resena`, formulario y rutas anidadas).
- [ ] Subida de imagen de portada del juego (validación de extensión/tamaño).
- [ ] Roles: `admin` vs `usuario` (permisos y panel simple de administración).
- [ ] Migraciones con Flask-Migrate para cambios de modelos sin perder datos.
- [ ] Tests con pytest (auth, permisos, formularios, flujos felices y de error).
- [ ] Despliegue en Render con Postgres (`DATABASE_URL`), `SECRET_KEY` y `start.sh`.

---

## 5) Despliegue (resumen Render)

- Asegúrate de tener en `requirements.txt`: Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Migrate, gunicorn, (y si usas Postgres) `psycopg2-binary`.
- Crea `start.sh` (Unix) con: `gunicorn run:app`.
- Sube a GitHub. En Render: New → Web Service → conecta el repo.
- Build: `pip install -r requirements.txt`
- Start: `./start.sh`
- Variables de entorno: `SECRET_KEY` y `DATABASE_URL` (Render Postgres).
- Nota: disco efímero; usa Postgres para persistencia.

---

## 6) Problemas comunes y soluciones

- CSRF Token Missing: asegurarse de incluir `{{ form.hidden_tag() }}` en los formularios.
- 405 Method Not Allowed: revisar `method="POST"` y la ruta acepte `methods=['POST']`.
- DB "locked" en Windows: cerrar procesos abiertos o usar `with app.app_context():` y `commit()` correctamente.
- Contraseña no valida: recuerda usar `generate_password_hash` / `check_password_hash`.
- SECRET_KEY faltante en producción: definirla como variable de entorno.

---

## 7) Anexo: estructura actual (resumen)

```
flask_project/
├─ run.py
├─ config.py
├─ requirements.txt
├─ instance/
│  └─ juegos.db
├─ my_app/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ forms.py
│  ├─ routes.py
│  ├─ static/
│  │  └─ css/style.css
│  └─ templates/
│     ├─ index.html
│     ├─ login.html
│     ├─ registro.html
│     ├─ nuevo_juego.html
│     └─ about.html
└─ (varias guías .md con teoría y prácticas)
```

---

¿Necesitas que genere los archivos que faltan (por ejemplo `perfil.html`, `editar_juego.html` y la ruta de eliminar) y los deje listos para usar? Puedo hacerlo ya.
