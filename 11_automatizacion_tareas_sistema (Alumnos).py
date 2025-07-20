# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: AUTOMATIZACIÓN DE TAREAS DEL SISTEMA EN WINDOWS CON PYTHON
# ? En esta lección vamos a ver cómo podemos interactuar con el sistema operativo Windows usando Python.
# ? Vamos a obtener información básica del sistema, monitorear el uso de CPU y memoria, y ver los procesos en ejecución.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * Ejemplo 1: Obtener información del sistema
# ? Python incluye una librería llamada `platform` que nos permite obtener datos del sistema como el nombre del OS y el procesador.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que obtenga y muestre la información del sistema operativo, la versión y el procesador.

# -------------------------------------------------------------------------------------------
# * Ejemplo 2: Monitorear el uso de CPU y memoria
# ? Usaremos comandos del sistema de Windows a través de Python para monitorear el uso de CPU y memoria.
# ? Para ello, utilizaremos el módulo `os` de Python que nos permite ejecutar comandos en el sistema operativo.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que use el comando de Windows para obtener el porcentaje de uso de la CPU y la memoria física disponible.

# -------------------------------------------------------------------------------------------
# * Ejemplo 3: Ver los procesos en ejecución
# ? Muchas veces es útil saber qué procesos se están ejecutando en el sistema. En Windows, esto se hace con el comando `tasklist`.
# -------------------------------------------------------------------------------------------

# TODO: Escribe una función que ejecute el comando `tasklist` para mostrar todos los procesos en ejecución en el sistema.

# -------------------------------------------------------------------------------------------
# * Ejemplo 4: Reiniciar el sistema (solo como ejemplo)
# ? En Python, también podemos enviar comandos para apagar o reiniciar el sistema, aunque debemos ser muy cuidadosos con esto.
# ? Como ejemplo, crearemos una función que muestre cómo se reiniciaría el sistema (sin ejecutarlo realmente).
# -------------------------------------------------------------------------------------------

# TODO: Crea una función que simule el comando para reiniciar el sistema pero sin ejecutarlo, usando el comando `shutdown`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: AUTOEVALUACIÓN FINAL
# -------------------------------------------------------------------------------------------
# * Ejercicio 1: Crear un sistema básico de monitoreo en Python.
# - Debes escribir un programa que cada 10 segundos monitoree el uso de CPU y memoria y guarde los resultados en un archivo de texto.
# - Usa las funciones que has creado para obtener los datos de CPU y memoria.
# - Guarda esos datos en un archivo de texto y añade la fecha y hora de cada medición.
# -------------------------------------------------------------------------------------------

# TODO: Crea una función que monitoree el uso de CPU y memoria cada 10 segundos, y que guarde los resultados en un archivo de registro.
