
# Entrada y Salida de Archivos en Python

## Introducción
La entrada y salida de archivos (I/O) en Python es un aspecto fundamental de la programación. Python proporciona una serie de funciones y métodos para trabajar con archivos de texto y binarios de manera sencilla y eficiente.

---

## 1. Abrir un Archivo
Para abrir un archivo en Python, utilizamos la función `open()`. Esta función requiere dos parámetros principales:
- **Nombre del archivo**: Nombre del archivo que deseamos abrir.
- **Modo de apertura**: Define cómo se abrirá el archivo ('r' para lectura, 'w' para escritura, 'a' para añadir, entre otros).

### Ejemplo de Apertura en Modo Lectura:
```python
archivo = open('archivo.txt', 'r')  # Abre el archivo en modo lectura
contenido = archivo.read()  # Lee todo el contenido
print(contenido)
archivo.close()  # Cierra el archivo para liberar recursos
```

**Explicación:**
- `open()` abre el archivo.
- `read()` lee su contenido.
- `close()` cierra el archivo para evitar errores.

---

## 2. Escritura en Archivos
Podemos escribir en archivos utilizando los modos:
- `'w'`: Sobrescribe el contenido del archivo si existe, o lo crea si no existe.
- `'a'`: Añade contenido al archivo sin sobrescribir el existente.

### Ejemplo de Escritura:
```python
archivo = open('archivo.txt', 'w')  # Abrir en modo escritura
archivo.write("Hola, este es un archivo de prueba.\n")
archivo.write("Esta es una segunda línea.\n")
archivo.close()
```

### Ejemplo de Añadir Datos:
```python
archivo = open('archivo.txt', 'a')  # Abrir en modo añadir
archivo.write("Esta es una nueva línea añadida.\n")
archivo.close()
```

**Explicación:**
- `write()` escribe en el archivo.
- En el modo `'w'`, se sobrescribe el contenido.
- En el modo `'a'`, se añade información sin eliminar la existente.

---

## 3. Leer Archivos Línea por Línea
Python permite leer archivos línea por línea con los métodos `readline()` y `readlines()`.

### Leer línea por línea con `readline()`:
```python
archivo = open('archivo.txt', 'r')
linea = archivo.readline()
while linea:
    print(linea.strip())  # `.strip()` elimina saltos de línea extras
    linea = archivo.readline()
archivo.close()
```

### Leer todas las líneas con `readlines()`:
```python
archivo = open('archivo.txt', 'r')
lineas = archivo.readlines()
archivo.close()
for linea in lineas:
    print(linea.strip())
```

**Explicación:**
- `readline()` lee línea por línea.
- `readlines()` almacena todas las líneas en una lista.

---

## 4. Uso de la Declaración `with`
`with` permite manejar archivos de forma segura y automática sin necesidad de llamar a `close()`.

### Ejemplo de uso de `with`:
```python
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
```

**Explicación:**
- `with open(...) as archivo:` asegura que el archivo se cierre automáticamente.

---

## 5. Manejo de Excepciones
Es importante manejar excepciones para evitar errores si el archivo no existe o si hay problemas en su lectura o escritura.

### Ejemplo de Manejo de Excepciones:
```python
try:
    archivo = open('archivo_inexistente.txt', 'r')
except FileNotFoundError:
    print("Error: El archivo no existe.")
else:
    contenido = archivo.read()
    print(contenido)
    archivo.close()
```

**Explicación:**
- `try-except` captura errores si el archivo no existe.
- `else` se ejecuta solo si no hay errores.

---

## 6. Ejercicio de Autoevaluación
1. Crear un archivo `datos.txt` y escribir información personal.
2. Añadir más líneas con información adicional.
3. Leer y mostrar el contenido del archivo línea por línea.
4. Implementar un manejo de excepciones.

### Código Resuelto:
```python
# Crear y escribir en el archivo
txt = """Nombre: Juan Pérez\nRango: Sargento\nID: 123456\nUnidad: Infantería\n"""
with open('datos.txt', 'w') as archivo:
    archivo.write(txt)

# Leer el archivo línea por línea
try:
    with open('datos.txt', 'r') as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")
```

---

## Conclusión
Este documento explica cómo manejar archivos en Python, incluyendo lectura, escritura, manejo de excepciones y mejores prácticas como el uso de `with`.

¡Practica estos conceptos para mejorar tu dominio de la entrada y salida de archivos en Python!

