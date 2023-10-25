<template lang="">
  <footer class="bg-white border-gray-200 dark:bg-gray-900 border-b py-5">
    <div class="grid grid-cols-12 max-w-screen-xl mx-auto gap-4 p-4">
      <!-- left side -->
      <div class="col-span-12 md:col-span-6 ">
        <div class="grid grid-cols-12 gap-5">
          <NuxtLink
            to="https://flowbite.com/"
            class="col-span-12  flex items-center justify-center md:justify-start
             font-extrabold text-red-500 hover:text-red-700 space-x-2 ">
            <Icon icon="mdi:target" class="h-7 w-7 self-center"></Icon>
            <span
              class="self-center text-2xl font-extrabold whitespace-nowrap dark:text-white" >
              target</span>
          </NuxtLink>

          <div class="col-span-12 md:col-span-6 space-y-4">
            <p class="font-medium text-sm text-gray-700 text-center md:text-left"   >
              The (target web app) offers real job oppotunaties for all people
              and all career fieds
            </p>
            <div class="flex space-x-4 justify-center md:justify-start">
              <Icon class="w-6 h-6 cursor-pointer text-gray-600 hover:text-blue-600"
                icon="ic:baseline-facebook" />
              <Icon class="w-6 h-6 cursor-pointer text-gray-600 hover:text-sky-600"
                icon="mdi:twitter" />
            </div>
          </div>

          <!--  -->
          <div class="col-span-12 md:col-span-6 space-y-4">
            <ul class="grid md:grid-cols-2 text-center md:text-left">
              <li v-for="link in links">
                <NuxtLink
                  class="text-gray-900 hover:font-normal block text-sm font-normal pl-3 pr-4 py-1.5 rounded-md hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:p-0 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
                  :to="link.href">
                    {{ "- " }} {{ link.label }}</NuxtLink>
              </li>
            </ul>
          </div>

        </div>
      </div>
      <!-- right side -->
      <div class="col-span-12 md:col-span-6 hidden md:block">
        <h3 class="text-sm font-semibold">Job fields</h3>

      </div>
      <p class="text-xs font-medium text-gray-800 col-span-full">all copyrights belong to <NuxtLink class="text-blue-700 font-semibold underline underline-offset-2">target</NuxtLink> 2023</p>
    </div>
  </footer>

  
</template>
<script setup>
import { Icon } from "@iconify/vue";

const links = [
  { label: "who are we?", href: "/about-us" },
  { label: "common questions", href: "/common-questions" },
  { label: "job opennings", href: "/job-opennings" },
  { label: "the website map", href: "/the-website-map" },
  { label: "customers feedback", href: "/customers-feedback" },
  { label: "our partners", href: "/our-partners" },
  { label: "contact us", href: "/our-partners" },
  { label: "our partners", href: "/contact-us" },
  { label: "browse companies", href: "/browse-companies" },
  { label: "policy aggrements", href: "/policy-aggrements" },
];
</script>
<style lang=""></style>
