/**
 * Validadores usando express-validator
 * Define reglas de validación reutilizables
 */

const { body, param, query, validationResult } = require('express-validator');
const { ApiError } = require('./errorHandler');

/**
 * Middleware para procesar errores de validación
 */
const validate = (req, res, next) => {
  const errors = validationResult(req);
  
  if (!errors.isEmpty()) {
    const formattedErrors = errors.array().map(err => ({
      field: err.path,
      message: err.msg
    }));
    
    return res.status(400).json({
      success: false,
      message: 'Error de validación',
      errors: formattedErrors
    });
  }
  
  next();
};

// ================================
// Validadores de Autenticación
// ================================

const registerValidation = [
  body('username')
    .trim()
    .notEmpty().withMessage('El nombre de usuario es obligatorio')
    .isLength({ min: 3, max: 30 }).withMessage('El usuario debe tener entre 3 y 30 caracteres')
    .matches(/^[a-zA-Z0-9_]+$/).withMessage('Solo se permiten letras, números y guiones bajos'),
  
  body('email')
    .trim()
    .notEmpty().withMessage('El email es obligatorio')
    .isEmail().withMessage('El email no es válido')
    .normalizeEmail(),
  
  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria')
    .isLength({ min: 6 }).withMessage('La contraseña debe tener al menos 6 caracteres'),
  
  body('displayName')
    .optional()
    .trim()
    .isLength({ max: 50 }).withMessage('El nombre no puede exceder 50 caracteres'),
  
  validate
];

const loginValidation = [
  body('email')
    .trim()
    .notEmpty().withMessage('El email o usuario es obligatorio'),
  
  body('password')
    .notEmpty().withMessage('La contraseña es obligatoria'),
  
  validate
];

// ================================
// Validadores de Posts
// ================================

const createPostValidation = [
  body('text')
    .trim()
    .notEmpty().withMessage('El texto del post es obligatorio')
    .isLength({ max: 280 }).withMessage('El post no puede exceder 280 caracteres'),
  
  validate
];

// ================================
// Validadores de Paginación
// ================================

const paginationValidation = [
  query('page')
    .optional()
    .isInt({ min: 1 }).withMessage('La página debe ser un número entero positivo')
    .toInt(),
  
  query('limit')
    .optional()
    .isInt({ min: 1, max: 100 }).withMessage('El límite debe ser entre 1 y 100')
    .toInt(),
  
  validate
];

// ================================
// Validadores de Parámetros
// ================================

const mongoIdValidation = (paramName = 'id') => [
  param(paramName)
    .isMongoId().withMessage('ID inválido'),
  
  validate
];

// ================================
// Validadores de Perfil
// ================================

const updateProfileValidation = [
  body('displayName')
    .optional()
    .trim()
    .isLength({ max: 50 }).withMessage('El nombre no puede exceder 50 caracteres'),
  
  body('bio')
    .optional()
    .trim()
    .isLength({ max: 160 }).withMessage('La bio no puede exceder 160 caracteres'),
  
  validate
];

module.exports = {
  validate,
  registerValidation,
  loginValidation,
  createPostValidation,
  paginationValidation,
  mongoIdValidation,
  updateProfileValidation
};
