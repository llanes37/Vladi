
# Ejemplo Completo con Funciones y Ejercicios en Python

Este archivo contiene ejemplos completos y ejercicios prácticos sobre cómo utilizar funciones en Python en un contexto de administración de sistemas.

---

## Sección 1: Función Básica para Saludar

Las funciones nos permiten dividir el código en piezas más pequeñas y reutilizables. Aquí tenemos una función que solicita el rango y nombre de un usuario, devolviendo un saludo personalizado.

### Código de ejemplo:
```python
def saludar():
    oficial = input("Introduce tu rango y nombre: ")
    return f"Bienvenido al sistema, {oficial}. Preparado para el servicio."

print(saludar())
```

---

## Sección 2: Función para Calcular el Uso de Recursos

Esta función solicita el uso de CPU y memoria de un servidor, permitiendo asignar un valor por defecto a la memoria si el usuario no introduce nada.

### Código de ejemplo:
```python
def calcular_uso_recursos():
    cpu = int(input("Introduce el uso de CPU en porcentaje: "))
    memoria = input("Introduce la memoria disponible en MB (o presiona enter para usar 2048MB): ")
    if memoria == "":
        memoria = 2048
    else:
        memoria = int(memoria)
    return f"El uso actual de CPU es {cpu}% y la memoria disponible es {memoria} MB."

print(calcular_uso_recursos())
```

---

## Sección 3: Función para Gestionar Usuarios

Una función que determina si un usuario tiene privilegios de administrador o no.

### Código de ejemplo:
```python
def gestionar_usuario():
    usuario = input("Introduce el nombre del usuario: ")
    es_administrador = input("¿El usuario es administrador? (s/n): ").lower() == 's'
    if es_administrador:
        return f"El usuario {usuario} tiene privilegios de administrador. Acceso completo al sistema."
    else:
        return f"El usuario {usuario} es un usuario estándar. Acceso limitado."

print(gestionar_usuario())
```

---

## Sección 4: Función para Comprobar Servicios Críticos

Esta función itera sobre una lista de servicios críticos y los comprueba uno a uno.

### Código de ejemplo:
```python
def comprobar_servicios():
    servicios_criticos = ["SSH", "VPN", "Firewall", "DNS"]
    for servicio in servicios_criticos:
        print(f"Comprobando el estado del servicio {servicio}...")

comprobar_servicios()
```

---

## Sección 5: Monitorización de Servidores

Una función que solicita el estado de varios servidores y registra cuáles están disponibles.

### Código de ejemplo:
```python
def monitorizar_servidores():
    servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    servidores_disponibles = []
    for servidor in servidores:
        disponible = input(f"¿El servidor {servidor} está disponible? (s/n): ").lower()
        if disponible == 's':
            servidores_disponibles.append(servidor)
        else:
            print(f"¡Atención! El servidor {servidor} no está disponible.")
    print(f"Servidores disponibles: {servidores_disponibles}")

monitorizar_servidores()
```

---

## Sección Final: Autoevaluación

### Tareas:
1. Crea una función que solicite el nombre del servidor y lo guarde en una variable.
2. Solicita el uso de CPU y memoria del servidor, ofreciendo un valor por defecto para la memoria.
3. Solicita el estado de varios servicios y guarda los que estén activos.
4. Solicita el estado de varios servidores y almacena los que estén disponibles.
5. Imprime un resumen final con el nombre del servidor, uso de CPU y memoria, servicios activos, y servidores disponibles.

### Código de ejemplo:
```python
def autoevaluacion():
    servidor_nombre = input("Introduce el nombre del servidor: ")
    cpu = int(input("Introduce el uso de CPU en porcentaje: "))
    memoria = input("Introduce la memoria disponible en MB (presiona enter para usar 2048MB): ")
    if memoria == "":
        memoria = 2048
    else:
        memoria = int(memoria)
    servicios = ["SSH", "VPN", "Firewall", "DNS"]
    servicios_activos = []
    for servicio in servicios:
        estado = input(f"¿El servicio {servicio} está activo? (s/n): ").lower()
        if estado == 's':
            servicios_activos.append(servicio)
    servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    servidores_disponibles = []
    for servidor in servidores:
        disponible = input(f"¿El servidor {servidor} está disponible? (s/n): ").lower()
        if disponible == 's':
            servidores_disponibles.append(servidor)
    print("
=== RESUMEN DEL SISTEMA ===")
    print(f"Servidor: {servidor_nombre}")
    print(f"Uso de CPU: {cpu}%")
    print(f"Memoria disponible: {memoria} MB")
    print(f"Servicios activos: {servicios_activos}")
    print(f"Servidores disponibles: {servidores_disponibles}")

autoevaluacion()
```

---

Este archivo cubre los fundamentos de las funciones en Python con ejemplos prácticos y ejercicios aplicados a la administración de sistemas.
