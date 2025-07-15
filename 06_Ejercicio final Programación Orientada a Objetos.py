# *******************************************************************************************
# * PRÁCTICA COMPLETA: GESTIÓN DE UN BAR PARA LAS FIESTAS DE UN PUEBLO            *
# * OBJETIVO: Crear un sistema que modele la gestión de una cantina usando POO en Python.   *
# *******************************************************************************************

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: CLASE BÁSICA
# -------------------------------------------------------------------------------------------

class Producto:
    """
    Clase que representa un producto en la cantina.
    """
    def __init__(self, nombre, precio, cantidad_disponible):
        """
        Constructor de la clase Producto.
        :param nombre: Nombre del producto (str).
        :param precio: Precio del producto (float).
        :param cantidad_disponible: Cantidad de unidades disponibles (int).
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def vender(self, cantidad):
        """
        Método para reducir la cantidad disponible del producto si es posible.
        :param cantidad: Cantidad a vender (int).
        """
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente cantidad de {self.nombre} para vender.")

    def mostrar_informacion(self):
        """
        Método para mostrar la información del producto.
        """
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad disponible: {self.cantidad_disponible}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: CLASE PRINCIPAL
# -------------------------------------------------------------------------------------------

class RESTAURANTE:
    """
    Clase que representa la administración de una cantina.
    """
    def __init__(self, nombre_cantina):
        """
        Constructor de la clase Cantina.
        :param nombre_cantina: Nombre de la cantina (str).
        """
        self.nombre_cantina = nombre_cantina
        self.productos = []  # Lista para almacenar objetos Producto.

    def agregar_producto(self, producto):
        """
        Método para agregar un nuevo producto a la cantina.
        :param producto: Objeto de tipo Producto.
        """
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la cantina {self.nombre_cantina}.")

    def mostrar_productos(self):
        """
        Método para mostrar todos los productos de la cantina.
        """
        print(f"Productos en {self.nombre_cantina}:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Método para realizar la venta de un producto si existe y tiene suficiente cantidad.
        :param nombre_producto: Nombre del producto a vender (str).
        :param cantidad: Cantidad a vender (int).
        """
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.vender(cantidad)
                return
        print(f"Producto {nombre_producto} no encontrado en la cantina.")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: HERENCIA Y ESPECIALIZACIÓN
# -------------------------------------------------------------------------------------------

class ProductoEspecial(Producto):
    """
    Subclase de Producto que representa productos exclusivos de las fiestas.
    """
    def __init__(self, nombre, precio, cantidad_disponible, fecha_caducidad):
        """
        Constructor de la clase ProductoEspecial.
        :param nombre: Nombre del producto (str).
        :param precio: Precio del producto (float).
        :param cantidad_disponible: Cantidad de unidades disponibles (int).
        :param fecha_caducidad: Fecha de caducidad del producto (str).
        """
        super().__init__(nombre, precio, cantidad_disponible)  # Llama al constructor de la clase base.
        self.fecha_caducidad = fecha_caducidad

    def mostrar_informacion(self):
        """
        Sobrescribe el método para mostrar también la fecha de caducidad.
        """
        print(f"Producto Especial: {self.nombre}, Precio: {self.precio}, "
              f"Cantidad disponible: {self.cantidad_disponible}, Fecha de caducidad: {self.fecha_caducidad}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: ENCAPSULACIÓN Y VALIDACIÓN
# -------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------
# * DESAFÍO FINAL: PROGRAMA PRINCIPAL
# -------------------------------------------------------------------------------------------

# Crear una instancia de Cantina.
BURGERkING = RESTAURANTE("bURGERkiNG")

# Agregar productos normales.
WHOPPER = Producto("WHOPPER", 2, 100)
PATATAS = Producto("PATATAS", 1, 50)
PATATAS.vender(10)  # Vender 10 unidades de PATATAS.
WHOPPER.vender(5)  # Vender 5 unidades de WHOPPER
BURGERkING.agregar_producto(WHOPPER)
BURGERkING.agregar_producto(PATATAS)
BURGERkING.mostrar_productos()
# Agregar productos especiales.
""" producto_especial = ProductoEspecial("Pastel Especial", 10.0, 10, "2025-01-30")
cantina.agregar_producto(producto_especial)

# Mostrar todos los productos.
print("\nLista de productos:")
cantina.mostrar_productos()

# Realizar una venta.
print("\nRealizando venta de 2 Refrescos...")
cantina.realizar_venta("Refresco", 2)

# Mostrar productos después de la venta.
print("\nLista de productos después de la venta:")
cantina.mostrar_productos() """


