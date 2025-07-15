# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN AL MANEJO DE EXCEPCIONES EN PYTHON
# ? En programación, no todo sale como se espera. A veces, ocurren errores que pueden hacer 
# ? que un programa falle. Python nos permite manejar esos errores usando `try` y `except`.
# ? De esta forma, el programa sigue funcionando sin bloquearse.
# -------------------------------------------------------------------------------------------

# * EJEMPLO BÁSICO DE TRY Y EXCEPT:
# ? Imagina que estás trabajando con un sistema de control de dispositivos electrónicos.
# ? A veces, un usuario puede introducir un dato incorrecto (por ejemplo, letras en lugar de números).
# ? Usamos `try` para intentar convertir un valor de texto en número y `except` para manejar cualquier error.

# TODO: Escribe el código que intente convertir el ID de un dispositivo en un número entero
# TODO: Si ocurre un error, muestra un mensaje de "ID no válido".


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: MANEJO DE MÚLTIPLES EXCEPCIONES
# ? A veces, pueden ocurrir diferentes tipos de errores. Por ejemplo, el usuario podría intentar 
# ? introducir un valor inválido o realizar una operación que no es posible (como dividir por cero).
# ? Podemos manejar diferentes tipos de errores usando varios bloques `except`.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Control de energía en dispositivos.
# ? Vamos a pedir al usuario que introduzca la cantidad de energía que quiere asignar a un dispositivo.
# ? Pero, ¿qué pasa si el usuario introduce un valor incorrecto o intenta asignar 0 energía?

# TODO: Escribe el código para capturar diferentes tipos de errores, como:
# - Valor no válido (si el usuario introduce texto en lugar de números)
# - Dividir por cero (si el usuario introduce 0 en una operación que lo prohiba)


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: USO DEL BLOQUE FINALLY
# ? El bloque `finally` siempre se ejecuta al final de un bloque `try` y `except`, 
# ? incluso si ocurre un error. Es útil para asegurarte de que algunas acciones siempre se realicen,
# ? como apagar un dispositivo o guardar información crítica.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Imagina que estás operando un sistema de seguridad. Queremos asegurarnos de que,
# ? aunque ocurra un error, el sistema siempre se apague de forma segura al final.
# TODO: Implementa el código para usar `finally` en un ejemplo donde siempre se cierre el sistema,
# TODO: sin importar si ocurre un error.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: CAPTURAR TODAS LAS EXCEPCIONES
# ? En algunos casos, no podemos predecir qué tipo de error ocurrirá. En estos casos, 
# ? podemos usar `except Exception` para capturar cualquier error, sin importar cuál sea.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Monitorización de una red.
# ? Si estás monitorizando la actividad de una red y ocurre un error inesperado, 
# ? es importante que el sistema no se detenga por completo.

# TODO: Escribe el código para manejar cualquier error inesperado usando `except Exception`.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: LANZAR EXCEPCIONES PERSONALIZADAS
# ? En ciertos casos, es útil crear y lanzar tus propios errores o excepciones, 
# ? especialmente cuando necesitas validar ciertos datos antes de continuar.
# ? Usamos `raise` para lanzar excepciones personalizadas.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Validación de acceso a un sistema seguro.
# ? Vamos a comprobar si un usuario tiene permisos para acceder a un sistema militar. 
# ? Si no tiene el nivel adecuado, lanzaremos una excepción personalizada que indique que el acceso no está permitido.

# TODO: Escribe el código para validar los permisos del usuario y lanzar una excepción personalizada 
# TODO: si no tiene el nivel necesario.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Solicita al usuario que introduzca el ID de un dispositivo y el número de horas que ha estado activo.
# 2. Captura los posibles errores:
#    - Si el usuario introduce un valor no válido, muestra un mensaje de error adecuado.
#    - Si intenta dividir por cero o realizar otra operación no válida, muestra el error correspondiente.
# 3. Asegúrate de que al final, el programa siempre muestra "Operación completada" usando `finally`.
# -------------------------------------------------------------------------------------------

# TODO: Escribe aquí el código de la autoevaluación que maneje los errores y siempre finalice la operación.
