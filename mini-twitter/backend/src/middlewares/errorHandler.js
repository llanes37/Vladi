/**
 * Middleware de manejo de errores centralizado
 * Captura todos los errores y devuelve respuestas consistentes
 */

/**
 * Clase personalizada para errores de la API
 */
class ApiError extends Error {
  constructor(statusCode, message, errors = null) {
    super(message);
    this.statusCode = statusCode;
    this.errors = errors;
    this.isOperational = true; // Marca errores operacionales vs errores de programación
    
    Error.captureStackTrace(this, this.constructor);
  }
  
  // Métodos estáticos para crear errores comunes
  static badRequest(message = 'Petición inválida', errors = null) {
    return new ApiError(400, message, errors);
  }
  
  static unauthorized(message = 'No autorizado') {
    return new ApiError(401, message);
  }
  
  static forbidden(message = 'Acceso prohibido') {
    return new ApiError(403, message);
  }
  
  static notFound(message = 'Recurso no encontrado') {
    return new ApiError(404, message);
  }
  
  static conflict(message = 'Conflicto con el estado actual') {
    return new ApiError(409, message);
  }
  
  static internal(message = 'Error interno del servidor') {
    return new ApiError(500, message);
  }
}

/**
 * Middleware para manejar rutas no encontradas (404)
 */
const notFoundHandler = (req, res, next) => {
  const error = ApiError.notFound(`Ruta no encontrada: ${req.method} ${req.originalUrl}`);
  next(error);
};

/**
 * Middleware principal de manejo de errores
 * Debe ser el último middleware de la aplicación
 */
const errorHandler = (err, req, res, next) => {
  // Log del error para debugging
  console.error('🔴 Error:', {
    message: err.message,
    stack: process.env.NODE_ENV === 'development' ? err.stack : undefined,
    path: req.path,
    method: req.method
  });
  
  // Valores por defecto
  let statusCode = err.statusCode || 500;
  let message = err.message || 'Error interno del servidor';
  let errors = err.errors || null;
  
  // Manejar errores específicos de Mongoose
  if (err.name === 'ValidationError') {
    // Error de validación de Mongoose
    statusCode = 400;
    message = 'Error de validación';
    errors = Object.values(err.errors).map(e => ({
      field: e.path,
      message: e.message
    }));
  } else if (err.name === 'CastError') {
    // Error de tipo (ej: ObjectId inválido)
    statusCode = 400;
    message = `Valor inválido para ${err.path}: ${err.value}`;
  } else if (err.code === 11000) {
    // Error de duplicado (índice único)
    statusCode = 409;
    const field = Object.keys(err.keyPattern)[0];
    message = `Ya existe un registro con ese ${field}`;
    errors = [{ field, message: `Este ${field} ya está en uso` }];
  } else if (err.name === 'JsonWebTokenError' || err.name === 'TokenExpiredError') {
    // Errores de JWT
    statusCode = 401;
    message = err.name === 'TokenExpiredError' 
      ? 'Token expirado. Por favor, inicia sesión de nuevo.'
      : 'Token inválido';
  }
  
  // En producción, no exponer detalles de errores internos
  if (statusCode === 500 && process.env.NODE_ENV === 'production') {
    message = 'Error interno del servidor';
    errors = null;
  }
  
  // Enviar respuesta de error
  res.status(statusCode).json({
    success: false,
    message,
    errors,
    // Solo incluir stack en desarrollo
    ...(process.env.NODE_ENV === 'development' && { stack: err.stack })
  });
};

module.exports = {
  ApiError,
  notFoundHandler,
  errorHandler
};
