/**
 * Modelo de Usuario
 * Define el esquema de usuarios en MongoDB
 */

const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new mongoose.Schema({
  // Nombre de usuario (único y obligatorio)
  username: {
    type: String,
    required: [true, 'El nombre de usuario es obligatorio'],
    unique: true,
    trim: true,
    minlength: [3, 'El nombre de usuario debe tener al menos 3 caracteres'],
    maxlength: [30, 'El nombre de usuario no puede exceder 30 caracteres'],
    match: [/^[a-zA-Z0-9_]+$/, 'Solo se permiten letras, números y guiones bajos']
  },
  
  // Email (único y obligatorio)
  email: {
    type: String,
    required: [true, 'El email es obligatorio'],
    unique: true,
    trim: true,
    lowercase: true,
    match: [/^\S+@\S+\.\S+$/, 'Por favor ingresa un email válido']
  },
  
  // Contraseña hasheada
  password: {
    type: String,
    required: [true, 'La contraseña es obligatoria'],
    minlength: [6, 'La contraseña debe tener al menos 6 caracteres'],
    select: false // No incluir en queries por defecto
  },
  
  // Nombre para mostrar
  displayName: {
    type: String,
    trim: true,
    maxlength: [50, 'El nombre no puede exceder 50 caracteres']
  },
  
  // Biografía del usuario
  bio: {
    type: String,
    trim: true,
    maxlength: [160, 'La bio no puede exceder 160 caracteres']
  },
  
  // URL del avatar
  avatarURL: {
    type: String,
    default: null
  },
  
  // Fecha de creación
  createdAt: {
    type: Date,
    default: Date.now
  }
}, {
  timestamps: true, // Añade createdAt y updatedAt automáticamente
  toJSON: {
    // Transformar el documento al convertir a JSON
    transform: (doc, ret) => {
      ret.id = ret._id;
      delete ret._id;
      delete ret.__v;
      delete ret.password;
      return ret;
    }
  }
});

// ================================
// Middleware de Mongoose (Hooks)
// ================================

/**
 * Pre-save hook: hashea la contraseña antes de guardar
 */
userSchema.pre('save', async function(next) {
  // Solo hashear si la contraseña fue modificada
  if (!this.isModified('password')) return next();
  
  try {
    const salt = await bcrypt.genSalt(12);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// ================================
// Métodos de instancia
// ================================

/**
 * Compara una contraseña en texto plano con el hash almacenado
 * @param {string} candidatePassword - Contraseña a verificar
 * @returns {Promise<boolean>} true si coinciden
 */
userSchema.methods.comparePassword = async function(candidatePassword) {
  return bcrypt.compare(candidatePassword, this.password);
};

/**
 * Devuelve los datos públicos del usuario (sin info sensible)
 * @returns {Object} Datos públicos
 */
userSchema.methods.toPublicJSON = function() {
  return {
    id: this._id,
    username: this.username,
    displayName: this.displayName || this.username,
    email: this.email,
    bio: this.bio,
    avatarURL: this.avatarURL,
    createdAt: this.createdAt
  };
};

// ================================
// Métodos estáticos
// ================================

/**
 * Busca un usuario por email o username
 * @param {string} identifier - Email o username
 * @returns {Promise<User|null>}
 */
userSchema.statics.findByEmailOrUsername = function(identifier) {
  return this.findOne({
    $or: [
      { email: identifier.toLowerCase() },
      { username: identifier }
    ]
  }).select('+password'); // Incluir password para verificación
};

// Crear índices para búsquedas eficientes
userSchema.index({ email: 1 });
userSchema.index({ username: 1 });

const User = mongoose.model('User', userSchema);

module.exports = User;
