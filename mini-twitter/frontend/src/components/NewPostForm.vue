<template>
  <v-card class="mb-4">
    <v-card-text class="pa-4">
      <div class="d-flex">
        <!-- Avatar del usuario -->
        <v-avatar size="48" color="primary" class="mr-3">
          <v-img 
            v-if="authStore.userAvatar" 
            :src="authStore.userAvatar" 
            alt="Avatar"
          />
          <span v-else class="text-white">
            {{ authStore.userDisplayName?.charAt(0).toUpperCase() }}
          </span>
        </v-avatar>
        
        <!-- Área de texto -->
        <div class="flex-grow-1">
          <v-textarea
            v-model="text"
            :placeholder="placeholder"
            rows="3"
            auto-grow
            variant="plain"
            density="compact"
            hide-details
            :maxlength="280"
            @keydown.ctrl.enter="handleSubmit"
          />
          
          <!-- Preview de imagen -->
          <div v-if="imagePreview" class="mt-3 position-relative">
            <v-img
              :src="imagePreview"
              max-height="300"
              cover
              rounded="lg"
              class="image-preview"
            />
            <v-btn
              icon
              size="small"
              color="error"
              class="remove-image-btn"
              @click="removeImage"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </div>
          
          <v-divider class="my-3" />
          
          <!-- Barra de acciones -->
          <div class="d-flex align-center justify-space-between">
            <div class="d-flex">
              <!-- Botón de imagen -->
              <v-tooltip text="Subir imagen" location="bottom">
                <template v-slot:activator="{ props }">
                  <v-btn
                    icon
                    variant="text"
                    color="primary"
                    size="small"
                    v-bind="props"
                    @click="triggerFileInput"
                  >
                    <v-icon>mdi-image</v-icon>
                  </v-btn>
                </template>
              </v-tooltip>
              
              <!-- Botón de emojis -->
              <v-menu
                v-model="showEmojiPicker"
                :close-on-content-click="false"
                location="bottom start"
              >
                <template v-slot:activator="{ props }">
                  <v-btn
                    icon
                    variant="text"
                    color="primary"
                    size="small"
                    v-bind="props"
                  >
                    <v-icon>mdi-emoticon-happy-outline</v-icon>
                  </v-btn>
                </template>
                
                <!-- Panel de emojis -->
                <v-card class="emoji-panel">
                  <v-card-text class="pa-2">
                    <div class="emoji-grid">
                      <span
                        v-for="emoji in emojis"
                        :key="emoji"
                        class="emoji-item"
                        @click="insertEmoji(emoji)"
                      >
                        {{ emoji }}
                      </span>
                    </div>
                  </v-card-text>
                </v-card>
              </v-menu>
              
              <!-- Input de archivo oculto -->
              <input
                ref="fileInput"
                type="file"
                accept="image/*"
                hidden
                @change="handleFileChange"
              />
            </div>
            
            <!-- Contador y botón de publicar -->
            <div class="d-flex align-center">
              <span 
                class="text-body-2 mr-3"
                :class="{ 
                  'text-error': text.length > 280,
                  'text-warning': text.length > 250 && text.length <= 280 
                }"
              >
                {{ text.length }}/280
              </span>
              
              <v-btn
                color="primary"
                :disabled="!canSubmit"
                :loading="loading"
                @click="handleSubmit"
              >
                Publicar
              </v-btn>
            </div>
          </div>
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { usePostsStore } from '@/stores/posts'

const emit = defineEmits(['post-created'])

const authStore = useAuthStore()
const postsStore = usePostsStore()

// State
const text = ref('')
const imageFile = ref(null)
const imagePreview = ref(null)
const loading = ref(false)
const showEmojiPicker = ref(false)
const fileInput = ref(null)

// Lista de emojis populares
const emojis = [
  '😀', '😃', '😄', '😁', '😅', '😂', '🤣', '😊', '😇', '🙂',
  '😉', '😌', '😍', '🥰', '😘', '😗', '😋', '😛', '😜', '🤪',
  '😎', '🤩', '🥳', '😏', '😒', '😞', '😔', '😟', '😕', '🙁',
  '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶',
  '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥',
  '👍', '👎', '👊', '✊', '🤛', '🤜', '👏', '🙌', '👐', '🤲',
  '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '💕', '💞', '💓',
  '🔥', '⭐', '🌟', '✨', '💫', '🎉', '🎊', '🎈', '🎁', '🏆'
]

// Computed
const canSubmit = computed(() => {
  return text.value.trim().length > 0 && 
         text.value.length <= 280 && 
         !loading.value
})

const placeholder = computed(() => {
  const hour = new Date().getHours()
  if (hour < 12) return '¿Buenos días! ¿Qué está pasando?'
  if (hour < 18) return '¿Qué está pasando?'
  return '¿Buenas noches! ¿Qué estás pensando?'
})

// Handlers
const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (!file) return
  
  // Validar tipo
  if (!file.type.startsWith('image/')) {
    alert('Por favor selecciona una imagen válida')
    return
  }
  
  // Validar tamaño (5MB)
  if (file.size > 5 * 1024 * 1024) {
    alert('La imagen no puede superar los 5MB')
    return
  }
  
  imageFile.value = file
  
  // Crear preview
  const reader = new FileReader()
  reader.onload = (e) => {
    imagePreview.value = e.target.result
  }
  reader.readAsDataURL(file)
}

const removeImage = () => {
  imageFile.value = null
  imagePreview.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

const insertEmoji = (emoji) => {
  text.value += emoji
  showEmojiPicker.value = false
}

const handleSubmit = async () => {
  if (!canSubmit.value) return
  
  loading.value = true
  
  try {
    // Crear FormData si hay imagen
    let postData
    if (imageFile.value) {
      postData = new FormData()
      postData.append('text', text.value.trim())
      postData.append('image', imageFile.value)
    } else {
      postData = { text: text.value.trim() }
    }
    
    await postsStore.createPost(postData)
    
    // Limpiar formulario
    text.value = ''
    removeImage()
    
    emit('post-created')
  } catch (error) {
    console.error('Error al publicar:', error)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.image-preview {
  position: relative;
}

.remove-image-btn {
  position: absolute;
  top: 8px;
  right: 8px;
}

.emoji-panel {
  max-width: 350px;
}

.emoji-grid {
  display: grid;
  grid-template-columns: repeat(10, 1fr);
  gap: 4px;
}

.emoji-item {
  font-size: 20px;
  padding: 4px;
  cursor: pointer;
  border-radius: 4px;
  text-align: center;
  transition: background-color 0.2s;
}

.emoji-item:hover {
  background-color: rgba(0, 0, 0, 0.1);
}

.v-theme--dark .emoji-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}
</style>
