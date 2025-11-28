/**
 * Middleware de Autenticación JWT
 * Verifica el token y añade el usuario a req.user
 */

const jwt = require('jsonwebtoken');
const { User } = require('../models');
const { jwtConfig } = require('../config');

/**
 * Middleware que verifica el token JWT y carga el usuario
 * Uso: router.get('/ruta-protegida', authMiddleware, controller)
 */
const authMiddleware = async (req, res, next) => {
  try {
    // 1. Obtener token del header Authorization
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({
        success: false,
        message: 'Acceso denegado. Token no proporcionado.'
      });
    }
    
    // 2. Extraer el token (formato: "Bearer <token>")
    const token = authHeader.split(' ')[1];
    
    if (!token) {
      return res.status(401).json({
        success: false,
        message: 'Acceso denegado. Token inválido.'
      });
    }
    
    // 3. Verificar y decodificar el token
    const decoded = jwt.verify(token, jwtConfig.secret);
    
    // 4. Buscar el usuario en la base de datos
    const user = await User.findById(decoded.userId);
    
    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'Usuario no encontrado. Token inválido.'
      });
    }
    
    // 5. Añadir el usuario a la request para uso posterior
    req.user = user;
    req.userId = user._id;
    
    next();
  } catch (error) {
    // Manejar errores específicos de JWT
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        success: false,
        message: 'Token inválido.'
      });
    }
    
    if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        success: false,
        message: 'Token expirado. Por favor, inicia sesión de nuevo.'
      });
    }
    
    // Error genérico
    console.error('Error en authMiddleware:', error);
    return res.status(500).json({
      success: false,
      message: 'Error al verificar la autenticación.'
    });
  }
};

/**
 * Middleware opcional de autenticación
 * No falla si no hay token, pero carga el usuario si existe
 */
const optionalAuthMiddleware = async (req, res, next) => {
  try {
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return next();
    }
    
    const token = authHeader.split(' ')[1];
    
    if (!token) {
      return next();
    }
    
    const decoded = jwt.verify(token, jwtConfig.secret);
    const user = await User.findById(decoded.userId);
    
    if (user) {
      req.user = user;
      req.userId = user._id;
    }
    
    next();
  } catch (error) {
    // En caso de error, simplemente continuar sin usuario
    next();
  }
};

module.exports = {
  authMiddleware,
  optionalAuthMiddleware
};
