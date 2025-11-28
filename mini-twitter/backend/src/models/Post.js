/**
 * Modelo de Post
 * Define el esquema de publicaciones en MongoDB
 */

const mongoose = require('mongoose');

const postSchema = new mongoose.Schema({
  // Autor del post (referencia al modelo User)
  author: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: [true, 'El autor es obligatorio'],
    index: true
  },
  
  // Contenido de texto del post
  text: {
    type: String,
    required: [true, 'El texto del post es obligatorio'],
    trim: true,
    maxlength: [280, 'El post no puede exceder 280 caracteres'] // Límite tipo Twitter
  },
  
  // URL de la imagen (opcional)
  imageURL: {
    type: String,
    default: null
  },
  
  // Contador de likes (para futuras implementaciones)
  likesCount: {
    type: Number,
    default: 0
  },
  
  // Contador de comentarios (para futuras implementaciones)
  commentsCount: {
    type: Number,
    default: 0
  }
}, {
  timestamps: true, // createdAt y updatedAt automáticos
  toJSON: {
    transform: (doc, ret) => {
      ret.id = ret._id;
      delete ret._id;
      delete ret.__v;
      return ret;
    }
  }
});

// ================================
// Índices para optimización
// ================================

// Índice compuesto para consultas de timeline (ordenado por fecha)
postSchema.index({ createdAt: -1 });

// Índice para buscar posts de un usuario específico
postSchema.index({ author: 1, createdAt: -1 });

// ================================
// Métodos estáticos
// ================================

/**
 * Obtiene el timeline (posts más recientes de todos los usuarios)
 * @param {Object} options - Opciones de paginación
 * @param {number} options.page - Número de página (1-indexed)
 * @param {number} options.limit - Posts por página
 * @returns {Promise<{posts: Post[], total: number, pages: number}>}
 */
postSchema.statics.getTimeline = async function({ page = 1, limit = 20 } = {}) {
  const skip = (page - 1) * limit;
  
  const [posts, total] = await Promise.all([
    this.find()
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit)
      .populate('author', 'username displayName avatarURL')
      .lean(),
    this.countDocuments()
  ]);
  
  return {
    posts: posts.map(post => ({
      ...post,
      id: post._id,
      _id: undefined,
      __v: undefined
    })),
    total,
    pages: Math.ceil(total / limit),
    currentPage: page,
    hasMore: skip + posts.length < total
  };
};

/**
 * Obtiene los posts de un usuario específico
 * @param {string} userId - ID del usuario
 * @param {Object} options - Opciones de paginación
 * @returns {Promise<{posts: Post[], total: number}>}
 */
postSchema.statics.getByUser = async function(userId, { page = 1, limit = 20 } = {}) {
  const skip = (page - 1) * limit;
  
  const [posts, total] = await Promise.all([
    this.find({ author: userId })
      .sort({ createdAt: -1 })
      .skip(skip)
      .limit(limit)
      .populate('author', 'username displayName avatarURL')
      .lean(),
    this.countDocuments({ author: userId })
  ]);
  
  return {
    posts: posts.map(post => ({
      ...post,
      id: post._id,
      _id: undefined,
      __v: undefined
    })),
    total,
    pages: Math.ceil(total / limit),
    currentPage: page,
    hasMore: skip + posts.length < total
  };
};

// ================================
// Métodos de instancia
// ================================

/**
 * Pobla el autor y devuelve el post formateado
 * @returns {Promise<Object>}
 */
postSchema.methods.toFormattedJSON = async function() {
  await this.populate('author', 'username displayName avatarURL');
  
  return {
    id: this._id,
    text: this.text,
    imageURL: this.imageURL,
    author: this.author,
    likesCount: this.likesCount,
    commentsCount: this.commentsCount,
    createdAt: this.createdAt,
    updatedAt: this.updatedAt
  };
};

const Post = mongoose.model('Post', postSchema);

module.exports = Post;
