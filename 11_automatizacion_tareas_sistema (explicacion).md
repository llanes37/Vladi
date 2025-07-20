# Automatización de Tareas del Sistema con Datos Reales de Windows

## Introducción
En este documento, se explica cómo utilizar Python para automatizar tareas en un sistema Windows. Se incluyen ejemplos de cómo obtener información del sistema, monitorear el uso de recursos y gestionar procesos.

---

## 1. Obtener Información del Sistema
Python proporciona la librería `platform` para obtener detalles sobre el sistema operativo y el hardware.

### Código:
```python
import platform

def obtener_informacion_sistema():
    nombre_sistema = platform.system()
    version_sistema = platform.version()
    procesador = platform.processor()
    print(f"Nombre del sistema operativo: {nombre_sistema}")
    print(f"Versión del sistema operativo: {version_sistema}")
    print(f"Procesador: {procesador}")

obtener_informacion_sistema()
```

**Explicación:**
- `platform.system()` obtiene el nombre del sistema operativo.
- `platform.version()` obtiene la versión de Windows.
- `platform.processor()` obtiene información sobre el procesador.

---

## 2. Monitorear Uso de CPU y Memoria
Podemos usar el módulo `os` para ejecutar comandos del sistema y obtener métricas en tiempo real.

### Código:
```python
import os

def monitorear_cpu():
    print("Monitoreo de CPU en curso:")
    os.system("wmic cpu get loadpercentage")

def monitorear_memoria():
    print("Monitoreo de memoria en curso:")
    os.system("systeminfo | findstr /C:\"Total Physical Memory\"")
    os.system("systeminfo | findstr /C:\"Available Physical Memory\"")

monitorear_cpu()
monitorear_memoria()
```

**Explicación:**
- `wmic cpu get loadpercentage` obtiene el uso de CPU.
- `systeminfo` con `findstr` obtiene detalles sobre la memoria total y disponible.

---

## 3. Mostrar Procesos en Ejecución
Podemos ver los procesos en ejecución usando el comando `tasklist`.

### Código:
```python
def mostrar_procesos():
    print("Procesos en ejecución en el sistema:")
    os.system("tasklist")

mostrar_procesos()
```

**Explicación:**
- `tasklist` proporciona una lista de procesos en ejecución.

---

## 4. Reiniciar el Sistema (Ejemplo)
Podemos enviar comandos de apagado o reinicio al sistema.

### Código:
```python
def reiniciar_sistema():
    print("Reiniciando el sistema (simulado)...")
    # os.system("shutdown /r /t 0")
```

**Explicación:**
- `shutdown /r /t 0` reinicia el sistema inmediatamente.
- Se ha comentado la línea para evitar ejecuciones accidentales.

---

## 5. Ejercicio de Autoevaluación: Monitoreo en Tiempo Real
Se debe crear un programa que registre el uso de CPU y memoria cada 10 segundos.

### Código:
```python
import time

def monitorear_y_registrar():
    with open("registro_monitoreo.txt", "a") as archivo:
        for _ in range(5):
            archivo.write("\nMonitoreo en curso:\n")
            archivo.write("Uso de CPU:\n")
            os.system("wmic cpu get loadpercentage >> registro_monitoreo.txt")
            archivo.write("Uso de Memoria:\n")
            os.system("systeminfo | findstr /C:\"Total Physical Memory\" >> registro_monitoreo.txt")
            os.system("systeminfo | findstr /C:\"Available Physical Memory\" >> registro_monitoreo.txt")
            archivo.write(f"Hora del monitoreo: {time.ctime()}\n")
            time.sleep(10)

monitorear_y_registrar()
```

**Explicación:**
- Monitorea CPU y memoria cada 10 segundos.
- Guarda la información en `registro_monitoreo.txt`.
- Se ejecuta 5 veces antes de finalizar.

---

