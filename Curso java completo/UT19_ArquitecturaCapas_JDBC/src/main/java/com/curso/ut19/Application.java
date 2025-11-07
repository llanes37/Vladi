package com.curso.ut19;

import com.curso.ut19.repository.UsuarioRepository;
import com.curso.ut19.repository.jdbc.UsuarioRepositoryJdbc;
import com.curso.ut19.service.UsuarioService;
import com.curso.ut19.persistence.Db;

import java.util.Scanner;

/**
 *                      📚 UT19 — ARQUITECTURA EN CAPAS CON JDBC + JUnit + Maven + Logging
 *  (Diseño de comentarios y menú al estilo UT17/UT18 — Better Comments)
 *
 * //! INTRODUCCIÓN
 * ? Teoría:
 *   - Separa la aplicación en capas: modelo ↔ repositorio ↔ servicio ↔ vista (CLI).
 *   - Repositorio oculta detalles de JDBC. Servicio aplica validaciones.
 * * Objetivo:
 *   - Refactor de prácticas UT17/UT18 a un diseño profesional.
 *
 * TODO (Alumno):
 *   - Añade casos de uso para Producto y Categoría replicando la estructura.
 */
public class Application {
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        // Wiring manual (sin DI):
        UsuarioRepository repo = new UsuarioRepositoryJdbc();
        UsuarioService service = new UsuarioService(repo);

        int opcion;
        do {
            // ================================
            // 📋 MENÚ PRINCIPAL — UT19 (estilo UT17/UT18)
            // ================================
            System.out.println("\n==================================");
            System.out.println("  MENÚ DE PRÁCTICAS - UT19 (Capas)");
            System.out.println("==================================");
            System.out.println(" 1. Insertar usuario");
            System.out.println(" 2. Listar usuarios");
            System.out.println(" 3. Actualizar usuario por ID");
            System.out.println(" 4. Eliminar usuario por ID");
            System.out.println(" 5. Salir (cerrar BD)");
            System.out.print("👉 Selecciona opción: ");
            opcion = readInt();

            switch (opcion) {
                case 1 -> insertar(service);
                case 2 -> listar(service);
                case 3 -> actualizar(service);
                case 4 -> eliminar(service);
                case 5 -> Db.close();
                default -> System.out.println("❌ Opción inválida.");
            }
        } while (opcion != 5);

        sc.close();
        System.out.println("👋 Programa finalizado. ¡Hasta luego!");
    }

    // ------------------------------------------------------
    // 📌 UTILIDADES DE ENTRADA — Lectura segura
    // ------------------------------------------------------
    private static int readInt() {
        while (!sc.hasNextInt()) { System.out.print("❌ Número inválido: "); sc.next(); }
        int val = sc.nextInt(); sc.nextLine(); return val;
    }
    private static String readNonEmpty(String prompt) {
        while (true) { System.out.print(prompt); String s = sc.nextLine().trim(); if (!s.isEmpty()) return s; System.out.println("❌ No puede estar vacío."); }
    }

    // ======================================================
    // CASOS DE USO (delegan en la capa servicio)
    // ======================================================
    private static void insertar(UsuarioService service) {
        String nombre = readNonEmpty("Nombre: ");
        System.out.print("Edad: ");
        int edad = readInt();
        try {
            var u = service.crear(nombre, edad);
            System.out.println("✅ Insertado con ID: " + u.getId());
        } catch (Exception e) {
            System.out.println("❌ " + e.getMessage());
        }
    }

    private static void listar(UsuarioService service) {
        System.out.println("ID | Nombre           | Edad");
        System.out.println("---+------------------+-----");
        service.listar().forEach(u -> System.out.printf("%2d | %-16s | %3d%n", u.getId(), u.getNombre(), u.getEdad()));
    }

    private static void actualizar(UsuarioService service) {
        System.out.print("ID a actualizar: ");
        int id = readInt();
        String nombre = readNonEmpty("Nuevo nombre: ");
        System.out.print("Nueva edad: ");
        int edad = readInt();
        try {
            boolean ok = service.actualizar(id, nombre, edad);
            System.out.println(ok ? "✅ Actualizado." : "⚠️ ID no encontrado.");
        } catch (Exception e) {
            System.out.println("❌ " + e.getMessage());
        }
    }

    private static void eliminar(UsuarioService service) {
        System.out.print("ID a eliminar: ");
        int id = readInt();
        boolean ok = service.borrar(id);
        System.out.println(ok ? "✅ Eliminado." : "⚠️ ID no encontrado.");
    }
}
