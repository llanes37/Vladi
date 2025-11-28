/**
 * Configuración de JWT (JSON Web Tokens)
 * Define cómo se generan y verifican los tokens de autenticación
 */

module.exports = {
  // Clave secreta para firmar tokens (desde variables de entorno)
  secret: process.env.JWT_SECRET || 'default_secret_change_me',
  
  // Tiempo de expiración del token
  expiresIn: process.env.JWT_EXPIRES_IN || '7d',
  
  // Algoritmo de firma
  algorithm: 'HS256'
};
