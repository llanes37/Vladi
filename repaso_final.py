# -------------------------------------------------------------------------------------------
# PROYECTO FINAL DE REPASO: "MI TIENDA DE POSTRES"
# Nivel: Fácil | Para repasar TODO lo aprendido en Python (variables, listas, funciones, clases...)
# -------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------
# * PARTE 1: VARIABLES Y LISTAS
# TODO: Crea una lista llamada `postres_disponibles` con 3 postres que te gusten.
# TODO: Crea una variable que guarde el nombre de la tienda.
# -------------------------------------------------------------------------------------------

# postres_disponibles = [...]
# nombre_tienda = "..."

# -------------------------------------------------------------------------------------------
# * PARTE 2: FUNCIONES Y CONDICIONALES
# TODO: Crea una función `mostrar_menu()` que imprima los postres disponibles.
# TODO: Crea una función `elegir_postre()` que pida al usuario uno de los postres.
#       Si el postre está en la lista, muestra "¡Buena elección!".
#       Si no está, muestra "Ese postre no está en la tienda.".
# -------------------------------------------------------------------------------------------

# def mostrar_menu():
#     # Mostrar todos los postres uno a uno con un bucle

# def elegir_postre():
#     # Pedir al usuario su elección
#     # Comprobar si está en la lista (con if)
#     # Mostrar el mensaje correspondiente


# -------------------------------------------------------------------------------------------
# * PARTE 3: USO DE DICCIONARIOS
# TODO: Crea un diccionario llamado `precios` con el nombre del postre como clave
#       y el precio como valor (por ejemplo: "Tarta": 3.5)
# TODO: Crea una función `mostrar_precios()` que imprima cada postre con su precio.
# -------------------------------------------------------------------------------------------

# precios = { ... }

# def mostrar_precios():
#     # Usar un bucle para imprimir postre y precio


# -------------------------------------------------------------------------------------------
# * PARTE 4: CLASES Y OBJETOS
# TODO: Crea una clase `Cliente` con:
#       - Atributos: nombre, postre_favorito
#       - Método: presentarse() que diga: "Hola, soy <nombre> y me gusta el <postre_favorito>"

# TODO: Crea una clase `TiendaPostres` con:
#       - Atributos: nombre_tienda, lista_postres
#       - Método: mostrar_postres() (similar a mostrar_menu)
#       - Método: agregar_postre(postre) que añade un nuevo postre a la lista

# -------------------------------------------------------------------------------------------

# class Cliente:
#     def __init__(self, nombre, postre_favorito):
#         # Guardar en atributos

#     def presentarse(self):
#         # Imprimir presentación


# class TiendaPostres:
#     def __init__(self, nombre_tienda, lista_postres):
#         # Guardar en atributos

#     def mostrar_postres(self):
#         # Mostrar todos los postres de la tienda

#     def agregar_postre(self, postre):
#         # Añadir postre a la lista


# -------------------------------------------------------------------------------------------
# * PRUEBA FINAL: SIMULAR LA TIENDA
# TODO:
#   - Crea un objeto Cliente y uno TiendaPostres
#   - Haz que el cliente se presente
#   - Muestra los postres, precios y permite elegir uno
#   - Agrega un nuevo postre con el método de la clase
# -------------------------------------------------------------------------------------------

# cliente1 = Cliente("Marta", "brownie")
# tienda = TiendaPostres("Delicias Dulces", ["brownie", "pastel", "galletas"])

# cliente1.presentarse()
# tienda.mostrar_postres()
# mostrar_precios()
# elegir_postre()
# tienda.agregar_postre("tarta de queso")
# tienda.mostrar_postres()
