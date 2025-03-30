<template>
  <div class="login-page">
    <h2>Login</h2>
    <LoginForm @login-success="onLoginSuccess" />
    <p>
      Don't have an account?
      <router-link to="/register">Register here</router-link>
    </p>
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";
console.log('VITE_API_URL:', import.meta.env.VITE_API_URL);

export default {
  name: "LoginPage",
  components: { LoginForm },
  methods: {
    onLoginSuccess() {
      this.$router.push({ name: "Dashboard"})
    },
  },
};
</script>
