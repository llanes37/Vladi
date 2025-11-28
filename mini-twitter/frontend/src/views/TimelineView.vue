<template>
  <v-container class="py-4" style="max-width: 600px;">
    <!-- Formulario para crear nuevo post -->
    <NewPostForm @post-created="handlePostCreated" />
    
    <!-- Loading inicial -->
    <div v-if="postsStore.loading && postsStore.isEmpty" class="text-center py-8">
      <v-progress-circular indeterminate color="primary" size="48" />
      <p class="text-body-2 text-medium-emphasis mt-4">Cargando posts...</p>
    </div>
    
    <!-- Lista de posts -->
    <div v-else>
      <!-- Estado vacío -->
      <v-card v-if="postsStore.isEmpty && !postsStore.loading" class="pa-8 text-center">
        <v-icon size="64" color="grey">mdi-message-text-outline</v-icon>
        <h3 class="text-h6 mt-4">No hay posts todavía</h3>
        <p class="text-body-2 text-medium-emphasis mt-2">
          ¡Sé el primero en publicar algo!
        </p>
      </v-card>
      
      <!-- Lista de posts -->
      <TransitionGroup name="slide-y" tag="div">
        <PostCard
          v-for="post in postsStore.posts"
          :key="post.id"
          :post="post"
          @delete="handleDeletePost"
          class="mb-3"
        />
      </TransitionGroup>
      
      <!-- Botón de cargar más -->
      <div v-if="postsStore.hasMore" class="text-center mt-4">
        <v-btn
          variant="outlined"
          color="primary"
          :loading="postsStore.loading"
          @click="loadMore"
        >
          Cargar más posts
        </v-btn>
      </div>
      
      <!-- Indicador de fin -->
      <p 
        v-if="!postsStore.isEmpty && !postsStore.hasMore && !postsStore.loading" 
        class="text-center text-body-2 text-medium-emphasis mt-4"
      >
        Has llegado al final 🎉
      </p>
    </div>
    
    <!-- Botón flotante para scroll to top -->
    <v-btn
      v-show="showScrollTop"
      icon
      color="primary"
      size="large"
      class="scroll-to-top"
      @click="scrollToTop"
      elevation="4"
    >
      <v-icon>mdi-chevron-up</v-icon>
    </v-btn>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onUnmounted, inject } from 'vue'
import { usePostsStore } from '@/stores/posts'
import NewPostForm from '@/components/NewPostForm.vue'
import PostCard from '@/components/PostCard.vue'

const postsStore = usePostsStore()
const showSnackbar = inject('showSnackbar')

// Scroll to top button
const showScrollTop = ref(false)

const handleScroll = () => {
  showScrollTop.value = window.scrollY > 400
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

// Cargar posts al montar
onMounted(async () => {
  window.addEventListener('scroll', handleScroll)
  
  try {
    await postsStore.fetchTimeline({ refresh: true })
  } catch (error) {
    showSnackbar('Error al cargar posts', 'error')
  }
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

// Handlers
const loadMore = async () => {
  try {
    await postsStore.loadMore()
  } catch (error) {
    showSnackbar('Error al cargar más posts', 'error')
  }
}

const handlePostCreated = () => {
  showSnackbar('¡Post publicado! 🎉', 'success')
  scrollToTop()
}

const handleDeletePost = async (postId) => {
  try {
    await postsStore.deletePost(postId)
    showSnackbar('Post eliminado', 'info')
  } catch (error) {
    showSnackbar('Error al eliminar post', 'error')
  }
}
</script>

<style scoped>
.scroll-to-top {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 100;
}
</style>
