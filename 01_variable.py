# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: EJEMPLO BÁSICO DE VARIABLES EN PYTHON
# ? LAS VARIABLES EN PYTHON SE UTILIZAN PARA ALMACENAR DATOS. EN ESTE CASO, SIMULAMOS LA GESTIÓN
# ? DE UN SERVIDOR, ALMACENANDO DATOS SOBRE SU NOMBRE, EL USO DE CPU, LA MEMORIA DISPONIBLE Y 
# ? SI ESTÁ ACTIVO O NO.
# -------------------------------------------------------------------------------------------

# DEFINIMOS ALGUNAS VARIABLES QUE REPRESENTAN EL ESTADO DE UN SERVIDOR.
nombre_servidor = "Servidor_1"  # Almacena el nombre del servidor como un texto (string).
cpu_uso = 85.5  # Almacena el porcentaje de uso de CPU como un número decimal (float).
memoria_disponible = 4096  # Almacena la memoria disponible en MB como un número entero (int).
es_activo = True  # Almacena si el servidor está activo o no, usando un valor booleano (True o False).

# IMPRIMIMOS LAS VARIABLES PARA VER SUS VALORES ACTUALES.
# La función `print()` nos permite mostrar información en la consola.
print(f"Nombre del servidor: {nombre_servidor}")
print(f"Uso de CPU: {cpu_uso}%")
print(f"Memoria disponible: {memoria_disponible} MB")
print(f"¿El servidor está activo? {es_activo}")

# SIMULAMOS UNA OPTIMIZACIÓN DEL SERVIDOR MODIFICANDO ALGUNOS VALORES DE LAS VARIABLES.
cpu_uso = 45.2  # Ahora el uso de CPU ha bajado tras la optimización.
memoria_disponible = 8192  # Ahora hay más memoria disponible tras la optimización.

# IMPRIMIMOS NUEVAMENTE LOS VALORES DESPUÉS DE HABER SIDO MODIFICADOS.
print("Después de la optimización del servidor:")
print(f"Nuevo uso de CPU: {cpu_uso}%")
print(f"Nueva memoria disponible: {memoria_disponible} MB")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: VERIFICACIÓN DE TIPOS DE VARIABLES
# ? PYTHON PERMITE TRABAJAR CON DIFERENTES TIPOS DE VARIABLES. PODEMOS USAR LA FUNCIÓN `TYPE()`
# ? PARA VERIFICAR EL TIPO DE DATO DE CADA VARIABLE.
# -------------------------------------------------------------------------------------------

# USAMOS LA FUNCIÓN `TYPE()` PARA VERIFICAR EL TIPO DE CADA VARIABLE.
# Verificar el tipo de la variable `nombre_servidor` que es un texto (string).
print(f"El tipo de nombre_servidor es: {type(nombre_servidor)}")

# Verificar el tipo de la variable `cpu_uso` que es un número decimal (float).
print(f"El tipo de cpu_uso es: {type(cpu_uso)}")

# Verificar el tipo de la variable `memoria_disponible` que es un número entero (int).
print(f"El tipo de memoria_disponible es: {type(memoria_disponible)}")

# Verificar el tipo de la variable `es_activo` que es un valor booleano (True/False).
print(f"El tipo de es_activo es: {type(es_activo)}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: CAMBIO DINÁMICO DE TIPO DE VARIABLES
# ? AQUÍ MOSTRAMOS CÓMO SE PUEDE CAMBIAR EL TIPO DE UNA VARIABLE EN PYTHON DE MANERA DINÁMICA.
# -------------------------------------------------------------------------------------------

# DEFINIMOS UNA VARIABLE CON UN NÚMERO DECIMAL (FLOAT).
cpu_uso = 85.5
print(f"Uso de CPU: {cpu_uso}% (tipo {type(cpu_uso)})")

# CAMBIAMOS EL TIPO DE LA VARIABLE A UN TEXTO (STRING).
cpu_uso = "85.5%"
print(f"Uso de CPU ahora es: {cpu_uso} (tipo {type(cpu_uso)})")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: VARIABLES Y ENTRADA DEL USUARIO
# ? EN ESTA SECCIÓN MOSTRAMOS CÓMO LAS VARIABLES PUEDEN TOMAR VALORES INTRODUCIDOS POR EL USUARIO.
# -------------------------------------------------------------------------------------------

# SOLICITAMOS AL USUARIO QUE INTRODUZCA UN NUEVO NOMBRE PARA EL SERVIDOR.
nuevo_nombre_servidor = input("Introduce el nuevo nombre del servidor: ")

# IMPRIMIMOS EL NUEVO NOMBRE INTRODUCIDO POR EL USUARIO.
print(f"El servidor ha sido renombrado a {nuevo_nombre_servidor}.")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: CONVERSIÓN DE TIPOS A PARTIR DE LA ENTRADA DEL USUARIO
# ? CONVERTIMOS ENTRADAS DEL USUARIO A OTROS TIPOS DE DATOS COMO ENTEROS PARA SU PROCESAMIENTO.
# -------------------------------------------------------------------------------------------

# SOLICITAMOS AL USUARIO EL NÚMERO DE PROCESOS QUE DESEA EJECUTAR.
# Convertimos el valor introducido en un número entero usando `int()`.
numero_procesos = int(input("Introduce el número de procesos que deseas ejecutar en paralelo: "))

# IMPRIMIMOS LA CANTIDAD DE PROCESOS CONFIGURADOS.
print(f"Se configuraron {numero_procesos} procesos para ejecutar en paralelo.")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: USO DE LISTAS Y DICCIONARIOS
# ? DEMOSTRAMOS EL USO DE LISTAS Y DICCIONARIOS EN UN CONTEXTO PRÁCTICO DE ADMINISTRACIÓN DE SISTEMAS.
# -------------------------------------------------------------------------------------------

# EJEMPLO DE LISTA: USUARIOS CONECTADOS EN UN SISTEMA.
usuarios_conectados = ["admin", "user1", "user2", "guest"]

# IMPRIMIMOS LA LISTA DE USUARIOS CONECTADOS.
print(f"Usuarios conectados: {usuarios_conectados}")

# AGREGAMOS UN NUEVO USUARIO A LA LISTA USANDO `APPEND()`.
usuarios_conectados.append("user3")

# IMPRIMIMOS LA LISTA ACTUALIZADA DE USUARIOS.
print(f"Usuarios conectados actualizados: {usuarios_conectados}")

# EJEMPLO DE DICCIONARIO: INFORMACIÓN DEL SERVIDOR.
servidor_info = {
    "nombre": "Servidor_1",  # Nombre del servidor (clave: "nombre").
    "cpu_uso": 75.5,  # Uso de CPU en porcentaje (clave: "cpu_uso").
    "memoria_disponible": 2048,  # Memoria disponible en MB (clave: "memoria_disponible").
    "activo": True  # Estado del servidor, si está activo o no (clave: "activo").
}

# IMPRIMIMOS LA INFORMACIÓN DEL SERVIDOR ALMACENADA EN EL DICCIONARIO.
print(f"Información del servidor: {servidor_info}")


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. CREA UNA VARIABLE QUE ALMACENE EL NOMBRE DE UN SERVIDOR (CADENA DE TEXTO).
# 2. DEFINE UNA LISTA QUE ALMACENE LOS NOMBRES DE DOS SERVICIOS ACTIVOS EN ESE SERVIDOR.
# 3. DEFINE UN DICCIONARIO QUE CONTENGA LOS SIGUIENTES DATOS: NOMBRE DEL SERVIDOR, CANTIDAD DE SERVICIOS, Y SI EL SERVIDOR ESTÁ ACTIVO O NO (BOOLEANO).
# 4. IMPRIME TODOS LOS DATOS ALMACENADOS, INCLUYENDO LA LISTA DE SERVICIOS.
# 5. CAMBIA EL ESTADO DEL SERVIDOR A 'NO ACTIVO' Y ACTUALIZA EL DICCIONARIO.
# -------------------------------------------------------------------------------------------

# CÓDIGO DE AUTOEVALUACIÓN:
# 1. Definir la variable que almacena el nombre del servidor.
nombre_servidor = "Servidor_Autoevaluacion"

# 2. Definir una lista con los nombres de dos servicios activos.
servicios_activos = ["Servicio_Web", "Servicio_BD"]

# 3. Definir un diccionario que almacene el nombre del servidor, la cantidad de servicios y el estado del servidor.
servidor_info = {
    "nombre": nombre_servidor,
    "cantidad_servicios": len(servicios_activos),  # Usamos `len()` para contar los elementos de la lista.
    "activo": True
}

# 4. Imprimir todos los datos almacenados.
print(f"Nombre del servidor: {servidor_info['nombre']}")
print(f"Cantidad de servicios: {servidor_info['cantidad_servicios']}")
print(f"Servicios activos: {servicios_activos}")
print(f"¿El servidor está activo? {servidor_info['activo']}")

# 5. Cambiar el estado del servidor a 'no activo' y actualizar el diccionario.
servidor_info["activo"] = False
print("El estado del servidor ha sido actualizado a: No activo.")
print(f"Estado actual del servidor: {servidor_info['activo']}")
