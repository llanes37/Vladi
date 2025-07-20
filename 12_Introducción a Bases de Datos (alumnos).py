# **Introducción a Bases de Datos con Python para Alumnos**

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: Conceptos Básicos de Bases de Datos Relacionales
# -------------------------------------------------------------------------------------------
# - Una base de datos relacional almacena datos en tablas que contienen filas (registros) y columnas (campos).
# - Las bases de datos relacionales utilizan claves primarias para identificar de manera única cada fila.
# - SQL (Structured Query Language) es el lenguaje utilizado para interactuar con las bases de datos.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: Introducción a SQLite y su uso con Python
# -------------------------------------------------------------------------------------------
# - SQLite es una base de datos ligera que está integrada en Python. No requiere instalación adicional.
# - Puedes usar SQLite para crear, leer, actualizar y eliminar registros en una base de datos.
# -------------------------------------------------------------------------------------------

# TODO: Crea una conexión a una base de datos SQLite y un cursor para ejecutar sentencias SQL.
# ? Recuerda que si la base de datos no existe, SQLite la creará automáticamente.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: Operaciones CRUD (Create, Read, Update, Delete)
# -------------------------------------------------------------------------------------------
# - Create: Insertar nuevos datos en una tabla.
# - Read: Leer datos de la tabla.
# - Update: Actualizar datos existentes.
# - Delete: Eliminar registros de una tabla.
# -------------------------------------------------------------------------------------------

# TODO: Crea una tabla llamada 'alumnos' con tres columnas: id (entero, clave primaria), nombre (texto) y edad (entero).

# TODO: Inserta al menos dos registros en la tabla 'alumnos' utilizando una sentencia INSERT.

# TODO: Crea una consulta SQL para leer todos los registros de la tabla 'alumnos'.

# TODO: Crea una consulta SQL para actualizar la edad de un alumno específico en la tabla.

# TODO: Crea una consulta SQL para eliminar un alumno de la tabla 'alumnos'.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: Consultas Básicas con SELECT y WHERE
# -------------------------------------------------------------------------------------------
# - La instrucción SELECT se utiliza para consultar datos en una tabla.
# - WHERE se utiliza para filtrar los resultados de una consulta.
# -------------------------------------------------------------------------------------------

# TODO: Realiza una consulta SQL para seleccionar todos los alumnos cuya edad sea mayor a 20.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: Manejo de Excepciones en Operaciones con Bases de Datos
# -------------------------------------------------------------------------------------------
# - Al trabajar con bases de datos, pueden ocurrir errores. Para manejarlos, utilizamos try-except.
# -------------------------------------------------------------------------------------------

# TODO: Utiliza un bloque try-except para manejar posibles errores al realizar una consulta a una tabla inexistente.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: Autoevaluación Final
# -------------------------------------------------------------------------------------------
# - Crea un programa que permita a un usuario interactuar con una base de datos de alumnos:
#   1. Inserta nuevos alumnos.
#   2. Muestra una lista de todos los alumnos.
#   3. Actualiza la información de un alumno.
#   4. Elimina un alumno.
# - Usa las operaciones CRUD y asegúrate de manejar las excepciones correctamente.
# -------------------------------------------------------------------------------------------
