# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: CONCEPTOS BÁSICOS DE ENTRADA/SALIDA DE ARCHIVOS (I/O) EN PYTHON
# ? La entrada/salida de archivos (I/O) nos permite leer y escribir datos en archivos.
# ? Podemos trabajar tanto con archivos de texto como con archivos binarios.
# -------------------------------------------------------------------------------------------

# * ABRIR Y LEER UN ARCHIVO
# ? Para leer un archivo en Python, usamos la función `open()` y le indicamos que queremos leerlo con el modo 'r'.
# ? Luego, usamos `read()` para leer el contenido completo del archivo.

# TODO: Escribe el código para abrir un archivo llamado 'archivo.txt', leerlo y mostrar su contenido.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: ESCRITURA EN ARCHIVOS
# ? Podemos escribir datos en un archivo usando el modo 'w' (escritura) o 'a' (añadir).
# ? El modo 'w' sobrescribe todo el contenido anterior, mientras que el modo 'a' añade al final.

# * ESCRITURA EN ARCHIVO
# ? Si abrimos un archivo con el modo 'w', cualquier contenido anterior se perderá.
# ? Si usamos el modo 'a', el contenido nuevo se añadirá al final del archivo.

# TODO: Escribe el código para crear o sobrescribir un archivo con algunas líneas de texto.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: LEER UN ARCHIVO LÍNEA POR LÍNEA
# ? Leer un archivo completo puede no ser siempre eficiente. A veces necesitamos leerlo línea por línea.
# ? Para esto, usamos `readline()` que lee una línea a la vez, o `readlines()` que lee todas las líneas y las convierte en una lista.

# * LEER LÍNEA POR LÍNEA
# ? Podemos leer un archivo línea por línea y procesar cada línea de manera individual.

# TODO: Escribe el código para abrir un archivo y leerlo línea por línea, mostrando cada línea en pantalla.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USO DE `WITH` PARA MANEJAR ARCHIVOS
# ? La declaración `with` en Python nos permite manejar archivos sin tener que preocuparnos por cerrarlos.
# ? Cuando salimos del bloque `with`, Python cierra el archivo automáticamente.

# * USAR `WITH` PARA LEER ARCHIVOS
# ? Usar `with` es la forma más recomendada de trabajar con archivos en Python, ya que evita posibles errores si olvidamos cerrar el archivo.

# TODO: Escribe el código para leer un archivo usando la declaración `with` y mostrar su contenido.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: MANEJO DE EXCEPCIONES CON ARCHIVOS
# ? A veces, el archivo que queremos abrir no existe, o puede haber errores al leer o escribir.
# ? Para evitar que el programa falle, usamos un bloque `try-except` para manejar estos errores.

# * MANEJAR ERRORES AL LEER ARCHIVOS
# ? Usamos `try-except` para capturar errores cuando trabajamos con archivos, como cuando intentamos abrir un archivo que no existe.

# TODO: Escribe el código para intentar leer un archivo inexistente y manejar el error usando `try-except`.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Crea un archivo llamado 'datos.txt' y escribe en él tu nombre, rango y unidad.
# 2. Añade una línea adicional con tu número de identificación.
# 3. Lee el archivo línea por línea y muestra cada línea en pantalla.
# 4. Implementa manejo de excepciones para asegurarte de que no haya errores si el archivo no existe.
# -------------------------------------------------------------------------------------------

# TODO: Escribe el código completo para resolver la autoevaluación final.
