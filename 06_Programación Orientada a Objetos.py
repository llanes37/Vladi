# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: Ejemplo básico de clases y objetos
# ? En Python, una clase es una plantilla que define atributos (datos) y métodos (comportamientos).
# ? Un objeto es una instancia de una clase, es decir, algo creado a partir de la clase.
# -------------------------------------------------------------------------------------------

# * Clase `Soldado`: Aquí crearemos una clase `Soldado` con dos atributos: nombre y rango.
# * También tendrá un método para mostrar la información del soldado.
# 
# TODO: Escribe el código para definir la clase `Soldado` con sus atributos y el método para mostrar información.

class Soldado:
    def __init__(self, nombre, rango):
        self.nombre = nombre  # Atributo que almacena el nombre del soldado
        self.rango = rango  # Atributo que almacena el rango del soldado

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Rango: {self.rango}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: Atributos y métodos
# ? Los atributos son las variables que pertenecen a una clase y describen sus características.
# ? Los métodos son funciones definidas dentro de una clase que permiten que los objetos hagan algo.
# -------------------------------------------------------------------------------------------

# * Clase `UnidadMilitar`: Aquí crearemos una clase `UnidadMilitar` con atributos como nombre, tipo y estado.
# * También agregaremos métodos para activar, desactivar y mostrar la información de la unidad.
#
# TODO: Escribe el código para definir la clase `UnidadMilitar` con sus atributos y métodos.

class UnidadMilitar:
    def __init__(self, nombre_unidad, tipo_unidad, estado="inactivo"):
        self.nombre_unidad = nombre_unidad  # Atributo que almacena el nombre de la unidad
        self.tipo_unidad = tipo_unidad  # Atributo que almacena el tipo de unidad
        self.estado = estado  # Atributo que almacena el estado de la unidad

    def activar(self):
        self.estado = "activo"
        print(f"La unidad {self.nombre_unidad} está ahora activa.")

    def desactivar(self):
        self.estado = "inactivo"
        print(f"La unidad {self.nombre_unidad} está ahora inactiva.")

    def mostrar_informacion(self):
        print(f"Unidad: {self.nombre_unidad}, Tipo: {self.tipo_unidad}, Estado: {self.estado}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: Herencia
# ? La herencia permite que una clase "hija" herede atributos y métodos de otra clase "padre".
# ? Esto permite reutilizar código y extender la funcionalidad de clases existentes.
# -------------------------------------------------------------------------------------------

# * Clase `UnidadEspecial`: Crea una clase `UnidadEspecial` que herede de la clase `UnidadMilitar`.
# * Agrega un atributo para especialidad y sobrescribe el método para mostrar información.
#
# TODO: Escribe el código para definir la clase `UnidadEspecial` que hereda de `UnidadMilitar`.

class UnidadEspecial(UnidadMilitar):
    def __init__(self, nombre_unidad, tipo_unidad, estado="inactivo", especialidad=""):
        super().__init__(nombre_unidad, tipo_unidad, estado)  # Inicializa la clase base
        self.especialidad = especialidad  # Atributo que almacena la especialidad de la unidad

    def mostrar_informacion(self):
        print(f"Unidad: {self.nombre_unidad}, Tipo: {self.tipo_unidad}, Estado: {self.estado}, Especialidad: {self.especialidad}")


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: Encapsulación
# ? La encapsulación es una técnica para proteger los datos dentro de una clase y controlar su acceso.
# ? Se logra mediante la creación de atributos privados y métodos para acceder a ellos de forma segura.
# -------------------------------------------------------------------------------------------

# * Clase `SoldadoPrivado`: Crea una clase con atributos privados y métodos para obtener y cambiar el código ID.
# * Implementa una validación para que el código ID tenga al menos 5 caracteres.
#
# TODO: Escribe el código para definir la clase `SoldadoPrivado` con encapsulación y validación.

class SoldadoPrivado:
    def __init__(self, nombre, codigo_id):
        self.__nombre = nombre  # Atributo privado para el nombre del soldado
        self.__codigo_id = codigo_id  # Atributo privado para el código ID del soldado

    def obtener_nombre(self):
        return self.__nombre

    def cambiar_codigo_id(self, nuevo_codigo):
        if len(nuevo_codigo) >= 5:
            self.__codigo_id = nuevo_codigo
            print(f"Código de identificación actualizado a {nuevo_codigo}.")
        else:
            print("El código debe tener al menos 5 caracteres.")
