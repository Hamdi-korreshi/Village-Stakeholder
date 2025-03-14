<template>
    <div class="container">
      <h2>Profile</h2>
      <LoadingSpinner v-if="loading" />
      <form @submit.prevent="handleSaveProfile">
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
        <button type="submit" :disabled="loading">
          {{ loading ? 'Saving...' : 'Save Changes' }}
        </button>
      </form>
      <p v-if="message" class="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import LoadingSpinner from './LoadingSpinner.vue';
  
  export default {
    components: {
      LoadingSpinner,
    },
    data() {
      return {
        username: '',
        email: '',
        loading: false,
        message: '',
      };
    },
    created() {
      // Fetch the user's profile data when the component is created
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        this.loading = true;
        try {
          const response = await fetch('http://127.0.0.1:8000/api/profile', {
            method: 'GET',
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`, // Assuming the token is stored in localStorage
            },
          });
  
          if (response.ok) {
            const data = await response.json();
            this.username = data.username;
            this.email = data.email;
          } else {
            this.message = 'Failed to fetch profile data';
          }
        } catch (error) {
          this.message = 'An error occurred: ' + error.message;
        } finally {
          this.loading = false;
        }
      },
      async handleSaveProfile() {
        this.loading = true;
        this.message = '';
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/profile', {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Bearer ${localStorage.getItem('token')}`,
            },
            body: JSON.stringify({
              username: this.username,
              email: this.email,
            }),
          });
  
          if (response.ok) {
            const data = await response.json();
            this.message = 'Profile updated successfully';
          } else {
            const errorData = await response.json();
            this.message = errorData.detail || 'Failed to update profile';
          }
        } catch (error) {
          this.message = 'An error occurred: ' + error.message;
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
  
  label {
    display: block;
    margin-bottom: 10px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
  
  .message {
    margin-top: 10px;
    color: green;
  }
  </style>