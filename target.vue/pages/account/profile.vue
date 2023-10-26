<template lang="">
  <div class="max-w-[850px] bg-white mx-auto">
    <section class="flex justify-between items-center p-5">
      <div>
        <Icon icon="material-symbols:account-circle-full" class="h-8 w-8"></Icon>
        <h3 class="">Profile</h3></div>
      
      <div class="flex space-x-4 text-sm">
        <NuxtLink class="border p-2 text-sm font-medium cursor-pointer" to="">Edit professonal info</NuxtLink>
        <NuxtLink class="border p-2 text-sm font-medium cursor-pointer" to="">Edit contact info</NuxtLink>
      </div>
    </section>
    
  </div>
</template>
<script>
import {Icon } from '@iconify/vue'
</script>
<style lang="">
  
</style>