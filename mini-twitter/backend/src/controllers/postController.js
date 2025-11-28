/**
 * Controlador de Posts
 * Maneja las peticiones HTTP de publicaciones
 */

const { postService } = require('../services');

/**
 * GET /api/posts
 * Obtiene el timeline (posts más recientes)
 */
const getTimeline = async (req, res, next) => {
  try {
    const { page = 1, limit = 20 } = req.query;
    
    const result = await postService.getTimeline({
      page: parseInt(page),
      limit: parseInt(limit)
    });
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    next(error);
  }
};

/**
 * POST /api/posts
 * Crea un nuevo post
 */
const createPost = async (req, res, next) => {
  try {
    const { text } = req.body;
    const imageFilename = req.file ? req.file.filename : null;
    
    const post = await postService.createPost({
      authorId: req.userId,
      text,
      imageFilename
    });
    
    res.status(201).json({
      success: true,
      message: 'Post publicado correctamente',
      data: { post }
    });
  } catch (error) {
    next(error);
  }
};

/**
 * GET /api/posts/:id
 * Obtiene un post específico
 */
const getPostById = async (req, res, next) => {
  try {
    const post = await postService.getPostById(req.params.id);
    
    res.json({
      success: true,
      data: { post }
    });
  } catch (error) {
    next(error);
  }
};

/**
 * DELETE /api/posts/:id
 * Elimina un post (solo el autor)
 */
const deletePost = async (req, res, next) => {
  try {
    await postService.deletePost(req.params.id, req.userId);
    
    res.json({
      success: true,
      message: 'Post eliminado correctamente'
    });
  } catch (error) {
    next(error);
  }
};

/**
 * GET /api/users/:id/posts
 * Obtiene los posts de un usuario específico
 */
const getPostsByUser = async (req, res, next) => {
  try {
    const { page = 1, limit = 20 } = req.query;
    
    const result = await postService.getPostsByUser(req.params.id, {
      page: parseInt(page),
      limit: parseInt(limit)
    });
    
    res.json({
      success: true,
      data: result
    });
  } catch (error) {
    next(error);
  }
};

module.exports = {
  getTimeline,
  createPost,
  getPostById,
  deletePost,
  getPostsByUser
};
