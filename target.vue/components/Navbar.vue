
<script setup>
import {Icon } from '@iconify/vue'

const route = useRoute()

const links = [
  { label: "Dashboard", href: "/dashboard" },
  { label: "Job Opennings", href: "/job-opennings" },
  { label: "Browse Jobs", href: "/browse-job" },
  { label: "Profile", href: "/account/profile" },  
];

let isCollapsed = ref(false)

</script>
<template>
  <nav class="bg-white  border-gray-200 dark:bg-gray-900 border-b mb-5">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto px-4 py-3">
      <NuxtLink to="https://flowbite.com/" 
        class="flex font-extrabold text-red-500 hover:text-red-700 justify-center space-x-4 items-center">
        <Icon icon="mdi:target" class="h-9 w-9 self-center "></Icon>
        
        <span class="self-center text-2xl font-extrabold whitespace-nowrap dark:text-white">Flowbite</span>
      </NuxtLink>
      <div class="flex items-center space-x-2 md:order-2">
        <NuxtLink
            to="/account/signup"
             class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-semibold rounded-md text-sm px-3.5 py-2 mr-3 md:mr-0  dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
            Sign up
            </NuxtLink>
          <NuxtLink
            to="/account/login"
            class="text-white font-semibold bg-gray-800 hover:bg-gray-900 focus:ring-4 focus:outline-none focus:ring-gray-300 font-sm rounded-md text-sm px-3.5 py-2 text-center mr-3 md:mr-0 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Login
          </NuxtLink>
        <button @click="isCollapsed = !isCollapsed" data-collapse-toggle="navbar-sticky" type="button"
          class="inline-flex items-center p-1 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-sticky" aria-expanded="false">
          <span class="sr-only">Open main menu</span>
          
          <Icon  icon="material-symbols:menu" class="h-6 w-6"/>

          
        </button>
      </div>
      <div :class="[isCollapsed ? 'flex' : 'hidden' ,'items-center justify-between w-full md:flex md:w-auto md:order-1']" id="navbar-sticky">
        <ul
          class="w-full flex flex-col font-normal text-sm p-4 md:p-0 mt-4 rounded-md bg-white md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
          <li v-for="link in links"
            >
            <NuxtLink :to="link.href" 
            :class="[link.href === $route.path
              ? 'text-blue-900 font-medium underline-offset-8 underline transition-all'
              : 'text-gray-900 transition-all', 
              'block pl-3 pr-4 py-2 rounded-md hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700']">{{ link.label }}</NuxtLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
