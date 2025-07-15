# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: INTRODUCCIÓN AL MANEJO DE EXCEPCIONES EN PYTHON
# ? En una operación militar de sistemas, es importante que los programas no fallen 
# ? cuando ocurre un error inesperado. En Python, podemos usar `try`, `except`, y `finally` 
# ? para manejar estos errores y asegurarnos de que el sistema siga funcionando.
# -------------------------------------------------------------------------------------------

# * EJEMPLO BÁSICO DE TRY Y EXCEPT:
# ? Imagina que estás desplegando sistemas en un entorno militar, y el sistema 
# ? necesita que los usuarios introduzcan correctamente los datos.
# ? Aquí intentamos convertir una cadena a un número entero, y si falla, manejamos el error.

try:
    equipo_id = int(input("Introduce el ID del equipo (número): "))  # Solicitar el ID del equipo
    print(f"ID del equipo: {equipo_id}")
except ValueError:
    print("Error: ID del equipo no válido. Por favor, introduce un número.")

# Explicación:
# - `try`: Aquí colocamos el código que podría causar un error (por ejemplo, el usuario introduce texto en vez de un número).
# - `except`: Si ocurre un error en el bloque try, el programa ejecutará el código en except para manejarlo sin que el programa se detenga.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: MANEJO DE MÚLTIPLES EXCEPCIONES
# ? En una operación de sistemas, a veces puedes tener múltiples tipos de errores.
# ? Podemos manejar diferentes excepciones utilizando varios bloques except para asegurar que el sistema siga funcionando.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Gestionar la carga de municiones en un sistema militar.
# ? Aquí intentamos realizar una operación que puede fallar por múltiples razones.

try:
    carga_municiones = int(input("Introduce el número de municiones a cargar: "))
    capacidad_max = 100
    resultado = capacidad_max / carga_municiones
    print(f"Municiones cargadas: {carga_municiones}")
except ValueError:
    print("Error: Introdujiste un valor no válido.")
except ZeroDivisionError:
    print("Error: No puedes cargar 0 municiones.")
    
# Explicación:
# - `except ValueError`: Captura el error si el usuario introduce texto en lugar de un número.
# - `except ZeroDivisionError`: Captura el error si el usuario intenta dividir por cero, es decir, si carga 0 municiones.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: USO DEL BLOQUE FINALLY
# ? El bloque `finally` siempre se ejecuta, independientemente de si ocurre un error o no.
# ? Es útil para tareas críticas como cerrar comunicaciones o liberar recursos después de una operación militar.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Controlar un sistema de radar
# ? Imagina que estás operando un radar, y siempre es necesario apagarlo correctamente, incluso si ocurre un error.

try:
    print("Activando radar...")
    # Aquí simulamos una posible operación fallida con el radar
    raise FileNotFoundError  # Simulamos un error al intentar cargar datos del radar
except FileNotFoundError:
    print("Error: No se pudo acceder a los datos del radar.")
finally:
    print("Apagando radar de forma segura.")

# Explicación:
# - `finally`: Siempre se ejecuta, útil para asegurar que el radar o cualquier equipo se apague correctamente sin importar el error.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: CAPTURAR TODAS LAS EXCEPCIONES
# ? A veces, no sabremos qué tipo de error puede ocurrir en una operación. 
# ? Podemos capturar cualquier tipo de error usando `except Exception`.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Monitoreo de la red en una operación militar.
# ? Aquí intentamos conectarnos a la red, pero si ocurre cualquier error, se maneja.

try:
    # Simulamos una operación que podría fallar, como conectarse a un servidor
    resultado = 10 / 0  # Simulamos un error
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

# Explicación:
# - `except Exception`: Captura cualquier tipo de excepción que ocurra, útil cuando no sabemos exactamente qué tipo de error esperar.
# - `e`: Es el objeto de la excepción que contiene información sobre el error.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: LANZAR EXCEPCIONES PERSONALIZADAS
# ? Puedes generar tus propias excepciones para asegurarte de que se cumplan ciertas reglas 
# ? en operaciones críticas. Esto es especialmente útil cuando quieres aplicar reglas de seguridad.
# -------------------------------------------------------------------------------------------

# * EJEMPLO: Verificar permisos de acceso en un sistema de control.
# ? Aquí creamos una excepción personalizada si el usuario no tiene el nivel de autorización adecuado.

def verificar_permisos(nivel):
    if nivel < 3:
        raise PermissionError("Error: No tienes suficientes permisos para acceder a este sistema.")
    else:
        print("Acceso autorizado. Bienvenido.")

# Explicación:
# - `raise`: Se utiliza para lanzar una excepción personalizada.
# - `PermissionError`: El tipo de excepción personalizada que lanzamos para indicar que el usuario no tiene los permisos adecuados.

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Solicita al usuario que introduzca el ID de un equipo y el número de operaciones que ha completado.
# 2. Captura los posibles errores: si el usuario no introduce números válidos y si intenta realizar una operación no válida (por ejemplo, dividir por cero).
# 3. Asegúrate de que al final, el programa siempre imprime "Operación completada" usando el bloque `finally`.
# -------------------------------------------------------------------------------------------

# CÓDIGO DE AUTOEVALUACIÓN:

try:
    equipo_id = int(input("Introduce el ID del equipo (número): "))
    operaciones_completadas = int(input("Introduce el número de operaciones completadas: "))
    eficiencia = equipo_id / operaciones_completadas
    print(f"El equipo {equipo_id} ha completado {operaciones_completadas} operaciones.")
except ValueError:
    print("Error: Debes introducir un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero.")
finally:
    print("Operación completada.")
