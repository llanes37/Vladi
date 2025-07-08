# *******************************************************************************************
# * PRÁCTICA COMPLETA: GESTIÓN DE LA CANTINA PARA LAS FIESTAS DE SAN JUAN BOSCO             *
# * OBJETIVO: Crear un sistema que modele la gestión de una cantina usando POO en Python.   *
# * DURACIÓN: 2 CLASES DE 50 MINUTOS                                                       *
# *******************************************************************************************

# *******************************************************************************************
# * IMPORTANTE: NO SE PERMITE EL USO DE INTELIGENCIA ARTIFICIAL PARA ESTA PRÁCTICA.        *
# * SOLO PUEDES UTILIZAR LOS APUNTES CREADOS POR TI COMO REFERENCIA.                       *
# *******************************************************************************************

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: CLASE BÁSICA (20 MINUTOS)
# TODO: Crear una clase básica llamada `Producto` que represente los productos que se venden en la cantina.
# 
# Requisitos:
#   - Atributos:
#       - `nombre`: Nombre del producto (string).
#       - `precio`: Precio del producto (float).
#       - `cantidad_disponible`: Cantidad de unidades disponibles (int).
#   - Métodos:
#       - `vender`: Reduce la cantidad disponible en una cantidad especificada.
#       - `mostrar_informacion`: Imprime la información del producto.
# -------------------------------------------------------------------------------------------

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        # Inicializa los atributos con los valores pasados como parámetros.
        pass

    def vender(self, cantidad):
        # Reduce `cantidad_disponible` según lo solicitado, si es posible.
        pass

    def mostrar_informacion(self):
        # Imprime el nombre, precio y cantidad disponible del producto.
        pass


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: CLASE PRINCIPAL (30 MINUTOS)
# TODO: Crear una clase llamada `Cantina` que represente la administración de la cantina.
# 
# Requisitos:
#   - Atributos:
#       - `nombre_cantina`: Nombre de la cantina (string).
#       - `productos`: Lista de objetos `Producto` (inicialmente vacía).
#   - Métodos:
#       - `agregar_producto`: Agrega un nuevo producto a la lista.
#       - `mostrar_productos`: Muestra la lista completa de productos con su información.
#       - `realizar_venta`: Busca un producto por nombre y realiza una venta si hay suficiente cantidad.
# -------------------------------------------------------------------------------------------

class Cantina:
    def __init__(self, nombre_cantina):
        # Inicializa el nombre de la cantina y crea una lista vacía para los productos.
        pass

    def agregar_producto(self, producto):
        # Agrega un objeto `Producto` a la lista de productos.
        pass

    def mostrar_productos(self):
        # Recorre la lista de productos y muestra la información de cada uno.
        pass

    def realizar_venta(self, nombre_producto, cantidad):
        # Busca un producto por nombre y realiza una venta si es posible.
        pass


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: HERENCIA Y ESPECIALIZACIÓN (20 MINUTOS)
# TODO: Crear una subclase llamada `ProductoEspecial` que represente productos exclusivos de las fiestas.
# 
# Requisitos:
#   - Hereda de `Producto`.
#   - Atributo adicional:
#       - `fecha_caducidad`: Fecha en la que caduca el producto (string).
#   - Métodos:
#       - `mostrar_informacion`: Sobrescribe el método para incluir la fecha de caducidad.
# -------------------------------------------------------------------------------------------

class ProductoEspecial(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, fecha_caducidad):
        # Inicializa los atributos de la clase base y el nuevo atributo `fecha_caducidad`.
        pass

    def mostrar_informacion(self):
        # Muestra la información del producto, incluyendo la fecha de caducidad.
        pass


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: ENCAPSULACIÓN Y VALIDACIÓN (30 MINUTOS)
# TODO: Crear una clase `AdministradorCantina` para gestionar datos privados de los administradores.
# 
# Requisitos:
#   - Atributos privados:
#       - `__nombre`: Nombre del administrador (string).
#       - `__clave`: Clave de acceso (string).
#   - Métodos:
#       - `verificar_clave`: Recibe una clave y devuelve True si coincide con la clave privada.
#       - `cambiar_clave`: Cambia la clave si la nueva tiene al menos 8 caracteres.
# -------------------------------------------------------------------------------------------

class AdministradorCantina:
    def __init__(self, nombre, clave):
        # Inicializa el nombre y clave como atributos privados.
        pass

    def verificar_clave(self, clave):
        # Verifica si la clave pasada coincide con la clave privada.
        pass

    def cambiar_clave(self, nueva_clave):
        # Cambia la clave privada si la nueva tiene al menos 8 caracteres.
        pass


# -------------------------------------------------------------------------------------------
# * DESAFÍO FINAL (TIEMPO RESTANTE, CON INTERNET)
# TODO: 
# - Este paso puede realizarse con ayuda de inteligencia artificial.
# - Primero completa las secciones anteriores desconectado de internet.
# - Luego reconecta el cable de internet para usar la IA en el siguiente programa principal:
#       - Crear una cantina y agregar productos normales y especiales.
#       - Mostrar la lista de productos.
#       - Realizar una venta.
#       - Cambiar la clave del administrador.
# -------------------------------------------------------------------------------------------
