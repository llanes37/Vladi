# ==============================================================================
# REPASO COMPLETO DE PYTHON - MENÚ INTERACTIVO
# ==============================================================================
# Este archivo contiene un resumen de los conceptos fundamentales de Python
# organizados en un menú para que puedas ejecutar y repasar cada tema por separado.
# ==============================================================================

import os
import sqlite3
import math
from random import randint

# === TEMA 1: VARIABLES Y TIPOS DE DATOS ===
def tema_1_variables():
    print("--- 1. Variables y Tipos de Datos ---")
    # Tipos numéricos
    numero_entero = 10         # int
    numero_flotante = 10.5     # float
    numero_complejo = 1 + 2j   # complex

    # Tipo de texto
    cadena_texto = "Hola, Python" # str

    # Tipo booleano
    es_verdadero = True        # bool (True o False)

    # Tipos de secuencia
    lista = [1, "manzana", 3.14] # list (mutable)
    tupla = (1, "manzana", 3.14) # tuple (inmutable)

    # Tipo de mapeo
    diccionario = {"nombre": "Juan", "edad": 30} # dict

    # Tipos de conjunto
    conjunto = {1, 2, 3, 4}      # set (elementos únicos y desordenados)

    print(f"Entero: {numero_entero} (Tipo: {type(numero_entero)})")
    print(f"Cadena: '{cadena_texto}' (Tipo: {type(cadena_texto)})")
    print(f"Lista: {lista} (Tipo: {type(lista)})")
    print(f"Diccionario: {diccionario} (Tipo: {type(diccionario)})")
    print("-" * 20 + "\\n")

# === TEMA 2: CONDICIONALES ===
def tema_2_condicionales():
    print("--- 2. Condicionales ---")
    try:
        edad_str = input("Introduce tu edad: ")
        edad = int(edad_str)
        if edad < 18:
            print("Eres menor de edad.")
        elif edad == 18:
            print("Justo tienes 18 años.")
        else:
            print("Eres mayor de edad.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
    print("-" * 20 + "\\n")

# === TEMA 3: BUCLES ===
def tema_3_bucles():
    print("--- 3. Bucles ---")
    # Bucle 'for': itera sobre una secuencia (lista, tupla, string, etc.).
    print("Bucle for con una lista:")
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(f"- {fruta}")

    # Bucle 'while': se ejecuta mientras una condición sea verdadera.
    print("\\nBucle while:")
    contador = 0
    while contador < 3:
        print(f"Contador: {contador}")
        contador += 1
    print("-" * 20 + "\\n")

# === TEMA 4: FUNCIONES ===
def tema_4_funciones():
    print("--- 4. Funciones ---")
    def saludar(nombre):
        """Esta función recibe un nombre y devuelve un saludo."""
        return f"¡Hola, {nombre}!"

    # Llamada a la función
    mensaje = saludar("Ana")
    print(mensaje)

    # Función con parámetros por defecto
    def potencia(base, exponente=2):
        """Calcula la potencia de un número. El exponente por defecto es 2."""
        return base ** exponente

    print(f"5 al cuadrado es: {potencia(5)}")
    print(f"2 al cubo es: {potencia(2, 3)}")
    print("-" * 20 + "\\n")

# === TEMA 5: LISTAS, DICCIONARIOS Y BUCLES ANIDADOS ===
def tema_5_estructuras_datos():
    print("--- 5. Estructuras de Datos y Bucles Anidados ---")
    # Listas: colección ordenada y mutable.
    numeros = [1, 2, 3, 4, 5]
    numeros.append(6) # Añadir al final
    print(f"Lista de números: {numeros}")
    print(f"El primer elemento es: {numeros[0]}")

    # Diccionarios: colección de pares clave-valor, desordenada y mutable.
    estudiante = {
        "nombre": "Carlos",
        "edad": 22,
        "cursos": ["Cálculo", "Física", "Programación"]
    }
    print(f"Información del estudiante: {estudiante}")
    print(f"Cursos de {estudiante['nombre']}: {estudiante['cursos']}")

    # Bucles anidados: un bucle dentro de otro.
    print("\\nTabla de multiplicar del 1 al 3 (ejemplo de bucle anidado):")
    for i in range(1, 4):
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}", end="\\t")
        print() # Nueva línea para la siguiente tabla
    print("-" * 20 + "\\n")

# === TEMA 6: PROGRAMACIÓN ORIENTADA A OBJETOS (POO) ===
def tema_6_poo():
    print("--- 6. Programación Orientada a Objetos (POO) ---")
    class Vehiculo:
        # Constructor: se ejecuta al crear un objeto
        def __init__(self, marca, modelo):
            self.marca = marca   # Atributo de instancia
            self.modelo = modelo # Atributo de instancia
            self.encendido = False

        # Método de instancia
        def arrancar(self):
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")

        def describir(self):
            return f"Vehículo: {self.marca} {self.modelo}"

    # Herencia: una clase (hija) hereda atributos y métodos de otra (padre).
    class Coche(Vehiculo):
        def __init__(self, marca, modelo, numero_puertas):
            # Llamamos al constructor de la clase padre
            super().__init__(marca, modelo)
            self.numero_puertas = numero_puertas

        # Sobrescribimos un método de la clase padre
        def describir(self):
            return f"Coche de {self.numero_puertas} puertas: {self.marca} {self.modelo}"

    # Creación de objetos (instanciación)
    mi_coche = Coche("Toyota", "Corolla", 4)
    mi_coche.arrancar()
    print(mi_coche.describir())
    print("-" * 20 + "\\n")

# === TEMA 7: MANEJO DE EXCEPCIONES ===
def tema_7_excepciones():
    print("--- 7. Manejo de Excepciones ---")
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    finally:
        # Este bloque se ejecuta siempre, haya error o no.
        print("La operación de división ha finalizado.")
    print("-" * 20 + "\\n")

# === TEMA 8: MÓDULOS Y LIBRERÍAS ===
def tema_8_modulos():
    print("--- 8. Módulos y Librerías ---")
    # Importar un módulo completo de la librería estándar
    print(f"La raíz cuadrada de 16 es: {math.sqrt(16)}")

    # Importar una función específica de un módulo
    numero_aleatorio = randint(1, 10)
    print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")
    print("-" * 20 + "\\n")

# === TEMA 9: ENTRADA/SALIDA DE ARCHIVOS ===
def tema_9_archivos():
    print("--- 9. Entrada/Salida de Archivos ---")
    # Escribir en un archivo
    try:
        with open("repaso.txt", "w") as archivo:
            archivo.write("Esta es una línea escrita desde Python.\\n")
            archivo.write("Esta es otra línea.\\n")
        print("Archivo 'repaso.txt' creado y escrito con éxito.")

        # Leer un archivo
        with open("repaso.txt", "r") as archivo:
            contenido = archivo.read()
        print("\\nContenido del archivo:")
        print(contenido)

    except IOError as e:
        print(f"Ocurrió un error de E/S: {e}")
    finally:
        # Limpieza (opcional): borrar el archivo creado
        if os.path.exists("repaso.txt"):
            os.remove("repaso.txt")
            print("\\nArchivo de prueba 'repaso.txt' eliminado.")
    print("-" * 20 + "\\n")

# === TEMA 11: AUTOMATIZACIÓN DE TAREAS DEL SISTEMA ===
def tema_11_automatizacion():
    print("--- 11. Automatización de Tareas ---")
    # Obtener el directorio de trabajo actual
    directorio_actual = os.getcwd()
    print(f"Directorio de trabajo actual: {directorio_actual}")

    # Listar archivos en el directorio
    print("\\nArchivos en el directorio actual (primeros 5):")
    try:
        archivos = os.listdir(directorio_actual)
        for archivo in archivos[:5]:
            print(f"- {archivo}")
    except Exception as e:
        print(f"No se pudieron listar los archivos: {e}")
    print("-" * 20 + "\\n")

# === TEMA 12: INTRODUCCIÓN A BASES DE DATOS ===
def tema_12_bases_datos():
    print("--- 12. Bases de Datos con sqlite3 ---")
    db_file = "repaso_db.sqlite"
    conn = None # Inicializar conn a None
    try:
        # Conexión a una base de datos
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Crear una tabla
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')

        # Insertar datos
        cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, email) VALUES (?, ?, ?)", (1, "Alice", "alice@example.com"))
        cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, email) VALUES (?, ?, ?)", (2, "Bob", "bob@example.com"))
        conn.commit()
        print("Tabla 'usuarios' creada y datos insertados.")

        # Consultar datos
        print("\\nUsuarios en la base de datos:")
        cursor.execute("SELECT * FROM usuarios")
        for fila in cursor.fetchall():
            print(f"- ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}")

    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
    finally:
        if conn:
            conn.close()
        if os.path.exists(db_file):
            os.remove(db_file)
            print(f"\\nBase de datos de prueba '{db_file}' eliminada.")
    print("-" * 20 + "\\n")

# === TEMA 13: TESTING Y DEBUGGING ===
def tema_13_testing():
    print("--- 13. Testing y Debugging ---")
    # Ejemplo de una función para probar
    def sumar(a, b):
        """Suma dos números."""
        return a + b

    # Testing simple con 'assert'
    print("Probando la función 'sumar':")
    assert sumar(2, 2) == 4
    assert sumar(-1, 1) == 0
    print("¡Todos los tests de 'sumar' pasaron!")

    # Ejemplo de debugging con print
    def dividir(a, b):
        print(f"DEBUG: 'a' es {a}, 'b' es {b}")
        if b == 0:
            print("DEBUG: 'b' es cero, se devolverá un error.")
            return "Error: no se puede dividir por cero"
        resultado = a / b
        print(f"DEBUG: el resultado es {resultado}")
        return resultado

    print("\\nEjemplo de debugging:")
    dividir(10, 2)
    dividir(5, 0)
    print("-" * 20 + "\\n")

# === MENÚ PRINCIPAL ===
def mostrar_menu():
    print("======================================")
    print("  MENÚ DE REPASO DE PYTHON")
    print("======================================")
    print("1.  Variables y Tipos de Datos")
    print("2.  Condicionales")
    print("3.  Bucles")
    print("4.  Funciones")
    print("5.  Listas, Diccionarios y Bucles Anidados")
    print("6.  Programación Orientada a Objetos (POO)")
    print("7.  Manejo de Excepciones")
    print("8.  Módulos y Librerías")
    print("9.  Entrada/Salida de Archivos")
    print("11. Automatización de Tareas")
    print("12. Introducción a Bases de Datos")
    print("13. Testing y Debugging")
    print("0.  Salir")
    print("======================================")

def main():
    # Mapeo de opciones a funciones
    opciones = {
        '1': tema_1_variables,
        '2': tema_2_condicionales,
        '3': tema_3_bucles,
        '4': tema_4_funciones,
        '5': tema_5_estructuras_datos,
        '6': tema_6_poo,
        '7': tema_7_excepciones,
        '8': tema_8_modulos,
        '9': tema_9_archivos,
        '11': tema_11_automatizacion,
        '12': tema_12_bases_datos,
        '13': tema_13_testing,
    }

    while True:
        mostrar_menu()
        eleccion = input("Elige un tema para repasar (introduce el número) o '0' para salir: ")

        if eleccion == '0':
            print("¡Hasta la próxima!")
            break

        funcion_a_ejecutar = opciones.get(eleccion)
        if funcion_a_ejecutar:
            funcion_a_ejecutar()
            input("Presiona Enter para volver al menú...")
        else:
            print("Opción no válida. Por favor, elige un número del menú.")
            input("Presiona Enter para continuar...")

# Punto de entrada del script
if __name__ == "__main__":
    main()
