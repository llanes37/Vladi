/**
 * Servicio de Posts
 * Maneja la lógica de negocio de publicaciones
 */

const { Post, User } = require('../models');
const { ApiError, deleteUploadedFile, getImageUrl } = require('../middlewares');

/**
 * Crea un nuevo post
 * @param {Object} postData - Datos del post
 * @param {string} postData.authorId - ID del autor
 * @param {string} postData.text - Texto del post
 * @param {string} [postData.imageFilename] - Nombre del archivo de imagen
 * @returns {Promise<Object>}
 */
const createPost = async ({ authorId, text, imageFilename }) => {
  // Verificar que el autor existe
  const author = await User.findById(authorId);
  if (!author) {
    throw ApiError.notFound('Usuario no encontrado');
  }
  
  // Crear el post
  const post = new Post({
    author: authorId,
    text,
    imageURL: imageFilename ? getImageUrl(imageFilename) : null
  });
  
  await post.save();
  
  // Devolver el post con datos del autor
  return post.toFormattedJSON();
};

/**
 * Obtiene el timeline (posts más recientes)
 * @param {Object} options - Opciones de paginación
 * @returns {Promise<Object>}
 */
const getTimeline = async ({ page = 1, limit = 20 } = {}) => {
  // Limitar el máximo de posts por página
  const safeLimit = Math.min(limit, 100);
  
  return Post.getTimeline({ page, limit: safeLimit });
};

/**
 * Obtiene los posts de un usuario específico
 * @param {string} userId - ID del usuario
 * @param {Object} options - Opciones de paginación
 * @returns {Promise<Object>}
 */
const getPostsByUser = async (userId, { page = 1, limit = 20 } = {}) => {
  // Verificar que el usuario existe
  const user = await User.findById(userId);
  if (!user) {
    throw ApiError.notFound('Usuario no encontrado');
  }
  
  const safeLimit = Math.min(limit, 100);
  
  return Post.getByUser(userId, { page, limit: safeLimit });
};

/**
 * Obtiene un post por ID
 * @param {string} postId - ID del post
 * @returns {Promise<Object>}
 */
const getPostById = async (postId) => {
  const post = await Post.findById(postId).populate('author', 'username displayName avatarURL');
  
  if (!post) {
    throw ApiError.notFound('Post no encontrado');
  }
  
  return {
    id: post._id,
    text: post.text,
    imageURL: post.imageURL,
    author: post.author,
    likesCount: post.likesCount,
    commentsCount: post.commentsCount,
    createdAt: post.createdAt,
    updatedAt: post.updatedAt
  };
};

/**
 * Elimina un post (solo el autor puede)
 * @param {string} postId - ID del post
 * @param {string} userId - ID del usuario que intenta eliminar
 * @returns {Promise<void>}
 */
const deletePost = async (postId, userId) => {
  const post = await Post.findById(postId);
  
  if (!post) {
    throw ApiError.notFound('Post no encontrado');
  }
  
  // Verificar que el usuario es el autor
  if (post.author.toString() !== userId.toString()) {
    throw ApiError.forbidden('No tienes permiso para eliminar este post');
  }
  
  // Si hay imagen, eliminarla
  if (post.imageURL) {
    const filename = post.imageURL.split('/').pop();
    deleteUploadedFile(filename);
  }
  
  await Post.findByIdAndDelete(postId);
};

module.exports = {
  createPost,
  getTimeline,
  getPostsByUser,
  getPostById,
  deletePost
};
