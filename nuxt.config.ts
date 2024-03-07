// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui',
    '@nuxt/test-utils/module',
    '@nuxtjs/google-fonts'
  ],
  googleFonts: {
    // Add font name and desired weights
    families: {
      'M PLUS Code Latin': [100, 200, 300, 400, 500], 
    },
    // Preload fonts for faster loading (optional)
    preload: true, 
    // Preconnect to Google Fonts servers (optional)
    preconnect: true, 
    // Other options like subsets and variants can be added here
  }
})
