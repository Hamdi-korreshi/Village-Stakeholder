<template>
    <div class="container">
      <h2>Register</h2>
     <!--<LoadingSpinner v-if="loading" />-->
      <form @submit.prevent="handleRegister">
        <label for="username">
          Username:
          <br />
          <input
            id="username"
            type="text"
            placeholder="Username"
            v-model="username"
            required
          />
        </label>
        <br />
        <label for="email">
          Email:
          <br />
          <input
            id="email"
            type="email"
            placeholder="Email"
            v-model="email"
            required
          />
        </label>
        <br />
        <label for="password">
          Password:
          <br />
          <input
            id="password"
            type="password"
            placeholder="Password"
            v-model="password"
            required
          />
        </label>
        <br />
        <label for="confirm-password">
          Confirm Password:
          <br />
          <input
            id="confirm-password"
            type="password"
            placeholder="Confirm Password"
            v-model="confirmPassword"
            required
          />
        </label>
        <br />
        <button type="submit" :disabled="loading">
          {{ loading ? 'Registering...' : 'Register' }}
        </button>
      </form>
      <p v-if="passwordError" style="color: red">{{ passwordError }}</p>
      <p class="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  //import LoadingSpinner from './LoadingSpinner.vue';
  
  export default {
    components: {
      LoadingSpinner,
    },
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        message: '',
        passwordError: '',
        loading: false,
      };
    },
    methods: {
      async handleRegister() {
        if (this.password !== this.confirmPassword) {
          this.passwordError = 'Passwords do not match';
          return;
        }
  
        this.loading = true;
        this.passwordError = '';
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
              username: this.username,
              email: this.email,
              password: this.password,
            }),
          });
  
          this.loading = false;
  
          if (response.ok) {
            const data = await response.json();
            this.message = 'Registration successful';
          } else {
            const errorData = await response.json();
            this.message = errorData.detail || 'Registration failed';
          }
        } catch (error) {
          this.loading = false;
          this.message = 'An error occurred: ' + error.message;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>