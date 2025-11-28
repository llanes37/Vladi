/**
 * Configuración de Multer para subida de archivos
 * Permite subir imágenes a una carpeta local
 */

const multer = require('multer');
const path = require('path');
const fs = require('fs');
const { ApiError } = require('./errorHandler');

// Crear carpeta de uploads si no existe
const uploadDir = path.join(__dirname, '../../uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir, { recursive: true });
}

// Configuración del almacenamiento
const storage = multer.diskStorage({
  // Carpeta de destino
  destination: (req, file, cb) => {
    cb(null, uploadDir);
  },
  
  // Nombre del archivo: timestamp-random-original
  filename: (req, file, cb) => {
    const uniqueSuffix = `${Date.now()}-${Math.round(Math.random() * 1E9)}`;
    const ext = path.extname(file.originalname);
    const name = path.basename(file.originalname, ext)
      .toLowerCase()
      .replace(/[^a-z0-9]/g, '-')
      .substring(0, 20);
    cb(null, `${uniqueSuffix}-${name}${ext}`);
  }
});

// Tipos de archivos permitidos
const ALLOWED_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp'];
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB

// Filtro de archivos
const fileFilter = (req, file, cb) => {
  if (ALLOWED_TYPES.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new ApiError(400, `Tipo de archivo no permitido. Solo se aceptan: ${ALLOWED_TYPES.join(', ')}`), false);
  }
};

// Instancia de Multer configurada
const upload = multer({
  storage,
  fileFilter,
  limits: {
    fileSize: MAX_FILE_SIZE,
    files: 1 // Máximo un archivo por request
  }
});

/**
 * Middleware para manejar errores de Multer
 */
const handleMulterError = (err, req, res, next) => {
  if (err instanceof multer.MulterError) {
    if (err.code === 'LIMIT_FILE_SIZE') {
      return res.status(400).json({
        success: false,
        message: `El archivo es demasiado grande. Máximo: ${MAX_FILE_SIZE / (1024 * 1024)}MB`
      });
    }
    if (err.code === 'LIMIT_FILE_COUNT') {
      return res.status(400).json({
        success: false,
        message: 'Solo se permite subir un archivo'
      });
    }
    return res.status(400).json({
      success: false,
      message: `Error al subir archivo: ${err.message}`
    });
  }
  next(err);
};

/**
 * Helper para obtener la URL de una imagen subida
 * @param {string} filename - Nombre del archivo
 * @returns {string} URL relativa de la imagen
 */
const getImageUrl = (filename) => {
  if (!filename) return null;
  return `/uploads/${filename}`;
};

/**
 * Helper para eliminar un archivo subido
 * @param {string} filename - Nombre del archivo
 */
const deleteUploadedFile = (filename) => {
  if (!filename) return;
  
  const filePath = path.join(uploadDir, filename);
  fs.unlink(filePath, (err) => {
    if (err && err.code !== 'ENOENT') {
      console.error('Error eliminando archivo:', err);
    }
  });
};

module.exports = {
  upload,
  handleMulterError,
  getImageUrl,
  deleteUploadedFile,
  uploadDir
};
