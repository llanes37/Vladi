# Guía completa de Netlify

> **Objetivo**: Entender, desde cero y a fondo, qué es Netlify, cómo encaja en la arquitectura moderna web (frontend, backend y bases de datos), qué significa *estático* vs *dinámico*, y cómo **subir** (deploy) proyectos paso a paso usando **Git**, **CLI** y **drag‑and‑drop**. Incluye **ejemplos** de `netlify.toml`, **_redirects**, **Functions**, **Edge Functions**, **programación de funciones**, **formularios**, **variables de entorno**, **dominios**, **HTTPS**, **almacenamiento** y **buenas prácticas**.

---

## 0) Índice rápido
- [1) Conceptos base: frontend, backend y BD](#1-conceptos-base-frontend-backend-y-bd)
- [2) De monolitos a JAMstack](#2-de-monolitos-a-jamstack)
- [3) ¿Qué es Netlify?](#3-qué-es-netlify)
- [4) Flujo mental: ¿mi proyecto es estático o dinámico?](#4-flujo-mental-mi-proyecto-es-estático-o-dinámico)
- [5) Maneras de desplegar en Netlify](#5-maneras-de-desplegar-en-netlify)
- [6) Configuración con `netlify.toml`](#6-configuración-con-netlifytoml)
- [7) Redirecciones y cabeceras (`_redirects` y `_headers`)](#7-redirecciones-y-cabeceras-_redirects-y-_headers)
- [8) Variables de entorno y secretos](#8-variables-de-entorno-y-secretos)
- [9) Funciones: Serverless y Edge](#9-funciones-serverless-y-edge)
- [10) Formularios, imágenes, prerender y otros servicios](#10-formularios-imágenes-prerender-y-otros-servicios)
- [11) Dominios, DNS y HTTPS](#11-dominios-dns-y-https)
- [12) Previews, ramas, split testing y equipos](#12-previews-ramas-split-testing-y-equipos)
- [13) Almacenamiento y datos en Netlify](#13-almacenamiento-y-datos-en-netlify)
- [14) Ejemplos prácticos por stack](#14-ejemplos-prácticos-por-stack)
- [15) Checklist de seguridad y rendimiento](#15-checklist-de-seguridad-y-rendimiento)
- [16) Problemas comunes y cómo depurarlos](#16-problemas-comunes-y-cómo-depurarlos)
- [17) Glosario](#17-glosario)
- [18) Enlaces útiles](#18-enlaces-útiles)

---

## 1) Conceptos base: frontend, backend y BD

**Frontend**: Todo lo que se ejecuta en el navegador del usuario (HTML, CSS, JS). Ej.: sitios estáticos, React/Vue/Angular compilado, SPA/MPA.

**Backend**: Lógica de negocio en el servidor. Tradicionalmente vive en servidores (Node, Java, Python, PHP, .NET…). Expone **APIs**.

**Base de Datos (BD)**: Donde persisten los datos (SQL como PostgreSQL/MySQL, NoSQL como MongoDB, KV/Redis, S3/Blobs…).

**Cómo encajan hoy**:
- Puedes servir **archivos estáticos** desde una **CDN** (rápido y barato).
- La parte **dinámica** (autenticación, pagos, CRUD…) puede ir en **funciones serverless** o **edge** y consumir BDs externas (SaaS/DBaaS) o servicios (Stripe, Supabase, Firebase, etc.).
- Beneficio: Escalas por piezas, pagas lo que usas, y reduces complejidad de servidores “siempre encendidos”.

---


## 3) ¿Qué es Netlify?

**Netlify** es una plataforma de despliegue y *orquestación* para proyectos web modernos:
- **Hospeda** sitios **estáticos** (output de tu build) en su **CDN global**.
- **Construye (build)** tu proyecto desde un repo de Git con comandos que defines.
- **Añade dinamismo** con **Netlify Functions** (serverless, Node/Go) y **Edge Functions** (runtime Deno en el borde).
- Proporciona **servicios integrados**: prerendering, formularios, imagen CDN, analíticas, identidad, redirects/headers, etc.

> Filosofía: “Todo lo que pueda ser **pre‑renderizado**, que lo sea; lo demás, a **APIs/funciones**”.

---

## 4) Flujo mental: ¿mi proyecto es estático o dinámico?

1. **¿Puedo generar HTML estático en build?**
   - Sí → perfecto para **Netlify estático** (Next/Eleventy/Hugo/Vite/astro… con SSG).
   - No → necesitarás **SSR** o **funciones**.
2. **¿Necesito backend propio?**
   - Si solo llamas a **APIs de terceros** (Stripe, Airtable, Notion…), basta con **frontend + funciones**.
   - Si tienes lógica/BD propia, puedes usar **DBaaS** (Supabase, Neon, PlanetScale) + **Functions**.
3. **¿Necesito estado del usuario en el borde (muy baja latencia)?**
   - Considera **Edge Functions**.

En Netlify, **lo estático** va a **CDN**; **lo dinámico** va a **Functions/Edge**.

---

## 5) Maneras de desplegar en Netlify

### A) Conectar un repositorio Git (recomendado)
1. Crea sitio en Netlify → **Import from Git**.
2. Conecta **GitHub/GitLab/Bitbucket**.
3. Indica:
   - **Build command** (ej.: `npm run build`).
   - **Publish directory** (ej.: `dist`, `build`, `out`, `public`).
4. Cada *push* a la rama objetivo dispara un **build** y despliegue.

### B) Arrastrar y soltar (drag‑and‑drop)
- Compila localmente (o crea HTML/CSS/JS estático).
- **Arrastra** la carpeta de salida al panel de Netlify (**Deploys → Drop**). Rápido para prototipos.

### C) Netlify CLI
```bash
# Instalar
npm i -g netlify-cli

# Login en Netlify
netlify login

# Desplegar una carpeta (preview)
netlify deploy --dir=dist

# Desplegar a producción (usa el site vinculado)
netlify deploy --prod --dir=dist
```

### D) API / Integraciones CI/CD
- Útil para flujos avanzados (monorepos, orquestación, pipelines externos).

---

## 6) Configuración con `netlify.toml`

**Archivo raíz** para controlar builds, redirects, headers, funciones, etc.

```toml
# netlify.toml (ejemplo completo)
[build]
  command = "npm run build"
  publish  = "dist"
  # directorio con funciones (Node/TypeScript/Go)
  functions = "netlify/functions"

[functions]
  # tiempo máx de ejecución, node_bundler, flags…
  node_bundler = "esbuild"
  included_files = ["src/**/*.md"]

[[plugins]]
  package = "@netlify/plugin-lighthouse"

# Redirects equivalentes a _redirects
[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200

# Headers equivalentes a _headers
[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

# Edge Functions
[[edge_functions]]
  path = "/edge/*"
  function = "hello-edge"
```

---

## 7) Redirecciones y cabeceras (`_redirects` y `_headers`)

### `_redirects`
Un archivo plano en tu *publish dir* con reglas por línea:

```
# SPA fallback
/* /index.html 200

# API a Serverless
/api/* /.netlify/functions/:splat 200

# Redirección 301 permanente
/blog /articulos 301
```

### `_headers`
Define cabeceras por ruta:

```
# Cache fuerte para estáticos
/assets/*
  Cache-Control: public, max-age=31536000, immutable

# Seguridad
/*
  Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: no-referrer-when-downgrade
  Permissions-Policy: geolocation=(), camera=()
```

> También puedes gestionarlo en `netlify.toml` si prefieres TOML.

---

## 8) Variables de entorno y secretos

- En la UI: **Site → Settings → Environment variables**.
- En `netlify.toml` puedes leerlas, pero **no las confirmes** en el repo.
- En build: disponibles como `process.env.MI_VAR`.
- En **Functions**/Edge: también via `process.env` / `Deno.env.get`.
- Usa **scopes por contexto** (deploy previews vs producción) para claves distintas.

---

## 9) Funciones: Serverless y Edge

### 9.1) Netlify Functions (serverless)
- Directorio por defecto: `netlify/functions`.
- Runtime: **Node.js** (o Go).
- Despliegue: se empaquetan y se ejecutan como **AWS Lambda** administradas por Netlify.

**Ejemplo (Node, TypeScript o JS):** `netlify/functions/hello.js`
```js
exports.handler = async (event, context) => {
  const { name = "mundo" } = event.queryStringParameters || {};
  return {
    statusCode: 200,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ msg: `Hola, ${name}!` })
  };
};
```
**Ruta pública**: `/.netlify/functions/hello?name=Joaquin`

**Programadas (cron)**
```toml
# netlify.toml
[[scheduled.functions]]
  name = "hello"
  cron = "0 * * * *" # cada hora
```

**Background**: dispara trabajos asíncronos largos sin bloquear la respuesta.

### 9.2) Netlify Edge Functions
- Runtime **Deno** en la **red de borde** (bajísima latencia, acceso a `Request/Response` estilo Fetch API).
- Ideal para **middleware**: A/B testing, reescrituras, i18n, autenticación ligera.

**Ejemplo:** `netlify/edge-functions/hello-edge.ts`
```ts
export default async (req: Request) => {
  return new Response(`Hola desde el borde: ${new Date().toISOString()}`);
};
```
Y en `netlify.toml`:
```toml
[[edge_functions]]
  path = "/edge/*"
  function = "hello-edge"
```

> **¿Cuándo usar cada una?**
> - **Functions (Lambda)**: lógica de negocio, integraciones con BDs/APIs, procesos de varios cientos de ms.
> - **Edge**: decisiones ultra rápidas por solicitud (geolocalización, cookies, feature flags).

---

## 10) Formularios, imágenes, prerender y otros servicios

- **Forms**: Basta con añadir el atributo `netlify` a tu `<form>` y un `name`.
  ```html
  <form name="contacto" method="POST" netlify>
    <input type="text" name="nombre" required>
    <button type="submit">Enviar</button>
  </form>
  ```
  Netlify almacena envíos, puede enviar notificaciones, activar *spam filtering* y *honeypots*.

- **Image CDN**: optimización y *on-the-fly transformations* (resize, formato AVIF/WebP) vía URLs.

- **Prerendering**: renderizar HTML para bots/crawlers cuando usas SPA pesadas.

- **Analytics**: métricas de tráfico sin insertar scripts de terceros.

- **Identity** (opcional): autenticación básica (registro/login) + rules. Útil para *sites* con contenido privado simple.

---

## 11) Dominios, DNS y HTTPS

1. **Dominio gratuito**: `https://tu-sitio.netlify.app`.
2. **Dominio personalizado**: añade tu dominio en **Domain settings**.
3. **DNS**: puedes delegar a **Netlify DNS** o solo apuntar **CNAME/A** desde tu proveedor.
4. **HTTPS**: certificados **automáticos** con **Let’s Encrypt** (renovación automática).

**Buenas prácticas**: fuerza HTTPS, añade HSTS en `_headers`, configura redirección `www ↔ apex` en `_redirects`.

---

## 12) Previews, ramas, split testing y equipos

- **Deploy Previews**: cada PR/merge request genera una **URL única** con el build de esa rama. Oro para QA y revisión.
- **Branch Deploys**: define ramas que publiquen a URLs persistentes (p. ej. `develop` → entorno staging).
- **Split Testing**: sirve varias versiones a segmentos del tráfico.
- **Teams**: permisos, roles y colaboración.

---

## 13) Almacenamiento y datos en Netlify

> Netlify no es “tu base de datos” general, pero ofrece **primitivas de datos** útiles y se integra muy bien con **DBaaS**.

- **Blobs**: almacenamiento de archivos/objetos (similar a S3) gestionado por Netlify; ideal para cargas puntuales desde funciones.
- **KV**: *key‑value store* para *caché* rápida, *feature flags* o contadores.
- **Edge Config**: valores de configuración replicados globalmente para leer desde Edge Functions.
- **Partners/DBaaS**: Supabase, Neon (Postgres), PlanetScale (MySQL), Mongo Atlas, Redis, etc. Consume desde Functions/Edge.

**Patrones típicos**:
- **SSR híbrido**: usar **On‑Demand Builders** para generar y **cachear** páginas estáticas al primer hit.
- **ISR-like**: invalidar/regen contenido con webhooks + builds rápidos.

---

## 14) Ejemplos prácticos por stack

### 14.1) Sitio estático puro (HTML/CSS/JS)
- **Publish dir**: la carpeta del sitio (ej. `public/`).
- **Drag‑and‑drop** o `netlify deploy --dir=public --prod`.
- `_redirects` con SPA fallback si usas rutas del lado del cliente:
  ```
  /* /index.html 200
  ```

### 14.2) Vite/React/Angular/Vue (SPA con build)
```jsonc
// package.json
{
  "scripts": {
    "build": "vite build",
    "preview": "vite preview"
  }
}
```
- En Netlify: **Build command** `npm run build`, **Publish dir** `dist`.
- Añade `_redirects` si hay rutas del cliente.

### 14.3) Next.js / SvelteKit / Astro
- Preferir **SSG** cuando sea posible (páginas estáticas).
- Para SSR/APIs: **Netlify adapter** (p. ej. `@netlify/adapter-next`) que mapea rutas a **Functions/Edge**.
- Habilita **On‑Demand Builders** para contenido semi‑dinámico de alto rendimiento.

### 14.4) Formularios + correo
- Form con `netlify` + **Function** que envía vía proveedor (SendGrid/SES). Mantienes claves en variables de entorno.

---

## 15) Checklist de seguridad y rendimiento

- [ ] **HTTPS forzado** + **HSTS** (en `_headers`).
- [ ] **Caché** fuerte para assets versionados (`/assets/*`).
- [ ] **.env** fuera del repo; usa **Environment variables** por entorno.
- [ ] **CSP** estricta si puedes (`Content-Security-Policy`).
- [ ] **Auditoría** con Lighthouse/Plugin de Netlify.
- [ ] **Logs** de Functions y monitoreo de errores.
- [ ] **Edge** para redirecciones/i18n de baja latencia.

---

## 16) Problemas comunes y cómo depurarlos

**❌ Build falla**
- Revisa **logs** de build (Deploy details → Logs).
- Verifica **Node/npm** versión (puedes fijarla en `engines` del `package.json` o en *environment*).
- Asegura que **Publish dir** existe tras build (`dist`, `build`, `out`).

**❌ 404 en SPA rutas**
- Falta fallback en `_redirects`: `/* /index.html 200`.

**❌ Function 500**
- Revisa **`netlify/functions`** estructura, `exports.handler`, dependencias empaquetadas.
- Ver logs en **Functions → Logs**.

**❌ Variables no llegan**
- Define en **Environment** y **re‑build**. En local, usa `.env` + `netlify dev`.

**❌ Dominio no resuelve / sin SSL**
- Verifica registros DNS (CNAME/A/ALIAS). Espera propagación. Forzar emisión de certificado si cambiaste dominio.

---

## 17) Glosario

- **CDN**: Red de entrega de contenido. Replica archivos cerca del usuario.
- **SSG**: Static Site Generation. HTML preconstruido en build.
- **SSR**: Server-Side Rendering bajo demanda.
- **CSR**: Client-Side Rendering (navegador arma la UI con JS).
- **Serverless**: Funciones bajo demanda (AWS Lambda) administradas.
- **Edge**: Ejecución en el borde (Deno) muy cerquita del usuario.
- **On‑Demand Builders**: Genera y cachea páginas la primera vez que se piden.

---

## 18) Enlaces útiles

- Documentación principal: https://docs.netlify.com/
- CLI: https://docs.netlify.com/cli/get-started/
- Deploy desde Git: https://docs.netlify.com/site-deploys/create-deploys/
- `netlify.toml`: https://docs.netlify.com/configure-builds/file-based-configuration/
- Redirects: https://docs.netlify.com/routing/redirects/
- Functions: https://docs.netlify.com/functions/overview/
- Edge Functions: https://docs.netlify.com/edge-functions/overview/
- Forms: https://docs.netlify.com/forms/setup/
- DNS y dominios: https://docs.netlify.com/domains-https/
- Identity: https://docs.netlify.com/visitor-access/identity/
- Image CDN: https://docs.netlify.com/image-cdn/overview/
- On‑Demand Builders: https://docs.netlify.com/frameworks/#!on-demand-builders
- Programar Functions (cron): https://docs.netlify.com/functions/scheduled-functions/

---

### Apéndice A) Plantilla mínima de proyecto estático

```
project/
├─ public/              # HTML/CSS/JS ya listos
├─ netlify.toml         # config (opcional)
└─ package.json         # scripts de build (opcional)
```

**Comandos**
```bash
# Build local (si aplica)
npm run build

# Deploy preview
netlify deploy --dir=public

# Deploy producción
netlify deploy --prod --dir=public
```

### Apéndice B) SPA con fallback + API serverless

```
project/
├─ dist/ (build de Vite/React)
├─ netlify/
│  ├─ functions/
│  │  └─ api.js
│  └─ edge-functions/
│     └─ hello-edge.ts
├─ netlify.toml
└─ _redirects
```

**`_redirects`**
```
/* /index.html 200
/api/* /.netlify/functions/:splat 200
```

**`netlify.toml` (extracto)**
```toml
[build]
  command = "npm run build"
  publish = "dist"
  functions = "netlify/functions"

[[edge_functions]]
  path = "/edge/*"
  function = "hello-edge"
```

---

> **Resumen**: Netlify destaca cuando tu **salida principal es estática** (SSG/SPA build) y lo dinámico lo delegas a **Functions/Edge** o **APIs externas**. Obtienes **CDN global**, **builds automáticos desde Git**, **previews por rama**, **dominios/SSL gestionados**, y utilidades como **redirects, headers, formularios, imagen CDN, analíticas** y **almacenamiento ligero**. Es una base sólida, simple y escalable para sitios modernos.

