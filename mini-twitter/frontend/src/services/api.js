/**
 * Configuración de Axios y servicios de API
 * Incluye interceptores para JWT y manejo de errores
 */

import axios from 'axios'

// ================================
// Configuración de Axios
// ================================

// URL base del backend
const API_URL = import.meta.env.VITE_API_URL || '/api'

// Crear instancia de Axios
const api = axios.create({
  baseURL: API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// ================================
// Interceptor de Request
// ================================

api.interceptors.request.use(
  (config) => {
    // Obtener token del localStorage
    const token = localStorage.getItem('token')
    
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// ================================
// Interceptor de Response
// ================================

api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Manejar errores de autenticación
    if (error.response?.status === 401) {
      // Token inválido o expirado
      localStorage.removeItem('token')
      
      // Redirigir a login si no estamos ya ahí
      if (window.location.pathname !== '/login') {
        window.location.href = '/login'
      }
    }
    
    return Promise.reject(error)
  }
)

// ================================
// API de Autenticación
// ================================

export const authApi = {
  /**
   * Registrar nuevo usuario
   * @param {Object} data - { username, email, password, displayName? }
   */
  register(data) {
    return api.post('/auth/register', data)
  },
  
  /**
   * Iniciar sesión
   * @param {Object} credentials - { email, password }
   */
  login(credentials) {
    return api.post('/auth/login', credentials)
  },
  
  /**
   * Obtener usuario actual
   */
  getCurrentUser() {
    return api.get('/auth/me')
  },
  
  /**
   * Actualizar perfil
   * @param {Object|FormData} data - Datos del perfil o FormData con avatar
   */
  updateProfile(data) {
    // Si es FormData (subida de avatar), cambiar headers
    const config = data instanceof FormData
      ? { headers: { 'Content-Type': 'multipart/form-data' } }
      : {}
    
    return api.put('/auth/profile', data, config)
  }
}

// ================================
// API de Posts
// ================================

export const postsApi = {
  /**
   * Obtener timeline
   * @param {Object} params - { page?, limit? }
   */
  getTimeline(params = {}) {
    return api.get('/posts', { params })
  },
  
  /**
   * Crear nuevo post
   * @param {Object|FormData} data - { text } o FormData con { text, image? }
   */
  createPost(data) {
    const config = data instanceof FormData
      ? { headers: { 'Content-Type': 'multipart/form-data' } }
      : {}
    
    return api.post('/posts', data, config)
  },
  
  /**
   * Obtener un post por ID
   * @param {string} id - ID del post
   */
  getPost(id) {
    return api.get(`/posts/${id}`)
  },
  
  /**
   * Eliminar un post
   * @param {string} id - ID del post
   */
  deletePost(id) {
    return api.delete(`/posts/${id}`)
  },
  
  /**
   * Obtener posts de un usuario
   * @param {string} userId - ID del usuario
   * @param {Object} params - { page?, limit? }
   */
  getUserPosts(userId, params = {}) {
    return api.get(`/users/${userId}/posts`, { params })
  }
}

// ================================
// API de Usuarios
// ================================

export const usersApi = {
  /**
   * Obtener perfil de un usuario
   * @param {string} id - ID del usuario
   */
  getUser(id) {
    return api.get(`/users/${id}`)
  }
}

// Exportar instancia de axios para uso directo si es necesario
export default api
