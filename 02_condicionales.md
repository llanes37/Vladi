
# Ejemplo Completo con Condicionales y Ejercicios en Python

Este archivo contiene ejemplos completos y ejercicios prácticos sobre cómo utilizar condicionales en Python en un contexto de administración de sistemas.

---

## Sección 1: Condicionales Básicos

Las condiciones en Python se utilizan para tomar decisiones en base a una expresión que puede ser verdadera o falsa. En este ejemplo, simulamos la monitorización del uso de CPU de un servidor.

### Código de ejemplo:
```python
uso_cpu = int(input("Introduce el uso de CPU (%): "))

if uso_cpu > 85:
    print("Alerta: CPU alta")
else:
    print("CPU normal")
```

---

## Sección 2: Condiciones Múltiples con `elif`

El `elif` (abreviatura de "else if") permite evaluar condiciones adicionales si la primera no se cumple. En este ejemplo, monitorizamos tanto el uso de CPU como el de memoria.

### Código de ejemplo:
```python
uso_memoria = int(input("Introduce el uso de memoria (%): "))

if uso_cpu > 85 and uso_memoria > 85:
    print("Alerta: CPU y memoria altas")
elif uso_cpu > 85:
    print("Alerta: Solo CPU alta")
elif uso_memoria > 85:
    print("Alerta: Solo memoria alta")
else:
    print("Todo normal")
```

---

## Sección 3: Condiciones Anidadas

Las condiciones anidadas permiten evaluar una condición dentro de otra. Esto es útil cuando las decisiones dependen de múltiples factores.

### Código de ejemplo:
```python
estado_red = input("Conectado a la red (sí/no): ").lower()

if estado_red == "sí":
    if uso_cpu > 85:
        print("Conectado y CPU alta")
    else:
        print("Conectado y CPU normal")
else:
    print("Desconectado de la red")
```

---

## Sección 4: Operadores de Comparación y Lógicos

En este ejemplo, usamos operadores de comparación (`>`, `<`, `>=`, `<=`) y operadores lógicos como `and` y `or` para tomar decisiones basadas en múltiples condiciones.

### Código de ejemplo:
```python
if uso_cpu < 50 and uso_memoria < 50:
    print("Servidor óptimo")
elif uso_cpu < 50 or uso_memoria < 50:
    print("Un recurso óptimo")
else:
    print("Altos recursos")
```

---

## Sección 5: Evaluación Combinada

Combinamos el estado de los recursos del servidor y su estado de seguridad (actualizaciones instaladas) para realizar una evaluación completa.

### Código de ejemplo:
```python
actualizaciones = input("Actualizaciones instaladas (sí/no): ").lower()

if uso_cpu < 50 and uso_memoria < 50 and actualizaciones == "sí":
    print("Servidor óptimo y seguro")
elif uso_cpu > 85 or uso_memoria > 85 and actualizaciones == "no":
    print("Alerta: Altos recursos y sin actualizaciones")
else:
    print("Servidor seguro, revisa recursos")
```

---

## Sección Final: Autoevaluación

### Tareas:
1. Solicita al usuario que introduzca el nombre del servidor.
2. Pide el uso de CPU y memoria del servidor.
3. Verifica si el uso de CPU o memoria es mayor al 85%. Si lo es, muestra una alerta.
4. Pregunta si el servidor tiene actualizaciones instaladas.
5. Muestra un resumen del estado del servidor basado en los recursos y seguridad.

### Código de ejemplo:
```python
nombre_servidor = input("Nombre del servidor: ")
uso_cpu = int(input("Uso de CPU (%): "))
uso_memoria = int(input("Uso de memoria (%): "))
actualizaciones = input("Actualizaciones instaladas (sí/no): ").lower()

print(f"Servidor: {nombre_servidor}")
print(f"CPU: {uso_cpu}%")
print(f"Memoria: {uso_memoria}%")
print(f"Seguridad: {'Actualizado' if actualizaciones == 'sí' else 'No actualizado'}")

if (uso_cpu > 85 or uso_memoria > 85) and actualizaciones == "no":
    print("Advertencia: Alto uso de recursos y sin actualizaciones")
```

---

Este archivo cubre los fundamentos de los condicionales en Python con ejemplos prácticos y ejercicios aplicados a la administración de sistemas.
