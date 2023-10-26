<template lang="">
  <div class="max-w-5xl mx-auto flex items-center justify-center">
      <section class="max-w-sm flex flex-1 flex-col bg-white rounded-lg ring-1 ring-slate-900/5 shadow-l">
        <div class="max-w-sm flex flex-1 flex-col p-6">
          <h3 class="font-extrabold text-md text-center p-5">Sign up with</h3>
          <TowFactorAuth />


          <div class="flex items-center">
            <p class="flex-1 border-b"></p>
            <span class="px-6">or</span>
            <p class="flex-1 border-b"></p>
          </div>


          <InputField
            label="Email"
            type="email"
            placeholder="enter email"
            htmlFor="signup_email" />
          <InputField
            label="Password"
            type="password"
            placeholder="enter password"
            htmlFor="signup_password" />
          <InputField
            label="Confirm password"
            type="password"
            placeholder="reenter password"
            htmlFor="signup_confirm_password" />
          <button
            class="bg-gray-700 hover:bg-gray-800 font-semibold text-sm text-white rounded-md p-2.5"
            type="button" >Sign up</button>
        </div>

        <div class="max-w-sm flex flex-1 p-6 border-t">
          <p class="text-sm text-salate-600">
            Already have account?
            <NuxtLink
              class="font-medium text-sm text-red-600 hover:underline"
              to="/account/login" >Sign up</NuxtLink>
          </p>
        </div>
      </section>
    </div>
</template>
<script>
export default {
  
}
</script>
<style lang="">
  
</style>