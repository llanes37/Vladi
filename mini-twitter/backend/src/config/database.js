/**
 * Configuración de la base de datos MongoDB
 * Usa Mongoose para la conexión y modelos
 */

const mongoose = require('mongoose');

/**
 * Conecta a MongoDB usando la URI de las variables de entorno
 * @returns {Promise} Promesa de conexión
 */
const connectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGODB_URI, {
      // Opciones recomendadas para Mongoose 8+
      // Las opciones useNewUrlParser y useUnifiedTopology ya no son necesarias
    });

    console.log(`✅ MongoDB conectado: ${conn.connection.host}`);
    return conn;
  } catch (error) {
    console.error(`❌ Error conectando a MongoDB: ${error.message}`);
    process.exit(1);
  }
};

/**
 * Desconecta de MongoDB (útil para tests)
 */
const disconnectDB = async () => {
  try {
    await mongoose.connection.close();
    console.log('📴 MongoDB desconectado');
  } catch (error) {
    console.error(`❌ Error desconectando de MongoDB: ${error.message}`);
  }
};

module.exports = { connectDB, disconnectDB };
