
# Ejemplo Completo con Bucles y Ejercicios en Python

Este archivo contiene ejemplos completos y ejercicios prácticos sobre cómo utilizar bucles en Python en un contexto de gestión de inventarios.

---

## Sección 1: Bucle `for` Básico

Los bucles `for` permiten iterar sobre una lista de productos para mostrar su inventario.

### Código de ejemplo:
```python
productos = ["Manzanas", "Plátanos", "Naranjas", "Leche", "Pan"]

for producto in productos:
    print(f"Producto disponible: {producto}")
```
---

## Sección 2: Bucle `for` con Precios

Podemos usar bucles `for` para mostrar productos junto con sus precios.
La palabra reservada zip, indica al bucle for que vamos a iterar dos conjuntos de elementos que tienen la misma longitud.

### Código de ejemplo:
```python
productos = ["Manzanas", "Plátanos", "Naranjas"]
precios = [1.2, 0.5, 0.8]

for producto, precio in zip(productos, precios):
    print(f"Producto: {producto} - Precio: ${precio}")
```
---

## Sección 3: Bucle `for` con Índice usando `enumerate()`

A veces necesitamos tanto el índice como el valor al iterar sobre una lista.
Con enumerate(), obtenemos el índice y el valor simultáneamente.

### Código de ejemplo:
```python
productos = ["Manzanas", "Plátanos", "Naranjas"]

for indice, producto in enumerate(productos):
    print(f"{indice + 1}. {producto}")
```
---

## Sección 4: Bucle `while` para Controlar el Stock

Los bucles `while` son útiles cuando necesitamos monitorear el estado de algo, como el stock de productos.

### Código de ejemplo:
```python
stock = 50  # Stock inicial de un producto

while stock > 10:
    print(f"Stock actual: {stock}. Vendiendo unidades...")
    stock -= 5

print(f"Stock bajo: {stock}. Es hora de reabastecer.")
```
---

## Sección 5: Bucle `while` con Condiciones Externas

Monitorear el stock y reabastecer automáticamente si cae por debajo de un umbral.

### Código de ejemplo:
```python
stock = 50

while stock > 0:
    print(f"Vendiendo producto. Stock actual: {stock}.")
    stock -= 10
    if stock < 20:
        print("¡Advertencia! Stock bajo. Reabasteciendo...")
        stock += 30
```

---

## Sección 6: Gestión de Productos y Stock

Un ejemplo avanzado que utiliza un bucle `for` para iterar sobre un diccionario de productos y verificar su stock.

### Código de ejemplo:
```python
inventario = {
    "Manzanas": 10,
    "Plátanos": 5,
    "Naranjas": 8,
    "Leche": 0,
    "Pan": 2
}

for producto, cantidad in inventario.items():
    if cantidad == 0:
        print(f"{producto}: Agotado. Necesita reabastecimiento.")
    elif cantidad < 5:
        print(f"{producto}: Stock bajo ({cantidad}).")
    else:
        print(f"{producto}: Stock suficiente ({cantidad}).")
```

---

## Sección Final: Autoevaluación

### Tareas:
1. Crea una lista de productos y sus precios.
2. Usa un bucle `for` para mostrar cada producto con su precio.
3. Crea un sistema que reduzca el stock de un producto hasta llegar a un umbral mínimo.
4. Usa un diccionario para gestionar el stock de múltiples productos y verifica cuáles necesitan reabastecimiento.

### Código de ejemplo resuelto:
```python
productos = ["Manzanas", "Plátanos", "Naranjas"]
precios = [1.2, 0.5, 0.8]
stock = {"Manzanas": 10, "Plátanos": 5, "Naranjas": 8}

# Mostrar productos y precios
for producto, precio in zip(productos, precios):
    print(f"Producto: {producto}, Precio: ${precio}")

# Reducir el stock de productos
for producto, cantidad in stock.items():
    while cantidad > 3:
        print(f"Vendiendo {producto}. Stock actual: {cantidad}.")
        cantidad -= 2
    stock[producto] = cantidad

# Verificar stock final
for producto, cantidad in stock.items():
    if cantidad <= 3:
        print(f"{producto}: Stock bajo ({cantidad}). Reabastecimiento necesario.")
```

---

Este archivo cubre los fundamentos de los bucles en Python aplicados a la gestión de inventarios, con ejemplos prácticos y ejercicios para reforzar el aprendizaje.
