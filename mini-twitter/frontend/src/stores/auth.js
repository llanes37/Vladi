/**
 * Store de Autenticación (Pinia)
 * Maneja el estado del usuario autenticado y tokens
 */

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/services/api'

export const useAuthStore = defineStore('auth', () => {
  // ================================
  // State
  // ================================
  
  const user = ref(null)
  const token = ref(localStorage.getItem('token') || null)
  const loading = ref(false)
  const error = ref(null)
  
  // ================================
  // Getters (Computed)
  // ================================
  
  const isAuthenticated = computed(() => !!user.value && !!token.value)
  
  const userDisplayName = computed(() => {
    return user.value?.displayName || user.value?.username || 'Usuario'
  })
  
  const userAvatar = computed(() => {
    return user.value?.avatarURL || null
  })
  
  // ================================
  // Actions
  // ================================
  
  /**
   * Registrar nuevo usuario
   */
  async function register(userData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.register(userData)
      
      // No hacer login automático, redirigir a login
      return response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al registrar usuario'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Iniciar sesión
   */
  async function login(credentials) {
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.login(credentials)
      
      // Guardar token y usuario
      token.value = response.data.data.token
      user.value = response.data.data.user
      
      // Persistir token en localStorage
      localStorage.setItem('token', token.value)
      
      return response.data
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al iniciar sesión'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Cerrar sesión
   */
  function logout() {
    user.value = null
    token.value = null
    localStorage.removeItem('token')
  }
  
  /**
   * Obtener usuario actual desde el servidor
   */
  async function fetchCurrentUser() {
    if (!token.value) return null
    
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.getCurrentUser()
      user.value = response.data.data.user
      return user.value
    } catch (err) {
      // Token inválido o expirado
      logout()
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Actualizar perfil del usuario
   */
  async function updateProfile(profileData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await authApi.updateProfile(profileData)
      user.value = response.data.data.user
      return user.value
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al actualizar perfil'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Inicializar el store (cargar usuario si hay token)
   */
  async function init() {
    if (token.value && !user.value) {
      try {
        await fetchCurrentUser()
      } catch {
        // Token inválido, ya se limpió en fetchCurrentUser
      }
    }
  }
  
  // Inicializar al crear el store
  init()
  
  return {
    // State
    user,
    token,
    loading,
    error,
    
    // Getters
    isAuthenticated,
    userDisplayName,
    userAvatar,
    
    // Actions
    register,
    login,
    logout,
    fetchCurrentUser,
    updateProfile,
    init
  }
})
