/**
 * Tests de Posts
 * Prueba los endpoints de publicaciones
 */

const request = require('supertest');
const mongoose = require('mongoose');
const app = require('../app');
const { User, Post } = require('../models');

// Datos de prueba
const testUser = {
  username: 'postuser',
  email: 'post@example.com',
  password: 'password123',
  displayName: 'Post User'
};

let token;
let userId;

// Antes de todos los tests: conectar a BD de prueba
beforeAll(async () => {
  const mongoUri = process.env.MONGODB_URI || 'mongodb://localhost:27017/mini-twitter-test';
  await mongoose.connect(mongoUri);
});

// Antes de cada test: limpiar BD y crear usuario
beforeEach(async () => {
  await User.deleteMany({});
  await Post.deleteMany({});
  
  // Registrar usuario y obtener token
  const res = await request(app).post('/api/auth/register').send(testUser);
  token = res.body.data.token;
  userId = res.body.data.user.id;
});

// Después de todos los tests: limpiar y desconectar
afterAll(async () => {
  await User.deleteMany({});
  await Post.deleteMany({});
  await mongoose.connection.close();
});

describe('Posts Endpoints', () => {
  
  // ================================
  // Tests de Crear Post
  // ================================
  
  describe('POST /api/posts', () => {
    
    it('debería crear un post correctamente', async () => {
      const res = await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({ text: 'Mi primer tweet! 🎉' });
      
      expect(res.statusCode).toBe(201);
      expect(res.body.success).toBe(true);
      expect(res.body.data.post.text).toBe('Mi primer tweet! 🎉');
      expect(res.body.data.post).toHaveProperty('author');
      expect(res.body.data.post).toHaveProperty('createdAt');
    });
    
    it('debería fallar sin autenticación', async () => {
      const res = await request(app)
        .post('/api/posts')
        .send({ text: 'Tweet sin auth' });
      
      expect(res.statusCode).toBe(401);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar sin texto', async () => {
      const res = await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({});
      
      expect(res.statusCode).toBe(400);
      expect(res.body.success).toBe(false);
    });
    
    it('debería fallar si el texto excede 280 caracteres', async () => {
      const longText = 'a'.repeat(281);
      
      const res = await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({ text: longText });
      
      expect(res.statusCode).toBe(400);
      expect(res.body.success).toBe(false);
    });
  });
  
  // ================================
  // Tests de Obtener Timeline
  // ================================
  
  describe('GET /api/posts', () => {
    
    beforeEach(async () => {
      // Crear algunos posts
      for (let i = 1; i <= 5; i++) {
        await request(app)
          .post('/api/posts')
          .set('Authorization', `Bearer ${token}`)
          .send({ text: `Post número ${i}` });
      }
    });
    
    it('debería obtener el timeline', async () => {
      const res = await request(app).get('/api/posts');
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data).toHaveProperty('posts');
      expect(res.body.data.posts).toHaveLength(5);
      expect(res.body.data).toHaveProperty('total');
    });
    
    it('debería paginar correctamente', async () => {
      const res = await request(app).get('/api/posts?page=1&limit=2');
      
      expect(res.statusCode).toBe(200);
      expect(res.body.data.posts).toHaveLength(2);
      expect(res.body.data.currentPage).toBe(1);
    });
    
    it('debería ordenar por fecha descendente (más recientes primero)', async () => {
      const res = await request(app).get('/api/posts');
      
      const posts = res.body.data.posts;
      // El post más reciente debería ser "Post número 5"
      expect(posts[0].text).toBe('Post número 5');
      expect(posts[4].text).toBe('Post número 1');
    });
  });
  
  // ================================
  // Tests de Posts por Usuario
  // ================================
  
  describe('GET /api/users/:id/posts', () => {
    
    beforeEach(async () => {
      // Crear posts del usuario
      await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({ text: 'Post del usuario 1' });
      
      await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({ text: 'Post del usuario 2' });
    });
    
    it('debería obtener posts de un usuario específico', async () => {
      const res = await request(app).get(`/api/users/${userId}/posts`);
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
      expect(res.body.data.posts).toHaveLength(2);
    });
    
    it('debería devolver error 404 si el usuario no existe', async () => {
      const fakeId = new mongoose.Types.ObjectId();
      const res = await request(app).get(`/api/users/${fakeId}/posts`);
      
      expect(res.statusCode).toBe(404);
    });
    
    it('debería devolver error 400 con ID inválido', async () => {
      const res = await request(app).get('/api/users/id-invalido/posts');
      
      expect(res.statusCode).toBe(400);
    });
  });
  
  // ================================
  // Tests de Eliminar Post
  // ================================
  
  describe('DELETE /api/posts/:id', () => {
    
    let postId;
    
    beforeEach(async () => {
      const res = await request(app)
        .post('/api/posts')
        .set('Authorization', `Bearer ${token}`)
        .send({ text: 'Post a eliminar' });
      
      postId = res.body.data.post.id;
    });
    
    it('debería eliminar un post propio', async () => {
      const res = await request(app)
        .delete(`/api/posts/${postId}`)
        .set('Authorization', `Bearer ${token}`);
      
      expect(res.statusCode).toBe(200);
      expect(res.body.success).toBe(true);
      
      // Verificar que ya no existe
      const checkRes = await request(app).get(`/api/posts/${postId}`);
      expect(checkRes.statusCode).toBe(404);
    });
    
    it('debería fallar al eliminar post de otro usuario', async () => {
      // Crear otro usuario
      const otherUser = {
        username: 'otheruser',
        email: 'other@example.com',
        password: 'password123'
      };
      const registerRes = await request(app).post('/api/auth/register').send(otherUser);
      const otherToken = registerRes.body.data.token;
      
      // Intentar eliminar el post con el otro usuario
      const res = await request(app)
        .delete(`/api/posts/${postId}`)
        .set('Authorization', `Bearer ${otherToken}`);
      
      expect(res.statusCode).toBe(403);
    });
  });
});
