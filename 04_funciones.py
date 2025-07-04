# -------------------------------------------------------------------------------------------
# En Python, una función es un bloque de código que se ejecuta solo cuando es llamada.
# Las funciones nos permiten dividir el código en piezas más pequeñas y reutilizables.
# Esto es particularmente útil en sistemas de administración donde algunas tareas se deben
# realizar repetidamente, como monitorear servidores, gestionar usuarios o revisar servicios.
# Aquí te mostramos ejemplos de funciones aplicadas en administración de sistemas.
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: FUNCIÓN BÁSICA PARA SALUDAR A UN OFICIAL DE SISTEMAS
# ? ESTA FUNCIÓN PIDE AL USUARIO SU NOMBRE Y RANGO, Y DEVUELVE UN MENSAJE DE BIENVENIDA.
# -------------------------------------------------------------------------------------------
def saludar():
    # ? Solicitar al oficial su rango y nombre
    oficial = input("Introduce tu rango y nombre: ")
    
    # * Devolver el mensaje de bienvenida
    return f"Bienvenido al sistema, {oficial}. Preparado para el servicio."

# Llamada a la función para probarla
print(saludar())

# Explicación:
# - Esta función es sencilla y permite solicitar información al usuario.
# - Utiliza `input()` para capturar la entrada del usuario.
# - El mensaje de salida incluye el rango y nombre que el usuario ha introducido.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: FUNCIÓN PARA CALCULAR EL USO DE RECURSOS (CPU Y MEMORIA)
# ? ESTA FUNCIÓN PIDE EL USO ACTUAL DE CPU Y MEMORIA DEL SERVIDOR, CON LA POSIBILIDAD DE USAR UN VALOR POR DEFECTO PARA LA MEMORIA.
# -------------------------------------------------------------------------------------------
def calcular_uso_recursos():
    # ? Solicitar el uso de CPU al usuario
    cpu = int(input("Introduce el uso de CPU en porcentaje: "))
    
    # ? Solicitar el uso de memoria o usar un valor por defecto si el usuario no introduce nada
    memoria = input("Introduce la memoria disponible en MB (o presiona enter para usar 2048MB): ")
    
    # * Si el usuario no introduce nada, asignar 2048 como valor por defecto
    if memoria == "":
        memoria = 2048  # Valor por defecto si no se ingresa un valor
    else:
        memoria = int(memoria)  # Convertir la entrada a entero
    
    # * Devolver el estado del sistema con el uso de CPU y memoria
    return f"El uso actual de CPU es {cpu}% y la memoria disponible es {memoria} MB."

# Llamada a la función para probarla
print(calcular_uso_recursos())

# Explicación:
# - Esta función utiliza una combinación de `input()` y `if-else`.
# - Es útil cuando queremos ofrecer una opción predeterminada, como la memoria disponible.
# - `return` se utiliza para devolver un resultado que luego puede imprimirse o utilizarse en otras partes del programa.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: FUNCIÓN PARA GESTIONAR USUARIOS DEL SISTEMA
# ? ESTA FUNCIÓN PERMITE VERIFICAR SI UN USUARIO TIENE PRIVILEGIOS DE ADMINISTRADOR O NO.
# -------------------------------------------------------------------------------------------
def gestionar_usuario():
    # ? Solicitar el nombre del usuario
    usuario = input("Introduce el nombre del usuario: ")
    
    # ? Preguntar si el usuario es administrador
    es_administrador = input("¿El usuario es administrador? (s/n): ").lower() == 's'
    
    # * Retornar el mensaje según los privilegios del usuario
    if es_administrador:
        return f"El usuario {usuario} tiene privilegios de administrador. Acceso completo al sistema."
    else:
        return f"El usuario {usuario} es un usuario estándar. Acceso limitado."

# Llamada a la función para probarla
print(gestionar_usuario())

# Explicación:
# - Esta función demuestra cómo capturar respuestas y cómo utilizarlas para decidir qué acción tomar.
# - `lower()` se utiliza para normalizar la entrada y aceptar tanto 'S' como 's'.
# - `if-else` se usa para devolver diferentes mensajes dependiendo de la respuesta del usuario.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: FUNCIÓN PARA COMPROBAR EL ESTADO DE LOS SERVICIOS CRÍTICOS
# ? ESTA FUNCIÓN ITERA SOBRE UNA LISTA DE SERVICIOS CRÍTICOS Y LOS COMPRUEBA UNO A UNO.
# -------------------------------------------------------------------------------------------
def comprobar_servicios():
    # ? Lista de servicios críticos que deben estar en funcionamiento
    servicios_criticos = ["SSH", "VPN", "Firewall", "DNS"]
    
    # * Iterar sobre los servicios y comprobar su estado
    for servicio in servicios_criticos:
        print(f"Comprobando el estado del servicio {servicio}...")

# Llamada a la función para probarla
comprobar_servicios()

# Explicación:
# - Usamos un bucle `for` para iterar sobre una lista de servicios.
# - Esto es útil para tareas de monitoreo donde se necesita revisar el estado de múltiples servicios.
# - La lista "servicios_criticos" puede ajustarse según los servicios que se deben verificar.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: MONITORIZAR SERVIDORES EN LA RED
# ? ESTA FUNCIÓN SOLICITA EL ESTADO DE VARIOS SERVIDORES Y REGISTRA CUÁLES ESTÁN DISPONIBLES.
# -------------------------------------------------------------------------------------------
def monitorizar_servidores():
    # ? Lista de direcciones IP de servidores en la red
    servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    
    # * Lista para almacenar los servidores disponibles
    servidores_disponibles = []
    
    # ? Iterar sobre los servidores y comprobar si están disponibles
    for servidor in servidores:
        disponible = input(f"¿El servidor {servidor} está disponible? (s/n): ").lower()
        if disponible == 's':
            servidores_disponibles.append(servidor)
        else:
            print(f"¡Atención! El servidor {servidor} no está disponible.")
    
    # * Mostrar la lista de servidores disponibles
    print(f"Servidores disponibles: {servidores_disponibles}")

# Llamada a la función para probarla
monitorizar_servidores()

# Explicación:
# - Este es un ejemplo de cómo realizar un monitoreo simple de servidores en una red.
# - Al igual que la función de servicios, esta función utiliza un bucle `for` para iterar sobre una lista.
# - La lista de servidores disponibles se va llenando conforme se confirma la disponibilidad de cada uno.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: FUNCIÓN PARA SUMAR DOS NÚMEROS
# ? ESTA FUNCIÓN RECIBE DOS PARÁMETROS 'A' Y 'B', Y DEVUELVE EL RESULTADO DE LA SUMA.
# -------------------------------------------------------------------------------------------
def sumar(a, b):
    # ? Suma de los dos números
    resultado = a + b
    return resultado

# Llamada a la función con valores fijos
print(sumar(10, 5))

# Explicación:
# - Esta función demuestra cómo pasar parámetros a una función y devolver un resultado.
# - `a` y `b` son los parámetros que se pasan al llamar a la función.
# - El resultado de la suma se almacena en `resultado` y luego se devuelve con `return`.

# -------------------------------------------------------------------------------------------
# * SECCIÓN 7: FUNCIÓN QUE LLAMA A OTRAS FUNCIONES
# ? ESTA FUNCIÓN SIRVE COMO EJEMPLO DE CÓMO UNA FUNCIÓN PUEDE LLAMAR A OTRAS FUNCIONES.
# -------------------------------------------------------------------------------------------
def proceso_completo():
    print("Inicio del proceso...")
    
    # Llamar a las funciones anteriores dentro de esta función
    print(saludar())
    print(calcular_uso_recursos())
    gestionar_usuario()
    
    # Comprobar servicios y monitorizar servidores
    comprobar_servicios()
    monitorizar_servidores()
    
    print("Proceso completo.")

# Llamada a la función que ejecuta todo el proceso
proceso_completo()

# Explicación:
# - Esta función integra todas las funciones anteriores para demostrar cómo una función puede
#   ser utilizada como punto de control o "workflow" para un conjunto de tareas.
# - En un escenario real, esto podría utilizarse para automatizar procesos largos o complejos
#   en un sistema, como una auditoría o verificación diaria.

# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# 1. CREA UNA FUNCIÓN QUE SOLICITE EL NOMBRE DEL SERVIDOR Y LO GUARDE EN UNA VARIABLE.
# 2. SOLICITA EL USO DE CPU Y EL USO DE MEMORIA DEL SERVIDOR (OFRECE UN VALOR POR DEFECTO SI NO SE INTRODUCE NADA).
# 3. SOLICITA EL ESTADO DE VARIOS SERVICIOS Y GUARDA LOS QUE ESTÉN ACTIVOS.
# 4. SOLICITA EL ESTADO DE VARIOS SERVIDORES Y ALMACENA LOS QUE ESTÉN DISPONIBLES.
# 5. IMPRIME UN RESUMEN FINAL CON EL NOMBRE DEL SERVIDOR, USO DE CPU Y MEMORIA, SERVICIOS ACTIVOS, Y SERVIDORES DISPONIBLES.
# -------------------------------------------------------------------------------------------

# CÓDIGO DE AUTOEVALUACIÓN:
def autoevaluacion():
    # 1. Solicitar el nombre del servidor
    servidor_nombre = input("Introduce el nombre del servidor: ")

    # 2. Solicitar uso de CPU y memoria (con valor por defecto para memoria)
    cpu = int(input("Introduce el uso de CPU en porcentaje: "))
    memoria = input("Introduce la memoria disponible en MB (presiona enter para usar 2048MB): ")
    if memoria == "":
        memoria = 2048
    else:
        memoria = int(memoria)

    # 3. Solicitar estado de servicios
    servicios = ["SSH", "VPN", "Firewall", "DNS"]
    servicios_activos = []
    for servicio in servicios:
        estado = input(f"¿El servicio {servicio} está activo? (s/n): ").lower()
        if estado == 's':
            servicios_activos.append(servicio)

    # 4. Solicitar estado de servidores
    servidores = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    servidores_disponibles = []
    for servidor in servidores:
        disponible = input(f"¿El servidor {servidor} está disponible? (s/n): ").lower()
        if disponible == 's':
            servidores_disponibles.append(servidor)

    # 5. Imprimir el resumen final
    print("\n=== RESUMEN DEL SISTEMA ===")
    print(f"Servidor: {servidor_nombre}")
    print(f"Uso de CPU: {cpu}%")
    print(f"Memoria disponible: {memoria} MB")
    print(f"Servicios activos: {servicios_activos}")
    print(f"Servidores disponibles: {servidores_disponibles}")

# Llamada a la autoevaluación
autoevaluacion()

# Explicación:
# - Esta autoevaluación junta todos los conceptos de funciones que hemos visto.
# - Permite al alumno practicar funciones con entrada y salida, bucles, condicionales y almacenamiento de datos.
# - Además, se integra en un contexto de administración de sistemas, lo que la hace práctica y relevante.
