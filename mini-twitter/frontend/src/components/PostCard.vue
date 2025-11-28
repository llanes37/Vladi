<template>
  <v-card class="post-card">
    <v-card-text class="pa-4">
      <div class="d-flex">
        <!-- Avatar del autor -->
        <router-link 
          :to="{ name: 'user-profile', params: { id: post.author.id || post.author._id } }"
          class="text-decoration-none"
        >
          <v-avatar size="48" color="primary" class="mr-3 cursor-pointer">
            <v-img 
              v-if="post.author.avatarURL" 
              :src="post.author.avatarURL" 
              alt="Avatar"
            />
            <span v-else class="text-white">
              {{ authorInitial }}
            </span>
          </v-avatar>
        </router-link>
        
        <!-- Contenido del post -->
        <div class="flex-grow-1 overflow-hidden">
          <!-- Header: nombre, username, fecha -->
          <div class="d-flex align-center flex-wrap">
            <router-link 
              :to="{ name: 'user-profile', params: { id: post.author.id || post.author._id } }"
              class="text-decoration-none"
            >
              <span class="font-weight-bold text-body-1">
                {{ post.author.displayName || post.author.username }}
              </span>
            </router-link>
            
            <span class="text-medium-emphasis text-body-2 ml-2">
              @{{ post.author.username }}
            </span>
            
            <span class="text-medium-emphasis mx-1">·</span>
            
            <v-tooltip :text="fullDate" location="bottom">
              <template v-slot:activator="{ props }">
                <span 
                  class="text-medium-emphasis text-body-2 cursor-pointer"
                  v-bind="props"
                >
                  {{ relativeTime }}
                </span>
              </template>
            </v-tooltip>
            
            <v-spacer />
            
            <!-- Menú de opciones (solo para el autor) -->
            <v-menu v-if="isAuthor">
              <template v-slot:activator="{ props }">
                <v-btn
                  icon
                  variant="text"
                  size="small"
                  v-bind="props"
                >
                  <v-icon>mdi-dots-horizontal</v-icon>
                </v-btn>
              </template>
              
              <v-list density="compact">
                <v-list-item @click="handleDelete" class="text-error">
                  <template v-slot:prepend>
                    <v-icon color="error" size="small">mdi-delete</v-icon>
                  </template>
                  <v-list-item-title>Eliminar</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </div>
          
          <!-- Texto del post -->
          <p class="text-body-1 mt-2 post-text" style="white-space: pre-wrap;">{{ post.text }}</p>
          
          <!-- Imagen del post -->
          <v-img
            v-if="post.imageURL"
            :src="post.imageURL"
            max-height="400"
            cover
            rounded="lg"
            class="mt-3 post-image cursor-pointer"
            @click="showImageDialog = true"
          />
          
          <!-- Acciones del post (preparado para likes, comentarios, etc.) -->
          <div class="d-flex mt-3">
            <v-btn
              variant="text"
              size="small"
              color="grey"
              class="action-btn"
              disabled
            >
              <v-icon size="small" class="mr-1">mdi-comment-outline</v-icon>
              <span class="text-body-2">{{ post.commentsCount || 0 }}</span>
            </v-btn>
            
            <v-btn
              variant="text"
              size="small"
              color="grey"
              class="action-btn ml-4"
              disabled
            >
              <v-icon size="small" class="mr-1">mdi-heart-outline</v-icon>
              <span class="text-body-2">{{ post.likesCount || 0 }}</span>
            </v-btn>
            
            <v-btn
              variant="text"
              size="small"
              color="grey"
              class="action-btn ml-4"
              disabled
            >
              <v-icon size="small" class="mr-1">mdi-share-variant-outline</v-icon>
            </v-btn>
          </div>
        </div>
      </div>
    </v-card-text>
    
    <!-- Diálogo para ver imagen ampliada -->
    <v-dialog v-model="showImageDialog" max-width="900">
      <v-card>
        <v-img
          :src="post.imageURL"
          max-height="80vh"
          contain
        />
        <v-btn
          icon
          class="close-image-btn"
          @click="showImageDialog = false"
        >
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-card>
    </v-dialog>
    
    <!-- Diálogo de confirmación de eliminación -->
    <v-dialog v-model="showDeleteDialog" max-width="400">
      <v-card>
        <v-card-title>¿Eliminar post?</v-card-title>
        <v-card-text>
          Esta acción no se puede deshacer. El post será eliminado permanentemente.
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn variant="text" @click="showDeleteDialog = false">Cancelar</v-btn>
          <v-btn color="error" @click="confirmDelete">Eliminar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { formatDistanceToNow, format } from 'date-fns'
import { es } from 'date-fns/locale'

const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['delete'])

const authStore = useAuthStore()

// State
const showImageDialog = ref(false)
const showDeleteDialog = ref(false)

// Computed
const authorInitial = computed(() => {
  const name = props.post.author.displayName || props.post.author.username
  return name?.charAt(0).toUpperCase() || '?'
})

const isAuthor = computed(() => {
  const authorId = props.post.author.id || props.post.author._id
  return authorId === authStore.user?.id
})

const relativeTime = computed(() => {
  return formatDistanceToNow(new Date(props.post.createdAt), {
    addSuffix: true,
    locale: es
  })
})

const fullDate = computed(() => {
  return format(new Date(props.post.createdAt), "d 'de' MMMM 'de' yyyy 'a las' HH:mm", {
    locale: es
  })
})

// Handlers
const handleDelete = () => {
  showDeleteDialog.value = true
}

const confirmDelete = () => {
  emit('delete', props.post.id)
  showDeleteDialog.value = false
}
</script>

<style scoped>
.post-text {
  word-break: break-word;
}

.post-image {
  transition: opacity 0.2s;
}

.post-image:hover {
  opacity: 0.9;
}

.action-btn:hover {
  color: var(--v-primary-base) !important;
}

.close-image-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(0, 0, 0, 0.5) !important;
  color: white !important;
}
</style>
