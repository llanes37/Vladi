# -------------------------------------------------------------------------------------------
# SISTEMA DE GESTIÓN DE SERVIDORES - VERSIÓN PARA EL PROFESOR
# Este archivo contiene un ejemplo completo que integra variables, condicionales, bucles
# y funciones. Permite gestionar servidores simulados y realizar acciones como optimización
# y reinicio de servidores.
# -------------------------------------------------------------------------------------------

# * SECCIÓN 1: DEFINICIÓN DE VARIABLES Y LISTAS
# Definir una lista de servidores con sus estados iniciales.
servidores = [
    {"nombre": "Servidor_1", "cpu": 90, "memoria": 2048, "activo": True},
    {"nombre": "Servidor_2", "cpu": 50, "memoria": 4096, "activo": True},
    {"nombre": "Servidor_3", "cpu": 95, "memoria": 1024, "activo": False},
]

# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: FUNCIONES

# Función para mostrar el estado de todos los servidores.
def mostrar_estado_servidores(servidores):
    print("\n=== ESTADO DE LOS SERVIDORES ===")
    for servidor in servidores:
        print(f"Nombre: {servidor['nombre']} - CPU: {servidor['cpu']}% - Memoria: {servidor['memoria']}MB - Activo: {servidor['activo']}")
    print("=" * 40)

# Función para optimizar un servidor.
def optimizar_servidor(servidor):
    if servidor["activo"]:
        servidor["cpu"] -= 10  # Reducimos la carga de CPU.
        servidor["memoria"] += 1024  # Aumentamos la memoria disponible.
        print(f"{servidor['nombre']} optimizado correctamente.")
    else:
        print(f"{servidor['nombre']} no está activo. No se puede optimizar.")

# Función para verificar el estado de los servidores y tomar acciones.
def verificar_servidores(servidores):
    print("\n=== VERIFICANDO SERVIDORES ===")
    for servidor in servidores:
        if servidor["cpu"] > 85:
            print(f"¡Alerta! {servidor['nombre']} tiene alta carga de CPU.")
            optimizar_servidor(servidor)
        elif not servidor["activo"]:
            print(f"{servidor['nombre']} está inactivo. Se recomienda reiniciarlo.")

# Función para reiniciar un servidor.
def reiniciar_servidor(servidor):
    if not servidor["activo"]:
        servidor["activo"] = True
        servidor["cpu"] = 50  # Restablecemos la carga de CPU.
        servidor["memoria"] = 2048  # Restablecemos la memoria.
        print(f"{servidor['nombre']} ha sido reiniciado.")
    else:
        print(f"{servidor['nombre']} ya está activo.")

# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: INTERACCIÓN DEL USUARIO
# Función principal del sistema.
def sistema_gestion():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar estado de los servidores")
        print("2. Verificar servidores")
        print("3. Reiniciar un servidor")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_estado_servidores(servidores)
        elif opcion == "2":
            verificar_servidores(servidores)
        elif opcion == "3":
            nombre_servidor = input("Introduce el nombre del servidor a reiniciar: ")
            for servidor in servidores:
                if servidor["nombre"] == nombre_servidor:
                    reiniciar_servidor(servidor)
                    break
            else:
                print("Servidor no encontrado.")
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Llamada a la función principal para iniciar el sistema.
sistema_gestion()
