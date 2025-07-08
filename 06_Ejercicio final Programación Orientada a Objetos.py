# *******************************************************************************************
# * PRÁCTICA COMPLETA: GESTIÓN DE LA CANTINA PARA LAS FIESTAS DE SAN JUAN BOSCO             *
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

class Cantina:
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

class AdministradorCantina:
    """
    Clase para gestionar los datos privados de los administradores de la cantina.
    """
    def __init__(self, nombre, clave):
        """
        Constructor de la clase AdministradorCantina.
        :param nombre: Nombre del administrador (str).
        :param clave: Clave de acceso (str).
        """
        self.__nombre = nombre  # Atributo privado.
        self.__clave = clave  # Atributo privado.

    def verificar_clave(self, clave):
        """
        Método para verificar si una clave es correcta.
        :param clave: Clave a verificar (str).
        :return: True si la clave coincide, False en caso contrario.
        """
        return self.__clave == clave

    def cambiar_clave(self, nueva_clave):
        """
        Método para cambiar la clave privada si cumple los requisitos.
        :param nueva_clave: Nueva clave (str).
        """
        if len(nueva_clave) >= 8:
            self.__clave = nueva_clave
            print("Clave cambiada con éxito.")
        else:
            print("La nueva clave debe tener al menos 8 caracteres.")


# -------------------------------------------------------------------------------------------
# * DESAFÍO FINAL: PROGRAMA PRINCIPAL
# -------------------------------------------------------------------------------------------

# Crear una instancia de Cantina.
cantina = Cantina("Cantina San Juan Bosco")

# Agregar productos normales.
producto1 = Producto("Refresco", 1.5, 100)
producto2 = Producto("Empanada", 2.0, 50)
cantina.agregar_producto(producto1)
cantina.agregar_producto(producto2)

# Agregar productos especiales.
producto_especial = ProductoEspecial("Pastel Especial", 10.0, 10, "2025-01-30")
cantina.agregar_producto(producto_especial)

# Mostrar todos los productos.
print("\nLista de productos:")
cantina.mostrar_productos()

# Realizar una venta.
print("\nRealizando venta de 2 Refrescos...")
cantina.realizar_venta("Refresco", 2)

# Mostrar productos después de la venta.
print("\nLista de productos después de la venta:")
cantina.mostrar_productos()

# Gestionar administrador.
admin = AdministradorCantina("María", "clave123")
print("\nVerificando clave del administrador:")
print(admin.verificar_clave("clave123"))  # Debería devolver True.

print("\nCambiando clave del administrador...")
admin.cambiar_clave("nuevaClaveSegura")

print("\nVerificando con la nueva clave:")
print(admin.verificar_clave("nuevaClaveSegura"))  # Debería devolver True.
