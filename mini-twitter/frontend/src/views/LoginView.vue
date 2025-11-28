<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <!-- Logo y título -->
        <div class="text-center mb-8">
          <v-icon color="primary" size="64">mdi-twitter</v-icon>
          <h1 class="text-h4 font-weight-bold mt-4">Mini Twitter</h1>
          <p class="text-body-2 text-medium-emphasis mt-2">
            Comparte tus pensamientos con el mundo
          </p>
        </div>
        
        <!-- Card de Login/Register -->
        <v-card class="pa-6">
          <!-- Tabs para cambiar entre login y registro -->
          <v-tabs v-model="activeTab" grow class="mb-6">
            <v-tab value="login">Iniciar Sesión</v-tab>
            <v-tab value="register">Registrarse</v-tab>
          </v-tabs>
          
          <!-- Formulario de Login -->
          <v-window v-model="activeTab">
            <v-window-item value="login">
              <v-form @submit.prevent="handleLogin" ref="loginForm">
                <v-text-field
                  v-model="loginData.email"
                  label="Email o nombre de usuario"
                  prepend-inner-icon="mdi-account"
                  :rules="[rules.required]"
                  :error-messages="loginError"
                  @input="loginError = ''"
                />
                
                <v-text-field
                  v-model="loginData.password"
                  label="Contraseña"
                  prepend-inner-icon="mdi-lock"
                  :type="showPassword ? 'text' : 'password'"
                  :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                  @click:append-inner="showPassword = !showPassword"
                  :rules="[rules.required]"
                  class="mt-4"
                />
                
                <v-btn
                  type="submit"
                  color="primary"
                  size="large"
                  block
                  class="mt-6"
                  :loading="loading"
                  :disabled="loading"
                >
                  Iniciar Sesión
                </v-btn>
              </v-form>
            </v-window-item>
            
            <!-- Formulario de Registro -->
            <v-window-item value="register">
              <v-form @submit.prevent="handleRegister" ref="registerForm">
                <v-text-field
                  v-model="registerData.username"
                  label="Nombre de usuario"
                  prepend-inner-icon="mdi-at"
                  :rules="[rules.required, rules.username]"
                  hint="Solo letras, números y guiones bajos"
                />
                
                <v-text-field
                  v-model="registerData.displayName"
                  label="Nombre para mostrar (opcional)"
                  prepend-inner-icon="mdi-account"
                  :rules="[rules.maxLength(50)]"
                  class="mt-4"
                />
                
                <v-text-field
                  v-model="registerData.email"
                  label="Email"
                  prepend-inner-icon="mdi-email"
                  type="email"
                  :rules="[rules.required, rules.email]"
                  class="mt-4"
                />
                
                <v-text-field
                  v-model="registerData.password"
                  label="Contraseña"
                  prepend-inner-icon="mdi-lock"
                  :type="showPassword ? 'text' : 'password'"
                  :append-inner-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                  @click:append-inner="showPassword = !showPassword"
                  :rules="[rules.required, rules.minLength(6)]"
                  hint="Mínimo 6 caracteres"
                  class="mt-4"
                />
                
                <v-text-field
                  v-model="registerData.confirmPassword"
                  label="Confirmar contraseña"
                  prepend-inner-icon="mdi-lock-check"
                  :type="showPassword ? 'text' : 'password'"
                  :rules="[rules.required, rules.passwordMatch]"
                  class="mt-4"
                />
                
                <v-alert
                  v-if="registerError"
                  type="error"
                  density="compact"
                  class="mt-4"
                >
                  {{ registerError }}
                </v-alert>
                
                <v-btn
                  type="submit"
                  color="primary"
                  size="large"
                  block
                  class="mt-6"
                  :loading="loading"
                  :disabled="loading"
                >
                  Crear Cuenta
                </v-btn>
              </v-form>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, reactive, inject } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()
const showSnackbar = inject('showSnackbar')

// State
const activeTab = ref('login')
const showPassword = ref(false)
const loading = ref(false)
const loginError = ref('')
const registerError = ref('')

// Formularios refs
const loginForm = ref(null)
const registerForm = ref(null)

// Datos de login
const loginData = reactive({
  email: '',
  password: ''
})

// Datos de registro
const registerData = reactive({
  username: '',
  displayName: '',
  email: '',
  password: '',
  confirmPassword: ''
})

// Reglas de validación
const rules = {
  required: v => !!v || 'Este campo es obligatorio',
  email: v => /.+@.+\..+/.test(v) || 'Email no válido',
  username: v => /^[a-zA-Z0-9_]+$/.test(v) || 'Solo letras, números y guiones bajos',
  minLength: (min) => v => v.length >= min || `Mínimo ${min} caracteres`,
  maxLength: (max) => v => !v || v.length <= max || `Máximo ${max} caracteres`,
  passwordMatch: v => v === registerData.password || 'Las contraseñas no coinciden'
}

// Handlers
const handleLogin = async () => {
  const { valid } = await loginForm.value.validate()
  if (!valid) return
  
  loading.value = true
  loginError.value = ''
  
  try {
    await authStore.login(loginData)
    
    showSnackbar('¡Bienvenido! 👋', 'success')
    
    // Redirigir a la página solicitada o al timeline
    const redirect = route.query.redirect || '/timeline'
    router.push(redirect)
  } catch (error) {
    loginError.value = error.response?.data?.message || 'Error al iniciar sesión'
  } finally {
    loading.value = false
  }
}

const handleRegister = async () => {
  const { valid } = await registerForm.value.validate()
  if (!valid) return
  
  loading.value = true
  registerError.value = ''
  
  try {
    await authStore.register({
      username: registerData.username,
      displayName: registerData.displayName || registerData.username,
      email: registerData.email,
      password: registerData.password
    })
    
    showSnackbar('¡Cuenta creada! Ahora puedes iniciar sesión', 'success')
    
    // Cambiar a tab de login
    activeTab.value = 'login'
    loginData.email = registerData.email
    
    // Limpiar formulario de registro
    registerData.username = ''
    registerData.displayName = ''
    registerData.email = ''
    registerData.password = ''
    registerData.confirmPassword = ''
  } catch (error) {
    registerError.value = error.response?.data?.message || 'Error al crear cuenta'
  } finally {
    loading.value = false
  }
}
</script>
