# Introducción a Bases de Datos con Python para Profesores

## 1. Conceptos Básicos de Bases de Datos Relacionales

### Explicación Teórica
- Una base de datos relacional está formada por una o más tablas.
- Cada tabla contiene filas (registros) y columnas (campos).
- Se utiliza SQL (Lenguaje de Consulta Estructurado) para gestionar los datos.
- Cada fila es identificada de forma única por una clave primaria.

---

## 2. Introducción a SQLite y su uso en Python

### Explicación Teórica
- SQLite es una base de datos ligera integrada en Python.
- No requiere instalación adicional y es ideal para proyectos pequeños.
- Almacena la base de datos en un único archivo portátil.

### Conexión a SQLite y Creación de Tabla
```python
import sqlite3

conexion = sqlite3.connect('alumnos.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
''')

conexion.commit()
```
**Explicación:**
- `CREATE TABLE IF NOT EXISTS` evita errores si la tabla ya existe.
- `id` es la clave primaria con autoincremento.
- `nombre` y `edad` son obligatorios.

---

## 3. Operaciones CRUD (Create, Read, Update, Delete)

### Insertar Datos
```python
cursor.execute('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', ('Ana', 25))
cursor.execute('INSERT INTO alumnos (nombre, edad) VALUES (?, ?)', ('Luis', 30))
conexion.commit()
```

### Leer Datos
```python
cursor.execute('SELECT * FROM alumnos')
alumnos = cursor.fetchall()
print("Alumnos:")
for alumno in alumnos:
    print(alumno)
```

### Actualizar Datos
```python
cursor.execute('UPDATE alumnos SET edad = 26 WHERE id = 1')
conexion.commit()
```

### Borrar Datos
```python
cursor.execute('DELETE FROM alumnos WHERE id = 2')
conexion.commit()
```

**Explicación:**
- `INSERT INTO` agrega registros.
- `SELECT * FROM` recupera registros.
- `UPDATE` modifica valores existentes.
- `DELETE` elimina registros.

---

## 4. Consultas Básicas con SELECT y WHERE

### Consulta con Filtrado
```python
cursor.execute('SELECT * FROM alumnos WHERE edad > 24')
resultado = cursor.fetchall()
print("Alumnos mayores de 24 años:")
for alumno in resultado:
    print(alumno)
```

**Explicación:**
- `SELECT *` obtiene todos los datos.
- `WHERE` filtra los resultados.

---

## 5. Manejo de Excepciones en Bases de Datos

### Manejo de Errores
```python
try:
    cursor.execute('SELECT * FROM tabla_inexistente')
except sqlite3.Error as error:
    print(f"Error al ejecutar la consulta: {error}")
```

**Explicación:**
- `try-except` captura errores y evita interrupciones.

---

## 6. Ejercicio de Autoevaluación

**Tareas:**
1. Crear la base de datos `sistema_escuela.db`.
2. Crear la tabla `cursos` con `id`, `nombre_curso`, `profesor`.
3. Insertar tres registros.
4. Leer y mostrar los cursos.
5. Actualizar el nombre de un curso.
6. Eliminar un curso.
7. Mostrar los cursos restantes.

### Solución:
```python
conexion = sqlite3.connect('sistema_escuela.db')
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_curso TEXT NOT NULL,
        profesor TEXT NOT NULL
    )
''')

cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Matemáticas', 'Carlos')")
cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Historia', 'Ana')")
cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Ciencias', 'Luis')")
conexion.commit()

cursor.execute('SELECT * FROM cursos')
cursos = cursor.fetchall()
print("Cursos:")
for curso in cursos:
    print(curso)

cursor.execute("UPDATE cursos SET nombre_curso = 'Matemáticas Avanzadas' WHERE id = 1")
conexion.commit()

cursor.execute('DELETE FROM cursos WHERE id = 2')
conexion.commit()

cursor.execute('SELECT * FROM cursos')
cursos_finales = cursor.fetchall()
print("Cursos después de la eliminación:")
for curso in cursos_finales:
    print(curso)

conexion.close()
```

**Explicación:**
- Se crean y gestionan registros en la tabla `cursos`.
- Se prueba CRUD en una base de datos real.

---

## Conclusión
Este documento proporciona una guía introductoria al uso de bases de datos en Python, utilizando SQLite para gestionar datos de manera eficiente.

