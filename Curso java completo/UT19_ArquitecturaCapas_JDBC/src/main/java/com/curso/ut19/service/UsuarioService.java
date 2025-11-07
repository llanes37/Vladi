package com.curso.ut19.service;

import com.curso.ut19.model.Usuario;
import com.curso.ut19.repository.UsuarioRepository;

import java.util.List;
import java.util.Optional;

/**
 * //! SERVICIO (reglas de negocio)
 * ? Teoría: La capa servicio aplica validaciones antes de delegar en el repositorio.
 * TODO (Alumno): Añade más reglas (longitud mínima, caracteres no permitidos, etc.).
 */
public class UsuarioService {
    private final UsuarioRepository repository;

    public UsuarioService(UsuarioRepository repository) {
        this.repository = repository;
    }

    public Usuario crear(String nombre, int edad) {
        validar(nombre, edad);
        return repository.save(new Usuario(nombre, edad));
    }

    public Optional<Usuario> obtener(int id) {
        return repository.findById(id);
    }

    public List<Usuario> listar() {
        return repository.findAll();
    }

    public boolean actualizar(int id, String nombre, int edad) {
        validar(nombre, edad);
        return repository.update(new Usuario(id, nombre, edad));
    }

    public boolean borrar(int id) {
        return repository.delete(id);
    }

    private void validar(String nombre, int edad) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre no puede estar vacío");
        }
        if (edad < 0) {
            throw new IllegalArgumentException("La edad no puede ser negativa");
        }
    }
}
