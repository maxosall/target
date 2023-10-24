import {resolve} from 'path'
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  alias:{
    '@': resolve(__dirname, '/')
  },
  css: ['~/assets/css/style.css'],
  modules:['nuxt-icon', ],
  devtools: { enabled: true },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})