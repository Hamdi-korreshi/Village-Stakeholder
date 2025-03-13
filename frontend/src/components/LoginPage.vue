<template>
  <div class="login-page">
    <h2>Login</h2>
    <LoginForm @login-success="onLoginSuccess" />
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";

export default {
  name: "LoginPage",
  components: { LoginForm },
  methods: {
    onLoginSuccess() {
      this.$emit("login-success");
    },
  },
};
</script>
