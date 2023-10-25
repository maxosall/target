<template lang="">
  <div class="max-w-5xl mx-auto flex items-center justify-center">
      <div class="max-w-sm flex flex-1 flex-col bg-white p-8 rounded-lg  ring-1 ring-slate-900/5 shadow-l">
        <h3 class="font-extrabold text-md text-center p-5">Sign up</h3>
        <TowFactorAuth />
        <InputField
          label="Email"
          type="email"
          placeholder="enter email"
          htmlFor="signup_email"
        />
        <InputField
          label="Password"
          type="password"
          placeholder="enter password"
          htmlFor="signup_password"
        />
        <InputField
          label="Confirm password"
          type="password"
          placeholder="reenter password"
          htmlFor="signup_confirm_password"
        />

        <button
          class="bg-gray-700 hover:bg-gray-800 font-semibold text-sm text-white rounded-md p-2.5"
          type="button"
        >
          Sign up
        </button>
      </div>
    </div>
</template>
<script>
export default {
  
}
</script>
<style lang="">
  
</style>