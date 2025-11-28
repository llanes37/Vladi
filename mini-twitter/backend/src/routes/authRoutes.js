/**
 * Rutas de Autenticación
 * /api/auth/*
 */

const express = require('express');
const router = express.Router();

const { authController } = require('../controllers');
const { 
  authMiddleware, 
  registerValidation, 
  loginValidation,
  updateProfileValidation,
  upload,
  handleMulterError
} = require('../middlewares');

/**
 * @route   POST /api/auth/register
 * @desc    Registrar nuevo usuario
 * @access  Public
 * @body    { username, email, password, displayName? }
 */
router.post('/register', registerValidation, authController.register);

/**
 * @route   POST /api/auth/login
 * @desc    Iniciar sesión
 * @access  Public
 * @body    { email, password }
 */
router.post('/login', loginValidation, authController.login);

/**
 * @route   GET /api/auth/me
 * @desc    Obtener usuario autenticado actual
 * @access  Private (requiere JWT)
 */
router.get('/me', authMiddleware, authController.getCurrentUser);

/**
 * @route   PUT /api/auth/profile
 * @desc    Actualizar perfil del usuario
 * @access  Private (requiere JWT)
 * @body    { displayName?, bio?, avatarURL? } o FormData con avatar
 */
router.put(
  '/profile',
  authMiddleware,
  upload.single('avatar'),
  handleMulterError,
  updateProfileValidation,
  authController.updateProfile
);

module.exports = router;
