<template>
  <div>
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Home,
    Navbar
  }
}
</script>
