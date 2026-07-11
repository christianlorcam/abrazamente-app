import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  build: {
    outDir: 'src/main/resources/static',
    emptyOutDir: true, // limpia el contenido previo de static al compilar
  },
  test: {
    environment: 'jsdom',
    setupFiles: ['./src/test/setup.js'],
  }
})
