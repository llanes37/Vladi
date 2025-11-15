# Guía mejorada: Usar Git con Visual Studio Code

Esta guía mejorada explica paso a paso cómo configurar, trabajar y colaborar con Git dentro de Visual Studio Code (VS Code). Está pensada para estudiantes y desarrolladores que quieren una referencia clara y práctica.

## 0. Antes de empezar (requisitos)
- Tener instalado Git: https://git-scm.com/
- Tener instalado Visual Studio Code: https://code.visualstudio.com/
- Contar con una cuenta de GitHub (u otro servidor Git) y acceso al repositorio que vayas a clonar.

## 1. Uso de HTTPS vs SSH (recomendación)
- HTTPS: más sencillo para principiantes; pide usuario/contraseña o token (PAT).
- SSH: más seguro y cómodo a largo plazo (configura claves SSH una vez y olvídate de introducir credenciales).
Recomendación: usa SSH si vas a trabajar con repositorios frecuentemente.

## 2. Configuración inicial de Git (global)
Abre la terminal (Terminal → Nueva Terminal) y ejecuta:

    git config --global user.name "Tu Nombre"
    git config --global user.email "tu@correo.com"
    git config --global core.editor "code --wait"
    git config --global credential.helper cache        # opcional: cache temporal

Configuración para finales de línea:
- En Windows:
    git config --global core.autocrlf true
- En macOS / Linux:
    git config --global core.autocrlf input

Si vas a usar SSH, agrega tu clave pública en GitHub (https://github.com/settings/ssh/new).

## 3. Clonar un repositorio
En VS Code: 
- Abre el Command Palette (Ctrl+Shift+P / Cmd+Shift+P) → escribe "Git: Clone" → pega la URL (SSH o HTTPS).
- Selecciona la carpeta local donde clonar.
- VS Code ofrecerá abrir la carpeta clonada; acepta.

O en la terminal:

    git clone git@github.com:usuario/repositorio.git   # SSH
    git clone https://github.com/usuario/repositorio.git  # HTTPS

## 4. Flujo de trabajo recomendado (resumen)
1. Crear una rama para cada tarea/feature/ejercicio:

    git checkout -b feature/mi-cambio

2. Trabaja en tus archivos. Usa VS Code para editar y ver cambios.
3. Añade archivos al staging (preparar commit):

    git add archivo1 archivo2
    git add .        # añade todos los cambios (usar con cuidado)

4. Haz commits con mensajes claros y cortos:

    git commit -m "feat: Añadir función X (breve descripción)"

5. Sube tu rama al remoto:

    git push -u origin feature/mi-cambio

6. Abre Pull Request (PR) en GitHub para revisión (si aplica).

7. Sincroniza con main/master regularmente:

    git fetch origin
    git rebase origin/main    # o git merge origin/main

Nota: si la base del proyecto usa `master` en lugar de `main`, sustituye el nombre según corresponda.

## 5. Trabajar con VS Code (interfaz)
- Vista Control de Código Fuente (ícono de ramas): lista cambios sin staged/staged.
- Hacer stage: pasar cambios a "Staged Changes" (clic en + o en el archivo).
- Escribir mensaje de commit en la caja superior y hacer commit (✔️) o usar Ctrl+Enter.
- Sincronizar (Push/Pull): botón de sincronización en la barra de estado o menú de los tres puntos (…).
- Crear/cambiar ramas: clic en el nombre de la rama en la esquina inferior izquierda.
- Abrir el Command Palette para comandos Git rápidos: "Git: " → ver opciones.

Extensiones útiles:
- GitLens — mejor historial, anotaciones (blame) y navegación del repo.
- Git Graph — visualiza el grafo de commits y facilita merges/rebases visuales.

## 6. Resolución de conflictos
Si al hacer pull/push hay conflictos:
- VS Code mostrará los archivos en conflicto y botones para elegir "Aceptar entrada actual", "Aceptar entrada entrante" o "Aceptar ambos cambios".
- Edita los conflictos manualmente si es necesario, luego:

    git add archivo-resuelto
    git commit -m "fix: Resolver conflicto en archivo-resuelto"

Si usaste rebase y quieres abortarlo:

    git rebase --abort

## 7. Comandos útiles (rapida referencia)
- Estado: git status
- Ver cambios: git diff (o en VS Code: vista diff)
- Ver log: git log --oneline --graph --all
- Volver a un archivo sin commitear: git checkout -- archivo
- Modificar último commit: git commit --amend -m "Nuevo mensaje"
- Guardar cambios temporales: git stash; recuperar: git stash pop
- Borrar una rama local: git branch -d nombre-rama

## 8. Buenas prácticas para commits y ramas
- Commits atómicos y con mensajes descriptivos.
- Una rama por tarea/ejercicio. Nombres con convenciones: feature/, fix/, chore/.
- Hacer PRs pequeños y revisables.

## 9. Subir cambios finales (Push)
- Si tu rama ya está enlazada al remoto:

    git push

- Si es la primera vez que subes la rama:

    git push -u origin nombre-rama

En VS Code: usa el botón de sincronizar o el menú … → Push.

## 10. Consejos y trucos rápidos
- Usa GitLens para ver quién cambió una línea y por qué.
- Configura un .gitignore desde https://gitignore.io/ según tu proyecto.
- Para evitar pedir credenciales repetidamente con HTTPS, crea un Personal Access Token (PAT) y/o usa el credential helper.
- Rebase vs Merge: rebase mantiene un historial lineal (más limpio), merge preserva el orden real de merges.

---

Con esto tendrás una guía práctica y clara para usar Git en VS Code. Si quieres, puedo:
- Crear este archivo en tu repo (nombrado Git/guia_git_vscode_mejorada.md).
- O adaptarlo con tu convención de ramas, comandos en Windows, o incluir capturas de pantalla.