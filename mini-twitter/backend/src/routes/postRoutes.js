/**
 * Rutas de Posts
 * /api/posts/*
 */

const express = require('express');
const router = express.Router();

const { postController } = require('../controllers');
const { 
  authMiddleware,
  optionalAuthMiddleware,
  createPostValidation,
  paginationValidation,
  mongoIdValidation,
  upload,
  handleMulterError
} = require('../middlewares');

/**
 * @route   GET /api/posts
 * @desc    Obtener timeline (posts recientes)
 * @access  Public
 * @query   { page?, limit? }
 */
router.get('/', paginationValidation, postController.getTimeline);

/**
 * @route   POST /api/posts
 * @desc    Crear nuevo post
 * @access  Private (requiere JWT)
 * @body    { text } o FormData con { text, image? }
 */
router.post(
  '/',
  authMiddleware,
  upload.single('image'),
  handleMulterError,
  createPostValidation,
  postController.createPost
);

/**
 * @route   GET /api/posts/:id
 * @desc    Obtener un post específico
 * @access  Public
 */
router.get('/:id', mongoIdValidation('id'), postController.getPostById);

/**
 * @route   DELETE /api/posts/:id
 * @desc    Eliminar un post (solo autor)
 * @access  Private (requiere JWT)
 */
router.delete(
  '/:id',
  authMiddleware,
  mongoIdValidation('id'),
  postController.deletePost
);

module.exports = router;
