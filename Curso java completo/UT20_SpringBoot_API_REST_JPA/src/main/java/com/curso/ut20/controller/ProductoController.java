package com.curso.ut20.controller;

import com.curso.ut20.model.Producto;
import com.curso.ut20.repository.ProductoRepository;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping("/api/productos")
public class ProductoController {
    private final ProductoRepository repo;
    public ProductoController(ProductoRepository repo) { this.repo = repo; }

    @GetMapping
    public List<Producto> listar() { return repo.findAll(); }

    @GetMapping("/{id}")
    public ResponseEntity<Producto> uno(@PathVariable Long id) {
        return repo.findById(id).map(ResponseEntity::ok).orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Producto> crear(@Valid @RequestBody Producto p) {
        Producto saved = repo.save(p);
        return ResponseEntity.created(URI.create("/api/productos/" + saved.getId())).body(saved);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Producto> actualizar(@PathVariable Long id, @Valid @RequestBody Producto datos) {
        return repo.findById(id).map(p -> {
            p.setNombre(datos.getNombre());
            p.setPrecio(datos.getPrecio());
            return ResponseEntity.ok(repo.save(p));
        }).orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> borrar(@PathVariable Long id) {
        if (!repo.existsById(id)) return ResponseEntity.notFound().build();
        repo.deleteById(id);
        return ResponseEntity.noContent().build();
    }
}
