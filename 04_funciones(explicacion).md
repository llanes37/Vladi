
# Ejemplo Completo con Funciones y Ejercicios en Python

Este archivo contiene ejemplos completos y ejercicios prácticos sobre cómo utilizar funciones en Python en un contexto de gestión de tareas personales.

---

## Sección 1: Función Básica para Crear una Tarea

Las funciones nos permiten dividir el código en piezas reutilizables. Aquí tenemos una función que solicita el nombre y la descripción de una tarea, devolviendo un mensaje de confirmación.

### Código de ejemplo:
```python
def crear_tarea():
    nombre_tarea = input("Introduce el nombre de la tarea: ")
    descripcion = input("Introduce una breve descripción: ")
    return f"Tarea '{nombre_tarea}' creada con éxito. Descripción: {descripcion}"

print(crear_tarea())
```

---

## Sección 2: Función para Mostrar Todas las Tareas

Esta función muestra todas las tareas almacenadas en una lista.

### Código de ejemplo:
```python
def mostrar_tareas(tareas):
    print("=== Lista de Tareas ===")
    for tarea in tareas:
        print(f"- {tarea}")

tareas = ["Hacer la compra", "Estudiar Python", "Llamar al médico"]
mostrar_tareas(tareas)
```

---

## Sección 3: Función para Completar una Tarea

Permite marcar una tarea como completada, eliminándola de la lista.

### Código de ejemplo:
```python
def completar_tarea(tareas):
    tarea_a_completar = input("Introduce el nombre de la tarea completada: ")
    if tarea_a_completar in tareas:
        tareas.remove(tarea_a_completar)
        print(f"Tarea '{tarea_a_completar}' completada.")
    else:
        print(f"La tarea '{tarea_a_completar}' no existe en la lista.")

tareas = ["Hacer la compra", "Estudiar Python", "Llamar al médico"]
completar_tarea(tareas)
mostrar_tareas(tareas)
```

---

## Sección 4: Función para Filtrar Tareas por Prioridad

Esta función permite filtrar tareas en base a su nivel de prioridad.

### Código de ejemplo:
```python
def filtrar_tareas_por_prioridad(tareas):
    prioridad = input("Introduce la prioridad a filtrar (alta/media/baja): ").lower()
    filtradas = [tarea for tarea, nivel in tareas if nivel == prioridad]
    print(f"Tareas con prioridad {prioridad}: {filtradas}")

tareas = [("Hacer la compra", "baja"), ("Estudiar Python", "alta"), ("Llamar al médico", "media")]
filtrar_tareas_por_prioridad(tareas)
```

---

## Sección 5: Resumen de Tareas

Una función que genera un resumen con las tareas creadas, completadas y pendientes.

### Código de ejemplo:
```python
def resumen_tareas(tareas, completadas):
    print("=== Resumen de Tareas ===")
    print("Tareas Pendientes:")
    for tarea in tareas:
        print(f"- {tarea}")
    print("Tareas Completadas:")
    for tarea in completadas:
        print(f"- {tarea}")

tareas = ["Hacer la compra", "Estudiar Python"]
completadas = ["Llamar al médico"]
resumen_tareas(tareas, completadas)
```

---

## Sección Final: Autoevaluación

### Tareas:
1. Crea una función que solicite el nombre y prioridad de una tarea, y la agregue a una lista.
2. Solicita al usuario que complete tareas de la lista.
3. Muestra un resumen con las tareas pendientes y completadas.
4. Permite filtrar tareas por prioridad y mostrar solo las que sean de alta prioridad.
5. Crea un menú interactivo para gestionar todas las funciones.

### Código de ejemplo:
```python
def autoevaluacion():
    tareas = []
    completadas = []

    while True:
        print("=== Gestor de Tareas ===")
        print("1. Crear Tarea")
        print("2. Completar Tarea")
        print("3. Mostrar Resumen")
        print("4. Filtrar por Prioridad")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            tarea = input("Introduce el nombre de la tarea: ")
            prioridad = input("Introduce la prioridad (alta/media/baja): ").lower()
            tareas.append((tarea, prioridad))
        elif opcion == "2":
            completar_tarea([t[0] for t in tareas])
        elif opcion == "3":
            resumen_tareas([t[0] for t in tareas], completadas)
        elif opcion == "4":
            filtrar_tareas_por_prioridad(tareas)
        elif opcion == "5":
            print("Saliendo del gestor.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

autoevaluacion()
```

---

Este archivo cubre los fundamentos de las funciones en Python aplicados a la gestión de tareas personales, con ejemplos prácticos para reforzar el aprendizaje.
