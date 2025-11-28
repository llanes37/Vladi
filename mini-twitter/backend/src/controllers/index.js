/**
 * Exportación centralizada de controladores
 */

const authController = require('./authController');
const postController = require('./postController');

module.exports = {
  authController,
  postController
};
