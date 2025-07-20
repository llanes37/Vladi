# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN A TESTING Y DEBUGGING EN PYTHON
# ? El Testing y el Debugging son herramientas esenciales para asegurar que el código funcione correctamente.
# ? El Testing se enfoca en verificar que el código cumple con los requisitos, mientras que el Debugging nos ayuda a encontrar y corregir errores.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: TIPOS DE TESTING
# ? Existen varios tipos de pruebas en programación, cada una con un propósito distinto.
# - Pruebas unitarias (Unit Testing): Verifican el funcionamiento de una función o unidad de código de forma aislada.
# - Pruebas de integración: Verifican cómo interactúan múltiples componentes del sistema entre sí.
# - Pruebas funcionales: Verifican que el sistema cumple con los requisitos funcionales.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * Ejemplo 1: Pruebas Unitarias en Python con el Módulo `unittest`
# ? El módulo `unittest` de Python permite realizar pruebas unitarias de manera sencilla.
# -------------------------------------------------------------------------------------------

import unittest

# * Definir una función simple para realizar pruebas
def suma(a, b):
    return a + b

# * Crear una clase de prueba heredando de `unittest.TestCase`
class TestSuma(unittest.TestCase):
    
    # Definir un método de prueba
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)  # Verificar si suma(1, 2) es igual a 3
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -2), -3)  # Verificar si suma(-1, -2) es igual a -3
    
    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)  # Verificar si suma(0, 0) es igual a 0

# * Ejecutar las pruebas cuando se ejecuta el archivo
if __name__ == "__main__":
    unittest.main()

# Explicación:
# - Hemos definido tres pruebas unitarias para la función `suma`.
# - Cada prueba verifica una situación diferente (números positivos, negativos y ceros).
# - Usamos `self.assertEqual()` para comparar el valor esperado con el valor real devuelto por la función.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: EL PROCESO DE DEBUGGING EN PYTHON
# ? Debugging es el proceso de identificar y corregir errores en el código.
# ? Python incluye herramientas como la función `print()` y el módulo `pdb` para facilitar el proceso de depuración.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * Ejemplo 2: Usar `print()` para depuración básica
# ? La depuración con `print()` es una técnica rápida para ver los valores de las variables en tiempo de ejecución.
# -------------------------------------------------------------------------------------------

def dividir(a, b):
    print(f"Valores recibidos: a = {a}, b = {b}")  # Depuración: Imprimir los valores recibidos
    if b == 0:
        print("Error: División por cero")
        return None
    return a / b

# * Probar la función con diferentes valores
resultado = dividir(10, 0)
print(f"Resultado de la división: {resultado}")

# Explicación:
# - Hemos usado `print()` para verificar los valores de `a` y `b` en tiempo de ejecución.
# - Si el valor de `b` es cero, imprimimos un mensaje de error en lugar de realizar la división.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: USANDO `pdb` PARA DEBUGGING INTERACTIVO
# ? El módulo `pdb` (Python Debugger) permite detener la ejecución del programa y examinar el estado del código en cualquier punto.
# -------------------------------------------------------------------------------------------

import pdb

def multiplicar(a, b):
    pdb.set_trace()  # Activar el modo de depuración interactiva
    return a * b

# * Probar la función con `pdb`
resultado = multiplicar(5, 7)
print(f"Resultado de la multiplicación: {resultado}")

# Explicación:
# - El método `pdb.set_trace()` detiene la ejecución del programa y abre un entorno interactivo de depuración.
# - En este entorno, podemos inspeccionar las variables, avanzar paso a paso, y ver cómo se ejecuta el código.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: ESTRATEGIAS DE DEPURACIÓN EFICIENTES
# ? Algunas estrategias de depuración incluyen:
# - Aislar el problema: Comentar partes del código para identificar dónde ocurre el error.
# - Probar con casos extremos: Usar valores inusuales o límites en las entradas para verificar el comportamiento del código.
# - Descomponer el problema: Dividir el código en partes más pequeñas para probarlas individualmente.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: AUTOEVALUACIÓN FINAL
# -------------------------------------------------------------------------------------------
# * Ejercicio 1:
# 1. Define una función que calcule el promedio de una lista de números.
# 2. Escribe una prueba unitaria para verificar si la función calcula correctamente el promedio.
# 3. Añade un caso de prueba para manejar una lista vacía, devolviendo `None` en ese caso.
# -------------------------------------------------------------------------------------------

# * Ejercicio 2:
# 1. Crea una función que encuentre el valor máximo en una lista de números.
# 2. Usa `pdb` para depurar un caso donde la lista esté vacía.
# 3. Utiliza `print()` para mostrar los valores de la lista en cada iteración de un bucle for.
# -------------------------------------------------------------------------------------------
