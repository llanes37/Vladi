# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN A MÓDULOS Y LIBRERÍAS EN PYTHON
# ? En Python, un módulo es un archivo que contiene código (funciones, variables, clases, etc.)
# ? Las librerías son colecciones de módulos que podemos utilizar para ahorrar tiempo y reutilizar código.
# ? Python viene con muchos módulos ya instalados, que podemos usar sin tener que escribir todo desde cero.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: USO DEL MÓDULO 'MATH'
# ? El módulo `math` incluye funciones matemáticas que nos permiten hacer cálculos como raíces cuadradas,
# ? potencias, y funciones trigonométricas como el seno y el coseno.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Calcular la raíz cuadrada de un número
# ? Usamos la función `sqrt()` del módulo `math` para calcular la raíz cuadrada.
# TODO: Escribe el código para calcular la raíz cuadrada de 16 usando el módulo `math`.

# * Ejemplo: Calcular el valor del seno de 90 grados
# ? Para trabajar con ángulos, primero convertimos los grados a radianes con `radians()` y luego
# ? usamos la función `sin()` para calcular el seno.
# TODO: Escribe el código para calcular el seno de 90 grados con el módulo `math`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: USO DEL MÓDULO 'DATETIME'
# ? El módulo `datetime` nos permite trabajar con fechas y horas.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Obtener la fecha y hora actual
# ? La función `datetime.now()` devuelve la fecha y hora actuales.
# TODO: Escribe el código para mostrar la fecha y hora actuales usando el módulo `datetime`.

# * Ejemplo: Crear una fecha personalizada
# ? Podemos crear una fecha personalizada usando `date()` del módulo `datetime`.
# TODO: Escribe el código para crear la fecha del 1 de enero de 2025 usando el módulo `datetime`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USO DEL MÓDULO 'RANDOM'
# ? El módulo `random` nos permite generar números aleatorios y hacer selecciones al azar.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Generar un número entero aleatorio
# ? Usamos la función `randint()` para generar un número entero aleatorio entre 1 y 100.
# TODO: Escribe el código para generar un número aleatorio entre 1 y 100 usando `random`.

# * Ejemplo: Seleccionar un elemento al azar de una lista
# ? La función `choice()` selecciona un elemento al azar de una lista.
# TODO: Escribe el código para elegir un servicio al azar de una lista como ["SSH", "Apache", "MySQL"].

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: USO DEL MÓDULO 'TIME'
# ? El módulo `time` permite pausar el programa durante un tiempo determinado o medir cuánto tiempo tarda en ejecutarse algo.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Pausar el programa por 2 segundos
# ? Usamos `time.sleep()` para detener la ejecución del programa durante el tiempo que deseemos.
# TODO: Escribe el código para pausar el programa durante 2 segundos usando el módulo `time`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: CREACIÓN DE MÓDULOS PERSONALIZADOS
# ? Podemos crear nuestros propios módulos para organizar mejor nuestro código.
# ? Esto nos permite reutilizar funciones y mejorar la estructura de nuestro programa.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Crear un módulo personalizado
# ? Podemos escribir funciones en un archivo `.py` y luego importarlo en otro archivo como un módulo.
# TODO: Crea un archivo `utilidades.py` con las funciones `saludar()` y `calcular_area_rectangulo()`.

# * Ejemplo: Usar el módulo personalizado
# ? Una vez creado el archivo `utilidades.py`, podemos importarlo en nuestro archivo principal.
# TODO: Importa las funciones `saludar()` y `calcular_area_rectangulo()` desde el módulo `utilidades`.

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Usa el módulo `math` para calcular el seno y coseno de un ángulo en grados.
# 2. Crea una fecha personalizada con el módulo `datetime` y calcula cuántos días faltan hasta esa fecha.
# 3. Genera 5 números aleatorios entre 1 y 50 usando `random.randint`.
# 4. Pausa el programa por 3 segundos usando el módulo `time.sleep()`.
# 5. Crea un módulo personalizado que contenga una función para saludar y otra para calcular el área de un triángulo.
# -------------------------------------------------------------------------------------------
