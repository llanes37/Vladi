/**
 * Punto de entrada de la aplicación Vue
 * Configura Vue, Vuetify, Router y Pinia
 */

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

// Estilos globales
import './styles/main.scss'

// Crear la aplicación Vue
const app = createApp(App)

// Instalar plugins
app.use(createPinia())  // Estado global con Pinia
app.use(router)          // Enrutamiento
app.use(vuetify)         // Componentes UI de Vuetify

// Montar la aplicación
app.mount('#app')
