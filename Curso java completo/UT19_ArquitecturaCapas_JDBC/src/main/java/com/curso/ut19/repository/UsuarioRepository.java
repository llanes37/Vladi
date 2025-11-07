package com.curso.ut19.repository;

import com.curso.ut19.model.Usuario;
import java.util.List;
import java.util.Optional;

/**
 * //! REPOSITORY (puerto) para Usuario
 */
public interface UsuarioRepository {
    Usuario save(Usuario u);
    Optional<Usuario> findById(int id);
    List<Usuario> findAll();
    boolean update(Usuario u);
    boolean delete(int id);
}
