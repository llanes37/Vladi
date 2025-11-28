/**
 * Rutas de Usuarios
 * /api/users/*
 */

const express = require('express');
const router = express.Router();

const { authController, postController } = require('../controllers');
const { 
  mongoIdValidation,
  paginationValidation
} = require('../middlewares');

/**
 * @route   GET /api/users/:id
 * @desc    Obtener perfil público de un usuario
 * @access  Public
 */
router.get('/:id', mongoIdValidation('id'), authController.getUserById);

/**
 * @route   GET /api/users/:id/posts
 * @desc    Obtener posts de un usuario
 * @access  Public
 * @query   { page?, limit? }
 */
router.get(
  '/:id/posts',
  mongoIdValidation('id'),
  paginationValidation,
  postController.getPostsByUser
);

module.exports = router;
