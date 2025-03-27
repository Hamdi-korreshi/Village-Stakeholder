<template>
  <div class="login-form">
    <form @submit.prevent="signinUser">
      <div>
        <label for="identifier">Email or Username:</label>
        <input type="text" id="identifier" v-model="identifier" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { signin } from "../services/authServices.js";

export default {
  name: "LoginForm",
  data() {
    return {
      identifier: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async signinUser() {
      try {
        const result = await signin(this.identifier, this.password);
        if (result.message === "Login successful") {
          // Optionally use result.random_value as needed.
          this.$emit("login-success");
        } else {
          this.errorMessage = "Login failed.";
        }
      } catch (error) {
        this.errorMessage = "Login failed. Please check your credentials.";
        console.error("Login error", error);
      }
    },
  },
};
</script>
