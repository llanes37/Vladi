package com.curso.ut19.persistence;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * //! GESTOR DE CONEXIÓN JDBC (SQLite)
 * ? Teoría:
 *   - Centralizamos la creación de la Connection.
 *   - Activamos claves foráneas y creamos tablas si no existen.
 * * Buenas prácticas:
 *   - Una conexión por aplicación en ejercicios pequeños (demo/CLI).
 */
public class Db {
    private static final Logger log = LoggerFactory.getLogger(Db.class);
    private static Connection connection;

    public static Connection getConnection() {
        if (connection == null) {
            try {
                Class.forName("org.sqlite.JDBC");
                connection = DriverManager.getConnection("jdbc:sqlite:miBaseDatos.db");
                try (Statement st = connection.createStatement()) {
                    st.execute("PRAGMA foreign_keys = ON");
                    st.execute("CREATE TABLE IF NOT EXISTS usuarios (" +
                            "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                            "nombre TEXT NOT NULL, " +
                            "edad INTEGER NOT NULL CHECK(edad >= 0))");
                }
                log.info("Conexión SQLite abierta en miBaseDatos.db");
            } catch (SQLException | ClassNotFoundException e) {
                throw new RuntimeException("Error abriendo conexión SQLite", e);
            }
        }
        return connection;
    }

    public static void close() {
        if (connection != null) {
            try {
                connection.close();
                log.info("Conexión SQLite cerrada");
            } catch (SQLException e) {
                log.error("Error cerrando conexión", e);
            }
            connection = null;
        }
    }
}
