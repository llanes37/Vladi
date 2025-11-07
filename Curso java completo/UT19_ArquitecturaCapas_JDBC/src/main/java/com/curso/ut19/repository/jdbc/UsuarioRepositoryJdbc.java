package com.curso.ut19.repository.jdbc;

import com.curso.ut19.model.Usuario;
import com.curso.ut19.persistence.Db;
import com.curso.ut19.repository.UsuarioRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * //! IMPLEMENTACIÓN JDBC de UsuarioRepository
 * ? Teoría: Acceso a datos con PreparedStatement y mapeo manual de ResultSet ➜ Usuario.
 */
public class UsuarioRepositoryJdbc implements UsuarioRepository {
    private static final Logger log = LoggerFactory.getLogger(UsuarioRepositoryJdbc.class);

    @Override
    public Usuario save(Usuario u) {
        String sql = "INSERT INTO usuarios(nombre, edad) VALUES(?,?)";
        try (PreparedStatement ps = Db.getConnection().prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            ps.setString(1, u.getNombre());
            ps.setInt(2, u.getEdad());
            ps.executeUpdate();
            try (ResultSet keys = ps.getGeneratedKeys()) {
                if (keys.next()) {
                    u.setId(keys.getInt(1));
                }
            }
            return u;
        } catch (SQLException e) {
            log.error("Error guardando usuario", e);
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Usuario> findById(int id) {
        String sql = "SELECT * FROM usuarios WHERE id=?";
        try (PreparedStatement ps = Db.getConnection().prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(map(rs));
                }
            }
            return Optional.empty();
        } catch (SQLException e) {
            log.error("Error buscando usuario por id", e);
            throw new RuntimeException(e);
        }
    }

    @Override
    public List<Usuario> findAll() {
        String sql = "SELECT * FROM usuarios ORDER BY id";
        List<Usuario> lista = new ArrayList<>();
        try (Statement st = Db.getConnection().createStatement(); ResultSet rs = st.executeQuery(sql)) {
            while (rs.next()) lista.add(map(rs));
            return lista;
        } catch (SQLException e) {
            log.error("Error listando usuarios", e);
            throw new RuntimeException(e);
        }
    }

    @Override
    public boolean update(Usuario u) {
        String sql = "UPDATE usuarios SET nombre=?, edad=? WHERE id=?";
        try (PreparedStatement ps = Db.getConnection().prepareStatement(sql)) {
            ps.setString(1, u.getNombre());
            ps.setInt(2, u.getEdad());
            ps.setInt(3, u.getId());
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            log.error("Error actualizando usuario", e);
            throw new RuntimeException(e);
        }
    }

    @Override
    public boolean delete(int id) {
        String sql = "DELETE FROM usuarios WHERE id=?";
        try (PreparedStatement ps = Db.getConnection().prepareStatement(sql)) {
            ps.setInt(1, id);
            return ps.executeUpdate() > 0;
        } catch (SQLException e) {
            log.error("Error eliminando usuario", e);
            throw new RuntimeException(e);
        }
    }

    private Usuario map(ResultSet rs) throws SQLException {
        return new Usuario(rs.getInt("id"), rs.getString("nombre"), rs.getInt("edad"));
    }
}
