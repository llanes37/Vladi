/**
 * Aplicación Express
 * Configura middlewares, rutas y manejo de errores
 */

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const path = require('path');

// Importar rutas
const { authRoutes, postRoutes, userRoutes } = require('./routes');

// Importar middlewares de errores
const { notFoundHandler, errorHandler } = require('./middlewares');

// Crear aplicación Express
const app = express();

// ================================
// Middlewares globales
// ================================

// Seguridad HTTP headers
app.use(helmet({
  crossOriginResourcePolicy: { policy: "cross-origin" } // Permitir cargar imágenes desde otros orígenes
}));

// CORS - Configurar orígenes permitidos
app.use(cors({
  origin: process.env.FRONTEND_URL || 'http://localhost:5173',
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// Parsear JSON en el body
app.use(express.json({ limit: '10mb' }));

// Parsear URL-encoded (formularios)
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Logging de peticiones (solo en desarrollo)
if (process.env.NODE_ENV !== 'test') {
  app.use(morgan('dev'));
}

// Servir archivos estáticos (imágenes subidas)
app.use('/uploads', express.static(path.join(__dirname, '../uploads')));

// ================================
// Rutas de la API
// ================================

// Ruta de salud (para verificar que el servidor funciona)
app.get('/api/health', (req, res) => {
  res.json({
    success: true,
    message: '🚀 Mini Twitter API funcionando correctamente',
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// Montar rutas
app.use('/api/auth', authRoutes);
app.use('/api/posts', postRoutes);
app.use('/api/users', userRoutes);

// ================================
// Manejo de errores
// ================================

// Ruta no encontrada (404)
app.use(notFoundHandler);

// Manejador global de errores
app.use(errorHandler);

module.exports = app;
