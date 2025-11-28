<template>
  <!-- Layout principal de la aplicación -->
  <v-app>
    <!-- App Bar superior -->
    <v-app-bar 
      v-if="authStore.isAuthenticated" 
      elevation="0"
      border="b"
    >
      <v-app-bar-nav-icon 
        @click="drawer = !drawer"
        class="d-lg-none"
      />
      
      <v-app-bar-title>
        <router-link to="/timeline" class="d-flex align-center text-decoration-none">
          <v-icon color="primary" size="32" class="mr-2">mdi-twitter</v-icon>
          <span class="font-weight-bold text-h6">Mini Twitter</span>
        </router-link>
      </v-app-bar-title>
      
      <v-spacer />
      
      <!-- Toggle de tema -->
      <v-btn
        icon
        @click="toggleTheme"
        :title="isDark ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro'"
      >
        <v-icon>{{ isDark ? 'mdi-white-balance-sunny' : 'mdi-moon-waning-crescent' }}</v-icon>
      </v-btn>
      
      <!-- Menú de usuario -->
      <v-menu>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props" class="ml-2">
            <v-avatar size="32" color="primary">
              <v-img 
                v-if="authStore.userAvatar" 
                :src="authStore.userAvatar" 
                alt="Avatar"
              />
              <span v-else class="text-white text-body-2">
                {{ authStore.userDisplayName?.charAt(0).toUpperCase() }}
              </span>
            </v-avatar>
          </v-btn>
        </template>
        
        <v-list>
          <v-list-item :to="{ name: 'profile' }">
            <template v-slot:prepend>
              <v-icon>mdi-account</v-icon>
            </template>
            <v-list-item-title>Mi Perfil</v-list-item-title>
          </v-list-item>
          
          <v-divider />
          
          <v-list-item @click="handleLogout" class="text-error">
            <template v-slot:prepend>
              <v-icon color="error">mdi-logout</v-icon>
            </template>
            <v-list-item-title>Cerrar Sesión</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    
    <!-- Navigation Drawer para móvil -->
    <v-navigation-drawer
      v-if="authStore.isAuthenticated"
      v-model="drawer"
      temporary
      class="d-lg-none"
    >
      <v-list nav>
        <v-list-item
          :to="{ name: 'timeline' }"
          prepend-icon="mdi-home"
          title="Timeline"
        />
        <v-list-item
          :to="{ name: 'profile' }"
          prepend-icon="mdi-account"
          title="Mi Perfil"
        />
        <v-divider class="my-2" />
        <v-list-item
          @click="handleLogout"
          prepend-icon="mdi-logout"
          title="Cerrar Sesión"
          class="text-error"
        />
      </v-list>
    </v-navigation-drawer>
    
    <!-- Contenido principal -->
    <v-main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </v-main>
    
    <!-- Snackbar global para notificaciones -->
    <v-snackbar
      v-model="snackbar.show"
      :color="snackbar.color"
      :timeout="snackbar.timeout"
      location="bottom right"
    >
      {{ snackbar.message }}
      <template v-slot:actions>
        <v-btn variant="text" @click="snackbar.show = false">
          Cerrar
        </v-btn>
      </template>
    </v-snackbar>
  </v-app>
</template>

<script setup>
import { ref, reactive, provide, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useTheme } from 'vuetify'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const theme = useTheme()
const authStore = useAuthStore()

// State del drawer
const drawer = ref(false)

// Sistema de snackbar global
const snackbar = reactive({
  show: false,
  message: '',
  color: 'success',
  timeout: 3000
})

// Función para mostrar notificaciones (se provee a componentes hijos)
const showSnackbar = (message, color = 'success', timeout = 3000) => {
  snackbar.message = message
  snackbar.color = color
  snackbar.timeout = timeout
  snackbar.show = true
}

// Proveer snackbar a componentes hijos
provide('showSnackbar', showSnackbar)

// Tema claro/oscuro
const isDark = computed(() => theme.global.current.value.dark)

const toggleTheme = () => {
  theme.global.name.value = isDark.value ? 'light' : 'dark'
  localStorage.setItem('theme', theme.global.name.value)
}

// Cargar preferencia de tema guardada
const savedTheme = localStorage.getItem('theme')
if (savedTheme) {
  theme.global.name.value = savedTheme
}

// Cerrar sesión
const handleLogout = () => {
  authStore.logout()
  router.push({ name: 'login' })
  showSnackbar('Sesión cerrada correctamente', 'info')
}
</script>
