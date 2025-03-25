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
    <button @click="changeValue" class="bg-blue-300 p-4">
      {{ temp }}
    </button>
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

  <script setup>
    import {ref} from "vue"
    const temp = ref("test")
    function changeValue(){
      temp.value = "placeholder"
    }
  </script>
  
  <style scoped>
  /* Overall layout */
  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    max-width: 400px;
    margin: 0 auto;
  }
  
  h2 {
    font-size: 2em;
    margin-bottom: 1.5rem;
    color: rgba(255, 255, 255, 0.87);
  }
  
  /* Form container */
  .container {
    width: 100%;
    padding: 2em;
    border-radius: 8px;
    background-color: #1a1a1a;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  
  /* Input fields */
  label {
    display: block;
    margin-bottom: 1rem;
    font-size: 1em;
    color: rgba(255, 255, 255, 0.87);
    text-align: left;
  }
  
  input {
    width: 100%;
    padding: 0.6em;
    margin-top: 0.5rem;
    border-radius: 8px;
    border: 1px solid #646cff;
    background-color: #242424;
    color: rgba(255, 255, 255, 0.87);
    font-family: inherit;
    font-size: 1em;
    transition: border-color 0.25s;
  }
  
  input:focus {
    border-color: #535bf2;
    outline: none;
  }
  
  /* Button styles */
  button {
    width: 100%;
    margin-top: 1rem;
    background-color: #646cff;
    color: white;
  }
  
  button:hover {
    background-color: #535bf2;
    border-color: #535bf2;
  }
  
  /* Message text */
  .message {
    margin-top: 1.5rem;
    color: #ff6b6b;
    font-size: 0.9em;
  }
  
  /* Light mode adaptation */
  @media (prefers-color-scheme: light) {
    h2 {
      color: #213547;
    }
    
    .container {
      background-color: #f9f9f9;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    label {
      color: #213547;
    }
    
    input {
      background-color: #ffffff;
      color: #213547;
      border: 1px solid #747bff;
    }
    
    button {
      background-color: #747bff;
    }
    
    button:hover {
      background-color: #646cff;
      border-color: #646cff;
    }
    
    .message {
      color: #ff5252;
    }
  }
  </style>