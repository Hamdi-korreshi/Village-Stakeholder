<template>
  <div>
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue';
console.log("API_URL:", import.meta.env.VITE_API_URL)

export default {
  name: 'App',
  components: {
    Home,
    Navbar
  }
}
</script>
