<script setup>
import { Icon } from "@iconify/vue";
</script>

<template lang="">
  <div class="grid grid-cols-12 space-y-5 md:space-y-0 md:space-x-5">
    <div class="col-span-12 md:col-span-8">
      <!-- header bar  -->
      <div
        class="space-x-4 flex flex-wrap bg-white p-5 items-center mb-5 rounded-sm"
      >
        <Icon
          icon="material-symbols:star-outline-rounded"
          class="h-6 w-6 text-red-500"
        />

        <h3 class="font-semibold text-black text-sm">
          Jobs that may suit you fields
        </h3>
        <span class="text-gray-500">(8 jobs)</span>
      </div>

      <!-- card deck -->
      <div class="grid md:grid-cols-2 gap-5 mb-5 rounded-sm">
        
          <JobCard
            jobTitle="Writer"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />
          <JobCard
            jobTitle="Marketing"
            logoUrl="https://unsplash.it/40/40"
            company="loop"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />
          <JobCard
            jobTitle="Busness Manager"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />
          <JobCard
            jobTitle="Engineer"
            logoUrl="https://unsplash.it/40/40"
            company="toxify-inc"
            location="cairo, ain shams"
            ageRange="18-35"
            date="9 days ago"
          />
        
      </div>

      <!-- {/* Job application history */} -->
        <div class="bg-white mb-5">
          <h3 class="font-semibold p-5 rounded-sm">
            List of jobs you have applied on
            <span class="font-extralight text-gray-500"> (4) jobs</span>
          </h3>

          <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
              <thead class="text-xs text-gray-700 uppercase  dark:bg-gray-700 dark:text-gray-400">
                <tr>
                  <th scope="col" class="px-6 py-3">
                    Job Title
                  </th>
                  <th scope="col" class="px-6 py-3">
                    Company
                  </th>
                  <th scope="col" class="px-6 py-3">
                    Applicans
                  </th>
                  <th scope="col" class="px-6 py-3">
                    Status
                  </th>
                  <th scope="col" class="px-6 py-3">
                    Application Date
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                  <th
                    scope="row"
                    class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    IOS Developer
                  </th>
                  <td class="px-6 py-3">Apple</td>
                  <td class="px-6 py-3">83</td>
                  <td class="px-6 py-3">rejected</td>
                  <td class="px-6 py-3">2 weeks ago </td>
                </tr>
                <tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th
                    scope="row"
                    class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    AI Developer
                  </th>
                  <td class="px-6 py-3"> OpenAI</td>
                  <td class="px-6 py-3">350</td>
                  <td class="px-6 py-3"> Noticed</td>
                  <td class="px-6 py-3"> 9 days ago </td>
                </tr>
                <tr class="bg-white border-b dark:bg-gray-900 dark:border-gray-700">
                  <th
                    scope="row"
                    class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    Pianist
                  </th>
                  <td class="px-6 py-3">MurderInc</td>
                  <td class="px-6 py-3">30</td>
                  <td class="px-6 py-3">---</td>
                  <td class="px-6 py-3">1 hour ago </td>
                </tr>
                <tr class="border-b bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
                  <th
                    scope="row"
                    class="px-6 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                  >
                    Photographer
                  </th>
                  <td class="px-6 py-3">Pink Moon</td>
                  <td class="px-6 py-3">12</td>
                  <td class="px-6 py-3">accepted</td>
                  <td class="px-6 py-3">3 days ago</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
    </div>
    <div class="col-span-12 md:col-span-4 space-y-5">
        <div class="space-x-4 flex bg-white p-5 items-center ">
          <span class="">
            You have <span class="font-semibold">(15 jobs)</span> to apply into it this week
          </span>
        </div>

        <div class=" bg-white ">
          <Accordion header="this text don't panic">
            
            <div class="grid grid-cols-12 gap-4">
              <figure class="col-span-4 rounded-md bg-slate-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-red-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-blue-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-green-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-yellow-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-stone-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-orange-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-lime-400 w-full h-16 "></figure>
              <figure class="col-span-4 rounded-md bg-indigo-400 w-full h-16 "></figure>
            </div>
          </Accordion>

          <Accordion header="Fist Question" >
            <div></div>
          </Accordion>

          <Accordion header="Fist Question" >
            <div></div>
          </Accordion>
        </div>
      </div>
  </div>
</template>
