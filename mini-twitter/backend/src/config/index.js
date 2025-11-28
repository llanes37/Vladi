/**
 * Configuración centralizada de la aplicación
 * Exporta todas las configuraciones desde un solo punto
 */

const { connectDB, disconnectDB } = require('./database');
const jwtConfig = require('./jwt');

module.exports = {
  connectDB,
  disconnectDB,
  jwtConfig,
  
  // Configuración del servidor
  server: {
    port: process.env.PORT || 3000,
    env: process.env.NODE_ENV || 'development'
  },
  
  // Configuración de uploads
  uploads: {
    maxFileSize: 5 * 1024 * 1024, // 5MB
    allowedTypes: ['image/jpeg', 'image/png', 'image/gif', 'image/webp'],
    uploadDir: 'uploads'
  },
  
  // Configuración de paginación
  pagination: {
    defaultLimit: 20,
    maxLimit: 100
  }
};
