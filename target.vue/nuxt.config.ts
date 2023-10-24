
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules:[
    'nuxt-icon'
  ],
  devtools: { enabled: true },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})