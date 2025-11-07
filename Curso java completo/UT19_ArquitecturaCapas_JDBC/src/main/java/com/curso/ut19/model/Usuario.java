package com.curso.ut19.model;

/**
 * //! ENTIDAD DE DOMINIO: Usuario
 * ? Teoría: POJO sencillo con id, nombre y edad.
 * TODO (Alumno): Añade equals/hashCode y toString si lo necesitas.
 */
public class Usuario {
    private Integer id;
    private String nombre;
    private int edad;

    public Usuario() {}

    public Usuario(Integer id, String nombre, int edad) {
        this.id = id;
        this.nombre = nombre;
        this.edad = edad;
    }

    public Usuario(String nombre, int edad) {
        this(null, nombre, edad);
    }

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public int getEdad() { return edad; }
    public void setEdad(int edad) { this.edad = edad; }
}
