<template>
  <div class="container">
    <h2>Register</h2>
    <form @submit.prevent="submitRegistration" class="register-form">
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
    <p v-if="errorMessage" style="color: red">{{ errorMessage }}</p>
    <p v-if="message" class="message">{{ message }}</p>
  </div>
</template>

<script>
import { register } from '../services/authServices.js'

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      message: '',
      passwordError: '',
      errorMessage: '',
      loading: false,
    };
  },
  methods: {
    async submitRegistration() {
      // Check password match first
      if (this.password !== this.confirmPassword) {
        this.passwordError = 'Passwords do not match';
        return;
      }
      
      this.loading = true;
      this.passwordError = '';
      this.errorMessage = '';
      this.message = '';

      try {
        const result = await register(this.email, this.username, this.password);
        if (result.message === "User registered successfully") {
          this.message = 'Registration successful';
          this.$emit("registration-success");
        } 
        else {
          this.errorMessage = result.error || "Registration failed.";
        }
      }
      catch (error) {
        this.errorMessage = "Registration failed please check your input";
        console.error("Registration error:", error);
      }
      finally {
        this.loading = false;
      }
    }
  }
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
    border: 1px solid #4472C4;
  }
  
  button {
    background-color: #4472C4;
  }
  
  button:hover:not(:disabled) {
    background-color: #4472C4;
    border-color: #4472C4;
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