<template>
  <div class="container">
    <h2>Change Password</h2>
    <form @submit.prevent="handleChangePassword">
      <label for="current-password">
        Current Password:
        <br />
        <input
          id="current-password"
          type="password"
          placeholder="current-password"
          v-model="currentPassword"
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
        {{ loading ? 'Changing...' : 'Change Password' }}
      </button>
    </form>
    <!--<p v-if="message" class="message">{{ message }}</p>
    <p v-if="error" class="error">{{ error }}</p>-->
  </div>
</template>

<script>
import { reset_password } from '../services/authServices.js';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
  name: "ChangePassword",
  data() {
    return {
      currentPassword: "",
      newPassword: "",
      confirmPassword: "",
      message: "",
      error: "",
      loading: false
    };
  },
  methods: {
    async handleChangePassword() {
    this.message = "";
    this.error = "";
    
    if (this.newPassword !== this.confirmPassword) {
      this.error = "New passwords do not match.";
      toast.error("New passwords do not match.", {
            autoClose: 5000, // 5 seconds
          });
      return;
    }
    
    this.loading = true;
    try {
      const response = await reset_password(
        this.currentPassword,
        this.newPassword,
        this.confirmPassword
      );
      
      // Clear any previous error
      this.error = "";
      
      // Handle different response structures
      if (response.data && response.data.detail) {
        this.message = response.data.detail;
        toast.success("Password updated successfully.", {
            autoClose: 5000, // 5 seconds
          });
      } else if (response.detail) {
        this.message = response.detail;
        toast.success("Password updated successfully.", {
            autoClose: 5000, // 5 seconds
          });
      } else {
        this.message = "Password updated successfully.";
        toast.success("Password updated successfully.", {
            autoClose: 5000, // 5 seconds
          });
      }
      
      // Clear form fields on success
      this.currentPassword = "";
      this.newPassword = "";
      this.confirmPassword = "";
      
    } catch (err) {
      this.message = ""; // Clear success message if there's an error
      this.error =
        (err.response && err.response.data && err.response.data.detail) ||
        err.message ||
        "An error occurred. Please try again.";
        toast.error("An error occurred. Please try again.", {
            autoClose: 5000, // 5 seconds
          });
    } finally {
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

.error {
  margin-top: 0.5rem;
  color: #ff6b6b;
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
  
  .error {
    color: #ff5252;
  }
}
</style>
