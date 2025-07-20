# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: AUTOMATIZACIÓN DE TAREAS DEL SISTEMA CON DATOS REALES DE WINDOWS
# ? En este archivo, vamos a utilizar funciones y librerías integradas para automatizar tareas
# ? en un sistema Windows. Realizaremos acciones como obtener el nombre del sistema, 
# ? monitorear recursos, y ver información sobre el procesador.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * Ejemplo 1: Obtener el nombre del sistema y la versión de Windows
# ? Podemos utilizar la librería integrada `platform` para obtener información básica
# ? del sistema operativo y de la máquina.
# -------------------------------------------------------------------------------------------

import platform

# * Función para obtener y mostrar información del sistema
def obtener_informacion_sistema():
    nombre_sistema = platform.system()  # Obtener el nombre del sistema operativo
    version_sistema = platform.version()  # Obtener la versión de Windows
    procesador = platform.processor()  # Obtener información sobre el procesador
    print(f"Nombre del sistema operativo: {nombre_sistema}")
    print(f"Versión del sistema operativo: {version_sistema}")
    print(f"Procesador: {procesador}")

# * Llamada a la función
obtener_informacion_sistema()

# Explicación:
# - Usamos la librería `platform` para obtener el nombre del sistema operativo, la versión y el tipo de procesador.
# - Esta es una forma sencilla de obtener datos reales sobre el sistema sin instalar librerías externas.

# -------------------------------------------------------------------------------------------
# * Ejemplo 2: Monitorear el uso de CPU y memoria en Windows (con datos reales)
# ? Podemos usar el módulo `os` en conjunto con comandos del sistema para obtener información 
# ? en tiempo real sobre el uso de CPU y memoria en Windows.
# -------------------------------------------------------------------------------------------

import os

# * Función para monitorear el uso de CPU
def monitorear_cpu():
    print("Monitoreo de CPU en curso:")
    os.system("wmic cpu get loadpercentage")  # Comando de Windows para obtener el uso de CPU

# * Función para monitorear el uso de memoria
def monitorear_memoria():
    print("Monitoreo de memoria en curso:")
    os.system("systeminfo | findstr /C:\"Total Physical Memory\"")  # Total de memoria física
    os.system("systeminfo | findstr /C:\"Available Physical Memory\"")  # Memoria disponible

# * Llamadas a las funciones
monitorear_cpu()
monitorear_memoria()

# Explicación:
# - Usamos el comando `wmic cpu get loadpercentage` para obtener el porcentaje de uso de CPU en tiempo real.
# - Utilizamos `systeminfo` para obtener detalles sobre la memoria física total y disponible.
# - Estos comandos son nativos de Windows, y los usamos a través del módulo `os`.

# -------------------------------------------------------------------------------------------
# * Ejemplo 3: Ver los procesos en ejecución (con datos reales)
# ? En un entorno de administración de sistemas, es común necesitar información sobre los
# ? procesos que se están ejecutando en el sistema. En este ejemplo, usamos el comando `tasklist`.
# -------------------------------------------------------------------------------------------

# * Función para mostrar los procesos en ejecución
def mostrar_procesos():
    print("Procesos en ejecución en el sistema:")
    os.system("tasklist")  # Comando de Windows para listar los procesos en ejecución

# * Llamada a la función
mostrar_procesos()

# Explicación:
# - El comando `tasklist` nos proporciona una lista completa de todos los procesos que se están ejecutando.
# - Es útil para monitorear el sistema y detectar posibles problemas de rendimiento.

# -------------------------------------------------------------------------------------------
# * Ejemplo 4: Reiniciar el sistema (solo como ejemplo, no ejecutar)
# ? Este es un ejemplo de cómo se puede usar Python para enviar comandos de sistema para
# ? realizar operaciones como apagar o reiniciar la máquina.
# -------------------------------------------------------------------------------------------

# * Función para reiniciar el sistema (solo un ejemplo)
def reiniciar_sistema():
    print("Reiniciando el sistema (simulado)...")
    # os.system("shutdown /r /t 0")  # Comando para reiniciar el sistema inmediatamente

# * Explicación:
# - La línea `os.system("shutdown /r /t 0")` reiniciaría el sistema.
# - Se ha comentado la línea para evitar que se ejecute sin querer.
# - En un entorno real, esta línea se usaría para reiniciar o apagar el sistema.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: AUTOEVALUACIÓN FINAL
# -------------------------------------------------------------------------------------------
# * Ejercicio 1: Crear un sistema básico de monitoreo en Python.
# - Crea un programa que cada 10 segundos monitoree el uso de CPU y memoria y guarde los resultados en un archivo de registro.
# - Usa las funciones `monitorear_cpu` y `monitorear_memoria` para obtener los datos.
# - Almacena estos datos en un archivo de texto junto con la fecha y hora de cada medición.
# -------------------------------------------------------------------------------------------

import time

def monitorear_y_registrar():
    with open("registro_monitoreo.txt", "a") as archivo:
        for _ in range(5):  # Monitoreamos 5 veces en intervalos de 10 segundos
            archivo.write("\nMonitoreo en curso:\n")
            archivo.write("Uso de CPU:\n")
            os.system("wmic cpu get loadpercentage >> registro_monitoreo.txt")  # Guardar el uso de CPU
            archivo.write("Uso de Memoria:\n")
            os.system("systeminfo | findstr /C:\"Total Physical Memory\" >> registro_monitoreo.txt")  # Guardar memoria total
            os.system("systeminfo | findstr /C:\"Available Physical Memory\" >> registro_monitoreo.txt")  # Guardar memoria disponible
            archivo.write(f"Hora del monitoreo: {time.ctime()}\n")
            time.sleep(10)  # Esperar 10 segundos antes de la siguiente medición

# * Llamada a la función
monitorear_y_registrar()

# Explicación:
# - Este programa monitorea el sistema cada 10 segundos y guarda el uso de CPU y memoria en un archivo de texto.
# - Se utiliza un bucle que repite el monitoreo 5 veces en intervalos de 10 segundos, simulando un sistema de monitoreo en tiempo real.
