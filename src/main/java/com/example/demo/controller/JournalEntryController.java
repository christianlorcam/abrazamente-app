package com.example.demo.controller;

import com.example.demo.model.JournalEntry;
import com.example.demo.model.User;
import com.example.demo.model.enums.PrivacyStatus;
import com.example.demo.repository.JournalEntryRepository;
import com.example.demo.repository.UserRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/journal")
@CrossOrigin(origins = "*")
@AllArgsConstructor
public class JournalEntryController {

    private final JournalEntryRepository journalRepository;
    private final UserRepository userRepository;

    @GetMapping
    public ResponseEntity<List<JournalEntry>> getAllEntries() {
        // En un entorno de producción obtendríamos el usuario del contexto de seguridad (Auth).
        // Para este MVP, asociamos las entradas al primer usuario de la BD, o devolvemos todas.
        List<JournalEntry> entries = journalRepository.findAll();
        return ResponseEntity.ok(entries);
    }

    @PostMapping
    public ResponseEntity<JournalEntry> createEntry(@RequestBody Map<String, String> request) {
        String contenido = request.get("contenido");
        String privacidadStr = request.getOrDefault("estadoPrivacidad", "PRIVATE");
        
        // Obtener o crear un usuario de demostración
        User user = userRepository.findAll().stream().findFirst().orElseGet(() -> {
            User demoUser = new User();
            demoUser.setNombres("Usuario");
            demoUser.setApellidos("Demostración");
            demoUser.setEmail("demo@abrazamente.com");
            demoUser.setPasswordHash("password");
            return userRepository.save(demoUser);
        });

        JournalEntry entry = new JournalEntry();
        entry.setUser(user);
        entry.setContenido(contenido);
        entry.setFechaEntrada(LocalDate.now());
        
        try {
            entry.setEstadoPrivacidad(PrivacyStatus.valueOf(privacidadStr));
        } catch (IllegalArgumentException e) {
            entry.setEstadoPrivacidad(PrivacyStatus.PRIVATE);
        }
        
        entry.setCreadoEn(LocalDateTime.now());
        entry.setActualizadoEn(LocalDateTime.now());

        JournalEntry savedEntry = journalRepository.save(entry);
        return new ResponseEntity<>(savedEntry, HttpStatus.CREATED);
    }
}
