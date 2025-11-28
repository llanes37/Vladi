/**
 * Store de Posts (Pinia)
 * Maneja el estado de las publicaciones y timeline
 */

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { postsApi } from '@/services/api'

export const usePostsStore = defineStore('posts', () => {
  // ================================
  // State
  // ================================
  
  const posts = ref([])
  const currentPage = ref(1)
  const totalPages = ref(1)
  const total = ref(0)
  const hasMore = ref(false)
  const loading = ref(false)
  const error = ref(null)
  
  // Posts de un usuario específico (para perfil)
  const userPosts = ref([])
  const userPostsPage = ref(1)
  const userPostsTotal = ref(0)
  const userPostsHasMore = ref(false)
  
  // ================================
  // Getters (Computed)
  // ================================
  
  const isEmpty = computed(() => posts.value.length === 0)
  const postCount = computed(() => posts.value.length)
  
  // ================================
  // Actions
  // ================================
  
  /**
   * Obtener timeline (posts de todos los usuarios)
   */
  async function fetchTimeline({ page = 1, limit = 20, refresh = false } = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await postsApi.getTimeline({ page, limit })
      const data = response.data.data
      
      if (refresh || page === 1) {
        // Reemplazar posts
        posts.value = data.posts
      } else {
        // Añadir más posts (infinite scroll)
        posts.value = [...posts.value, ...data.posts]
      }
      
      currentPage.value = data.currentPage
      totalPages.value = data.pages
      total.value = data.total
      hasMore.value = data.hasMore
      
      return data
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al cargar posts'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Cargar más posts (paginación)
   */
  async function loadMore() {
    if (!hasMore.value || loading.value) return
    
    return fetchTimeline({ 
      page: currentPage.value + 1,
      refresh: false 
    })
  }
  
  /**
   * Crear un nuevo post
   */
  async function createPost(postData) {
    loading.value = true
    error.value = null
    
    try {
      const response = await postsApi.createPost(postData)
      const newPost = response.data.data.post
      
      // Añadir al principio de la lista
      posts.value.unshift(newPost)
      total.value++
      
      return newPost
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al publicar'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Eliminar un post
   */
  async function deletePost(postId) {
    loading.value = true
    error.value = null
    
    try {
      await postsApi.deletePost(postId)
      
      // Eliminar de la lista local
      posts.value = posts.value.filter(p => p.id !== postId)
      userPosts.value = userPosts.value.filter(p => p.id !== postId)
      total.value--
      
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al eliminar post'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Obtener posts de un usuario específico
   */
  async function fetchUserPosts(userId, { page = 1, limit = 20, refresh = false } = {}) {
    loading.value = true
    error.value = null
    
    try {
      const response = await postsApi.getUserPosts(userId, { page, limit })
      const data = response.data.data
      
      if (refresh || page === 1) {
        userPosts.value = data.posts
      } else {
        userPosts.value = [...userPosts.value, ...data.posts]
      }
      
      userPostsPage.value = data.currentPage
      userPostsTotal.value = data.total
      userPostsHasMore.value = data.hasMore
      
      return data
    } catch (err) {
      error.value = err.response?.data?.message || 'Error al cargar posts del usuario'
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Refrescar el timeline
   */
  async function refresh() {
    return fetchTimeline({ page: 1, refresh: true })
  }
  
  /**
   * Limpiar el state
   */
  function clearPosts() {
    posts.value = []
    currentPage.value = 1
    totalPages.value = 1
    total.value = 0
    hasMore.value = false
    error.value = null
  }
  
  function clearUserPosts() {
    userPosts.value = []
    userPostsPage.value = 1
    userPostsTotal.value = 0
    userPostsHasMore.value = false
  }
  
  return {
    // State
    posts,
    currentPage,
    totalPages,
    total,
    hasMore,
    loading,
    error,
    userPosts,
    userPostsPage,
    userPostsTotal,
    userPostsHasMore,
    
    // Getters
    isEmpty,
    postCount,
    
    // Actions
    fetchTimeline,
    loadMore,
    createPost,
    deletePost,
    fetchUserPosts,
    refresh,
    clearPosts,
    clearUserPosts
  }
})
