<template>
    <div>
      <h2>Login</h2>
      <!--<LoadingSpinner v-if="loading" />-->
      <form class="container" @submit.prevent="handleLogin">
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
        <button type="submit">Login</button>
      </form>
      <p class="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  //import LoadingSpinner from './LoadingSpinner.vue';
  
  export default {
    components: {
      //LoadingSpinner,
    },
    props: {
      onLoginSuccess: {
        type: Function,
        required: true,
      },
    },
    setup(props) {
      const username = ref('');
      const password = ref('');
      const message = ref('');
      const loading = ref(false);
      const router = useRouter();
  
      const handleLogin = async () => {
        loading.value = true;
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/login', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
              username: username.value,
              password: password.value,
            }),
          });
  
          loading.value = false;
  
          if (response.ok) {
            const data = await response.json();
            const token = data.token;
            localStorage.setItem('access_token', token);
            message.value = 'Login successful';
            props.onLoginSuccess();
            router.push({ path: '/', state: { message: 'Login Successful' } });
          } else {
            const errorData = await response.json();
            message.value = errorData.detail || 'Invalid username or password';
          }
        } catch (error) {
          loading.value = false;
          message.value = 'An error occurred: ' + error.message;
        }
      };
  
      return {
        username,
        password,
        message,
        loading,
        handleLogin,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>