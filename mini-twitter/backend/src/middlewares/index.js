/**
 * Exportación centralizada de middlewares
 */

const { authMiddleware, optionalAuthMiddleware } = require('./auth');
const { ApiError, notFoundHandler, errorHandler } = require('./errorHandler');
const { upload, handleMulterError, getImageUrl, deleteUploadedFile } = require('./upload');
const validators = require('./validators');

module.exports = {
  // Auth
  authMiddleware,
  optionalAuthMiddleware,
  
  // Errors
  ApiError,
  notFoundHandler,
  errorHandler,
  
  // Upload
  upload,
  handleMulterError,
  getImageUrl,
  deleteUploadedFile,
  
  // Validators
  ...validators
};
