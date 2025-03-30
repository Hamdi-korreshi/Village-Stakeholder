<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="signinUser">
      <label for="identifier">
        Email or Username:
        <br />
        <input
          id="identifier"
          type="text"
          placeholder="Username"
          v-model="identifier"
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
    <!--<p v-if="errorMessage" class="error">{{ errorMessage }}</p>-->
  </div>
</template>

<script>
import { signin } from "../services/authServices.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

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
      this.errorMessage = "";
      try {
        const response = await signin(identifier.value, password.value);
        
        console.log("API Response:", response); // Debug log
        
        // Handle successful login
        if (response.message === "Login successful!") {
          console.log("Redirecting to dashboard...");
          this.$emit("login-success");
          toast.success("Login Successful!", {
              autoClose: 5000, // 5 seconds
          });
          setTimeout(() => {
            this.$router.push({ name: "Dashboard" });
          }, 2000);
          return;
        }
        
        // Handle other cases
        this.errorMessage = response.message || "Login failed. Please try again.";
        toast.error("Login failed. Please check your credentials.", {
              autoClose: 5000, // 5 seconds
          });
        
      } catch (error) {
        console.error("Login error:", error);
        this.errorMessage = error.response?.data?.message || 
                          "Login failed. Please check your credentials.";
            toast.error("Login failed. Please check your credentials.", {
              autoClose: 5000, // 5 seconds
          });
      }
    },
  },
};
</script>

<style scoped>
/* Your existing styles remain the same */
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
}

button:hover {
  background-color: #4472C4;
  border-color: #4472C4;
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
    border: 1px solid #4472C4;
  }
  
  button {
    background-color: #4472C4;
  }
  
  button:hover {
    background-color: #4472C4;
    border-color: #4472C4;
  }
  
  .message {
    color: #ff5252;
  }
}
</style>