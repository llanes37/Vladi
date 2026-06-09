# 📚 GUÍA COMPLETA DE BASES DE DATOS
> Teoría + Práctica + Herramientas + Ejercicios guiados con IA

---

## ÍNDICE

1. [¿Qué es una Base de Datos?](#1-qué-es-una-base-de-datos)
2. [Bases de Datos Relacionales (SQL)](#2-bases-de-datos-relacionales-sql)
3. [Bases de Datos No Relacionales (NoSQL)](#3-bases-de-datos-no-relacionales-nosql)
4. [Comparativa SQL vs NoSQL](#4-comparativa-sql-vs-nosql)
5. [Gestores de Bases de Datos más importantes](#5-gestores-de-bases-de-datos-más-importantes)
6. [Herramientas en VS Code](#6-herramientas-en-vs-code)
7. [Herramientas externas gratuitas](#7-herramientas-externas-gratuitas)
8. [Modelado y Diseño de BBDD](#8-modelado-y-diseño-de-bbdd)
9. [SQL Práctico desde cero](#9-sql-práctico-desde-cero)
10. [Ejercicios Prácticos con IA](#10-ejercicios-prácticos-con-ia)
11. [Proyecto Final: BBDD de cero](#11-proyecto-final-bbdd-de-cero)

---

## 1. ¿Qué es una Base de Datos?

Una **base de datos** es un sistema organizado para almacenar, gestionar y recuperar información de forma eficiente.

```
DATO → INFORMACIÓN → BASE DE DATOS → SISTEMA DE GESTIÓN (SGBD/DBMS)
```

### Conceptos clave

| Término | Significado |
|---|---|
| **BBDD / DB** | Base de Datos |
| **SGBD / DBMS** | Sistema Gestor de Base de Datos (MySQL, PostgreSQL, MongoDB...) |
| **Tabla / Colección** | Estructura donde se guardan los datos |
| **Fila / Documento** | Un registro individual |
| **Columna / Campo** | Un atributo de cada registro |
| **Query / Consulta** | Petición para obtener o modificar datos |
| **Índice** | Estructura que acelera las búsquedas |
| **Transacción** | Conjunto de operaciones que se ejecutan como una sola unidad |

### Tipos de bases de datos (visión general)

```
BASES DE DATOS
│
├── RELACIONALES (SQL)
│   ├── MySQL
│   ├── PostgreSQL
│   ├── SQLite
│   ├── Oracle
│   └── SQL Server
│
└── NO RELACIONALES (NoSQL)
    ├── Documentos → MongoDB, Firestore
    ├── Clave-Valor → Redis, DynamoDB
    ├── Columnar → Cassandra, HBase
    └── Grafos → Neo4j, ArangoDB
```

---

## 2. Bases de Datos Relacionales (SQL)

### ¿Qué son?

Organizan los datos en **tablas** con **filas** y **columnas**. Las tablas se relacionan entre sí mediante **claves**.

### Conceptos fundamentales

#### Clave Primaria (PRIMARY KEY)
Identifica de forma **única** cada fila de una tabla.
```sql
CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY,  -- No puede repetirse ni ser NULL
    nombre TEXT NOT NULL,
    edad INTEGER
);
```

#### Clave Foránea (FOREIGN KEY)
Relaciona una tabla con otra.
```sql
CREATE TABLE matriculas (
    id INTEGER PRIMARY KEY,
    alumno_id INTEGER,
    curso_id INTEGER,
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);
```

#### Tipos de relaciones

| Tipo | Ejemplo | Cómo se implementa |
|---|---|---|
| **1:1** (uno a uno) | Persona ↔ DNI | FK en cualquiera de las dos tablas |
| **1:N** (uno a muchos) | Profesor → Alumnos | FK en la tabla del "muchos" |
| **N:M** (muchos a muchos) | Alumnos ↔ Cursos | Tabla intermedia (pivot) |

#### Normalización (simplificada)

| Forma Normal | Regla principal |
|---|---|
| **1FN** | Cada celda contiene un solo valor |
| **2FN** | Todo depende de la clave completa |
| **3FN** | Nada depende de columnas que no sean clave |

```
Sin normalizar:
┌──────────────────────────────────────────────────────┐
│ alumno_id │ nombre │ curso1      │ curso2      │ ... │
│ 1         │ Ana    │ Matemáticas │ Historia    │ ... │
└──────────────────────────────────────────────────────┘

Normalizado (3FN):
Tabla alumnos: id, nombre
Tabla cursos: id, nombre
Tabla matriculas: alumno_id, curso_id
```

### ACID — Las 4 propiedades de las transacciones

| Propiedad | Significado |
|---|---|
| **A**tomicity | Todo o nada. Si falla algo, se deshace todo |
| **C**onsistency | La BBDD siempre pasa de un estado válido a otro válido |
| **I**solation | Las transacciones no se interfieren entre sí |
| **D**urability | Lo que se confirma (COMMIT) queda guardado permanentemente |

---

## 3. Bases de Datos No Relacionales (NoSQL)

### ¿Cuándo usar NoSQL?

- Datos sin estructura fija o que cambia mucho
- Necesitas escalar horizontalmente (millones de registros)
- Alta velocidad de lectura/escritura
- Datos en forma de JSON, grafos, o series temporales

### Tipos de NoSQL

---

### 3.1 Orientadas a Documentos

Almacenan datos como **documentos JSON/BSON**. Cada documento puede tener estructura diferente.

**Gestores:** MongoDB, CouchDB, Firestore (Firebase)

```json
// Ejemplo MongoDB — colección "alumnos"
{
  "_id": "ObjectId('abc123')",
  "nombre": "Ana García",
  "edad": 22,
  "cursos": ["Matemáticas", "Historia"],
  "direccion": {
    "ciudad": "Madrid",
    "cp": "28001"
  }
}
```

**Cuándo usarla:**
- Catálogos de productos (e-commerce)
- Perfiles de usuario
- CMS (blogs, contenido)

---

### 3.2 Clave-Valor (Key-Value)

Los datos se guardan como pares `clave → valor`. Extremadamente rápidas.

**Gestores:** Redis, DynamoDB, Memcached

```
SET usuario:1001:nombre "Carlos"
SET usuario:1001:sesion "token_xyz123"
GET usuario:1001:nombre  → "Carlos"
```

**Cuándo usarla:**
- Caché (guardar resultados temporales)
- Sesiones de usuario
- Colas de mensajes

---

### 3.3 Columnar (Wide-Column)

Organizan los datos por **columnas** en lugar de por filas. Ideales para analítica masiva.

**Gestores:** Apache Cassandra, HBase, Google Bigtable

```
Fila: usuario_123
  columna: nombre → "Laura"
  columna: email → "laura@mail.com"
  columna: última_conexión → "2026-06-09"
```

**Cuándo usarla:**
- Series temporales (IoT, logs)
- Analítica de big data
- Historial de actividad

---

### 3.4 Bases de Datos de Grafos

Los datos son **nodos** conectados por **aristas** (relaciones). Perfectas para redes sociales, recomendaciones.

**Gestores:** Neo4j, ArangoDB, Amazon Neptune

```
(Ana)-[:AMIGA_DE]->(Carlos)
(Carlos)-[:TRABAJA_EN]->(Empresa_X)
(Ana)-[:LE_GUSTA]->(Python)
```

**Cuándo usarla:**
- Redes sociales
- Motores de recomendación
- Detección de fraude
- Mapas y rutas

---

## 4. Comparativa SQL vs NoSQL

| Característica | SQL (Relacional) | NoSQL |
|---|---|---|
| **Estructura** | Tablas fijas con esquema | Flexible, sin esquema fijo |
| **Lenguaje** | SQL estándar | Varía por gestor |
| **Escalado** | Vertical (más potencia al servidor) | Horizontal (más servidores) |
| **Transacciones** | ACID completo | Eventual consistency (BASE) |
| **Relaciones** | Nativas con JOIN | Embebidas o referencias manuales |
| **Consistencia** | Alta | Variable |
| **Velocidad escritura** | Media | Muy alta (key-value, columnar) |
| **Curva aprendizaje** | Media | Alta (depende del tipo) |
| **Uso principal** | Negocio, finanzas, ERPs | Web, big data, tiempo real |

### ¿Cuál elegir?

```
¿Los datos tienen estructura fija y relaciones complejas?
  → SQL (PostgreSQL, MySQL)

¿Necesitas flexibilidad de esquema y escalar rápido?
  → MongoDB (documentos)

¿Necesitas velocidad extrema y caché?
  → Redis (clave-valor)

¿Son datos de red o con muchas relaciones complejas?
  → Neo4j (grafos)

¿Son series temporales o logs masivos?
  → Cassandra o InfluxDB
```

---

## 5. Gestores de Bases de Datos más importantes

### SQL

#### PostgreSQL
- **Tipo:** Relacional, open source
- **Puntos fuertes:** El más potente y completo. Soporta JSON, arrays, funciones avanzadas, extensiones
- **Usos típicos:** Aplicaciones empresariales, backend robusto, finanzas
- **Instalación:** [postgresql.org](https://www.postgresql.org/)
- **Puerto por defecto:** 5432

#### MySQL / MariaDB
- **Tipo:** Relacional, open source (MySQL es de Oracle, MariaDB es el fork libre)
- **Puntos fuertes:** El más popular en web. Rápido, fácil de usar, muy documentado
- **Usos típicos:** WordPress, PHP apps, proyectos web
- **Puerto por defecto:** 3306

#### SQLite
- **Tipo:** Relacional, archivo único, sin servidor
- **Puntos fuertes:** Sin instalación, el archivo ES la BBDD. Perfecto para aprender y proyectos pequeños
- **Usos típicos:** Apps móviles, prototipos, aprendizaje, ficheros locales
- **Puerto:** No aplica (es un fichero .db o .sqlite)

```
💡 Para aprender SQL → empieza con SQLite (cero configuración)
💡 Para proyectos web → MySQL o PostgreSQL
💡 Para producción seria → PostgreSQL
```

#### Oracle Database
- **Tipo:** Relacional, propietario
- **Puntos fuertes:** El más robusto para grandes empresas, bancos, hospitales
- **Usos típicos:** Banca, sector público, grandes corporaciones
- **Nota:** De pago, pero tiene versión Express gratuita

#### Microsoft SQL Server
- **Tipo:** Relacional, propietario (Microsoft)
- **Puntos fuertes:** Integración total con ecosistema Microsoft (.NET, Azure, Windows)
- **Usos típicos:** Empresas con stack Microsoft
- **Nota:** Versión Express gratuita

---

### NoSQL

#### MongoDB
- **Tipo:** Documentos (JSON/BSON)
- **Puntos fuertes:** El NoSQL más popular, gran ecosistema, Atlas (cloud gratuito)
- **Puerto por defecto:** 27017
- **Web:** [mongodb.com](https://www.mongodb.com/)

#### Redis
- **Tipo:** Clave-Valor (en memoria)
- **Puntos fuertes:** El más rápido del mundo para caché y sesiones
- **Puerto por defecto:** 6379

#### Firebase / Firestore
- **Tipo:** Documentos + tiempo real
- **Puntos fuertes:** Sin servidor, sincronización en tiempo real, perfecto para apps móviles
- **Web:** [firebase.google.com](https://firebase.google.com)

#### Cassandra
- **Tipo:** Columnar distribuido
- **Puntos fuertes:** Escala masiva, alta disponibilidad, usado por Netflix, Uber
- **Puerto por defecto:** 9042

---

## 6. Herramientas en VS Code

### Extensiones esenciales

---

#### SQLite (por alexcvzz)
- **ID:** `alexcvzz.vscode-sqlite`
- **Para:** SQLite
- **Funciones:** Ver, editar y consultar archivos .db/.sqlite directamente en VS Code
- **Cómo usarla:**
  1. Click derecho en archivo `.db` → "Open Database"
  2. Panel lateral "SQLite Explorer" para ver tablas
  3. `Ctrl+Shift+P` → "SQLite: New Query" para escribir SQL

---

#### MySQL (por cweijan)
- **ID:** `cweijan.vscode-mysql`
- **Para:** MySQL, MariaDB
- **Funciones:** Conectar a servidor MySQL, explorar BBDD, ejecutar queries
- **Cómo conectar:**
  ```
  Host: localhost
  Port: 3306
  User: root
  Password: tu_password
  ```

---

#### Database Client PLUS (por cweijan) ⭐ MÁS COMPLETA
- **ID:** `cweijan.vscode-database-client2`
- **Para:** MySQL, PostgreSQL, SQLite, MongoDB, Redis, y más
- **Funciones:**
  - Gestor visual completo para múltiples gestores
  - Editor SQL con autocompletado
  - Exportar/importar datos
  - Diagrama ER visual
- **Recomendada si quieres una sola extensión para todo**

---

#### PostgreSQL (por Chris Kolkman)
- **ID:** `ckolkman.vscode-postgres`
- **Para:** PostgreSQL
- **Funciones:** Conectar, explorar schemas, ejecutar queries, autocompletado SQL

---

#### MongoDB for VS Code (oficial)
- **ID:** `mongodb.mongodb-vscode`
- **Para:** MongoDB
- **Funciones:** Conectar a MongoDB Atlas o local, explorar colecciones, Playground para queries

---

#### Thunder Client (para APIs + BBDD via REST)
- **ID:** `rangav.vscode-thunder-client`
- **Para:** Probar APIs REST que interactúan con BBDD
- **Útil para:** Cuando tu backend expone una API sobre la BBDD

---

#### ERD Editor (para diseño visual)
- **ID:** `dineug.vuerd-vscode`
- **Para:** Diseñar esquemas de BBDD visualmente (tablas, relaciones)
- **Funciones:** Crear diagramas ER, exportar a SQL

---

### Resumen de extensiones por gestor

| Gestor | Extensión recomendada |
|---|---|
| SQLite | `alexcvzz.vscode-sqlite` |
| MySQL/MariaDB | `cweijan.vscode-mysql` |
| PostgreSQL | `ckolkman.vscode-postgres` |
| MongoDB | `mongodb.mongodb-vscode` |
| Todo en uno | `cweijan.vscode-database-client2` |
| Diseño ER | `dineug.vuerd-vscode` |

---

## 7. Herramientas Externas Gratuitas

### Para SQL

#### DBeaver (IMPRESCINDIBLE) ⭐
- **Web:** dbeaver.io
- **Para:** MySQL, PostgreSQL, SQLite, Oracle, SQL Server, y más de 80 gestores
- **Por qué usarla:**
  - Interfaz visual potente
  - Editor SQL con autocompletado
  - Diagramas ER automáticos
  - Exportar datos a CSV, Excel, JSON
  - Completamente gratuita
- **Ideal para:** Gestionar cualquier BBDD desde una sola herramienta

#### TablePlus
- **Web:** tableplus.com
- **Por qué:** Interfaz limpia y moderna. Versión gratuita limitada pero muy usable
- **Para:** MySQL, PostgreSQL, SQLite, Redis, MongoDB

#### DB Browser for SQLite
- **Web:** sqlitebrowser.org
- **Para:** Exclusivamente SQLite
- **Por qué:** La herramienta visual más sencilla para explorar y editar archivos .db

#### HeidiSQL
- **Web:** heidisql.com
- **Para:** MySQL, MariaDB, PostgreSQL, SQL Server
- **Por qué:** Muy ligera y rápida, popular en Windows

---

### Para MongoDB

#### MongoDB Compass (oficial)
- **Web:** mongodb.com/compass
- **Por qué:** Herramienta oficial, interfaz visual completa para explorar y consultar MongoDB
- **Gratis**

#### MongoDB Atlas (cloud)
- **Web:** cloud.mongodb.com
- **Por qué:** Cluster gratuito en la nube (512MB), sin instalar nada
- **Perfecto para:** Empezar sin instalar MongoDB localmente

---

### Para Redis

#### RedisInsight (oficial)
- **Web:** redis.io/insight
- **Por qué:** Herramienta visual oficial para explorar datos en Redis

---

### Herramientas online (sin instalar nada)

| Herramienta | URL | Para qué |
|---|---|---|
| **SQLiteOnline** | sqliteonline.com | SQL en el navegador, cero instalación |
| **DB Fiddle** | dbfiddle.uk | Probar SQL en MySQL/PostgreSQL/SQLite online |
| **SQL Fiddle** | sqlfiddle.com | Compartir y probar queries SQL |
| **Mongo Playground** | mongoplayground.net | Probar queries MongoDB online |
| **drawSQL** | drawsql.app | Diseñar esquemas ER online |
| **dbdiagram.io** | dbdiagram.io | Diseñar BBDD con código (DBML) |

---

## 8. Modelado y Diseño de BBDD

### Diagrama Entidad-Relación (ER)

Antes de crear una BBDD se diseña el modelo conceptual.

```
[Alumno] ──────────< [Matricula] >────────── [Curso]
  │                                              │
  id (PK)                                     id (PK)
  nombre                                      nombre
  email                                       duracion
  fecha_nacimiento                            precio
```

### Pasos para diseñar una BBDD

```
1. ANÁLISIS → ¿Qué información necesito guardar?
2. ENTIDADES → ¿Cuáles son los "objetos" principales?
3. ATRIBUTOS → ¿Qué datos tiene cada entidad?
4. RELACIONES → ¿Cómo se conectan las entidades?
5. CARDINALIDAD → ¿1:1, 1:N, N:M?
6. NORMALIZACIÓN → ¿Está bien diseñado? ¿Hay redundancia?
7. CREACIÓN → Escribir el SQL (DDL)
8. POBLAR → Insertar datos de prueba
9. CONSULTAR → Probar con queries
```

### Ejemplo: Sistema de una academia

```
ENTIDADES:
- Alumno (id, nombre, email, teléfono)
- Profesor (id, nombre, especialidad)
- Curso (id, nombre, precio, duración_horas)
- Matrícula (id, alumno_id, curso_id, fecha, estado)
- Clase (id, curso_id, profesor_id, fecha_hora, aula)

RELACIONES:
- Un Alumno puede tener muchas Matrículas (1:N)
- Una Matrícula pertenece a un Curso (N:1)
- Un Curso puede tener muchos Profesores y viceversa (N:M) → tabla Asignaciones
- Una Clase pertenece a un Curso (N:1)
- Una Clase la imparte un Profesor (N:1)
```

---

## 9. SQL Práctico desde cero

### DDL — Definir estructura

```sql
-- Crear base de datos
CREATE DATABASE academia;

-- Crear tabla
CREATE TABLE alumnos (
    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
    nombre      TEXT        NOT NULL,
    apellidos   TEXT        NOT NULL,
    email       TEXT        UNIQUE NOT NULL,
    telefono    TEXT,
    fecha_alta  DATE        DEFAULT CURRENT_DATE
);

-- Modificar tabla (añadir columna)
ALTER TABLE alumnos ADD COLUMN activo BOOLEAN DEFAULT 1;

-- Eliminar tabla
DROP TABLE IF EXISTS alumnos;
```

### DML — Manipular datos

```sql
-- Insertar
INSERT INTO alumnos (nombre, apellidos, email)
VALUES ('Ana', 'García López', 'ana@mail.com');

-- Insertar varios
INSERT INTO alumnos (nombre, apellidos, email) VALUES
('Carlos', 'Martínez', 'carlos@mail.com'),
('Laura', 'Pérez', 'laura@mail.com'),
('Pedro', 'Ruiz', 'pedro@mail.com');

-- Actualizar
UPDATE alumnos
SET telefono = '612345678'
WHERE id = 1;

-- Eliminar (con cuidado)
DELETE FROM alumnos WHERE id = 5;
```

### DQL — Consultar datos

```sql
-- Consulta básica
SELECT * FROM alumnos;

-- Filtrar
SELECT nombre, email FROM alumnos
WHERE activo = 1
ORDER BY nombre ASC;

-- Limitar resultados
SELECT * FROM alumnos LIMIT 10 OFFSET 20;

-- Contar
SELECT COUNT(*) AS total_alumnos FROM alumnos;

-- Agrupar
SELECT fecha_alta, COUNT(*) AS altas_ese_dia
FROM alumnos
GROUP BY fecha_alta
HAVING COUNT(*) > 1;
```

### JOINs — Unir tablas

```sql
-- INNER JOIN: solo registros que coinciden en ambas tablas
SELECT a.nombre, c.nombre AS curso
FROM alumnos a
INNER JOIN matriculas m ON a.id = m.alumno_id
INNER JOIN cursos c ON m.curso_id = c.id;

-- LEFT JOIN: todos los alumnos, aunque no tengan matrícula
SELECT a.nombre, c.nombre AS curso
FROM alumnos a
LEFT JOIN matriculas m ON a.id = m.alumno_id
LEFT JOIN cursos c ON m.curso_id = c.id;

-- Diagrama mental de JOINs:
--
-- INNER JOIN:  A ∩ B  (solo la intersección)
-- LEFT JOIN:   A + (A ∩ B)  (todo A, más lo que coincide)
-- RIGHT JOIN:  B + (A ∩ B)  (todo B, más lo que coincide)
-- FULL JOIN:   A ∪ B  (todo)
```

### Funciones de agregado

```sql
SELECT
    COUNT(*)        AS total,
    AVG(precio)     AS precio_medio,
    MAX(precio)     AS precio_max,
    MIN(precio)     AS precio_min,
    SUM(precio)     AS ingresos_totales
FROM cursos;
```

### Subconsultas

```sql
-- Alumnos que se matricularon en algún curso de más de 100€
SELECT nombre FROM alumnos
WHERE id IN (
    SELECT alumno_id FROM matriculas
    WHERE curso_id IN (
        SELECT id FROM cursos WHERE precio > 100
    )
);
```

### Índices (optimización)

```sql
-- Crear índice para búsquedas frecuentes por email
CREATE INDEX idx_alumnos_email ON alumnos(email);

-- Índice único
CREATE UNIQUE INDEX idx_alumnos_email ON alumnos(email);

-- Ver índices (SQLite)
PRAGMA index_list('alumnos');
```

---

## 10. Ejercicios Prácticos con IA

### Cómo usar la IA para practicar bases de datos

Puedes pedirle a Claude o cualquier IA que te genere ejercicios, datos de prueba, y te corrija queries. Aquí tienes **prompts** listos para copiar y pegar:

---

### Prompts para generar una BBDD desde cero

```
PROMPT 1 — Crear esquema completo:
"Actúa como profesor de bases de datos. Quiero practicar SQL.
Diseña una base de datos para una [tienda de ropa / clínica veterinaria / 
biblioteca / videoclub / gimnasio]. Dime:
1. Las entidades y sus atributos
2. Las relaciones entre ellas (con cardinalidad)
3. El SQL CREATE TABLE completo para SQLite
4. 20 filas de datos de prueba con INSERT INTO
5. 10 ejercicios de consulta SELECT de dificultad progresiva"
```

```
PROMPT 2 — Practicar JOINs:
"Tengo esta base de datos: [pega tu esquema].
Genera 5 ejercicios que requieran usar JOINs entre al menos 2 tablas.
Para cada ejercicio: el enunciado en español, la solución SQL,
y una explicación de por qué se usa ese tipo de JOIN."
```

```
PROMPT 3 — Que te corrija tus queries:
"Tengo esta tabla: [pega el CREATE TABLE].
Quiero obtener: [describe en español qué quieres].
He escrito esta query: [pega tu SQL].
¿Es correcta? Si no, explícame el error y dame la solución."
```

```
PROMPT 4 — Practicar diseño:
"Dame un caso de negocio real: una descripción de una empresa
con sus necesidades de datos. Solo la descripción, sin el diseño.
Yo haré el modelo ER y luego tú lo corriges."
```

```
PROMPT 5 — Casos de error comunes:
"Enséñame los 5 errores más comunes que cometen los principiantes
en SQL con este tipo de base de datos: [pega esquema].
Para cada error, muéstrame la query incorrecta y la correcta."
```

```
PROMPT 6 — MongoDB:
"Quiero practicar MongoDB. Diseña una base de datos de documentos
para [red social / sistema de pedidos / plataforma de cursos].
Dame:
1. La estructura de los documentos (JSON)
2. 10 documentos de ejemplo para insertar
3. 8 queries de práctica con explicación
4. Cuándo tiene sentido embeber vs referenciar en este caso"
```

---

### Ejercicios base para empezar ahora mismo

#### Ejercicio 1 — SQLite desde cero (nivel iniciación)

**Objetivo:** Crear y consultar tu primera BBDD real

```sql
-- 1. Crea este archivo: academia.db (con DB Browser o extensión SQLite)
-- 2. Ejecuta este código:

CREATE TABLE alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    email TEXT UNIQUE,
    nota_media REAL
);

CREATE TABLE cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    duracion_horas INTEGER,
    precio REAL
);

CREATE TABLE matriculas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno_id INTEGER REFERENCES alumnos(id),
    curso_id INTEGER REFERENCES cursos(id),
    fecha_matricula DATE DEFAULT CURRENT_DATE
);

-- 3. Inserta 5 alumnos, 3 cursos, y 7 matrículas
-- 4. Responde estas preguntas con SQL:
--    a) ¿Cuántos alumnos hay en total?
--    b) ¿Qué alumnos están matriculados en el curso "Python"?
--    c) ¿Cuántos alumnos tiene cada curso?
--    d) ¿Qué alumnos no tienen ninguna matrícula?
--    e) ¿Cuál es la nota media de los alumnos matriculados en cada curso?
```

#### Ejercicio 2 — Diseño ER (nivel iniciación)

**Objetivo:** Diseñar antes de programar

```
Diseña en papel o en dbdiagram.io la BBDD para:
"Una aplicación de gestión de una veterinaria que necesita guardar:
- Datos de mascotas y sus dueños
- Veterinarios que trabajan en la clínica
- Visitas/consultas realizadas
- Tratamientos y medicamentos recetados"

Pasos:
1. Identifica las entidades (mínimo 4)
2. Define los atributos de cada una
3. Establece las relaciones y su cardinalidad
4. Escribe el SQL CREATE TABLE
5. Pide a la IA que lo revise
```

---

## 11. Proyecto Final: BBDD de cero

### El reto completo

Implementa una base de datos completa siguiendo todos los pasos del proceso real:

---

### Paso 1 — Elegir el dominio

Escoge uno de estos escenarios (o el que prefieras):

| Opción | Descripción |
|---|---|
| A | Sistema de pedidos de un restaurante |
| B | Plataforma de alquiler de películas |
| C | Gestión de un torneo de eSports |
| D | Sistema de reservas de un hotel |
| E | Red social básica (posts, likes, seguidos) |

---

### Paso 2 — Análisis de requisitos

Escribe (en texto) qué información necesitas guardar. Ejemplo para opción A:
```
- Necesito saber qué mesas hay y su capacidad
- Los clientes que hacen pedidos (puede ser sin cuenta)
- Qué productos hay en el menú con su precio
- Los pedidos: qué mesa, qué productos, a qué hora
- Los camareros que atienden cada mesa
- El estado del pedido: pendiente, en cocina, servido, cobrado
```

---

### Paso 3 — Modelo ER

Dibuja el diagrama. Herramientas recomendadas:
- **Online:** dbdiagram.io (puedes escribir código DBML)
- **VS Code:** Extensión ERD Editor
- **Manual:** Papel y boli también vale

---

### Paso 4 — SQL DDL (creación)

```sql
-- Crea todas las tablas con:
-- ✓ Claves primarias
-- ✓ Claves foráneas
-- ✓ Restricciones NOT NULL donde corresponda
-- ✓ Valores por defecto donde tenga sentido
-- ✓ Tipos de dato correctos
```

---

### Paso 5 — Poblar la BBDD

Inserta datos de prueba realistas:
- Mínimo 10 filas en las tablas principales
- Usa la IA para generar INSERTs si lo necesitas

---

### Paso 6 — Consultas obligatorias

Implementa al menos estas queries:
```
1. Listado completo con JOIN de al menos 3 tablas
2. Consulta con GROUP BY y HAVING
3. Subconsulta con IN o EXISTS
4. Consulta que use LEFT JOIN para mostrar registros sin relación
5. Estadísticas con AVG, COUNT, SUM
```

---

### Paso 7 — Optimización

```sql
-- Añade índices en las columnas que más consultas
-- Explica con un comentario por qué cada índice tiene sentido
```

---

### Paso 8 — Documentación

Crea un `README.md` en tu proyecto con:
- Descripción del dominio
- Diagrama ER (imagen o texto)
- Instrucciones para ejecutarlo
- Ejemplos de queries con su resultado esperado

---

### Checklist de entrega

```
[ ] Modelo ER diseñado antes de escribir código
[ ] Todas las tablas tienen PRIMARY KEY
[ ] Las relaciones usan FOREIGN KEY
[ ] Datos insertados (mínimo 10 filas por tabla principal)
[ ] 6 queries implementadas y documentadas
[ ] Al menos 1 índice añadido con justificación
[ ] README.md con diagrama y descripción
[ ] Probado en DBeaver o DB Browser que todo funciona
```

---

## Recursos adicionales

### Para seguir aprendiendo

| Recurso | URL | Para qué |
|---|---|---|
| **SQLBolt** | sqlbolt.com | Aprender SQL interactivo, paso a paso |
| **Mode SQL Tutorial** | mode.com/sql-tutorial | SQL para análisis de datos |
| **MongoDB University** | university.mongodb.com | Cursos oficiales MongoDB gratis |
| **Use The Index, Luke** | use-the-index-luke.com | Optimización y rendimiento SQL |
| **pgExercises** | pgexercises.com | Ejercicios PostgreSQL online |

### Cheatsheet rápida SQL

```sql
-- ESTRUCTURA
CREATE TABLE / ALTER TABLE / DROP TABLE

-- DATOS
INSERT INTO / UPDATE ... SET / DELETE FROM

-- CONSULTAS
SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT

-- JOINS
INNER JOIN / LEFT JOIN / RIGHT JOIN / FULL OUTER JOIN

-- FUNCIONES
COUNT() / SUM() / AVG() / MAX() / MIN()
UPPER() / LOWER() / LENGTH() / SUBSTR()
DATE() / STRFTIME() (SQLite)

-- RESTRICCIONES
PRIMARY KEY / FOREIGN KEY / UNIQUE / NOT NULL / DEFAULT / CHECK

-- OTROS
CREATE INDEX / EXPLAIN / PRAGMA (SQLite)
BEGIN / COMMIT / ROLLBACK (transacciones)
```

---

*Documento creado para práctica autodidacta con IA — actualizable conforme avances*
