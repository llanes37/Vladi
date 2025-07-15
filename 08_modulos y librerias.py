# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN A MÓDULOS Y LIBRERÍAS EN PYTHON
# ? Un módulo es un archivo que contiene código Python (funciones, variables, clases, etc.).
# ? Una librería es una colección de módulos. Python incluye muchas librerías estándar que podemos usar.
# -------------------------------------------------------------------------------------------

# * ¿Por qué usar módulos?
# - Permiten reutilizar código en diferentes partes del programa o en proyectos distintos.
# - Mejoran la organización del código, separando funcionalidades en archivos independientes.
# - Ahorra tiempo al utilizar funcionalidades ya implementadas.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: USO DEL MÓDULO 'MATH'
# ? El módulo `math` proporciona acceso a muchas funciones matemáticas comunes como seno, coseno,
# ? tangente, logaritmos, potencias y más.
# -------------------------------------------------------------------------------------------

import math

# Calcular la raíz cuadrada de un número
numero = 16
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")

# Calcular el valor del seno de 90 grados (convertido a radianes)
angulo_grados = 90
angulo_radianes = math.radians(angulo_grados)
valor_seno = math.sin(angulo_radianes)
print(f"El seno de {angulo_grados} grados es {valor_seno}")

# Redondear un número hacia arriba y hacia abajo
numero_decimal = 7.3
print(f"{numero_decimal} redondeado hacia abajo es {math.floor(numero_decimal)}")
print(f"{numero_decimal} redondeado hacia arriba es {math.ceil(numero_decimal)}")

# Calcular el valor de Pi y E (números matemáticos importantes)
print(f"El valor de Pi es {math.pi}")
print(f"El valor de Euler (E) es {math.e}")

# Explicación:
# - `math.sqrt(x)` devuelve la raíz cuadrada de `x`.
# - `math.radians(x)` convierte grados a radianes.
# - `math.sin(x)` calcula el seno de un ángulo en radianes.
# - `math.floor(x)` redondea hacia abajo, mientras que `math.ceil(x)` redondea hacia arriba.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: USO DEL MÓDULO 'DATETIME'
# ? El módulo `datetime` proporciona clases para manipular fechas y horas.
# -------------------------------------------------------------------------------------------

import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()
print(f"La fecha y hora actual es: {fecha_hora_actual}")

# Obtener solo la fecha actual
fecha_actual = datetime.date.today()
print(f"La fecha actual es: {fecha_actual}")

# Crear una fecha personalizada
fecha_personalizada = datetime.date(2024, 9, 26)
print(f"Una fecha personalizada es: {fecha_personalizada}")

# Calcular la diferencia entre dos fechas
fecha_inicio = datetime.date(2023, 1, 1)
dias_diferencia = fecha_actual - fecha_inicio
print(f"Han pasado {dias_diferencia.days} días desde el 1 de enero de 2023")

# Explicación:
# - `datetime.datetime.now()` devuelve la fecha y hora actuales.
# - `datetime.date(year, month, day)` crea un objeto de fecha.
# - Restar dos fechas devuelve un objeto `timedelta` que contiene la diferencia entre ellas.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USO DEL MÓDULO 'RANDOM'
# ? El módulo `random` se utiliza para generar números aleatorios, hacer selecciones al azar, 
# ? mezclar listas y más.
# -------------------------------------------------------------------------------------------

import random

# Generar un número entero aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatorio entre 1 y 100: {numero_aleatorio}")

# Elegir una opción al azar de una lista de opciones
opciones = ['Ejecutar', 'Reiniciar', 'Apagar']
opcion_seleccionada = random.choice(opciones)
print(f"La opción seleccionada al azar es: {opcion_seleccionada}")

# Barajar una lista de números
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(f"Números después de barajarlos: {numeros}")

# Generar un número decimal aleatorio entre 0 y 1
numero_decimal_aleatorio = random.random()
print(f"Número decimal aleatorio entre 0 y 1: {numero_decimal_aleatorio}")

# Explicación:
# - `random.randint(a, b)` genera un número entero aleatorio entre `a` y `b`.
# - `random.choice(lista)` selecciona un elemento al azar de una lista.
# - `random.shuffle(lista)` baraja los elementos de una lista.
# - `random.random()` genera un número decimal aleatorio entre 0 y 1.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: USO DEL MÓDULO 'TIME'
# ? El módulo `time` nos permite pausar la ejecución del programa por un tiempo determinado.
# ? También nos permite medir el tiempo de ejecución de fragmentos de código.
# -------------------------------------------------------------------------------------------

import time

# Pausar el programa durante 2 segundos
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Continuando con el programa!")

# Medir el tiempo que tarda un fragmento de código en ejecutarse
inicio = time.time()
# Simulamos un proceso que tarda 1 segundo en ejecutarse
time.sleep(1)
fin = time.time()
print(f"El proceso tomó {fin - inicio} segundos en ejecutarse.")

# Explicación:
# - `time.sleep(x)` pausa la ejecución durante `x` segundos.
# - `time.time()` devuelve el tiempo en segundos desde la "época" (1 de enero de 1970).
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: CREACIÓN DE MÓDULOS PERSONALIZADOS
# ? Podemos crear nuestros propios módulos para organizar mejor el código.
# ? Basta con escribir funciones en un archivo .py y luego importarlo.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Crear un módulo personalizado llamado `utilidades.py`
# Archivo: utilidades.py
# def saludar(nombre):
#     return f"Hola, {nombre}! Bienvenido al sistema."
#
# def calcular_area_rectangulo(largo, ancho):
#     return largo * ancho
#
# Ahora podemos importar este archivo en nuestro programa principal:
# from utilidades import saludar, calcular_area_rectangulo

# * Llamar a las funciones del módulo `utilidades`
# print(saludar("Carlos"))
# print(f"El área del rectángulo es: {calcular_area_rectangulo(5, 3)}")

# Explicación:
# - El módulo `utilidades.py` contiene funciones reutilizables.
# - Importamos las funciones `saludar` y `calcular_area_rectangulo` y las usamos en nuestro programa principal.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Utiliza el módulo `math` para calcular el seno y coseno de un ángulo en grados.
# 2. Usa el módulo `datetime` para crear una fecha personalizada y calcular cuántos días han pasado
#    desde el inicio del año hasta hoy.
# 3. Genera 5 números aleatorios entre 1 y 50 usando `random.randint`.
# 4. Crea un cronómetro que mida cuánto tiempo tarda en ejecutarse un fragmento de código usando `time.time`.
# -------------------------------------------------------------------------------------------
