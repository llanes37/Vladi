# *******************************************************************************************
# * IMPORTANTE: NO SE PERMITE EL USO DE INTELIGENCIA ARTIFICIAL PARA RESOLVER ESTE EXAMEN. *
# * SOLO PUEDES UTILIZAR LOS APUNTES CREADOS POR TI COMO REFERENCIA.                       *
# *******************************************************************************************

# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: Ejemplo básico de clases y objetos (2 PUNTOS)
# TODO: Crea una clase `Soldado` que tenga:
#   - Dos atributos: `nombre` y `rango`.
#   - Un método `mostrar_informacion` que imprima los valores de estos atributos.

class Soldado:
    pass  # Escribe el código aquí


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: Atributos y métodos (3 PUNTOS)
# TODO: Crea una clase `UnidadMilitar` con:
#   - Atributos: `nombre_unidad`, `tipo_unidad`, `estado` (por defecto "inactivo").
#   - Métodos:
#       - `activar`: Cambia el estado a "activo".
#       - `desactivar`: Cambia el estado a "inactivo".
#       - `mostrar_informacion`: Imprime todos los atributos.

class UnidadMilitar:
    pass  # Escribe el código aquí


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: Herencia (2 PUNTOS)
# TODO: Crea una clase `UnidadEspecial` que herede de `UnidadMilitar` y:
#   - Tenga un atributo adicional: `especialidad`.
#   - Sobrescriba el método `mostrar_informacion` para incluir la especialidad.

class UnidadEspecial(UnidadMilitar):
    pass  # Escribe el código aquí


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: Encapsulación (3 PUNTOS)
# TODO: Crea una clase `SoldadoPrivado` con:
#   - Atributos privados: `__nombre` y `__codigo_id`.
#   - Métodos:
#       - `obtener_nombre`: Devuelve `__nombre`.
#       - `cambiar_codigo_id`: Cambia `__codigo_id` solo si tiene al menos 5 caracteres.

class SoldadoPrivado:
    pass  # Escribe el código aquí
