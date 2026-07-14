package com.example.demo.controller;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
class JournalEntryControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldGetAllEntries() throws Exception {
        mockMvc.perform(get("/api/journal"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON));
    }

    @Test
    void shouldCreateNewEntry() throws Exception {
        mockMvc.perform(post("/api/journal")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"contenido\":\"Hoy me siento bien\",\"estadoPrivacidad\":\"PRIVATE\"}"))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.contenido").exists());
    }

    @Test
    void shouldHandleOfflineEntry() throws Exception {
        mockMvc.perform(post("/api/journal")
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"contenido\":\"Test entry\",\"estadoPrivacidad\":\"PROFESSIONAL\"}"))
                .andExpect(status().isCreated());
    }
}
