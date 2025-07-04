# -------------------------------------------------------------------------------------------
# * SECCIÓN 1: EJEMPLO BÁSICO DE UNA FUNCIÓN EN PYTHON
# ? Una función en Python es un bloque de código que solo se ejecuta cuando es llamada.
# ? Las funciones pueden tomar parámetros, que son valores que se le pasan para que la función los use.
# ? Después de realizar sus tareas, una función puede devolver un valor usando "return".
# ? Crear funciones ayuda a organizar el código, hacerlo más fácil de leer y reutilizable.
# -------------------------------------------------------------------------------------------

# * FUNCIÓN PARA SALUDAR A UN OFICIAL DE SISTEMAS
# ? Esta función pide al usuario su nombre y rango, y devuelve un mensaje de bienvenida.
# ? Recuerda: Usamos la función input() para pedir datos al usuario, y return para devolver un mensaje.

# TODO: Escribe aquí tu código para definir y llamar a la función de saludo.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 2: FUNCIÓN PARA CALCULAR EL USO DE RECURSOS (CPU Y MEMORIA)
# ? En esta función, le pedimos al usuario que introduzca dos valores: el uso de CPU y el uso de memoria.
# ? Si el usuario no introduce un valor para la memoria, podemos asignar un valor por defecto usando una condición.
# ? Recuerda que puedes convertir los datos que recibe la función en otros tipos, como convertir un texto (string) en número (int).
# -------------------------------------------------------------------------------------------

# * SOLICITAR EL USO DE CPU Y MEMORIA, CON UN VALOR POR DEFECTO SI EL USUARIO NO INTRODUCE NADA.
# ? En este ejercicio, la memoria será opcional y si no se introduce un valor, se usará un valor por defecto (2048 MB).

# TODO: Escribe aquí tu código para definir y llamar a la función que calcula el uso de recursos.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 3: FUNCIÓN PARA GESTIONAR USUARIOS DEL SISTEMA
# ? En administración de sistemas, es importante gestionar usuarios y sus privilegios.
# ? En esta función, le pediremos al usuario que introduzca el nombre de un usuario y si tiene privilegios de administrador.
# ? Usamos condiciones (if/else) para devolver diferentes mensajes según si el usuario es o no administrador.
# -------------------------------------------------------------------------------------------

# * SOLICITAR EL NOMBRE DEL USUARIO Y VERIFICAR SI TIENE PRIVILEGIOS DE ADMINISTRADOR.
# ? Si el usuario tiene privilegios, mostramos un mensaje que diga que tiene acceso completo; si no, indicamos que tiene acceso limitado.

# TODO: Escribe aquí tu código para definir y llamar a la función de gestión de usuarios.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 4: FUNCIÓN PARA COMPROBAR EL ESTADO DE LOS SERVICIOS CRÍTICOS
# ? Un servidor generalmente ejecuta varios servicios importantes, como SSH, VPN, Firewall, entre otros.
# ? Esta función recorre una lista de servicios críticos y verifica si están funcionando correctamente.
# ? Usamos un bucle (for) para iterar sobre la lista de servicios y comprobar su estado.
# -------------------------------------------------------------------------------------------

# * COMPROBAR EL ESTADO DE LOS SERVICIOS CRÍTICOS QUE DEBEN ESTAR FUNCIONANDO EN EL SERVIDOR.
# ? La función iterará sobre la lista de servicios, comprobando su estado uno por uno.

# TODO: Escribe aquí tu código para definir y llamar a la función de comprobación de servicios.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 5: FUNCIÓN PARA MONITORIZAR SERVIDORES EN LA RED
# ? En un sistema en red, hay varios servidores conectados. Esta función pide al usuario que introduzca el estado de cada servidor.
# ? Dependiendo de la respuesta del usuario (si está o no disponible), se almacenarán los servidores que están en buen estado.
# ? Esta función usa un bucle para verificar el estado de cada servidor en la lista.
# -------------------------------------------------------------------------------------------

# * MONITORIZAR UNA LISTA DE SERVIDORES Y MOSTRAR CUÁLES ESTÁN DISPONIBLES.
# ? Si el servidor está disponible, lo añadimos a una lista de servidores disponibles; si no, mostramos un aviso de alerta.

# TODO: Escribe aquí tu código para definir y llamar a la función que monitoriza los servidores.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 6: FUNCIÓN CON VARIOS PARÁMETROS Y RETURN
# ? Las funciones también pueden aceptar parámetros. Los parámetros son valores que le pasamos a la función para que los use.
# ? En esta sección, crearemos una función que suma dos números y devuelve el resultado.
# ? La palabra clave "return" se usa para devolver un valor desde la función al lugar donde fue llamada.
# -------------------------------------------------------------------------------------------

# * SUMAR DOS NÚMEROS Y DEVOLVER EL RESULTADO.
# ? Los parámetros de la función serán dos números, y devolverá la suma de estos números.

# TODO: Escribe aquí tu código para definir y llamar a la función que suma dos números.


# -------------------------------------------------------------------------------------------
# * SECCIÓN 7: FUNCIÓN QUE LLAMA A OTRAS FUNCIONES
# ? Es posible que una función llame a otras funciones dentro de su código para ejecutar varias tareas en conjunto.
# ? En este caso, creamos una función que llamará a las funciones anteriores para ejecutar todo un proceso automatizado.
# -------------------------------------------------------------------------------------------

# * LLAMAR A TODAS LAS FUNCIONES PREVIAMENTE DEFINIDAS PARA COMPLETAR UN PROCESO.
# ? Esta función puede servir como un "resumen" donde llamamos a varias funciones que hemos definido antes.

# TODO: Escribe aquí tu código para definir y llamar a una función que ejecute un proceso completo.


# -------------------------------------------------------------------------------------------
# * AUTOEVALUACIÓN FINAL:
# ? En esta parte, combinaremos todo lo aprendido.
# 1. Solicita el nombre de un usuario del sistema y salúdale usando una función.
# 2. Solicita el uso de CPU y memoria de un servidor y muestra los resultados usando una función.
# 3. Solicita el estado de tres servidores y registra cuáles están disponibles.
# 4. Solicita la suma de dos números y devuelve el resultado.
# 5. Llama a todas las funciones definidas anteriormente en un proceso completo.
# -------------------------------------------------------------------------------------------

# TODO: Escribe aquí tu código para la autoevaluación final que incluya todas las funciones que has definido.
