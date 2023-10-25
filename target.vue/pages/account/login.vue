<template lang="">
  <div class="max-w-full mx-auto flex flex-shrink-1 items-center justify-center rounded-lg ">
      
      <div class='max-w-sm flex flex-1 flex-col bg-white p-8'>
        <h3 class="font-extrabold text-md text-center p-5">Login</h3>
        <InputField label="Email" type="email" placeholder="enter email" htmlFor="login_email" />
        <InputField label="Password" type="password" placeholder="enter password" htmlFor="login_password" />
        <div class='flex justify-between'>
          <div>
            <input type="checkbox" name="" id="rmbr_me" />
            <label htmlFor="rmbr_me"> remmber me</label>
          </div>
          <Link class='font-semibold text-sm pb-4 text-red-600' href="">forgot password?</Link>
        </div>
        <button class='bg-gray-700 hover:bg-gray-800 font-semibold text-sm text-white rounded-md p-2' type='button'>Login</button>
      </div>

      <!-- {/* <div class="max-w-sm flex flex-1">
        <p class="">don't have an account? <Link class='font-semibold text-sm' href="">create new</Link></p>
      </div> */} -->
      
    </div>
</template>
<script>
export default {
  
}
</script>
<style lang="">
  
</style>