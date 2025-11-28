/**
 * Exportación centralizada de servicios
 */

const authService = require('./authService');
const postService = require('./postService');

module.exports = {
  authService,
  postService
};
