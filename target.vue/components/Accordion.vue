<template lang="">
  <div>
      <h3 @click="isActive = !isActive" class="p-4 text-sm font-semibold cursor-pointer border-b">
        {{header}}</h3>
        <div :class="['p-5' , isActive ? 'block' : 'hidden']">
          <slot></slot>
        </div>
    </div>
</template>
<script setup>
  let isActive= ref(false)
  function toggleIsActive(){
    return isActive = !isActive
  }
  defineProps({
    header: String  
  })
</script>
<style lang="">
  
</style>