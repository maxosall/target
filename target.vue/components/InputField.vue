<template lang="">
  <div class="mb-4">
    <label :for="htmlFor" class="block font-semibold text-sm ">{{label}}</label>
    <input class="rounded-md w-full text-sm p-2 border border-gray-300 outline-none transition-all focus-within:bg-zinc-50 focus-within:border-zinc-500 focus-within:transition-all"  type="text" :placeholder="placeholder" :id="htmlFor"/>
  </div>
</template>
<script setup>
  defineProps({
    label: String,
    type:String,
    placeholder:String,
    htmlFor: String
  })
</script>
<style lang="">
  
</style>