<template lang="">
  <div className="max-w-full mx-auto flex flex-shrink-1 items-center justify-center rounded-lg ">
      
      <div className='max-w-sm flex flex-1 flex-col bg-white p-8'>
        <h3 className="font-extrabold text-md text-center p-5">Login</h3>
        <InputField label="Email" type="email" placeholder="enter email" htmlFor="login_email" />
        <InputField label="Password" type="password" placeholder="enter password" htmlFor="login_password" />
        <div className='flex justify-between'>
          <div>
            <input type="checkbox" name="" id="rmbr_me" />
            <label htmlFor="rmbr_me"> remmber me</label>
          </div>
          <Link className='font-semibold text-sm pb-4 text-red-600' href="">forgot password?</Link>
        </div>
        <button className='bg-gray-700 hover:bg-gray-800 font-semibold text-sm text-white rounded-md p-2' type='button'>Login</button>
      </div>

      <!-- {/* <div className="max-w-sm flex flex-1">
        <p className="">don't have an account? <Link className='font-semibold text-sm' href="">create new</Link></p>
      </div> */} -->
      
    </div>
</template>
<script>
export default {
  
}
</script>
<style lang="">
  
</style>