/**
 * Punto de entrada del servidor
 * Carga variables de entorno, conecta a BD e inicia el servidor
 */

// Cargar variables de entorno ANTES de cualquier otra cosa
require('dotenv').config();

const app = require('./app');
const { connectDB, server: serverConfig } = require('./config');

// Puerto del servidor
const PORT = serverConfig.port;

/**
 * Función principal para iniciar el servidor
 */
const startServer = async () => {
  try {
    // 1. Conectar a MongoDB
    console.log('🔄 Conectando a MongoDB...');
    await connectDB();
    
    // 2. Iniciar el servidor HTTP
    const server = app.listen(PORT, () => {
      console.log(`
╔════════════════════════════════════════════════════════╗
║                                                        ║
║   🐦 Mini Twitter API                                  ║
║                                                        ║
║   Servidor corriendo en: http://localhost:${PORT}        ║
║   Entorno: ${(serverConfig.env || 'development').padEnd(40)}║
║                                                        ║
║   Endpoints disponibles:                               ║
║   • GET  /api/health         - Estado del servidor     ║
║   • POST /api/auth/register  - Registrar usuario       ║
║   • POST /api/auth/login     - Iniciar sesión          ║
║   • GET  /api/auth/me        - Usuario actual          ║
║   • GET  /api/posts          - Timeline                ║
║   • POST /api/posts          - Crear post              ║
║   • GET  /api/users/:id      - Perfil de usuario       ║
║   • GET  /api/users/:id/posts - Posts de usuario       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
      `);
    });
    
    // Manejar errores del servidor
    server.on('error', (error) => {
      if (error.code === 'EADDRINUSE') {
        console.error(`❌ El puerto ${PORT} ya está en uso`);
      } else {
        console.error('❌ Error del servidor:', error);
      }
      process.exit(1);
    });
    
    // Manejar señales de cierre graceful
    const gracefulShutdown = (signal) => {
      console.log(`\n📴 Recibida señal ${signal}. Cerrando servidor...`);
      server.close(() => {
        console.log('✅ Servidor cerrado correctamente');
        process.exit(0);
      });
    };
    
    process.on('SIGTERM', () => gracefulShutdown('SIGTERM'));
    process.on('SIGINT', () => gracefulShutdown('SIGINT'));
    
  } catch (error) {
    console.error('❌ Error al iniciar el servidor:', error);
    process.exit(1);
  }
};

// Iniciar el servidor
startServer();
