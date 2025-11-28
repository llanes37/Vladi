/**
 * Servicio de Autenticación
 * Maneja la lógica de negocio de registro, login y tokens JWT
 */

const jwt = require('jsonwebtoken');
const { User } = require('../models');
const { jwtConfig } = require('../config');
const { ApiError } = require('../middlewares');

/**
 * Genera un token JWT para un usuario
 * @param {string} userId - ID del usuario
 * @returns {string} Token JWT
 */
const generateToken = (userId) => {
  return jwt.sign(
    { userId },
    jwtConfig.secret,
    { 
      expiresIn: jwtConfig.expiresIn,
      algorithm: jwtConfig.algorithm
    }
  );
};

/**
 * Registra un nuevo usuario
 * @param {Object} userData - Datos del usuario
 * @returns {Promise<{user: Object, token: string}>}
 */
const register = async ({ username, email, password, displayName }) => {
  // Verificar si el email ya existe
  const existingEmail = await User.findOne({ email: email.toLowerCase() });
  if (existingEmail) {
    throw ApiError.conflict('Este email ya está registrado');
  }
  
  // Verificar si el username ya existe
  const existingUsername = await User.findOne({ username });
  if (existingUsername) {
    throw ApiError.conflict('Este nombre de usuario ya está en uso');
  }
  
  // Crear el usuario
  const user = new User({
    username,
    email: email.toLowerCase(),
    password,
    displayName: displayName || username
  });
  
  await user.save();
  
  // Generar token
  const token = generateToken(user._id);
  
  return {
    user: user.toPublicJSON(),
    token
  };
};

/**
 * Inicia sesión de un usuario
 * @param {string} email - Email o username
 * @param {string} password - Contraseña
 * @returns {Promise<{user: Object, token: string}>}
 */
const login = async (email, password) => {
  // Buscar usuario por email o username
  const user = await User.findByEmailOrUsername(email);
  
  if (!user) {
    throw ApiError.unauthorized('Credenciales incorrectas');
  }
  
  // Verificar contraseña
  const isValidPassword = await user.comparePassword(password);
  
  if (!isValidPassword) {
    throw ApiError.unauthorized('Credenciales incorrectas');
  }
  
  // Generar token
  const token = generateToken(user._id);
  
  return {
    user: user.toPublicJSON(),
    token
  };
};

/**
 * Obtiene el usuario actual por ID
 * @param {string} userId - ID del usuario
 * @returns {Promise<Object>}
 */
const getCurrentUser = async (userId) => {
  const user = await User.findById(userId);
  
  if (!user) {
    throw ApiError.notFound('Usuario no encontrado');
  }
  
  return user.toPublicJSON();
};

/**
 * Actualiza el perfil del usuario
 * @param {string} userId - ID del usuario
 * @param {Object} updates - Campos a actualizar
 * @returns {Promise<Object>}
 */
const updateProfile = async (userId, { displayName, bio, avatarURL }) => {
  const user = await User.findById(userId);
  
  if (!user) {
    throw ApiError.notFound('Usuario no encontrado');
  }
  
  // Actualizar solo los campos proporcionados
  if (displayName !== undefined) user.displayName = displayName;
  if (bio !== undefined) user.bio = bio;
  if (avatarURL !== undefined) user.avatarURL = avatarURL;
  
  await user.save();
  
  return user.toPublicJSON();
};

/**
 * Obtiene un usuario por ID (perfil público)
 * @param {string} userId - ID del usuario
 * @returns {Promise<Object>}
 */
const getUserById = async (userId) => {
  const user = await User.findById(userId);
  
  if (!user) {
    throw ApiError.notFound('Usuario no encontrado');
  }
  
  return user.toPublicJSON();
};

module.exports = {
  generateToken,
  register,
  login,
  getCurrentUser,
  updateProfile,
  getUserById
};
