# 🐦 Mini Twitter - Red Social con Vue 3 + Node.js

Una mini red social tipo Twitter construida con tecnologías modernas.

## 🏗️ Arquitectura

```
mini-twitter/
├── backend/          # API REST con Node.js + Express
│   ├── src/
│   │   ├── config/   # Configuración (DB, JWT, etc.)
│   │   ├── controllers/
│   │   ├── middlewares/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── tests/
│   └── uploads/      # Imágenes subidas
├── frontend/         # SPA con Vue 3 + Vuetify
│   └── src/
│       ├── components/
│       ├── views/
│       ├── router/
│       ├── stores/
│       └── services/
└── README.md
```

## 🛠️ Tecnologías

### Backend
- **Node.js + Express**: Servidor REST
- **MongoDB + Mongoose**: Base de datos NoSQL
- **JWT**: Autenticación stateless
- **bcrypt**: Encriptación de contraseñas
- **Multer**: Subida de archivos
- **Jest**: Testing

### Frontend
- **Vue 3**: Framework reactivo con Composition API
- **Vuetify 3**: Componentes Material Design
- **Pinia**: Gestión de estado
- **Vue Router**: Navegación SPA
- **Axios**: Cliente HTTP

## 🚀 Instalación y Ejecución

### Requisitos previos
- Node.js 18+
- MongoDB (local o Atlas)
- npm o pnpm

### 1. Clonar e instalar

```bash
# Backend
cd backend
npm install

# Frontend
cd ../frontend
npm install
```

### 2. Configurar variables de entorno

Crear `backend/.env`:
```env
PORT=3000
MONGODB_URI=mongodb://localhost:27017/mini-twitter
JWT_SECRET=tu_clave_secreta_muy_segura_cambiar_en_produccion
JWT_EXPIRES_IN=7d
```

### 3. Ejecutar

```bash
# Terminal 1 - Backend
cd backend
npm run dev

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### 4. Acceder
- Frontend: http://localhost:5173
- Backend API: http://localhost:3000/api

## 📡 Endpoints API

### Autenticación
| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/api/auth/register` | Registrar usuario |
| POST | `/api/auth/login` | Iniciar sesión |
| GET | `/api/auth/me` | Obtener usuario actual |

### Posts
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/api/posts` | Listar posts (paginado) |
| POST | `/api/posts` | Crear post |
| GET | `/api/users/:id/posts` | Posts de un usuario |

## 🎨 Características

- ✅ Registro e inicio de sesión
- ✅ Timeline con posts de todos los usuarios
- ✅ Crear posts con texto, emojis e imágenes
- ✅ Perfil de usuario
- ✅ Tema claro/oscuro
- ✅ Diseño responsive
- ✅ Tiempo relativo ("hace 2 minutos")

## 📝 Licencia

MIT - Proyecto educativo
