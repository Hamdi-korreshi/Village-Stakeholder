<template>
  <div id="app">
    <LoginPage v-if="!isAuthenticated" @login-success="handleLoginSuccess" />
    <Dashboard v-else @logout="handleLogout" />
  </div>
</template>

<script>
import LoginPage from "./components/LoginPage.vue";
import Dashboard from "./components/Dashboard.vue";

export default {
  name: 'App',
  data() {
     return {
      isAuthenticated: false,
    };
  },
  methods: {
    handleLoginSuccess() {
      this.isAuthenticated = true;
    },
    handleLogout() {
      this.isAuthenticated = false;
    },
  },
};
</script>
