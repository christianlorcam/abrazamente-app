import os

def create_slides():
    output_dir = r"c:\Users\Ricardo\Desktop\rep\mental-app\slides"
    os.makedirs(output_dir, exist_ok=True)
    
    # ----------------------------------------------------
    # SVG COMMON ELEMENTS & STYLES (Light Theme)
    # ----------------------------------------------------
    svg_defs = """  <defs>
    <!-- Background Gradients (Light Lavender to Pale Pink) -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#DCE2F8" />
      <stop offset="100%" stop-color="#F5E1E7" />
    </linearGradient>
    
    <!-- Decorative Glow Blobs -->
    <radialGradient id="blobBlue" cx="15%" cy="15%" r="45%">
      <stop offset="0%" stop-color="#A5B4FC" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#A5B4FC" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="blobPink" cx="85%" cy="85%" r="45%">
      <stop offset="0%" stop-color="#FDA4AF" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#FDA4AF" stop-opacity="0" />
    </radialGradient>
    
    <!-- Text Gradients -->
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#1E293B" />
    </linearGradient>
    
    <!-- Brand / Tech Colors -->
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563EB" />
      <stop offset="100%" stop-color="#1D4ED8" />
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#047857" />
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C3AED" />
      <stop offset="100%" stop-color="#6D28D9" />
    </linearGradient>
    <linearGradient id="orangeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EA580C" />
      <stop offset="100%" stop-color="#C2410C" />
    </linearGradient>

    <!-- Translucent Dark Card Borders (Figma high-contrast look) -->
    <linearGradient id="cardBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0.02" />
    </linearGradient>
    
    <!-- Drop Shadow -->
    <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#000000" flood-opacity="0.15" />
    </filter>
  </defs>"""

    # ----------------------------------------------------
    # SLIDE 1: COVER
    # ----------------------------------------------------
    slide_1 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
{svg_defs}
  <!-- Background Light Gradient -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#blobBlue)" />
  <rect width="1920" height="1080" fill="url(#blobPink)" />

  <!-- Wave / Ribbon Graphic (Matching the background aesthetic) -->
  <g opacity="0.15">
    <path d="M-100,700 C400,900 800,500 1200,800 C1600,1100 1800,700 2100,800 L2100,1100 L-100,1100 Z" fill="#93C5FD" />
    <path d="M-100,750 C450,920 750,550 1250,830 C1550,1050 1850,750 2100,850 L2100,1100 L-100,1100 Z" fill="#F472B6" />
  </g>

  <!-- Content Container -->
  <g transform="translate(180, 260)">
    <!-- Eyebrow -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="350" height="42" rx="21" fill="#FFFFFF" fill-opacity="0.8" stroke="#D1D5DB" stroke-width="1.5" />
      <circle cx="25" cy="21" r="6" fill="#2563EB" />
      <text x="45" y="27" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#4B5563" letter-spacing="1.5">ARQUITECTURA REACT &amp; BD</text>
    </g>

    <!-- Main Title -->
    <text x="0" y="150" font-family="Inter, sans-serif" font-size="96" font-weight="800" fill="url(#titleGrad)" letter-spacing="-1.5">AbrazaMente</text>
    
    <!-- Subtitle -->
    <text x="0" y="230" font-family="Inter, sans-serif" font-size="32" font-weight="500" fill="#374151">Integración de React SPA con Modelos de Persistencia Spring Boot</text>
    
    <!-- Divider -->
    <line x1="0" y1="280" x2="600" y2="280" stroke="#D1D5DB" stroke-width="2" />
    
    <!-- Presenter info (High-contrast Dark Card to match Jira/GitHub slides) -->
    <g transform="translate(0, 330)">
      <rect x="0" y="0" width="550" height="150" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
      
      <!-- Details -->
      <text x="30" y="50" font-family="Inter, sans-serif" font-size="22" font-weight="700" fill="#FFFFFF">Ricardo Sanhueza</text>
      <text x="30" y="82" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#60A5FA">Desarrollo, Q.A. &amp; 3º Scrum Master</text>
      <text x="30" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF" letter-spacing="0.5">Mente Conecta Platform · Copia Funcional (React Fork)</text>
    </g>
  </g>

  <!-- Brand Footer -->
  <text x="1740" y="1000" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#4B5563" text-anchor="end" letter-spacing="2">ABRAZAMENTE.CL</text>
</svg>"""

    # ----------------------------------------------------
    # SLIDE 2: STACK TECNOLOGICO
    # ----------------------------------------------------
    slide_2 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
{svg_defs}
  <!-- Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#blobBlue)" />
  <rect width="1920" height="1080" fill="url(#blobPink)" />

  <!-- Header -->
  <g transform="translate(100, 100)">
    <text x="0" y="40" font-family="Inter, sans-serif" font-size="48" font-weight="800" fill="url(#titleGrad)">Stack Tecnológico: React &amp; Spring Boot</text>
    <text x="0" y="75" font-family="Inter, sans-serif" font-size="20" font-weight="500" fill="#4B5563">Integración ágil conectando componentes de frontend con entidades JPA de base de datos</text>
  </g>

  <!-- Columns (High contrast dark cards, matching Jira/GitHub slides) -->
  
  <!-- COLUMN 1: FRONTEND -->
  <g transform="translate(100, 240)">
    <rect width="520" height="660" rx="24" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <!-- Gradient Top Bar -->
    <path d="M 24,0 L 496,0 A 24,24 0 0,1 520,24 L 520,24 A 0,0 0 0,1 520,24 L 0,24 A 0,0 0 0,1 0,24 L 0,24 A 24,24 0 0,1 24,0 Z" fill="url(#blueGrad)" />
    
    <!-- Title -->
    <text x="40" y="75" font-family="Inter, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Frontend React</text>
    <text x="40" y="105" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#60A5FA">Arquitectura por Componentes</text>
    
    <!-- Items -->
    <g transform="translate(40, 160)">
      <!-- Item 1 -->
      <circle cx="20" cy="20" r="15" fill="#1E293B" />
      <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#60A5FA">R</text>
      <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">React SPA (Vite)</text>
      <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Maquetación ágil, reactividad y Virtual DOM</text>
      
      <!-- Item 2 -->
      <g transform="translate(0, 80)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="12" font-weight="700" fill="#60A5FA">TW</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Tailwind CSS</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Diseño responsive basado en clases utilitarias</text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 160)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="14" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#60A5FA">JS</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">JavaScript (ES6+) / Hooks</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Consumo de la API con Fetch y useEffect</text>
      </g>

      <!-- Item 4 -->
      <g transform="translate(0, 240)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#60A5FA">C</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Componentes UI</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Temporizadores, Diario y Formularios</text>
      </g>

      <!-- Visual Banner -->
      <rect x="0" y="320" width="440" height="110" rx="12" fill="#1E293B" fill-opacity="0.4" stroke="#3B82F6" stroke-opacity="0.2" />
      <text x="20" y="45" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#3B82F6">MIGRACIÓN DE FRONTEND</text>
      <text x="20" y="75" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Copia Funcional React</text>
      <circle cx="390" cy="55" r="25" fill="#3B82F6" fill-opacity="0.2" />
      <path d="M380,55 L387,62 L402,47" fill="none" stroke="#3B82F6" stroke-width="3" />
    </g>
  </g>

  <!-- COLUMN 2: BACKEND -->
  <g transform="translate(650, 240)">
    <rect width="520" height="660" rx="24" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <!-- Gradient Top Bar -->
    <path d="M 24,0 L 496,0 A 24,24 0 0,1 520,24 L 520,24 A 0,0 0 0,1 520,24 L 0,24 A 0,0 0 0,1 0,24 L 0,24 A 24,24 0 0,1 24,0 Z" fill="url(#greenGrad)" />
    
    <!-- Title -->
    <text x="40" y="75" font-family="Inter, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Backend API</text>
    <text x="40" y="105" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#34D399">Servicios Java Spring Boot</text>
    
    <!-- Items -->
    <g transform="translate(40, 160)">
      <!-- Item 1 -->
      <circle cx="20" cy="20" r="15" fill="#1E293B" />
      <text x="14" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#34D399">JV</text>
      <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Java 17 (LTS)</text>
      <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Código backend tipado y robusto</text>
      
      <!-- Item 2 -->
      <g transform="translate(0, 80)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#34D399">S</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Spring Boot 3.x</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Exposición de endpoints JSON estructurados</text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 160)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="14" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#34D399">H</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Spring Data JPA / Hibernate</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Mapeo de base de datos a objetos Java</text>
      </g>

      <!-- Item 4 -->
      <g transform="translate(0, 240)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#34D399">L</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Project Lombok</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Modelos limpios con anotaciones Getter/Setter</text>
      </g>

      <!-- Visual Banner -->
      <rect x="0" y="320" width="440" height="110" rx="12" fill="#1E293B" fill-opacity="0.4" stroke="#10B981" stroke-opacity="0.2" />
      <text x="20" y="45" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#10B981">SEGURIDAD BACKEND</text>
      <text x="20" y="75" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">CORS &amp; JWT/OAuth</text>
      <circle cx="390" cy="55" r="25" fill="#10B981" fill-opacity="0.2" />
      <path d="M380,55 L387,62 L402,47" fill="none" stroke="#10B981" stroke-width="3" />
    </g>
  </g>

  <!-- COLUMN 3: BD & INFRA -->
  <g transform="translate(1200, 240)">
    <rect width="520" height="660" rx="24" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <!-- Gradient Top Bar -->
    <path d="M 24,0 L 496,0 A 24,24 0 0,1 520,24 L 520,24 A 0,0 0 0,1 520,24 L 0,24 A 0,0 0 0,1 0,24 L 0,24 A 24,24 0 0,1 24,0 Z" fill="url(#purpleGrad)" />
    
    <!-- Title -->
    <text x="40" y="75" font-family="Inter, sans-serif" font-size="28" font-weight="800" fill="#FFFFFF">Datos &amp; DevOps</text>
    <text x="40" y="105" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#A78BFA">Persistencia e Infraestructura</text>
    
    <!-- Items -->
    <g transform="translate(40, 160)">
      <!-- Item 1 -->
      <circle cx="20" cy="20" r="15" fill="#1E293B" />
      <text x="14" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#A78BFA">PG</text>
      <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">PostgreSQL (Neon)</text>
      <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Base de datos serverless con cifrado SSL</text>
      
      <!-- Item 2 -->
      <g transform="translate(0, 80)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#A78BFA">H2</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">H2 DB (Desarrollo)</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Base de datos rápida en memoria para testing</text>
      </g>

      <!-- Item 3 -->
      <g transform="translate(0, 160)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#A78BFA">CI</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">GitHub Actions CI</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Compilación y validación de código con Maven</text>
      </g>

      <!-- Item 4 -->
      <g transform="translate(0, 240)">
        <circle cx="20" cy="20" r="15" fill="#1E293B" />
        <text x="15" y="25" font-family="Inter, sans-serif" font-size="14" font-weight="700" fill="#A78BFA">G</text>
        <text x="50" y="18" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">Git / GitHub</text>
        <text x="50" y="38" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Control de versiones distribuidas (Feature Branch)</text>
      </g>

      <!-- Visual Banner -->
      <rect x="0" y="320" width="440" height="110" rx="12" fill="#1E293B" fill-opacity="0.4" stroke="#8B5CF6" stroke-opacity="0.2" />
      <text x="20" y="45" font-family="Inter, sans-serif" font-size="14" font-weight="600" fill="#8B5CF6">BASE DE DATOS CLOUD</text>
      <text x="20" y="75" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF">Neon Serverless Integration</text>
      <circle cx="390" cy="55" r="25" fill="#8B5CF6" fill-opacity="0.2" />
      <path d="M380,55 L387,62 L402,47" fill="none" stroke="#8B5CF6" stroke-width="3" />
    </g>
  </g>

  <!-- Footer -->
  <text x="1820" y="1000" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#4B5563" text-anchor="end">AbrazaMente · Presentación Técnica</text>
</svg>"""

    # ----------------------------------------------------
    # SLIDE 3: ARQUITECTURA DEL SISTEMA
    # ----------------------------------------------------
    slide_3 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
{svg_defs}
  <!-- Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#blobBlue)" />
  <rect width="1920" height="1080" fill="url(#blobPink)" />

  <!-- Header -->
  <g transform="translate(100, 100)">
    <text x="0" y="40" font-family="Inter, sans-serif" font-size="48" font-weight="800" fill="url(#titleGrad)">Arquitectura de 3 Capas Desacopladas</text>
    <text x="0" y="75" font-family="Inter, sans-serif" font-size="20" font-weight="500" fill="#4B5563">Flujo e integración de datos entre el Frontend React y la Persistencia de Datos</text>
  </g>

  <!-- DIAGRAM AREA (Dark cards for high contrast) -->

  <!-- 1. Capa Cliente (Left) -->
  <g transform="translate(100, 260)">
    <rect width="400" height="560" rx="20" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <rect width="400" height="70" rx="20" fill="url(#blueGrad)" />
    <rect y="40" width="400" height="30" fill="url(#blueGrad)" />
    
    <text x="200" y="45" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF" text-anchor="middle">Capa Cliente</text>
    <text x="200" y="110" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#9CA3AF" text-anchor="middle">React SPA (Vite)</text>
    
    <!-- Components -->
    <g transform="translate(30, 150)">
      <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#2563EB" stroke-opacity="0.3" />
      <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Componentes React</text>
      <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Diario, Grounding, Reservas, Foro</text>

      <g transform="translate(0, 110)">
        <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#2563EB" stroke-opacity="0.3" />
        <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Client API (Fetch)</text>
        <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Peticiones asíncronas a endpoints</text>
      </g>

      <g transform="translate(0, 220)">
        <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#2563EB" stroke-opacity="0.3" />
        <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Tailwind CSS Styles</text>
        <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Clases responsive y orbs interactivos</text>
      </g>
    </g>
    
    <rect x="30" y="475" width="340" height="50" rx="8" fill="#1E293B" fill-opacity="0.5" />
    <text x="200" y="505" font-family="Inter, sans-serif" font-size="15" font-weight="600" fill="#60A5FA" text-anchor="middle">Ejecución en Web / Navegador</text>
  </g>

  <!-- 2. Capa Servidor (Center) -->
  <g transform="translate(760, 260)">
    <rect width="400" height="560" rx="20" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <rect width="400" height="70" rx="20" fill="url(#greenGrad)" />
    <rect y="40" width="400" height="30" fill="url(#greenGrad)" />
    
    <text x="200" y="45" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF" text-anchor="middle">Capa Servidor</text>
    <text x="200" y="110" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#9CA3AF" text-anchor="middle">Spring Boot API</text>
    
    <!-- Components -->
    <g transform="translate(30, 150)">
      <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#059669" stroke-opacity="0.3" />
      <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">REST Controllers</text>
      <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Endpoints /api/users, /api/auth, etc.</text>

      <g transform="translate(0, 110)">
        <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#059669" stroke-opacity="0.3" />
        <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Servicios de Negocio</text>
        <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Lógica clínica, mapeos y auth</text>
      </g>

      <g transform="translate(0, 220)">
        <rect width="340" height="75" rx="10" fill="#1E293B" stroke="#059669" stroke-opacity="0.3" />
        <text x="20" y="32" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">JPA Persistencia</text>
        <text x="20" y="55" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Mapeo a entidades con Hibernate</text>
      </g>
    </g>

    <rect x="30" y="475" width="340" height="50" rx="8" fill="#1E293B" fill-opacity="0.5" />
    <text x="200" y="505" font-family="Inter, sans-serif" font-size="15" font-weight="600" fill="#34D399" text-anchor="middle">Servidor de Aplicaciones</text>
  </g>

  <!-- 3. Capa Datos (Right) -->
  <g transform="translate(1420, 260)">
    <rect width="400" height="560" rx="20" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <rect width="400" height="70" rx="20" fill="url(#purpleGrad)" />
    <rect y="40" width="400" height="30" fill="url(#purpleGrad)" />
    
    <text x="200" y="45" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#FFFFFF" text-anchor="middle">Capa de Datos</text>
    <text x="200" y="110" font-family="Inter, sans-serif" font-size="16" font-weight="500" fill="#9CA3AF" text-anchor="middle">Persistencia Relacional</text>
    
    <!-- Components -->
    <g transform="translate(30, 150)">
      <rect width="340" height="180" rx="10" fill="#1E293B" stroke="#7C3AED" stroke-opacity="0.3" />
      <text x="20" y="40" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">PostgreSQL (Neon)</text>
      <text x="20" y="70" font-family="Inter, sans-serif" font-size="14" font-weight="500" fill="#A78BFA">Base de Datos Cloud</text>
      <text x="20" y="110" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Almacenamiento seguro en prod</text>
      <text x="20" y="135" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Conexión JDBC sobre SSL</text>
      
      <g transform="translate(0, 205)">
        <rect width="340" height="150" rx="10" fill="#1E293B" stroke="#7C3AED" stroke-opacity="0.3" />
        <text x="20" y="40" font-family="Inter, sans-serif" font-size="20" font-weight="700" fill="#FFFFFF">H2 Database</text>
        <text x="20" y="70" font-family="Inter, sans-serif" font-size="14" font-weight="500" fill="#A78BFA">En memoria (Local/CI)</text>
        <text x="20" y="100" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Rapidez en testing y dev</text>
        <text x="20" y="125" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Aislamiento en GitHub Actions</text>
      </g>
    </g>
    
    <rect x="30" y="505" width="340" height="40" rx="8" fill="#1E293B" fill-opacity="0.5" />
    <text x="200" y="530" font-family="Inter, sans-serif" font-size="15" font-weight="600" fill="#A78BFA" text-anchor="middle">ACID Cumplimiento</text>
  </g>

  <!-- Connectors (Arrows) -->
  
  <!-- Client to Server Arrow -->
  <g transform="translate(520, 500)">
    <line x1="0" y1="0" x2="220" y2="0" stroke="#059669" stroke-width="4" stroke-dasharray="8 6" />
    <polygon points="220,-8 236,0 220,8" fill="#059669" />
    <rect x="15" y="-35" width="190" height="25" rx="4" fill="#0D1117" stroke="#374151" stroke-width="1" />
    <text x="110" y="-18" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">HTTP / JSON REST Request</text>
  </g>
  
  <!-- Server to Client Arrow (Back) -->
  <g transform="translate(520, 560)">
    <line x1="220" y1="0" x2="16" y2="0" stroke="#2563EB" stroke-width="4" />
    <polygon points="16,-8 0,0 16,8" fill="#2563EB" />
    <rect x="15" y="10" width="190" height="25" rx="4" fill="#0D1117" stroke="#374151" stroke-width="1" />
    <text x="110" y="27" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">HTTP JSON Response</text>
  </g>

  <!-- Server to DB Arrow -->
  <g transform="translate(1180, 500)">
    <line x1="0" y1="0" x2="220" y2="0" stroke="#7C3AED" stroke-width="4" />
    <polygon points="220,-8 236,0 220,8" fill="#7C3AED" />
    <rect x="15" y="-35" width="190" height="25" rx="4" fill="#0D1117" stroke="#374151" stroke-width="1" />
    <text x="110" y="-18" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">JDBC / JPA Connection</text>
  </g>

  <!-- DB to Server Arrow (Back) -->
  <g transform="translate(1180, 560)">
    <line x1="220" y1="0" x2="16" y2="0" stroke="#7C3AED" stroke-width="4" stroke-dasharray="8 6" />
    <polygon points="16,-8 0,0 16,8" fill="#7C3AED" />
    <rect x="15" y="10" width="190" height="25" rx="4" fill="#0D1117" stroke="#374151" stroke-width="1" />
    <text x="110" y="27" font-family="Inter, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">ResultSet / Entities</text>
  </g>

  <!-- Footer -->
  <text x="1820" y="1000" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#4B5563" text-anchor="end">AbrazaMente · Presentación Técnica</text>
</svg>"""

    # ----------------------------------------------------
    # SLIDE 4: CONEXION DE MODELOS (NEW!)
    # ----------------------------------------------------
    slide_4 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
{svg_defs}
  <!-- Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#blobPurple)" />
  <rect width="1920" height="1080" fill="url(#blobPink)" />

  <!-- Header -->
  <g transform="translate(100, 100)">
    <text x="0" y="40" font-family="Inter, sans-serif" font-size="48" font-weight="800" fill="url(#titleGrad)">Mapeo y Conexión de Modelos</text>
    <text x="0" y="75" font-family="Inter, sans-serif" font-size="20" font-weight="500" fill="#4B5563">Cómo interactúan los componentes React con las entidades JPA de la base de datos</text>
  </g>

  <!-- Main Map Area (Dark Card) -->
  <g transform="translate(100, 240)">
    <rect width="1720" height="660" rx="24" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1.5" filter="url(#cardShadow)" />
    <path d="M 24,0 L 1696,0 A 24,24 0 0,1 1720,24 L 1720,24 A 0,0 0 0,1 1720,24 L 0,24 A 0,0 0 0,1 0,24 L 0,24 A 24,24 0 0,1 24,0 Z" fill="url(#purpleGrad)" />
    
    <!-- Columns Titles -->
    <text x="80" y="65" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#60A5FA">Componentes React (Frontend)</text>
    <text x="580" y="65" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#38BDF8">Controlador REST (API)</text>
    <text x="1080" y="65" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#34D399">Modelo JPA (Backend)</text>
    <text x="1420" y="65" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#A78BFA">Persistencia (Tablas SQL)</text>
    
    <!-- Divider lines in map -->
    <line x1="500" y1="40" x2="500" y2="620" stroke="#374151" stroke-width="1" />
    <line x1="1000" y1="40" x2="1000" y2="620" stroke="#374151" stroke-width="1" />
    
    <!-- Row 1: Users -->
    <g transform="translate(40, 110)">
      <!-- React Component -->
      <rect x="20" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#2563EB" stroke-width="1" />
      <text x="40" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">&lt;UserProfile /&gt;</text>
      <text x="40" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Registro, Perfil de Usuario y Login</text>
      
      <!-- Arrow -->
      <line x1="430" y1="45" x2="520" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="520,40 530,45 520,50" fill="#4B5563" />
      
      <!-- Spring Controller -->
      <rect x="540" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#059669" stroke-width="1" />
      <text x="560" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">UserController &amp; AuthController</text>
      <text x="560" y="62" font-family="Inter, sans-serif" font-size="13" font-weight="400" fill="#9CA3AF">POST /api/users, POST /auth/google</text>
      
      <!-- Arrow -->
      <line x1="950" y1="45" x2="1020" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1020,40 1030,45 1020,50" fill="#4B5563" />
      
      <!-- JPA Model -->
      <rect x="1040" y="0" width="300" height="90" rx="12" fill="#1E293B" stroke="#7C3AED" stroke-width="1" />
      <text x="1060" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">User.java</text>
      <text x="1060" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#A78BFA">Entidad JPA</text>
      
      <!-- Arrow -->
      <line x1="1350" y1="45" x2="1390" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1390,40 1400,45 1390,50" fill="#4B5563" />
      
      <!-- Database Table -->
      <rect x="1410" y="0" width="230" height="90" rx="12" fill="#1E293B" stroke="#D1D5DB" stroke-opacity="0.2" stroke-width="1" />
      <text x="1430" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">usuarios</text>
      <text x="1430" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Tabla SQL física</text>
    </g>

    <!-- Row 2: Journal -->
    <g transform="translate(40, 230)">
      <!-- React Component -->
      <rect x="20" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#2563EB" stroke-width="1" />
      <text x="40" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">&lt;MoodTracker /&gt;</text>
      <text x="40" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Diario Emocional y registro de estados</text>
      
      <!-- Arrow -->
      <line x1="430" y1="45" x2="520" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="520,40 530,45 520,50" fill="#4B5563" />
      
      <!-- Spring Controller -->
      <rect x="540" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#059669" stroke-width="1" />
      <text x="560" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">JournalController</text>
      <text x="560" y="62" font-family="Inter, sans-serif" font-size="13" font-weight="400" fill="#9CA3AF">POST /api/journal, GET /api/journal/user/{id}</text>
      
      <!-- Arrow -->
      <line x1="950" y1="45" x2="1020" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1020,40 1030,45 1020,50" fill="#4B5563" />
      
      <!-- JPA Model -->
      <rect x="1040" y="0" width="300" height="90" rx="12" fill="#1E293B" stroke="#7C3AED" stroke-width="1" />
      <text x="1060" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">JournalEntry.java</text>
      <text x="1060" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#A78BFA">Entidad JPA</text>
      
      <!-- Arrow -->
      <line x1="1350" y1="45" x2="1390" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1390,40 1400,45 1390,50" fill="#4B5563" />
      
      <!-- Database Table -->
      <rect x="1410" y="0" width="230" height="90" rx="12" fill="#1E293B" stroke="#D1D5DB" stroke-opacity="0.2" stroke-width="1" />
      <text x="1430" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">diario_emocional</text>
      <text x="1430" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Tabla SQL física</text>
    </g>

    <!-- Row 3: SessionReservation -->
    <g transform="translate(40, 350)">
      <!-- React Component -->
      <rect x="20" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#2563EB" stroke-width="1" />
      <text x="40" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">&lt;SessionScheduler /&gt;</text>
      <text x="40" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Calendario y agendamiento de telemedicina</text>
      
      <!-- Arrow -->
      <line x1="430" y1="45" x2="520" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="520,40 530,45 520,50" fill="#4B5563" />
      
      <!-- Spring Controller -->
      <rect x="540" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#059669" stroke-width="1" />
      <text x="560" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">SessionReservationController</text>
      <text x="560" y="62" font-family="Inter, sans-serif" font-size="13" font-weight="400" fill="#9CA3AF">POST /api/sessions/book, GET /api/sessions</text>
      
      <!-- Arrow -->
      <line x1="950" y1="45" x2="1020" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1020,40 1030,45 1020,50" fill="#4B5563" />
      
      <!-- JPA Model -->
      <rect x="1040" y="0" width="300" height="90" rx="12" fill="#1E293B" stroke="#7C3AED" stroke-width="1" />
      <text x="1060" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">SessionReservation.java</text>
      <text x="1060" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#A78BFA">Entidad JPA</text>
      
      <!-- Arrow -->
      <line x1="1350" y1="45" x2="1390" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1390,40 1400,45 1390,50" fill="#4B5563" />
      
      <!-- Database Table -->
      <rect x="1410" y="0" width="230" height="90" rx="12" fill="#1E293B" stroke="#D1D5DB" stroke-opacity="0.2" stroke-width="1" />
      <text x="1430" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">reservas_sesiones</text>
      <text x="1430" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Tabla SQL física</text>
    </g>

    <!-- Row 4: Professionals -->
    <g transform="translate(40, 470)">
      <!-- React Component -->
      <rect x="20" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#2563EB" stroke-width="1" />
      <text x="40" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">&lt;ClinicianDirectory /&gt;</text>
      <text x="40" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Directorio clínico y tarjetas de psicólogos</text>
      
      <!-- Arrow -->
      <line x1="430" y1="45" x2="520" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="520,40 530,45 520,50" fill="#4B5563" />
      
      <!-- Spring Controller -->
      <rect x="540" y="0" width="400" height="90" rx="12" fill="#1E293B" stroke="#059669" stroke-width="1" />
      <text x="560" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">ProfessionalController</text>
      <text x="560" y="62" font-family="Inter, sans-serif" font-size="13" font-weight="400" fill="#9CA3AF">GET /api/professionals</text>
      
      <!-- Arrow -->
      <line x1="950" y1="45" x2="1020" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1020,40 1030,45 1020,50" fill="#4B5563" />
      
      <!-- JPA Model -->
      <rect x="1040" y="0" width="300" height="90" rx="12" fill="#1E293B" stroke="#7C3AED" stroke-width="1" />
      <text x="1060" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Professional.java</text>
      <text x="1060" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#A78BFA">Entidad JPA</text>
      
      <!-- Arrow -->
      <line x1="1350" y1="45" x2="1390" y2="45" stroke="#4B5563" stroke-width="2" />
      <polygon points="1390,40 1400,45 1390,50" fill="#4B5563" />
      
      <!-- Database Table -->
      <rect x="1410" y="0" width="230" height="90" rx="12" fill="#1E293B" stroke="#D1D5DB" stroke-opacity="0.2" stroke-width="1" />
      <text x="1430" y="38" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">profesionales</text>
      <text x="1430" y="62" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">Tabla SQL física</text>
    </g>
  </g>

  <!-- Footer -->
  <text x="1820" y="1000" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#4B5563" text-anchor="end">AbrazaMente · Presentación Técnica</text>
</svg>"""

    # ----------------------------------------------------
    # SLIDE 5: DEVOPS Y CICLO DE VIDA
    # ----------------------------------------------------
    slide_5 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%">
{svg_defs}
  <!-- Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#blobTeal)" />
  <rect width="1920" height="1080" fill="url(#blobPink)" />

  <!-- Header -->
  <g transform="translate(100, 100)">
    <text x="0" y="40" font-family="Inter, sans-serif" font-size="48" font-weight="800" fill="url(#titleGrad)">DevOps: Integración y Calidad de Código</text>
    <text x="0" y="75" font-family="Inter, sans-serif" font-size="20" font-weight="500" fill="#4B5563">Flujo ágil y pruebas automatizadas en el repositorio fork para mantener el estándar clínico</text>
  </g>

  <!-- Horizontal Timeline (Light Background Style) -->
  
  <!-- Step line connector -->
  <line x1="200" y1="480" x2="1720" y2="480" stroke="#D1D5DB" stroke-width="6" />
  <line x1="200" y1="480" x2="1340" y2="480" stroke="#059669" stroke-width="6" stroke-dasharray="10 8" />

  <!-- STEP 1: JIRA / DAILY -->
  <g transform="translate(200, 480)">
    <!-- Circle indicator -->
    <circle cx="0" cy="0" r="24" fill="#0D1117" stroke="#2563EB" stroke-width="5" />
    <text x="0" y="6" font-family="Inter, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">1</text>
    
    <!-- Top label -->
    <text x="0" y="-120" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#0F172A" text-anchor="middle">Gestión Ágil</text>
    <text x="0" y="-95" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#2563EB" text-anchor="middle">Jira &amp; Sprints</text>
    <path d="M0,-80 L0,-40" stroke="#2563EB" stroke-width="2" />
    
    <!-- Bottom Info Card -->
    <g transform="translate(-160, 50)">
      <rect width="320" height="230" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1" filter="url(#cardShadow)" />
      <text x="25" y="45" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Planificación</text>
      <text x="25" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Sincronización diaria del equipo</text>
      <text x="25" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Flujo Scrum bien definido</text>
      <text x="25" y="145" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Estimaciones en Jira Board</text>
      <text x="25" y="175" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Ricardo S.: Dev &amp; Q.A. / SM</text>
    </g>
  </g>

  <!-- STEP 2: GIT BRANCHING -->
  <g transform="translate(580, 480)">
    <!-- Circle indicator -->
    <circle cx="0" cy="0" r="24" fill="#0D1117" stroke="#059669" stroke-width="5" />
    <text x="0" y="6" font-family="Inter, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">2</text>
    
    <!-- Top label -->
    <text x="0" y="-120" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#0F172A" text-anchor="middle">Control Git</text>
    <text x="0" y="-95" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#059669" text-anchor="middle">Ramas de Propósito</text>
    <path d="M0,-80 L0,-40" stroke="#059669" stroke-width="2" />
    
    <!-- Bottom Info Card -->
    <g transform="translate(-160, 50)">
      <rect width="320" height="230" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1" filter="url(#cardShadow)" />
      <text x="25" y="45" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Modelo de Ramas</text>
      <text x="25" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Ramas sin nombres personales</text>
      <text x="25" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Naming: feature/, fix/, docs/</text>
      <text x="25" y="145" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Trabajo aislado en el Fork</text>
      <text x="25" y="175" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Integración limpia de React</text>
    </g>
  </g>

  <!-- STEP 3: PULL REQUEST & REVIEW -->
  <g transform="translate(960, 480)">
    <!-- Circle indicator -->
    <circle cx="0" cy="0" r="24" fill="#0D1117" stroke="#059669" stroke-width="5" />
    <text x="0" y="6" font-family="Inter, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">3</text>
    
    <!-- Top label -->
    <text x="0" y="-120" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#0F172A" text-anchor="middle">Pull Request</text>
    <text x="0" y="-95" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#059669" text-anchor="middle">Revisión por Pares</text>
    <path d="M0,-80 L0,-40" stroke="#059669" stroke-width="2" />
    
    <!-- Bottom Info Card -->
    <g transform="translate(-160, 50)">
      <rect width="320" height="230" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1" filter="url(#cardShadow)" />
      <text x="25" y="45" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Calidad de Código</text>
      <text x="25" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Bloqueo de commits en main</text>
      <text x="25" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Revisiones con Sourcery AI</text>
      <text x="25" y="145" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Feedback constructivo en PRs</text>
      <text x="25" y="175" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Fusión tras aprobaciones</text>
    </g>
  </g>

  <!-- STEP 4: GITHUB ACTIONS CI -->
  <g transform="translate(1340, 480)">
    <!-- Circle indicator -->
    <circle cx="0" cy="0" r="24" fill="#0D1117" stroke="#059669" stroke-width="5" />
    <text x="0" y="6" font-family="Inter, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">4</text>
    
    <!-- Top label -->
    <text x="0" y="-120" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#0F172A" text-anchor="middle">Pipeline CI</text>
    <text x="0" y="-95" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#059669" text-anchor="middle">GitHub Actions</text>
    <path d="M0,-80 L0,-40" stroke="#059669" stroke-width="2" />
    
    <!-- Bottom Info Card -->
    <g transform="translate(-160, 50)">
      <rect width="320" height="230" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1" filter="url(#cardShadow)" />
      <text x="25" y="45" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Automatización</text>
      <text x="25" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Compilación automatizada Maven</text>
      <text x="25" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Tests unitarios JUnit con H2</text>
      <text x="25" y="145" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Análisis estático de seguridad CodeQL</text>
      <text x="25" y="175" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Aprobación requerida para merge</text>
    </g>
  </g>

  <!-- STEP 5: NEON DB & DELIVER -->
  <g transform="translate(1720, 480)">
    <!-- Circle indicator -->
    <circle cx="0" cy="0" r="24" fill="#0D1117" stroke="#EA580C" stroke-width="5" />
    <text x="0" y="6" font-family="Inter, sans-serif" font-size="18" font-weight="800" fill="#FFFFFF" text-anchor="middle">5</text>
    
    <!-- Top label -->
    <text x="0" y="-120" font-family="Inter, sans-serif" font-size="22" font-weight="800" fill="#0F172A" text-anchor="middle">Entrega</text>
    <text x="0" y="-95" font-family="Inter, sans-serif" font-size="15" font-weight="700" fill="#EA580C" text-anchor="middle">Neon DB Branching</text>
    <path d="M0,-80 L0,-40" stroke="#EA580C" stroke-width="2" />
    
    <!-- Bottom Info Card -->
    <g transform="translate(-160, 50)">
      <rect width="320" height="230" rx="16" fill="#0D1117" fill-opacity="0.95" stroke="url(#cardBorder)" stroke-width="1" filter="url(#cardShadow)" />
      <text x="25" y="45" font-family="Inter, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Despliegue</text>
      <text x="25" y="85" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Ramas aisladas de Neon DB</text>
      <text x="25" y="115" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Base de datos Postgres serverless</text>
      <text x="25" y="145" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Migraciones automáticas</text>
      <text x="25" y="175" font-family="Inter, sans-serif" font-size="14" font-weight="400" fill="#9CA3AF">• Fusión e integración en la nube</text>
    </g>
  </g>

  <!-- Footer -->
  <text x="1820" y="1000" font-family="Inter, sans-serif" font-size="16" font-weight="700" fill="#4B5563" text-anchor="end">AbrazaMente · Presentación Técnica</text>
</svg>"""

    # Write each slide out
    slides = [
        ("slide_1_cover.svg", slide_1),
        ("slide_2_stack.svg", slide_2),
        ("slide_3_architecture.svg", slide_3),
        ("slide_4_model_connection.svg", slide_4),
        ("slide_5_cicd.svg", slide_5)
    ]
    
    for filename, content in slides:
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated slide: {filepath}")

if __name__ == "__main__":
    create_slides()
