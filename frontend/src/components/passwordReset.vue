<template>
    <div class="container">
      <h2>Reset Password</h2>
      <!---<LoadingSpinner v-if="loading" />-->
      <form @submit.prevent="handleResetPassword">
        <label for="email">
          Email:
          <br />
          <input
            id="email"
            type="email"
            placeholder="Enter your email"
            v-model="email"
            required
          />
        </label>
        <br />
        <label for="new-password">
          New Password:
          <br />
          <input
            id="new-password"
            type="password"
            placeholder="Enter a new password"
            v-model="newPassword"
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
            placeholder="Confirm your new password"
            v-model="confirmPassword"
            required
          />
        </label>
        <br />
        <button type="submit" :disabled="loading">
          {{ loading ? 'Resetting...' : 'Reset Password' }}
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
        email: '',
        newPassword: '',
        confirmPassword: '',
        message: '',
        passwordError: '',
        loading: false,
      };
    },
    methods: {
      async handleResetPassword() {
        // Validate passwords match
        if (this.newPassword !== this.confirmPassword) {
          this.passwordError = 'Passwords do not match';
          return;
        }
  
        this.loading = true;
        this.passwordError = '';
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/reset-password', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
              email: this.email,
              new_password: this.newPassword,
            }),
          });
  
          this.loading = false;
  
          if (response.ok) {
            const data = await response.json();
            this.message = 'Password reset successful';
          } else {
            const errorData = await response.json();
            this.message = errorData.detail || 'Password reset failed';
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