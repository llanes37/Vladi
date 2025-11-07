package com.curso.ut20.controller;

import com.curso.ut20.model.Usuario;
import com.curso.ut20.repository.UsuarioRepository;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping("/api/usuarios")
public class UsuarioController {
    private final UsuarioRepository repo;
    public UsuarioController(UsuarioRepository repo) { this.repo = repo; }

    @GetMapping
    public List<Usuario> listar() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<Usuario> uno(@PathVariable Long id) {
        return repo.findById(id).map(ResponseEntity::ok).orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Usuario> crear(@Valid @RequestBody Usuario u) {
        Usuario saved = repo.save(u);
        return ResponseEntity.created(URI.create("/api/usuarios/" + saved.getId())).body(saved);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Usuario> actualizar(@PathVariable Long id, @Valid @RequestBody Usuario datos) {
        return repo.findById(id).map(u -> {
            u.setNombre(datos.getNombre());
            u.setEdad(datos.getEdad());
            return ResponseEntity.ok(repo.save(u));
        }).orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> borrar(@PathVariable Long id) {
        if (!repo.existsById(id)) return ResponseEntity.notFound().build();
        repo.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
