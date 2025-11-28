/**
 * Configuración de Vuetify
 * Tema claro/oscuro y componentes Material Design
 */

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import '@mdi/font/css/materialdesignicons.css'

// Tema personalizado para la app tipo Twitter
const lightTheme = {
  dark: false,
  colors: {
    background: '#F5F8FA',
    surface: '#FFFFFF',
    primary: '#1DA1F2',      // Azul Twitter
    secondary: '#14171A',
    accent: '#794BC4',
    error: '#E0245E',
    info: '#1DA1F2',
    success: '#17BF63',
    warning: '#FFAD1F',
    'on-background': '#14171A',
    'on-surface': '#14171A'
  }
}

const darkTheme = {
  dark: true,
  colors: {
    background: '#15202B',
    surface: '#192734',
    primary: '#1DA1F2',
    secondary: '#8899A6',
    accent: '#794BC4',
    error: '#E0245E',
    info: '#1DA1F2',
    success: '#17BF63',
    warning: '#FFAD1F',
    'on-background': '#FFFFFF',
    'on-surface': '#FFFFFF'
  }
}

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi
    }
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: lightTheme,
      dark: darkTheme
    }
  },
  defaults: {
    VBtn: {
      rounded: 'pill',
      elevation: 0
    },
    VCard: {
      rounded: 'lg',
      elevation: 1
    },
    VTextField: {
      variant: 'outlined',
      density: 'comfortable'
    },
    VTextarea: {
      variant: 'outlined',
      density: 'comfortable'
    }
  }
})

export default vuetify
