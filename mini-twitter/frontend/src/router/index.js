/**
 * Configuración del Router de Vue
 * Define las rutas de la aplicación y guards de navegación
 */

import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Lazy loading de vistas para mejor rendimiento
const LoginView = () => import('@/views/LoginView.vue')
const TimelineView = () => import('@/views/TimelineView.vue')
const ProfileView = () => import('@/views/ProfileView.vue')

const routes = [
  {
    path: '/',
    redirect: '/timeline'
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: {
      requiresGuest: true, // Solo para usuarios no autenticados
      title: 'Iniciar Sesión'
    }
  },
  {
    path: '/timeline',
    name: 'timeline',
    component: TimelineView,
    meta: {
      requiresAuth: true, // Solo para usuarios autenticados
      title: 'Timeline'
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: {
      requiresAuth: true,
      title: 'Mi Perfil'
    }
  },
  {
    path: '/user/:id',
    name: 'user-profile',
    component: ProfileView,
    meta: {
      requiresAuth: true,
      title: 'Perfil de Usuario'
    }
  },
  {
    // Ruta catch-all para 404
    path: '/:pathMatch(.*)*',
    redirect: '/timeline'
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0 }
  }
})

// ================================
// Navigation Guards
// ================================

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // Intentar cargar usuario si hay token
  if (!authStore.isAuthenticated && authStore.token) {
    try {
      await authStore.fetchCurrentUser()
    } catch (error) {
      // Token inválido, limpiar
      authStore.logout()
    }
  }
  
  // Actualizar título de la página
  document.title = to.meta.title 
    ? `${to.meta.title} | Mini Twitter` 
    : 'Mini Twitter'
  
  // Verificar si la ruta requiere autenticación
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    return next({ 
      name: 'login',
      query: { redirect: to.fullPath }
    })
  }
  
  // Verificar si la ruta es solo para invitados
  if (to.meta.requiresGuest && authStore.isAuthenticated) {
    return next({ name: 'timeline' })
  }
  
  next()
})

export default router
