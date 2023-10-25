<template lang="">
  <section class="flex justify-between pb-4">
    <button class="group flex items-center space-x-1 bg-slate-100 hover:bg-slate-200 py-2 px-3 text-sm transition-all hover:transition-all rounded-full">
      <Icon icon="ci:google" class="h-5 w-5 group-hover:text-red-500"></Icon>
      <span class="group-hover:text-slate-900 text-slate-600 group-hover:font-medium">Google</span>
    </button>

    <button class="group flex items-center space-x-1 bg-slate-100 hover:bg-slate-200 py-2 px-3 text-sm transition-all hover:transition-all rounded-full">
      <Icon icon="logos:facebook" class="h-5 w-5 hover:text-blue-500"></Icon> 
      <span class="group-hover:text-slate-900 text-slate-600 group-hover:font-medium">Facebook</span>
    </button>

    <button class="group flex items-center space-x-1 bg-slate-100 hover:bg-slate-200 py-2 px-3 text-sm transition-all hover:transition-all rounded-full">
      <Icon icon="logos:twitter" class="h-5 w-5 hover:text-sky-500"></Icon>
      <span class="group-hover:text-slate-900 text-slate-600 group-hover:font-medium">Twitter</span>
    </button>
  </section>
</template>
<script setup>
import { Icon } from '@iconify/vue'
</script>
<style lang="">
  
</style>