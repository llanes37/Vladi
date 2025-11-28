/**
 * Controlador de Autenticación
 * Maneja las peticiones HTTP de registro, login y perfil
 */

const { authService } = require('../services');

/**
 * POST /api/auth/register
 * Registra un nuevo usuario
 */
const register = async (req, res, next) => {
  try {
    const { username, email, password, displayName } = req.body;
    
    const result = await authService.register({
      username,
      email,
      password,
      displayName
    });
    
    res.status(201).json({
      success: true,
      message: 'Usuario registrado correctamente',
      data: result
    });
  } catch (error) {
    next(error);
  }
};

/**
 * POST /api/auth/login
 * Inicia sesión y devuelve token JWT
 */
const login = async (req, res, next) => {
  try {
    const { email, password } = req.body;
    
    const result = await authService.login(email, password);
    
    res.json({
      success: true,
      message: 'Inicio de sesión exitoso',
      data: result
    });
  } catch (error) {
    next(error);
  }
};

/**
 * GET /api/auth/me
 * Devuelve el usuario autenticado actual
 */
const getCurrentUser = async (req, res, next) => {
  try {
    const user = await authService.getCurrentUser(req.userId);
    
    res.json({
      success: true,
      data: { user }
    });
  } catch (error) {
    next(error);
  }
};

/**
 * PUT /api/auth/profile
 * Actualiza el perfil del usuario autenticado
 */
const updateProfile = async (req, res, next) => {
  try {
    const { displayName, bio } = req.body;
    let avatarURL = req.body.avatarURL;
    
    // Si se subió un archivo de avatar
    if (req.file) {
      avatarURL = `/uploads/${req.file.filename}`;
    }
    
    const user = await authService.updateProfile(req.userId, {
      displayName,
      bio,
      avatarURL
    });
    
    res.json({
      success: true,
      message: 'Perfil actualizado correctamente',
      data: { user }
    });
  } catch (error) {
    next(error);
  }
};

/**
 * GET /api/users/:id
 * Devuelve el perfil público de un usuario
 */
const getUserById = async (req, res, next) => {
  try {
    const user = await authService.getUserById(req.params.id);
    
    res.json({
      success: true,
      data: { user }
    });
  } catch (error) {
    next(error);
  }
};

module.exports = {
  register,
  login,
  getCurrentUser,
  updateProfile,
  getUserById
};
