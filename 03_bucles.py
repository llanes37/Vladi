# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: EJEMPLO BÁSICO DE BUCLES FOR EN PYTHON
# ? LOS BUCLES FOR PERMITEN ITERAR SOBRE UN RANGO O UNA COLECCIÓN DE ELEMENTOS, COMO LISTAS.
# ? SON IDEALES CUANDO CONOCEMOS EL NÚMERO DE VECES QUE QUEREMOS REPETIR UNA OPERACIÓN.
# -------------------------------------------------------------------------------------------

# * BUCLE FOR: ITERANDO SOBRE UN RANGO DE NÚMEROS
# ? ESTE EJEMPLO SIMULA LA COMPROBACIÓN DE LA DISPONIBILIDAD DE SERVIDORES DEL 1 AL 5.
# ? RANGE(1, 6) GENERA UNA SECUENCIA DE NÚMEROS DEL 1 AL 5.
for servidor in range(1, 6):  # Iteramos desde el servidor 1 hasta el servidor 5.
    print(f"Comprobando disponibilidad del servidor {servidor}...")

# Explicación:
# - Usamos el bucle for para repetir el bloque de código 5 veces.
# - En cada iteración, la variable "servidor" toma un valor del 1 al 5.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: BUCLE FOR CON LISTAS
# ? PODEMOS UTILIZAR LOS BUCLES FOR PARA ITERAR SOBRE ELEMENTOS DE UNA LISTA. 
# ? ESTE EJEMPLO SIMULA LA COMPROBACIÓN DEL ESTADO DE SERVICIOS EN UN SERVIDOR.
# -------------------------------------------------------------------------------------------

# * LISTA DE SERVICIOS QUE QUEREMOS MONITOREAR
servicios = ["SSH", "Apache", "MySQL", "FTP", "Firewall"]

for servicio in servicios:  # Iteramos sobre la lista de servicios.
    print(f"Comprobando estado del servicio: {servicio}")

# Explicación:
# - En cada iteración, la variable "servicio" toma un valor de la lista.
# - Usamos el bucle for para comprobar cada servicio.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: BUCLE FOR CON ÍNDICE USANDO ENUMERATE()
# ? A VECES NECESITAMOS TANTO EL ÍNDICE COMO EL VALOR AL ITERAR SOBRE UNA LISTA.
# ? CON ENUMERATE(), OBTENEMOS EL ÍNDICE Y EL VALOR SIMULTÁNEAMENTE.
# -------------------------------------------------------------------------------------------

# * ENUMERAMOS UNA LISTA DE SERVICIOS Y MOSTRAMOS SU ÍNDICE.
for indice, servicio in enumerate(servicios):
    print(f"Servicio {indice + 1}: {servicio}")

# Explicación:
# - "enumerate()" devuelve el índice y el valor.
# - Esto es útil para numerar elementos durante la iteración.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: BUCLE WHILE
# ? EL BUCLE WHILE SE UTILIZA CUANDO NO SABEMOS CUÁNTAS VECES SE DEBE REPETIR EL BUCLE. 
# ? CONTINÚA EJECUTÁNDOSE MIENTRAS UNA CONDICIÓN SEA VERDADERA.
# -------------------------------------------------------------------------------------------

# * SIMULAMOS EL MONITOREO DE UN ARCHIVO DE LOGS HASTA QUE DETECTAMOS UN ERROR.
logs = ["Inicio del sistema", "Conexión SSH establecida", "Actualización exitosa", "Error: Base de datos desconectada"]

i = 0  # Inicializamos el índice en 0.
while i < len(logs):  # Mientras haya más logs por procesar...
    log = logs[i]  # Tomamos el log actual.
    print(f"Monitoreo de logs: {log}")
    if "Error" in log:  # Si encontramos un error...
        print("¡Se ha detectado un error en el sistema! Revisar inmediatamente.")
        break  # Salimos del bucle cuando encontramos un error.
    i += 1  # Incrementamos el índice para pasar al siguiente log.

# Explicación:
# - Usamos un bucle while para monitorear los logs hasta encontrar un error.
# - El bucle continúa hasta que se encuentra un log que contiene la palabra "Error".


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: BUCLE WHILE CON UNA CONDICIÓN EXTERNA
# ? ESTE EJEMPLO SIMULA LA MONITORIZACIÓN DE LA CARGA DEL CPU DE UN SERVIDOR HASTA QUE LLEGUE A UN NIVEL ACEPTABLE.
# -------------------------------------------------------------------------------------------

# * SUPONEMOS QUE LA CARGA INICIAL DEL CPU ES DEL 95%
carga_cpu = 95

while carga_cpu > 75:  # Mientras la carga sea mayor a 75%, seguimos monitoreando.
    print(f"Carga del CPU: {carga_cpu}% - ¡Alerta! Carga alta.")
    carga_cpu -= 5  # Simulamos que la carga del CPU disminuye.

print(f"Carga del CPU bajo control: {carga_cpu}%. Sistema estable.")

# Explicación:
# - El bucle while continúa ejecutándose mientras la carga del CPU sea mayor al 75%.
# - El valor de la variable "carga_cpu" disminuye en cada iteración, simulando una mejora en el rendimiento.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: EJEMPLO AVANZADO: GESTIÓN DE USUARIOS CONECTADOS A UN SERVIDOR
# ? SUPONGAMOS QUE TENEMOS UNA LISTA DE USUARIOS Y NECESITAMOS REALIZAR UNA ACCIÓN SEGÚN SI ESTÁN CONECTADOS O NO.
# -------------------------------------------------------------------------------------------

# * LISTA DE USUARIOS Y SU ESTADO DE CONEXIÓN
usuarios = [
    {"nombre": "Ana", "conectado": True},
    {"nombre": "Luis", "conectado": False},
    {"nombre": "Pedro", "conectado": True},
    {"nombre": "Marta", "conectado": False},
]

for usuario in usuarios:
    if usuario["conectado"]:
        print(f"Usuario {usuario['nombre']} está conectado. Enviando notificación de mantenimiento.")
    else:
        print(f"Usuario {usuario['nombre']} no está conectado. Omitiendo.")

# Explicación:
# - Usamos un bucle for para iterar sobre una lista de diccionarios, donde cada diccionario representa un usuario.
# - Dependiendo del estado del usuario (conectado o no), realizamos una operación diferente.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 7: AUTOMATIZACIÓN DE COPIAS DE SEGURIDAD
# ? SUPONGAMOS QUE NECESITAMOS REALIZAR COPIAS DE SEGURIDAD PARA UNA LISTA DE SERVIDORES.
# -------------------------------------------------------------------------------------------

# * LISTA DE SERVIDORES PARA LOS QUE VAMOS A REALIZAR COPIAS DE SEGURIDAD
servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for servidor in servidores:
    print(f"Iniciando copia de seguridad en el servidor {servidor}...")
    # Aquí podríamos ejecutar comandos de copia de seguridad.
    print(f"Copia de seguridad en el servidor {servidor} completada.")

# Explicación:
# - Simulamos el proceso de realizar una copia de seguridad en varios servidores.
# - En cada iteración, realizamos una operación diferente en cada servidor.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. CREA UNA LISTA QUE ALMACENE 3 DIRECCIONES IP DE SERVIDORES.
# 2. USA UN BUCLE FOR PARA REALIZAR UNA "VERIFICACIÓN" EN CADA SERVIDOR.
# 3. CREA UNA VARIABLE QUE REPRESENTE LA CARGA INICIAL DEL CPU DE UN SERVIDOR.
# 4. UTILIZA UN BUCLE WHILE PARA SIMULAR LA REDUCCIÓN GRADUAL DE LA CARGA DEL CPU HASTA UN NIVEL ACEPTABLE (75%).
# 5. IMPRIME EL RESULTADO FINAL CUANDO LA CARGA DEL CPU SEA SEGURA.
# -------------------------------------------------------------------------------------------

# CÓDIGO DE AUTOEVALUACIÓN:
# 1. Definir una lista con 3 direcciones IP de servidores.
servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

# 2. Usar un bucle for para simular una verificación en cada servidor.
for servidor in servidores:
    print(f"Verificando estado del servidor {servidor}...")

# 3. Definir una variable que representa la carga inicial del CPU (90%).
carga_cpu = 90

# 4. Utilizar un bucle while para reducir la carga del CPU.
while carga_cpu > 75:
    print(f"Carga actual del CPU: {carga_cpu}% - ¡Alerta! Reduciendo carga.")
    carga_cpu -= 5

# 5. Imprimir el mensaje final cuando la carga del CPU sea segura.
print(f"Carga del CPU bajo control: {carga_cpu}%. Sistema estable.")
