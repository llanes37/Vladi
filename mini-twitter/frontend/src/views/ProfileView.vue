<template>
  <v-container class="py-4" style="max-width: 600px;">
    <!-- Loading -->
    <div v-if="loading" class="text-center py-8">
      <v-progress-circular indeterminate color="primary" size="48" />
    </div>
    
    <!-- Contenido del perfil -->
    <div v-else-if="profileUser">
      <!-- Card de información del usuario -->
      <v-card class="mb-4">
        <v-card-text class="pa-6">
          <div class="d-flex align-start">
            <!-- Avatar -->
            <v-avatar size="80" color="primary" class="mr-4">
              <v-img 
                v-if="profileUser.avatarURL" 
                :src="profileUser.avatarURL" 
                alt="Avatar"
              />
              <span v-else class="text-h4 text-white">
                {{ profileUser.displayName?.charAt(0).toUpperCase() }}
              </span>
            </v-avatar>
            
            <!-- Info del usuario -->
            <div class="flex-grow-1">
              <h1 class="text-h5 font-weight-bold">
                {{ profileUser.displayName || profileUser.username }}
              </h1>
              <p class="text-body-2 text-medium-emphasis">
                @{{ profileUser.username }}
              </p>
              
              <p v-if="profileUser.bio" class="text-body-1 mt-3">
                {{ profileUser.bio }}
              </p>
              
              <div class="d-flex flex-wrap mt-3 text-body-2 text-medium-emphasis">
                <div class="mr-4">
                  <v-icon size="small" class="mr-1">mdi-email-outline</v-icon>
                  {{ profileUser.email }}
                </div>
                <div>
                  <v-icon size="small" class="mr-1">mdi-calendar</v-icon>
                  Se unió {{ formatDate(profileUser.createdAt) }}
                </div>
              </div>
              
              <div class="mt-3">
                <strong>{{ postsStore.userPostsTotal }}</strong>
                <span class="text-medium-emphasis"> posts</span>
              </div>
            </div>
          </div>
          
          <!-- Botón de editar perfil (solo si es el propio usuario) -->
          <v-btn
            v-if="isOwnProfile"
            variant="outlined"
            class="mt-4"
            @click="editDialog = true"
          >
            <v-icon start>mdi-pencil</v-icon>
            Editar perfil
          </v-btn>
        </v-card-text>
      </v-card>
      
      <!-- Posts del usuario -->
      <h2 class="text-h6 mb-3">
        {{ isOwnProfile ? 'Mis Posts' : 'Posts' }}
      </h2>
      
      <!-- Estado vacío -->
      <v-card v-if="postsStore.userPosts.length === 0 && !postsStore.loading" class="pa-6 text-center">
        <v-icon size="48" color="grey">mdi-message-text-outline</v-icon>
        <p class="text-body-2 text-medium-emphasis mt-3">
          {{ isOwnProfile ? 'Todavía no has publicado nada' : 'Este usuario no ha publicado nada' }}
        </p>
        <v-btn
          v-if="isOwnProfile"
          color="primary"
          variant="tonal"
          class="mt-4"
          :to="{ name: 'timeline' }"
        >
          Ir a Timeline
        </v-btn>
      </v-card>
      
      <!-- Lista de posts -->
      <PostCard
        v-for="post in postsStore.userPosts"
        :key="post.id"
        :post="post"
        @delete="handleDeletePost"
        class="mb-3"
      />
      
      <!-- Cargar más -->
      <div v-if="postsStore.userPostsHasMore" class="text-center mt-4">
        <v-btn
          variant="outlined"
          color="primary"
          :loading="postsStore.loading"
          @click="loadMore"
        >
          Cargar más posts
        </v-btn>
      </div>
    </div>
    
    <!-- Error: usuario no encontrado -->
    <v-card v-else class="pa-6 text-center">
      <v-icon size="64" color="error">mdi-account-alert</v-icon>
      <h3 class="text-h6 mt-4">Usuario no encontrado</h3>
      <v-btn color="primary" class="mt-4" :to="{ name: 'timeline' }">
        Volver al Timeline
      </v-btn>
    </v-card>
    
    <!-- Diálogo de editar perfil -->
    <v-dialog v-model="editDialog" max-width="500">
      <v-card>
        <v-card-title class="d-flex align-center">
          <span>Editar Perfil</span>
          <v-spacer />
          <v-btn icon variant="text" @click="editDialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        
        <v-card-text>
          <v-form @submit.prevent="handleUpdateProfile" ref="editForm">
            <v-text-field
              v-model="editData.displayName"
              label="Nombre para mostrar"
              :rules="[v => !v || v.length <= 50 || 'Máximo 50 caracteres']"
            />
            
            <v-textarea
              v-model="editData.bio"
              label="Biografía"
              rows="3"
              counter="160"
              :rules="[v => !v || v.length <= 160 || 'Máximo 160 caracteres']"
              class="mt-4"
            />
          </v-form>
        </v-card-text>
        
        <v-card-actions>
          <v-spacer />
          <v-btn variant="text" @click="editDialog = false">Cancelar</v-btn>
          <v-btn 
            color="primary" 
            @click="handleUpdateProfile"
            :loading="updating"
          >
            Guardar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, reactive, computed, watch, onMounted, inject } from 'vue'
import { useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { usePostsStore } from '@/stores/posts'
import { usersApi } from '@/services/api'
import PostCard from '@/components/PostCard.vue'
import { format } from 'date-fns'
import { es } from 'date-fns/locale'

const route = useRoute()
const authStore = useAuthStore()
const postsStore = usePostsStore()
const showSnackbar = inject('showSnackbar')

// State
const loading = ref(true)
const profileUser = ref(null)
const editDialog = ref(false)
const updating = ref(false)
const editForm = ref(null)

const editData = reactive({
  displayName: '',
  bio: ''
})

// Computed
const isOwnProfile = computed(() => {
  if (!route.params.id) return true // /profile sin ID = propio perfil
  return route.params.id === authStore.user?.id
})

const userId = computed(() => {
  return route.params.id || authStore.user?.id
})

// Cargar perfil
const loadProfile = async () => {
  loading.value = true
  postsStore.clearUserPosts()
  
  try {
    if (isOwnProfile.value) {
      profileUser.value = authStore.user
    } else {
      const response = await usersApi.getUser(userId.value)
      profileUser.value = response.data.data.user
    }
    
    // Cargar posts del usuario
    await postsStore.fetchUserPosts(userId.value, { refresh: true })
    
    // Actualizar datos de edición
    if (profileUser.value) {
      editData.displayName = profileUser.value.displayName || ''
      editData.bio = profileUser.value.bio || ''
    }
  } catch (error) {
    profileUser.value = null
    showSnackbar('Error al cargar perfil', 'error')
  } finally {
    loading.value = false
  }
}

// Formatear fecha
const formatDate = (date) => {
  return format(new Date(date), "d 'de' MMMM 'de' yyyy", { locale: es })
}

// Handlers
const handleUpdateProfile = async () => {
  const { valid } = await editForm.value.validate()
  if (!valid) return
  
  updating.value = true
  
  try {
    await authStore.updateProfile(editData)
    profileUser.value = authStore.user
    editDialog.value = false
    showSnackbar('Perfil actualizado', 'success')
  } catch (error) {
    showSnackbar('Error al actualizar perfil', 'error')
  } finally {
    updating.value = false
  }
}

const handleDeletePost = async (postId) => {
  try {
    await postsStore.deletePost(postId)
    showSnackbar('Post eliminado', 'info')
  } catch (error) {
    showSnackbar('Error al eliminar post', 'error')
  }
}

const loadMore = async () => {
  try {
    await postsStore.fetchUserPosts(userId.value, {
      page: postsStore.userPostsPage + 1,
      refresh: false
    })
  } catch (error) {
    showSnackbar('Error al cargar más posts', 'error')
  }
}

// Watch para cambios en la ruta (navegación entre perfiles)
watch(() => route.params.id, () => {
  loadProfile()
})

// Cargar al montar
onMounted(() => {
  loadProfile()
})
</script>
