# **Introducción a Bases de Datos con Python para Profesores**

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: Conceptos Básicos de Bases de Datos Relacionales
# -------------------------------------------------------------------------------------------
# * Explicación Teórica:
# - Una base de datos relacional está formada por una o más tablas.
# - Cada tabla contiene filas (registros) y columnas (campos).
# - Las bases de datos relacionales utilizan SQL (Lenguaje de Consulta Estructurado) para
#   realizar consultas y gestionar datos.
# - Cada fila es identificada de forma única por una clave primaria.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: Introducción a SQLite y su uso en Python
# -------------------------------------------------------------------------------------------
# * Explicación Teórica:
# - SQLite es una base de datos ligera y fácil de usar, integrada en Python.
# - No requiere instalación adicional y es ideal para proyectos pequeños o medianos.
# - SQLite guarda toda la base de datos en un único archivo de disco, lo que lo hace portátil.
# - En esta sección, veremos cómo conectarnos a una base de datos SQLite y crear una tabla.

# **Conexión a SQLite**:
# Para conectarse a una base de datos SQLite, usamos la función `connect()` de la librería `sqlite3`.

import sqlite3  # Librería para trabajar con bases de datos SQLite

# Crear una conexión a la base de datos (se crea el archivo si no existe)
conexion = sqlite3.connect('alumnos.db')

# Crear un cursor que permitirá ejecutar sentencias SQL
cursor = conexion.cursor()

# **Creación de una Tabla**:
# A continuación, creamos una tabla llamada 'alumnos' con tres columnas: id, nombre, y edad.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
''')

# Confirmar los cambios
conexion.commit()

# Explicación:
# - La sentencia `CREATE TABLE` crea una nueva tabla en la base de datos si no existe.
# - La columna `id` es la clave primaria y se auto incrementa con cada nuevo registro.
# - Los campos `nombre` y `edad` son obligatorios (NOT NULL).
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: Operaciones CRUD (Create, Read, Update, Delete)
# -------------------------------------------------------------------------------------------
# * Explicación Teórica:
# - CRUD son las cuatro operaciones básicas para gestionar datos en una base de datos.
# - `Create`: Insertar nuevos registros en la tabla.
# - `Read`: Leer o consultar datos de la tabla.
# - `Update`: Actualizar registros existentes.
# - `Delete`: Eliminar registros de la tabla.

# **Insertar Datos**:
# Insertamos algunos registros en la tabla 'alumnos'.
cursor.execute('''
    INSERT INTO alumnos (nombre, edad) VALUES ('Ana', 25)
''')
cursor.execute('''
    INSERT INTO alumnos (nombre, edad) VALUES ('Luis', 30)
''')

# Confirmar los cambios
conexion.commit()

# **Leer Datos**:
# Leemos todos los registros de la tabla 'alumnos'.
cursor.execute('SELECT * FROM alumnos')
alumnos = cursor.fetchall()  # Obtener todos los resultados

# Mostrar los registros
print("Alumnos:")
for alumno in alumnos:
    print(alumno)

# **Actualizar Datos**:
# Actualizamos la edad del alumno con id 1.
cursor.execute('''
    UPDATE alumnos SET edad = 26 WHERE id = 1
''')

# Confirmar los cambios
conexion.commit()

# **Borrar Datos**:
# Borramos el registro del alumno con id 2.
cursor.execute('''
    DELETE FROM alumnos WHERE id = 2
''')

# Confirmar los cambios
conexion.commit()

# Explicación:
# - Usamos `INSERT INTO` para insertar nuevos registros en la tabla.
# - Usamos `SELECT * FROM` para leer todos los registros de la tabla.
# - Usamos `UPDATE` para modificar registros específicos.
# - Usamos `DELETE` para eliminar registros de la tabla.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: Consultas Básicas con SELECT y WHERE
# -------------------------------------------------------------------------------------------
# * Explicación Teórica:
# - `SELECT` es la sentencia SQL que se usa para leer datos de una tabla.
# - `WHERE` es una cláusula que permite filtrar los resultados según una condición.

# **Consulta con Filtrado**:
# Leer los registros donde la edad sea mayor a 24.
cursor.execute('SELECT * FROM alumnos WHERE edad > 24')
resultado = cursor.fetchall()

# Mostrar los registros filtrados
print("Alumnos mayores de 24 años:")
for alumno in resultado:
    print(alumno)

# Explicación:
# - `SELECT *` selecciona todas las columnas de la tabla.
# - `WHERE` especifica que solo queremos los registros donde la edad es mayor a 24.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: Manejo de Excepciones en Bases de Datos
# -------------------------------------------------------------------------------------------
# * Explicación Teórica:
# - Al trabajar con bases de datos, pueden ocurrir errores por muchas razones (fallo de conexión, tabla inexistente, etc.).
# - En Python, podemos manejar estos errores usando la estructura `try-except`.

# **Manejo de Errores**:
# Intentamos ejecutar una consulta en una tabla inexistente para simular un error.
try:
    cursor.execute('SELECT * FROM tabla_inexistente')
except sqlite3.Error as error:
    print(f"Error al ejecutar la consulta: {error}")

# Explicación:
# - El bloque `try` intenta ejecutar el código dentro de él.
# - Si ocurre un error, el bloque `except` captura el error y lo muestra.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: Ejercicio de Autoevaluación
# -------------------------------------------------------------------------------------------
# * Explicación del Ejercicio:
# - En esta sección, los alumnos pondrán en práctica lo aprendido.
# - Crearán su propia base de datos, insertarán datos, los leerán, actualizarán y eliminarán registros.
# -------------------------------------------------------------------------------------------

# **Ejercicio de Autoevaluación**:
# 1. Crear una base de datos llamada `sistema_escuela.db`.
# 2. Crear una tabla llamada `cursos` con tres columnas: id, nombre del curso, y profesor.
# 3. Insertar tres cursos diferentes.
# 4. Leer y mostrar todos los cursos.
# 5. Actualizar el nombre de un curso.
# 6. Eliminar un curso.
# 7. Mostrar los cursos restantes después de la eliminación.

# **Solución del Ejercicio**:

# Crear la base de datos `sistema_escuela.db`
conexion = sqlite3.connect('sistema_escuela.db')
cursor = conexion.cursor()

# Crear la tabla 'cursos'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_curso TEXT NOT NULL,
        profesor TEXT NOT NULL
    )
''')

# Insertar cursos
cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Matemáticas', 'Carlos')")
cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Historia', 'Ana')")
cursor.execute("INSERT INTO cursos (nombre_curso, profesor) VALUES ('Ciencias', 'Luis')")
conexion.commit()

# Leer y mostrar los cursos
cursor.execute('SELECT * FROM cursos')
cursos = cursor.fetchall()

print("Cursos:")
for curso in cursos:
    print(curso)

# Actualizar el nombre de un curso
cursor.execute("UPDATE cursos SET nombre_curso = 'Matemáticas Avanzadas' WHERE id = 1")
conexion.commit()

# Leer y mostrar los cursos actualizados
cursor.execute('SELECT * FROM cursos')
cursos_actualizados = cursor.fetchall()

print("Cursos actualizados:")
for curso in cursos_actualizados:
    print(curso)

# Borrar un curso
cursor.execute("DELETE FROM cursos WHERE id = 2")
conexion.commit()

# Leer y mostrar los cursos después de la eliminación
cursor.execute('SELECT * FROM cursos')
cursos_finales = cursor.fetchall()

print("Cursos después de la eliminación:")
for curso in cursos_finales:
    print(curso)

# Cerrar la conexión a la base de datos
conexion.close()

# Explicación del Ejercicio:
# - Los alumnos seguirán el mismo proceso que se ha mostrado en las secciones anteriores:
#   crear una tabla, insertar datos, leer registros, actualizar registros, y eliminarlos.
# - El objetivo es que los alumnos se familiaricen con las operaciones básicas de CRUD en bases de datos.
