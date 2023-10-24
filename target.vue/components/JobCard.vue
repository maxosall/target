<template lang="">
  <div  class="block space-y-4 md:max-w-md p-6 bg-white border border-gray-200 rounded-sm shadow-sm hover:bg-gray-100 dark:bg-gray-800 dark:border-gray-700 dark:hover:bg-gray-700">
      <!-- card header  -->
      <div class='flex items-center justify-between text-sm'>
        <h3 class='font-semibold '>{{jobTitle}}</h3>
        <img class='rounded-full' :src="logoUrl" />
      </div>

      <div class='text-sm'>
        <p class='flex space-x-4 items-center'>Company: <span class='font-semibold'> {{' '}} {{company}}</span></p>
        <p class='flex space-x-4 items-center'><IoLocationOutline /><span>{{location}}</span></p>
        <p class='flex justify-between  space-x-4 items-center'> 
          <span class='flex items-center '> 
          <CgCalendarDates />{{date}} . age range ({{ageRange}})</span>
        </p>
      </div>
      <button type="button" class="px-5 py-2.5 w-full text-sm font-medium text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-md text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">view description</button>

    </div>
</template>

<script setup>
defineProps({
    jobTitle:String,
    logoUrl: String,
    company: String,
    location: String,
    ageRange: String,
    date: String
  })
</script>
<style lang=""></style>
