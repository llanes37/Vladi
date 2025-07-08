# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: LISTAS EN PYTHON
# ? Las listas son colecciones ordenadas que pueden almacenar múltiples elementos en una sola variable.
# ? En administración de sistemas, las listas pueden usarse para almacenar registros de usuarios conectados o servicios activos.
# -------------------------------------------------------------------------------------------

# * Ejemplo básico: Lista de usuarios conectados
# Creamos una lista llamada "usuarios_conectados" que almacena los nombres de los usuarios conectados a un servidor.

usuarios_conectados = ["admin", "user1", "user2", "user3"]

# * Acceder a elementos de la lista
# Podemos acceder a los elementos de una lista usando el índice. Los índices empiezan desde 0.

print(f"Primer usuario conectado: {usuarios_conectados[0]}")  # Imprimimos el primer usuario
print(f"Último usuario conectado: {usuarios_conectados[-1]}")  # Imprimimos el último usuario

# * Modificar elementos de una lista
# Podemos cambiar el valor de un elemento de la lista accediendo a su índice.

usuarios_conectados[1] = "user5"
print(f"Usuarios conectados después de la modificación: {usuarios_conectados}")

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: DICCIONARIOS EN PYTHON
# ? Los diccionarios permiten almacenar pares de clave-valor. Son útiles cuando necesitamos relacionar elementos.
# ? En administración de sistemas, los diccionarios pueden usarse para guardar información clave sobre un servidor.
# -------------------------------------------------------------------------------------------

# * Ejemplo básico: Información de un servidor
# Creamos un diccionario llamado "info_servidor" que almacena el nombre, la IP y el estado de un servidor.

info_servidor = {
    "nombre": "Servidor_1",
    "IP": "192.168.1.100",
    "estado": "activo"
}

# * Acceder a los valores del diccionario
# Para acceder a un valor en el diccionario, usamos la clave.

print(f"Nombre del servidor: {info_servidor['nombre']}")
print(f"IP del servidor: {info_servidor['IP']}")

# * Modificar valores en el diccionario
# Podemos cambiar los valores asignados a una clave.

info_servidor["estado"] = "en mantenimiento"
print(f"Estado actual del servidor: {info_servidor['estado']}")

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: BUCLES ANIDADOS
# ? Un bucle anidado es un bucle dentro de otro bucle. Se utiliza cuando necesitamos trabajar con estructuras de datos más complejas.
# -------------------------------------------------------------------------------------------

# * Ejemplo: Combinación de listas y diccionarios
# Vamos a crear una lista de diccionarios que almacena información sobre varios servidores y sus servicios.

servidores = [
    {
        "nombre": "Servidor_1",
        "IP": "192.168.1.101",
        "servicios": ["Apache", "MySQL", "SSH"]
    },
    {
        "nombre": "Servidor_2",
        "IP": "192.168.1.102",
        "servicios": ["FTP", "DNS", "VPN"]
    }
]

# * Usamos bucles anidados para recorrer cada servidor y sus servicios
for servidor in servidores:
    print(f"\nServicios del {servidor['nombre']} ({servidor['IP']}):")
    
    for servicio in servidor["servicios"]:
        print(f"- {servicio}")

# Explicación:
# - El primer bucle itera sobre cada servidor en la lista.
# - El segundo bucle itera sobre la lista de servicios de cada servidor.

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. Crea una lista de diccionarios, donde cada diccionario contenga la información de un servidor (nombre, IP y lista de servicios).
# 2. Utiliza un bucle anidado para iterar sobre los servidores y sus servicios.
# 3. Modifica el estado de un servicio en un servidor específico y muestra los cambios.
# -------------------------------------------------------------------------------------------

# * Resolución de la autoevaluación:

# Paso 1: Crear la lista de diccionarios
servidores_red = [
    {
        "nombre": "Servidor_A",
        "IP": "192.168.1.10",
        "servicios": ["HTTP", "SSH", "DNS"]
    },
    {
        "nombre": "Servidor_B",
        "IP": "192.168.1.11",
        "servicios": ["FTP", "VPN", "MySQL"]
    }
]

# Paso 2: Usar bucles anidados para iterar sobre los servidores y sus servicios
for servidor in servidores_red:
    print(f"\nServicios del {servidor['nombre']} ({servidor['IP']}):")
    for servicio in servidor["servicios"]:
        print(f"- {servicio}")

# Paso 3: Modificar el estado de un servicio en un servidor específico
# Supongamos que necesitamos cambiar "FTP" por "SFTP" en el Servidor_B
for servidor in servidores_red:
    if servidor["nombre"] == "Servidor_B":
        index = servidor["servicios"].index("FTP")  # Encontramos el índice del servicio "FTP"
        servidor["servicios"][index] = "SFTP"  # Cambiamos "FTP" por "SFTP"

# Verificar la modificación
print("\nDespués de modificar el servicio FTP en el Servidor_B:")
for servidor in servidores_red:
    print(f"\nServicios del {servidor['nombre']} ({servidor['IP']}):")
    for servicio in servidor["servicios"]:
        print(f"- {servicio}")
