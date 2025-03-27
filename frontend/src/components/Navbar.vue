<template>
  <div id="app">
    <header class="flex items-center px-20 py-5 w-full bg-gray-100 max-md:px-10 max-md:py-5 max-sm:flex-col max-sm:px-5 max-sm:py-5 max-sm:text-center">
      <div class="flex items-center text-xl font-bold text-blue-500 object-contain h-[84px] max-sm:mb-5">
        <img src="../assets/logo.png" alt="B the Cause Logo" class="h-20 mr-2" />

      </div>
      <nav class="px-8 py-7 ml-44 bg-gray-50 rounded-[35px] w-[600px] max-md:ml-20 max-md:w-[500px] max-sm:w-full max-sm:ml-0">
        <ul class="flex gap-11 justify-center max-sm:flex-col max-sm:gap-5 max-sm:items-center">
          <li>
            <router-link 
              to="/" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Home</router-link>
          </li>
          <li>
            <router-link 
              to="/login" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Login</router-link>
          </li>
          <li>
            <router-link 
              to="/registration" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Register</router-link>
          </li>
          <li>
            <router-link 
              to="/profile" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Profile</router-link>
          </li>
          <li>
            <router-link 
              to="/passwordReset" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Reset Password</router-link>
          </li>
          <li>
            <router-link 
              to="/emailVerification" 
              class="text-xs cursor-pointer text-stone-500 hover:text-black hover:font-bold"
              active-class="text-blue-700 font-bold"
            >Verify Email</router-link>
          </li>
        </ul>
      </nav>
    </header>
  </div>
</template>

<script>
import { createApp } from "vue";

export default {
  name: "Header",
};

const app = createApp({
  name: "Header",
  components: {
    Header: {
      template: "#app",
    },
  },
});

app.mount("#app");
</script>