/**
 * Tests de Autenticación
 * Prueba los endpoints de registro y login
 */

const request = require('supertest');
const mongoose = require('mongoose');
const app = require('../app');
const { User } = require('../models');

// Datos de prueba
const testUser = {
  username: 'testuser',
  email: 'test@example.com',
  password: 'password123',
  displayName: 'Test User'
};

// Antes de todos los tests: conectar a una BD de prueba
beforeAll(async () => {
  // Usar una BD de test diferente
  const mongoUri = process.env.MONGODB_URI || 'mongodb://localhost:27017/mini-twitter-test';
  await mongoose.connect(mongoUri);
});

// Antes de cada test: limpiar la BD
beforeEach(async () => {
  await User.deleteMany({});
});

// Después de todos los tests: desconectar
afterAll(async () => {
  await User.deleteMany({});
  await mongoose.connection.close();
});

describe('Auth Endpoints', () => {
  
  // ================================
  // Tests de Registro
  // ================================
  
  describe('POST /api/auth/register', () => {
    
    it('debería registrar un usuario nuevo correctamente', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send(testUser);
      
      expect(res.statusCode).toBe(201);
      expect(res.body.success).toBe(true);
      expect(res.body.data).toHaveProperty('user');
      expect(res.body.data).toHaveProperty('token');
      expect(res.body.data.user.username).toBe(testUser.username);
      expect(res.body.data.user.email).toBe(testUser.email);
      expect(res.body.data.user).not.toHaveProperty('password');
    });
    
    it('debería fallar si el email ya existe', async () => {
      // Crear usuario primero
      await request(app).post('/api/auth/register').send(testUser);
      
      // Intentar registrar con el mismo email
      const res = await request(app)
        .post('/api/auth/register')
        .send({
          ...testUser,
          username: 'otrouser'
        });
      
      expect(res.statusCode).toBe(409);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar si el username ya existe', async () => {
      // Crear usuario primero
      await request(app).post('/api/auth/register').send(testUser);
      
      // Intentar registrar con el mismo username
      const res = await request(app)
        .post('/api/auth/register')
        .send({
          ...testUser,
          email: 'otro@example.com'
        });
      
      expect(res.statusCode).toBe(409);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar si falta el username', async () => {
      const { username, ...userData } = testUser;
      
      const res = await request(app)
        .post('/api/auth/register')
        .send(userData);
      
      expect(res.statusCode).toBe(400);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar si el email no es válido', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send({
          ...testUser,
          email: 'email-invalido'
        });
      
      expect(res.statusCode).toBe(400);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar si la contraseña es muy corta', async () => {
      const res = await request(app)
        .post('/api/auth/register')
        .send({
          ...testUser,
          password: '123'
        });
      
      expect(res.statusCode).toBe(400);
      expect(res.body.success).toBe(false);
    });
  });
  
  // ================================
  // Tests de Login
  // ================================
  
  describe('POST /api/auth/login', () => {
    
    beforeEach(async () => {
      // Registrar usuario antes de cada test de login
      await request(app).post('/api/auth/register').send(testUser);
    });
    
    it('debería hacer login correctamente con email', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: testUser.email,
          password: testUser.password
        });
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data).toHaveProperty('user');
      expect(res.body.data).toHaveProperty('token');
    });
    
    it('debería hacer login correctamente con username', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: testUser.username, // También acepta username
          password: testUser.password
        });
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
    });
    
    it('debería fallar con contraseña incorrecta', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: testUser.email,
          password: 'contraseña-incorrecta'
        });
      
      expect(res.statusCode).toBe(401);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar con email que no existe', async () => {
      const res = await request(app)
        .post('/api/auth/login')
        .send({
          email: 'noexiste@example.com',
          password: testUser.password
        });
      
      expect(res.statusCode).toBe(401);
      expect(res.body.success).toBe(false);
    });
  });
  
  // ================================
  // Tests de Usuario Actual
  // ================================
  
  describe('GET /api/auth/me', () => {
    
    let token;
    
    beforeEach(async () => {
      // Registrar y obtener token
      const res = await request(app).post('/api/auth/register').send(testUser);
      token = res.body.data.token;
    });
    
    it('debería devolver el usuario autenticado', async () => {
      const res = await request(app)
        .get('/api/auth/me')
        .set('Authorization', `Bearer ${token}`);
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data.user.username).toBe(testUser.username);
    });
    
    it('debería fallar sin token', async () => {
      const res = await request(app).get('/api/auth/me');
      
      expect(res.statusCode).toBe(401);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar con token inválido', async () => {
      const res = await request(app)
        .get('/api/auth/me')
        .set('Authorization', 'Bearer token-invalido');
      
      expect(res.statusCode).toBe(401);
      expect(res.body.success).toBe(false);
    });
  });
});
