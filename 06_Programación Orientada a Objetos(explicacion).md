# Programación Orientada a Objetos (POO) en Python

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que nos permite modelar el mundo real de manera intuitiva y estructurada en nuestro código. Este paradigma se basa en la creación de **clases** que actúan como plantillas para **objetos**, los cuales representan entidades específicas del mundo real. Los objetos se caracterizan por tener:

- **Atributos**: Propiedades o datos que describen las características del objeto.
- **Métodos**: Acciones o comportamientos que el objeto puede realizar.

La POO es fundamental porque:

1. **Organiza el código**: Facilita la división en componentes lógicos.
2. **Fomenta la reutilización**: Gracias a conceptos como la herencia y el polimorfismo.
3. **Hace el código escalable**: Es más sencillo extender el código existente sin modificarlo drásticamente.

### Ejemplo del mundo real:

Imaginemos que queremos modelar un sistema que administre vehículos. Cada vehículo tiene atributos como marca, modelo y color, y también puede realizar acciones como arrancar o detenerse.

Podríamos crear una clase `Vehiculo` para representar esta idea:

```python
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca  # Atributo que almacena la marca del vehículo
        self.modelo = modelo  # Atributo que almacena el modelo del vehículo
        self.color = color  # Atributo que almacena el color del vehículo

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} ha arrancado.")

    def detenerse(self):
        print(f"El vehículo {self.marca} {self.modelo} se ha detenido.")

# Crear una instancia de la clase Vehiculo
mi_coche = Vehiculo("Toyota", "Corolla", "Rojo")
mi_coche.arrancar()
mi_coche.detenerse()
```

En este ejemplo:
- Creamos una clase `Vehiculo` que tiene atributos y métodos.
- Creamos un objeto `mi_coche` que representa un vehículo específico.

### Conceptos fundamentales:

1. **Clases e instancias**: Una clase es una plantilla, y una instancia es un objeto creado a partir de esa plantilla.
2. **Encapsulación**: Protege los datos del objeto y controla su acceso.
3. **Herencia**: Permite crear nuevas clases que reutilizan y extienden las características de otras.
4. **Polimorfismo**: Proporciona formas de usar una misma interfaz para diferentes tipos de datos.
5. **Abstracción**: Oculta los detalles internos del objeto y expone solo lo necesario.

### Beneficios de usar POO:

- **Modularidad**: El código se divide en piezas lógicas y manejables.
- **Reutilización**: Se pueden crear clases generales y especializarlas sin duplicar código.
- **Mantenibilidad**: Facilita la corrección de errores y la incorporación de nuevas funcionalidades.

### Ejercicio sugerido:

Crea una clase `Persona` que tenga atributos como `nombre`, `edad` y `ocupación`. Añade métodos como `presentarse` para imprimir un mensaje con los detalles de la persona y `cumplir_anios` para incrementar la edad en uno. Luego, crea varias instancias y prueba los métodos. Este documento incluye teoría, ejemplos y ejercicios para reforzar el aprendizaje de los conceptos fundamentales de POO en Python.

---

## **Sección 1: Creación de clases y objetos**

### ¿Qué es una clase y qué es un objeto?

- **Clase**: Es una plantilla que define los atributos y métodos de los objetos. Es decir, especifica qué datos y comportamientos tendrán las instancias de esta clase.
- **Objeto**: Es una instancia de una clase, creada a partir de la plantilla. Los objetos representan entidades concretas con datos específicos.

### Ejemplo básico:

```python
class Usuario:  # Definimos la clase Usuario
    def __init__(self, nombre, rol):  # Constructor de la clase, inicializa los atributos
        self.nombre = nombre  # Atributo nombre del objeto
        self.rol = rol  # Atributo rol del objeto
    
    def mostrar_info(self):  # Método para mostrar la información del objeto
        print(f"Usuario: {self.nombre}, Rol: {self.rol}")

# Crear un objeto de la clase Usuario
usuario1 = Usuario("Ana", "admin")  # Se crea una instancia con nombre 'Ana' y rol 'admin'
usuario1.mostrar_info()  # Llamamos al método mostrar_info para imprimir los datos del usuario
```

#### Explicación:

- **`__init__`**: Es el constructor de la clase. Se ejecuta automáticamente cuando se crea un objeto y sirve para inicializar los atributos.
- **self**: Es una referencia al objeto actual. Permite acceder a los atributos y métodos de la instancia.
- Creamos un objeto `usuario1` de la clase `Usuario`, asignando un nombre y un rol, y luego mostramos la información usando el método `mostrar_info`.

#### Ejercicio:

Crea una clase llamada `Producto` que tenga los atributos `nombre` y `precio`. Luego, crea un objeto de la clase y un método para mostrar la información del producto.

---

## **Sección 2: Atributos y Métodos**

### Atributos y Métodos

- **Atributos**: Son variables que pertenecen a una clase. Describen las características o propiedades de los objetos.
- **Métodos**: Son funciones dentro de una clase que describen el comportamiento de los objetos.

### Ejemplo:

```python
class Servidor:  # Definimos la clase Servidor
    def __init__(self, nombre, ip, estado="inactivo"):  # Constructor con estado por defecto 'inactivo'
        self.nombre = nombre  # Atributo nombre del servidor
        self.ip = ip  # Atributo dirección IP del servidor
        self.estado = estado  # Atributo estado del servidor
    
    def encender(self):  # Método para cambiar el estado a 'activo'
        if self.estado == "inactivo":
            self.estado = "activo"
            print(f"Servidor {self.nombre} ha sido encendido.")
        else:
            print(f"El servidor {self.nombre} ya está activo.")
    
    def reiniciar(self):  # Método para reiniciar el servidor
        print(f"Reiniciando servidor {self.nombre}...")
        self.estado = "reiniciando"
    
    def mostrar_info(self):  # Método para mostrar la información del servidor
        print(f"Servidor: {self.nombre}, IP: {self.ip}, Estado: {self.estado}")

# Crear un objeto Servidor y usar sus métodos
servidor1 = Servidor("Servidor Alfa", "192.168.1.1")  # Instanciamos un servidor
servidor1.mostrar_info()  # Mostramos la información inicial del servidor
servidor1.encender()  # Encendemos el servidor
servidor1.reiniciar()  # Reiniciamos el servidor
```

#### Explicación:

- En este ejemplo, `nombre`, `ip` y `estado` son atributos que describen al servidor.
- Los métodos `encender`, `reiniciar` y `mostrar_info` describen el comportamiento del servidor.

#### Ejercicio:

Crea una clase `Coche` con atributos como `marca`, `modelo` y `estado`. Agrega métodos para arrancar el coche y mostrar su información.

---

## **Sección 3: Herencia**

### ¿Qué es la herencia?

La herencia permite que una clase derive de otra, heredando sus atributos y métodos. Esto facilita la reutilización y extensión del código.

- **Clase base (superclase)**: La clase de la que se heredan atributos y métodos.
- **Clase derivada (subclase)**: La clase que hereda los atributos y métodos de la clase base.

### Ejemplo:

```python
class ServidorWeb(Servidor):  # Heredamos de la clase Servidor
    def __init__(self, nombre, ip, estado="inactivo"):  # Constructor que utiliza el de la superclase
        super().__init__(nombre, ip, estado)  # Inicializamos atributos de la clase base
    
    def configurar_dominio(self, dominio):  # Método adicional exclusivo de ServidorWeb
        self.dominio = dominio  # Atributo dominio del servidor web
        print(f"Servidor web {self.nombre} configurado con el dominio {dominio}")

# Crear un objeto ServidorWeb
servidor_web1 = ServidorWeb("Servidor Web Alfa", "192.168.1.3")  # Instanciamos un servidor web
servidor_web1.mostrar_info()  # Mostramos la información inicial
servidor_web1.configurar_dominio("www.ejemplo.com")  # Configuramos un dominio para el servidor web
```

#### Explicación:

- La clase `ServidorWeb` hereda los atributos y métodos de `Servidor`, y añade un nuevo método `configurar_dominio`.
- **`super()`**: Llama al constructor de la clase base para reutilizar su funcionalidad.

#### Ejercicio:

Crea una clase `Electrodomestico` con atributos como `marca` y `potencia`. Luego, crea una subclase `Lavadora` que tenga un método para indicar el tipo de carga (frontal o superior).

---

## **Sección 4: Encapsulación**

### ¿Qué es la encapsulación?

La encapsulación protege los datos de un objeto y controla el acceso a ellos. Esto se logra usando atributos privados y métodos de acceso.

### Ejemplo:

```python
class ServidorSeguro:  # Definimos la clase ServidorSeguro
    def __init__(self, nombre, ip):  # Constructor para inicializar atributos privados
        self.__nombre = nombre  # Atributo privado nombre
        self.__ip = ip  # Atributo privado IP
    
    def obtener_nombre(self):  # Método para acceder al atributo privado __nombre
        return self.__nombre
    
    def cambiar_nombre(self, nuevo_nombre):  # Método para modificar el atributo privado __nombre
        if len(nuevo_nombre) > 3:
            self.__nombre = nuevo_nombre
            print(f"Nombre del servidor cambiado a {nuevo_nombre}")
        else:
            print("Error: El nombre debe tener más de 3 caracteres")

# Probar la encapsulación
servidor_seguro = ServidorSeguro("Servidor Seguro", "192.168.0.1")  # Creamos un servidor seguro
print(servidor_seguro.obtener_nombre())  # Obtenemos el nombre del servidor
servidor_seguro.cambiar_nombre("Srv")  # Intentamos cambiar el nombre a uno muy corto
servidor_seguro.cambiar_nombre("Servidor Seguro Alfa")  # Cambiamos el nombre correctamente
```

#### Explicación:

- Los atributos `__nombre` y `__ip` están protegidos y solo pueden ser accedidos o modificados mediante los métodos de acceso.

#### Ejercicio:

Crea una clase `Banco` con un atributo privado `__saldo`. Agrega métodos para depositar, retirar y consultar el saldo, asegurando que el saldo nunca sea negativo.

---

## **Sección 5: Polimorfismo**

### ¿Qué es el polimorfismo?

El polimorfismo permite usar un mismo método en varias clases, pero con comportamientos distintos. Es una forma de escribir código flexible y reutilizable.

### Ejemplo:

```python
class Servidor:  # Clase base
    def mostrar_tipo(self):  # Método común en todas las subclases
        print("Soy un servidor genérico.")

class ServidorWeb(Servidor):  # Subclase
    def mostrar_tipo(self):  # Sobrescribimos el método mostrar_tipo
        print("Soy un servidor web.")

class ServidorBaseDatos(Servidor):  # Otra subclase
    def mostrar_tipo(self):  # Sobrescribimos el método mostrar_tipo
        print("Soy un servidor de base de datos.")

# Crear diferentes tipos de servidores y usar polimorfismo
servidores = [Servidor(), ServidorWeb(), ServidorBaseDatos()]  # Lista de instancias de diferentes clases

for servidor in servidores:
    servidor.mostrar_tipo()  # Cada objeto usa su propia implementación de mostrar_tipo
```

#### Explicación:

- El método `mostrar_tipo` tiene diferentes implementaciones dependiendo de la clase a la que pertenece el objeto.

#### Ejercicio:

Crea una clase base `Animal` con un método `hacer_sonido`. Luego, crea subclases como `Perro` y `Gato` que implementen el método con sonidos específicos (ladrar y maullar).

---

## **Autoevaluación Final**

1. Crea una clase `Usuario` con atributos de nombre y rol, y un método para mostrar la información del usuario.
2. Crea una clase `Servidor` que tenga atributos de nombre, IP y estado, y métodos para encender, reiniciar y mostrar información.
3. Crea una clase `ServidorWeb` que herede de `Servidor`, añadiendo un método para configurar un dominio.
4. Crea una clase `ServidorSeguro` que tenga atributos privados, y métodos para obtener y cambiar el nombre con validación.
5. Implementa polimorfismo con varias clases que tengan un método común pero con diferentes implementaciones.

### Correcciones sugeridas:

1. **Clase Usuario:**

```python
class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol

    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Rol: {self.rol}")

usuario = Usuario("Carlos", "editor")
usuario.mostrar_info()
```

2. **Clase Servidor:**

```python
class Servidor:
    def __init__(self, nombre, ip, estado="inactivo"):
        self.nombre = nombre
        self.ip = ip
        self.estado = estado

    def encender(self):
        self.estado = "activo"
        print(f"Servidor {self.nombre} encendido.")

    def reiniciar(self):
        self.estado = "reiniciando"
        print(f"Servidor {self.nombre} reiniciando.")

    def mostrar_info(self):
        print(f"Servidor: {self.nombre}, IP: {self.ip}, Estado: {self.estado}")

servidor = Servidor("Servidor Alfa", "192.168.1.1")
servidor.mostrar_info()
servidor.encender()
servidor.reiniciar()
```

3. **Clase ServidorWeb:**

```python
class ServidorWeb(Servidor):
    def configurar_dominio(self, dominio):
        self.dominio = dominio
        print(f"Servidor {self.nombre} configurado con dominio {dominio}")

servidor_web = ServidorWeb("Servidor Web", "192.168.1.2")
servidor_web.configurar_dominio("www.ejemplo.com")
```

4. **Clase ServidorSeguro:**

```python
class ServidorSeguro:
    def __init__(self, nombre, ip):
        self.__nombre = nombre
        self.__ip = ip

    def obtener_nombre(self):
        return self.__nombre

    def cambiar_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 3:
            self.__nombre = nuevo_nombre
            print(f"Nombre cambiado a {nuevo_nombre}")
        else:
            print("Nombre demasiado corto.")

servidor_seguro = ServidorSeguro("Servidor Seguro", "192.168.1.3")
print(servidor_seguro.obtener_nombre())
servidor_seguro.cambiar_nombre("Srv")
servidor_seguro.cambiar_nombre("Servidor Alfa")
```

5. **Polimorfismo:**

```python
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

animales = [Perro(), Gato()]

for animal in animales:
    animal.hacer_sonido()
```

