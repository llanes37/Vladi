# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: CONCEPTOS BÁSICOS DE ENTRADA/SALIDA DE ARCHIVOS (I/O) EN PYTHON
# ? La entrada/salida de archivos (I/O) se refiere a la lectura y escritura de datos en archivos.
# ? Python proporciona funciones sencillas para trabajar con archivos de texto y binarios.
# -------------------------------------------------------------------------------------------

# * ¿Cómo abrir un archivo?
# ? Para abrir un archivo, usamos la función `open()`, que acepta dos parámetros principales: 
# ? - El nombre del archivo.
# ? - El modo en que queremos abrirlo: 'r' (lectura), 'w' (escritura), 'a' (añadir), 'b' (binario), entre otros.

# * Ejemplo 1: Abrir un archivo para lectura
# ? Aquí abrimos un archivo llamado 'archivo.txt' en modo lectura ('r').
archivo = open('archivo.txt', 'r')  # Abre el archivo para leerlo
contenido = archivo.read()  # Lee todo el contenido del archivo
print(contenido)  # Muestra el contenido del archivo en la consola
archivo.close()  # Es importante cerrar el archivo después de trabajar con él.

# Explicación:
# - `open()` abre el archivo. Si el archivo no existe, arroja un error.
# - `read()` lee el contenido completo del archivo.
# - Siempre cerramos el archivo después de usarlo con `close()` para liberar recursos.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: ESCRITURA EN ARCHIVOS
# ? Para escribir datos en un archivo, usamos el modo de apertura 'w' o 'a'.
# ? 'w' sobrescribe el archivo si ya existe; 'a' añade contenido al final del archivo sin borrarlo.
# -------------------------------------------------------------------------------------------

# * Ejemplo 2: Abrir un archivo para escribir
# ? Aquí creamos o sobrescribimos un archivo con el texto "Hola, este es un archivo de prueba."
archivo = open('archivo.txt', 'w')  # Abrir para escribir
archivo.write("Hola, este es un archivo de prueba.\n")  # Escribir texto en el archivo
archivo.write("Esta es una segunda línea.\n")  # Escribir otra línea
archivo.close()  # Cerrar el archivo

# Explicación:
# - Usamos `write()` para escribir en el archivo. Si el archivo no existe, Python lo crea.
# - Al abrir con 'w', cualquier contenido anterior se sobrescribe.

# * Ejemplo 3: Abrir un archivo para añadir datos
# ? Aquí añadimos más texto al archivo sin borrar el contenido existente.
archivo = open('archivo.txt', 'a')  # Abrir en modo añadir
archivo.write("Esta es una nueva línea añadida.\n")  # Añadir al final del archivo
archivo.close()  # Cerrar el archivo

# Explicación:
# - Al usar el modo 'a', el contenido nuevo se añade al final sin eliminar lo existente.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: LECTURA Y ESCRITURA DE LÍNEAS
# ? Python proporciona métodos para leer archivos línea por línea, lo que es útil para procesar grandes archivos.
# ? Métodos comunes: `readline()` y `readlines()`.
# -------------------------------------------------------------------------------------------

# * Ejemplo 4: Leer un archivo línea por línea
# ? Aquí usamos `readline()` para leer el archivo línea a línea.
archivo = open('archivo.txt', 'r')  # Abrir para leer
linea = archivo.readline()  # Leer la primera línea
while linea:
    print(linea.strip())  # Mostrar la línea sin los saltos de línea extra
    linea = archivo.readline()  # Leer la siguiente línea
archivo.close()  # Cerrar el archivo

# Explicación:
# - `readline()` lee una línea a la vez, ideal para manejar grandes archivos.
# - El ciclo while continúa leyendo hasta que `readline()` devuelve una cadena vacía (final del archivo).

# * Ejemplo 5: Leer todas las líneas de una vez con `readlines()`
archivo = open('archivo.txt', 'r')  # Abrir para leer
lineas = archivo.readlines()  # Leer todas las líneas en una lista
archivo.close()  # Cerrar el archivo
for linea in lineas:
    print(linea.strip())  # Mostrar cada línea

# Explicación:
# - `readlines()` lee todas las líneas y las devuelve como una lista.
# - Luego iteramos sobre esa lista para mostrar cada línea en la consola.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USANDO LA DECLARACIÓN "WITH"
# ? La declaración `with` asegura que el archivo se cierre automáticamente después de ser usado.
# -------------------------------------------------------------------------------------------

# * Ejemplo 6: Usar la declaración `with` para manejar archivos
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# Explicación:
# - Al usar `with`, no es necesario llamar a `close()`. Python cierra el archivo automáticamente cuando sale del bloque.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: MANEJO DE EXCEPCIONES CON ARCHIVOS
# ? Es importante manejar excepciones para evitar errores si el archivo no existe o si ocurre algún problema al leer o escribir.
# -------------------------------------------------------------------------------------------

# * Ejemplo 7: Manejar errores al abrir un archivo que no existe
try:
    archivo = open('archivo_inexistente.txt', 'r')
except FileNotFoundError:
    print("Error: El archivo no existe.")
else:
    contenido = archivo.read()
    print(contenido)
    archivo.close()

# Explicación:
# - Usamos un bloque `try-except` para capturar el error si el archivo no existe.
# - La cláusula `else` se ejecuta solo si no ocurre ninguna excepción.

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Crea un archivo llamado 'datos.txt' y escribe tu nombre y tu rango en el archivo.
# 2. Añade dos líneas más con tu número de identificación y el nombre de tu unidad.
# 3. Lee el archivo línea por línea y muestra cada línea en la consola.
# 4. Implementa un manejo de excepciones para asegurarte de que no haya errores si el archivo no existe.
# -------------------------------------------------------------------------------------------

# CÓDIGO RESUELTO:
# 1. Crear el archivo y escribir en él.
with open('datos.txt', 'w') as archivo:
    archivo.write("Nombre: Juan Pérez\n")
    archivo.write("Rango: Sargento\n")
    archivo.write("ID: 123456\n")
    archivo.write("Unidad: Infantería\n")

# 2. Leer el archivo línea por línea.
try:
    with open('datos.txt', 'r') as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")

# -------------------------------------------------------------------------------------------
# Este archivo está diseñado para enseñar a los profesores cómo trabajar con la entrada y salida de archivos en Python.
# Contiene ejemplos de lectura, escritura, manejo de excepciones y el uso adecuado de recursos con `with`.
