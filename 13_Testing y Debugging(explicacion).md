# Introducción a Testing y Debugging en Python

## 1. Introducción
Testing y Debugging son herramientas esenciales para garantizar que el código funcione correctamente:
- **Testing**: Verifica que el código cumple con los requisitos esperados.
- **Debugging**: Identifica y corrige errores en el código.

---

## 2. Tipos de Testing
Existen diferentes tipos de pruebas en programación:
- **Pruebas Unitarias**: Verifican el funcionamiento de una función o unidad de código de forma aislada.
- **Pruebas de Integración**: Evalúan cómo interactúan múltiples componentes del sistema.
- **Pruebas Funcionales**: Aseguran que el sistema cumple con los requisitos funcionales.

---

## 3. Pruebas Unitarias con `unittest`

Python proporciona el módulo `unittest` para realizar pruebas unitarias.

### Ejemplo:
```python
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -2), -3)
    
    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
```

**Explicación:**
- Se definen pruebas unitarias para verificar diferentes escenarios.
- `self.assertEqual()` compara el resultado esperado con el valor obtenido.

---

## 4. Debugging en Python

### Debugging con `print()`
```python
def dividir(a, b):
    print(f"Valores recibidos: a = {a}, b = {b}")
    if b == 0:
        print("Error: División por cero")
        return None
    return a / b

resultado = dividir(10, 0)
print(f"Resultado de la división: {resultado}")
```

**Explicación:**
- Se usa `print()` para depurar los valores de entrada.
- Se verifica la condición de división por cero antes de ejecutar la operación.

---

### Debugging con `pdb`

Python proporciona el módulo `pdb` para depuración interactiva.

```python
import pdb

def multiplicar(a, b):
    pdb.set_trace()  # Activa la depuración interactiva
    return a * b

resultado = multiplicar(5, 7)
print(f"Resultado de la multiplicación: {resultado}")
```

**Explicación:**
- `pdb.set_trace()` pausa la ejecución y permite inspeccionar variables.
- Se puede avanzar paso a paso en el código.

---

## 5. Estrategias de Depuración
- **Aislar el problema**: Comentar partes del código para identificar el origen del error.
- **Probar casos extremos**: Evaluar con valores límites.
- **Descomponer el código**: Dividir el problema en partes más pequeñas.

---

## 6. Autoevaluación

### Ejercicio 1: Pruebas Unitarias
1. Define una función que calcule el promedio de una lista de números.
2. Escribe una prueba unitaria para verificar si la función calcula correctamente el promedio.
3. Añade un caso de prueba para manejar una lista vacía, devolviendo `None`.

### Ejercicio 2: Depuración
1. Crea una función que encuentre el valor máximo en una lista de números.
2. Usa `pdb` para depurar un caso donde la lista esté vacía.
3. Utiliza `print()` para mostrar los valores de la lista en cada iteración de un bucle `for`.

---

## Conclusión
Testing y Debugging son esenciales para el desarrollo de software confiable. Con `unittest` y `pdb`, podemos validar y depurar código de manera eficiente.

