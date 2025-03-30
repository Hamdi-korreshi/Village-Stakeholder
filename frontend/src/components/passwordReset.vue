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
      <!--<p v-if="passwordError" style="color: red">{{ passwordError }}</p>
      <p class="message">{{ message }}</p>-->
    </div>
  </template>
  
  <script>
  //import LoadingSpinner from './LoadingSpinner.vue';
  import { toast } from "vue3-toastify";
  import "vue3-toastify/dist/index.css";
  
  export default {
    components: {
      //LoadingSpinner,
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
          toast.error("Passwords do not match", {
              autoClose: 5000, // 5 seconds
          });
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
            toast.success("Password reset successful", {
              autoClose: 5000, // 5 seconds
            });
          } else {
            const errorData = await response.json();
            this.message = errorData.detail || 'Password reset failed';
            toast.error("Passwords reset failed", {
              autoClose: 5000, // 5 seconds
            });
          }
        } catch (error) {
          this.loading = false;
          this.message = 'An error occurred: ' + error.message;
          toast.error("An error occured " + error.message, {
              autoClose: 5000, // 5 seconds
          });
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Overall layout */
  .container {
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
  form {
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
    border: 1px solid #4472C4;
    background-color: #242424;
    color: rgba(255, 255, 255, 0.87);
    font-family: inherit;
    font-size: 1em;
    transition: border-color 0.25s;
  }
  
  input:focus {
    border-color: #4472C4;
    outline: none;
  }
  
  input::placeholder {
    color: rgba(255, 255, 255, 0.5);
  }
  
  /* Button styles */
  button {
    width: 100%;
    margin-top: 1rem;
    background-color: #4472C4;
    color: white;
    transition: background-color 0.25s;
  }
  
  button:hover:not(:disabled) {
    background-color: #4472C4;
    border-color: #4472C4;
  }
  
  button:disabled {
    background-color: #3a3a3a;
    cursor: not-allowed;
    opacity: 0.7;
  }
  
  /* Message and error text */
  .message {
    margin-top: 1.5rem;
    color: #4CAF50; /* Success color */
    font-size: 0.9em;
  }
  
  p[style*="color: red"] {
    margin-top: 0.5rem;
    color: #ff6b6b !important;
    font-size: 0.9em;
  }
  
  /* Light mode adaptation */
  @media (prefers-color-scheme: light) {
    h2 {
      color: #213547;
    }
    
    form {
      background-color: #f9f9f9;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    label {
      color: #213547;
    }
    
    input {
      background-color: #ffffff;
      color: #213547;
      border-color: #4472C4;
    }
    
    input::placeholder {
      color: rgba(0, 0, 0, 0.5);
    }
    
    button {
      background-color: #4472C4;
    }
    
    button:hover:not(:disabled) {
      background-color: #4472C4;
    }
    
    button:disabled {
      background-color: #e0e0e0;
    }
    
    .message {
      color: #2E7D32; /* Darker success green for light mode */
    }
    
    p[style*="color: red"] {
      color: #ff5252 !important;
    }
  }
  </style>