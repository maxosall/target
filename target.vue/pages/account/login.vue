<template lang="">
  <div
    class="max-w-full mx-auto flex flex-shrink-1 items-center justify-center rounded-lg">
    <section class="max-w-sm flex flex-1 flex-col bg-white rounded-lg ring-1 ring-slate-900/5 shadow-l" >
      <div class="max-w-sm flex flex-1 flex-col p-6">
        <h3 class="font-extrabold text-md text-center p-5">Login with</h3>
        <TowFactorAuth />

        <Divider/>

        <InputField
          label="Email"
          type="email"
          placeholder="enter email"
          htmlFor="login_email"/>

        <InputField
          label="Password"
          type="password"
          placeholder="enter password"
          htmlFor="login_password"/>
        <div class="flex justify-between mb-4">
          <div>
            <input type="checkbox" name="" id="rmbr_me" />
            <label for="rmbr_me"> Remmber me</label>
          </div>
          <NuxtLink
            class="font-semibold text-sm text-red-600 hover:underline"
            to="/" >forgot password?</NuxtLink>
        </div>
        <button
          class="bg-gray-800 hover:bg-gray-900 font-medium text-sm text-white rounded-md p-2.5"
          type="button">
          Login
        </button>
      </div>

      <div class="max-w-sm flex flex-1 p-6 border-t">
        <p class="text-sm text-salate-600">
          Don't have an account?
          <NuxtLink
            class="font-medium text-sm text-red-600 hover:underline"
            to="/account/signup" >create new account</NuxtLink>
        </p>
      </div>
    </section>
  </div>
</template>
<script setup></script>
<style lang=""></style>
