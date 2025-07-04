# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: EJEMPLO BÁSICO DE CONDICIONES EN PYTHON
# ? LAS CONDICIONES EN PYTHON SE UTILIZAN PARA TOMAR DECISIONES EN BASE A UNA EXPRESIÓN
# ? QUE PUEDE SER VERDADERA O FALSA. EN ESTE EJEMPLO, SIMULAMOS LA MONITORIZACIÓN
# ? DEL USO DE CPU DE UN SERVIDOR.
# -------------------------------------------------------------------------------------------

# Solicitamos al usuario que introduzca el uso de CPU.
# `input()` recibe la entrada del usuario como texto, pero lo convertimos a entero con `int()`.
uso_cpu = int(input("Introduce el uso de CPU (%): "))

# Verificamos si el uso de CPU es mayor al 85%.
# La estructura if/else permite ejecutar diferentes bloques de código en función de si la condición es verdadera o falsa.
if uso_cpu > 85:
    # Si el uso de CPU es mayor que 85, mostramos un mensaje de alerta.
    print("Alerta: CPU alta")
else:
    # Si no se cumple la condición, se ejecuta el bloque else y se muestra un mensaje indicando que el uso de CPU es normal.
    print("CPU normal")

# Explicación:
# - `if` verifica si la condición (uso_cpu > 85) es verdadera.
# - Si es verdadera, se ejecuta el bloque de código que sigue a `if`.
# - Si es falsa, se ejecuta el bloque de código dentro de `else`.
# - Este tipo de estructura es fundamental para permitir que un programa "decida" qué acción tomar.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: CONDICIONES MÚLTIPLES CON ELIF
# ? ELIF ES UNA ABREVIATURA DE "ELSE IF". SE UTILIZA PARA EVALUAR CONDICIONES ADICIONALES
# ? CUANDO LA PRIMERA CONDICIÓN NO SE CUMPLE. EN ESTE EJEMPLO, MONITORIZAMOS
# ? EL USO DE CPU Y MEMORIA EN EL SERVIDOR.
# -------------------------------------------------------------------------------------------

# Solicitamos al usuario que introduzca el uso de memoria del servidor.
uso_memoria = int(input("Introduce el uso de memoria (%): "))

# Evaluamos diferentes combinaciones de uso de CPU y memoria.
# Usamos `and` para verificar si ambas condiciones son verdaderas (uso de CPU y memoria > 85).
if uso_cpu > 85 and uso_memoria > 85:
    # Si ambos recursos están por encima del 85%, mostramos una alerta para ambos.
    print("Alerta: CPU y memoria altas")
elif uso_cpu > 85:
    # Si solo el uso de CPU está alto, mostramos una alerta para CPU.
    print("Alerta: Solo CPU alta")
elif uso_memoria > 85:
    # Si solo el uso de memoria está alto, mostramos una alerta para memoria.
    print("Alerta: Solo memoria alta")
else:
    # Si ninguno de los recursos está por encima del 85%, se considera normal.
    print("Todo normal")

# Explicación:
# - `elif` permite evaluar múltiples condiciones de manera secuencial.
# - El programa ejecuta el primer bloque de código donde la condición es verdadera.
# - Si ninguna de las condiciones es verdadera, se ejecuta el bloque `else` al final.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: CONDICIONES ANIDADAS
# ? LAS CONDICIONES ANIDADAS PERMITEN EVALUAR UNA CONDICIÓN DENTRO DE OTRA.
# ? ESTO ES ÚTIL CUANDO LAS DECISIONES DEPENDEN DE VARIAS VARIABLES O FACTORES.
# ? EN ESTE EJEMPLO, EVALUAMOS SI EL SERVIDOR ESTÁ CONECTADO A LA RED Y EL USO DE CPU.
# -------------------------------------------------------------------------------------------

# Solicitamos al usuario que introduzca el estado de la red, si está conectado o no.
# `lower()` convierte la entrada a minúsculas para evitar problemas con mayúsculas/minúsculas.
estado_red = input("Conectado a la red (sí/no): ").lower()

# Verificamos si el servidor está conectado a la red.
if estado_red == "sí":
    # Si está conectado, evaluamos el uso de CPU.
    if uso_cpu > 85:
        # Si el uso de CPU es alto y el servidor está conectado, mostramos una alerta específica.
        print("Conectado y CPU alta")
    else:
        # Si está conectado pero el uso de CPU es normal, mostramos un mensaje indicando eso.
        print("Conectado y CPU normal")
else:
    # Si el servidor no está conectado a la red, mostramos un mensaje informando que está desconectado.
    print("Desconectado de la red")

# Explicación:
# - Aquí tenemos una condición `if` dentro de otra condición `if`, lo que se llama una "condición anidada".
# - Esto nos permite hacer decisiones más detalladas dependiendo de múltiples variables.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: OPERADORES DE COMPARACIÓN Y LÓGICOS
# ? EN ESTE EJEMPLO USAMOS OPERADORES DE COMPARACIÓN (`>`, `<`, `>=`, `<=`) Y OPERADORES LÓGICOS
# ? COMO `AND` Y `OR` PARA TOMAR DECISIONES BASADAS EN MÚLTIPLES CONDICIONES.
# -------------------------------------------------------------------------------------------

# Verificamos si el uso de CPU y memoria es menor al 50%.
if uso_cpu < 50 and uso_memoria < 50:
    # Si ambos recursos están por debajo del 50%, el servidor se considera óptimo.
    print("Servidor óptimo")
elif uso_cpu < 50 or uso_memoria < 50:
    # Si al menos uno de los recursos está por debajo del 50%, mostramos que un recurso es óptimo.
    print("Un recurso óptimo")
else:
    # Si ninguno de los recursos está por debajo del 50%, mostramos que los recursos están altos.
    print("Altos recursos")

# Explicación:
# - Los operadores lógicos `and` y `or` permiten combinar múltiples condiciones.
# - `and` requiere que ambas condiciones sean verdaderas, mientras que `or` solo necesita que una condición sea verdadera.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: EVALUACIÓN COMBINADA
# ? AQUÍ EVALUAMOS NO SOLO EL USO DE CPU Y MEMORIA, SINO TAMBIÉN SI EL SERVIDOR TIENE
# ? INSTALADAS ACTUALIZACIONES DE SEGURIDAD, COMBINANDO MÚLTIPLES CONDICIONES.
# -------------------------------------------------------------------------------------------

# Solicitamos al usuario si el servidor tiene actualizaciones instaladas.
# Convertimos la respuesta a minúsculas con `lower()` para facilitar la comparación.
actualizaciones = input("Actualizaciones instaladas (sí/no): ").lower()

# Evaluamos el estado general del servidor (CPU, memoria y actualizaciones).
if uso_cpu < 50 and uso_memoria < 50 and actualizaciones == "sí":
    # Si el servidor tiene recursos bajos y está actualizado, es óptimo y seguro.
    print("Servidor óptimo y seguro")
elif uso_cpu > 85 or uso_memoria > 85 and actualizaciones == "no":
    # Si los recursos son altos y no tiene actualizaciones, mostramos una alerta de alto riesgo.
    print("Alerta: Altos recursos y sin actualizaciones")
else:
    # Si el servidor está en un estado intermedio, es seguro pero debe revisar los recursos.
    print("Servidor seguro, revisa recursos")

# Explicación:
# - Aquí combinamos tres variables: uso de CPU, uso de memoria y estado de seguridad.
# - Se utilizan operadores lógicos para hacer una evaluación combinada.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. PIDE AL USUARIO QUE INTRODUZCA EL NOMBRE DEL SERVIDOR.
# 2. SOLICITA EL USO DE CPU Y MEMORIA DEL SERVIDOR.
# 3. VERIFICA SI EL USO DE CPU O MEMORIA ES MAYOR AL 85%. SI LO ES, MUESTRA UNA ALERTA.
# 4. PREGUNTA SI EL SERVIDOR TIENE LAS ACTUALIZACIONES INSTALADAS.
# 5. MUESTRA UN RESUMEN DEL ESTADO DEL SERVIDOR BASADO EN LOS RECURSOS Y SEGURIDAD.
# -------------------------------------------------------------------------------------------

# 1. Pedimos al usuario que introduzca el nombre del servidor.
nombre_servidor = input("Nombre del servidor: ")

# 2. Pedimos el uso de CPU y memoria.
uso_cpu = int(input("Uso de CPU (%): "))
uso_memoria = int(input("Uso de memoria (%): "))

# 3. Verificamos si el uso de CPU o memoria es mayor al 85% y mostramos una alerta.
if uso_cpu > 85 or uso_memoria > 85:
    print(f"Alerta: {nombre_servidor} tiene alto uso de recursos")

# 4. Preguntamos si el servidor tiene actualizaciones instaladas.
actualizaciones = input("Actualizaciones instaladas (sí/no): ").lower()

# 5. Mostramos un resumen del estado del servidor.
print(f"Servidor: {nombre_servidor}")
print(f"CPU: {uso_cpu}%")
print(f"Memoria: {uso_memoria}%")
print(f"Seguridad: {'Actualizado' if actualizaciones == 'sí' else 'No actualizado'}")

# Si el servidor tiene altos recursos y no está actualizado, mostramos advertencia.
if (uso_cpu > 85 or uso_memoria > 85) and actualizaciones == "no":
    print("Advertencia: Alto uso de recursos y sin actualizaciones")
