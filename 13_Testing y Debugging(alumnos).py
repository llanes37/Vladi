# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN A TESTING Y DEBUGGING EN PYTHON
# ? El Testing y el Debugging son herramientas que nos permiten verificar que el código funcione correctamente.
# ? El Testing se encarga de probar que el código cumple con lo esperado. El Debugging es el proceso de buscar y corregir errores.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: TIPOS DE TESTING
# ? Existen varios tipos de pruebas que podemos realizar en un programa:
# - Pruebas Unitarias: Prueban una función o bloque de código de manera aislada.
# - Pruebas de Integración: Verifican cómo interactúan diferentes partes del programa.
# -------------------------------------------------------------------------------------------

# * Ejemplo 1: Pruebas Unitarias en Python con el Módulo `unittest`
# ? Vamos a usar `unittest`, un módulo de Python que nos permite realizar pruebas unitarias.
# -------------------------------------------------------------------------------------------

# TODO: Crea una función simple que realice una suma entre dos números.
# TODO: Escribe una prueba unitaria para comprobar que la función suma correctamente.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: USO DEL `print()` PARA DEPURACIÓN
# ? A veces es útil usar `print()` para ver qué está ocurriendo en el código.
# ? Podemos usarlo para mostrar los valores de las variables y ver si el código está funcionando como esperamos.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que divida dos números. Usa `print()` para mostrar los valores de entrada y salida.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USO DE `pdb` PARA DEPURAR PASO A PASO
# ? El módulo `pdb` de Python nos permite detener la ejecución del código y ver qué está ocurriendo en un momento específico.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que multiplique dos números y usa `pdb.set_trace()` para detener el programa y ver el valor de las variables.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: ESTRATEGIAS PARA DEBUGGING
# ? Algunas técnicas útiles para depurar incluyen:
# - Probar el código en pequeñas partes.
# - Usar casos límite o inusuales para probar cómo responde el código.
# - Añadir impresiones (`print()`) en las partes clave del código.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: AUTOEVALUACIÓN FINAL
# -------------------------------------------------------------------------------------------
# * Ejercicio 1:
# 1. Crea una función que reciba una lista de números y devuelva el promedio.
# 2. Escribe una prueba unitaria que verifique si la función devuelve el promedio correcto.
# 3. Asegúrate de manejar el caso donde la lista esté vacía (debería devolver `None`).
# -------------------------------------------------------------------------------------------

# TODO: Escribe la función de promedio y realiza las pruebas unitarias.

# * Ejercicio 2:
# 1. Escribe una función que encuentre el valor máximo en una lista de números.
# 2. Usa `pdb` para depurar un caso donde la lista esté vacía.
# 3. Usa `print()` para mostrar los valores de la lista en cada iteración mientras buscas el máximo.
# -------------------------------------------------------------------------------------------

# TODO: Escribe la función para encontrar el valor máximo y usa técnicas de depuración para comprobar su funcionamiento.
