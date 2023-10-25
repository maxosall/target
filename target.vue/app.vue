<template>
    <Navbar/>
    
    <NuxtLayout >
      <main class="max-w-screen-xl mx-auto p-4 ">
        <NuxtPage/>
      </main>

      
    </NuxtLayout>
    <Footer v-if="['/account/login', '/account/signup'].includes($route.path) === false " />
</template>
<script setup>
const route = useRoute()

</script>

