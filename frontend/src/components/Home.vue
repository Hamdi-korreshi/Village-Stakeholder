<template>
  <div class="homepage">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>EMPOWERING YOUR JOURNEY</h1>
        <p class="hero-text">Our solutions are designed to meet people where they are, creating the greatest chance for success in education, employment, and life.</p>
        <button class="cta-button">Discover BTC</button>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission">
      <h2>BTC IS ALL ABOUT SOLVING REAL PROBLEMS</h2>
      <p>Too many young people face a lack of physical and digital equity in education, support, networking, resources, health and wellness services, and skill development. We place youth at the center of our work to address equity and agency head-on.</p>
    </section>

    <!-- Welcome Section -->
    <section class="welcome">
      <h2>WELCOME TO THE BTC PLATFORM</h2>
      <div class="login-container">
        <h3>Login to Your Account</h3>
        <form class="login-form" @submit.prevent="signinUser">
          <label for="identifier">
            Email or Username:
            <input
              id="identifier"
              type="text"
              placeholder="Username or Email"
              v-model="identifier"
              required
            />
          </label>
          <label for="password">
            Password:
            <input
              id="password"
              type="password"
              placeholder="Password"
              v-model="password"
              required
            />
          </label>
          <button type="submit">Login</button>
        </form>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { signin } from "../services/authServices.js";

export default {
  setup() {
    const identifier = ref('');
    const password = ref('');
    const errorMessage = ref('');
    const router = useRouter();

    const signinUser = async () => {
      errorMessage.value = "";
      try {
        const response = await signin(identifier.value, password.value);
        
        console.log("API Response:", response); // Debug log
        
        // Handle successful login
        if (response.message === "Login successful") {
          console.log("Redirecting to dashboard...");
          router.push({ name: "Dashboard" });
          return; // Important: Stop further execution
        }
        
        // Handle other cases
        errorMessage.value = response.message || "Login failed. Please try again.";
        
      } catch (error) {
        console.error("Login error:", error);
        errorMessage.value = error.response?.data?.message || 
                          "Login failed. Please check your credentials.";
      }
    };

    return {
      identifier,
      password,
      errorMessage,
      signinUser,
    };
  },
};
</script>

<style scoped>
.homepage {
  font-family: Arial, sans-serif;
  color: #333;
}

/* Hero Section */
.hero {
  background-color: #1a1a1a;
  color: white;
  padding: 4rem 2rem;
  text-align: center;
}

.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.hero-text {
  font-size: 1.2rem;
  max-width: 800px;
  margin: 0 auto 2rem;
}

.cta-button {
  background-color: #4472C4;
  color: white;
  padding: 0.8rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.cta-button:hover {
  background-color: #4472C4;
}

/* Mission Section */
.mission {
  padding: 3rem 2rem;
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.mission h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #1a1a1a;
}

.mission p {
  font-size: 1.1rem;
  line-height: 1.6;
}

/* Welcome Section */
.welcome {
  background-color: #f5f5f5;
  padding: 3rem 2rem;
  text-align: center;
}

.welcome h2 {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 2rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.login-container h3 {
  margin-bottom: 1.5rem;
  color: #1a1a1a;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.login-form label {
  text-align: left;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.login-form input {
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.login-form button {
  background-color: #4472C4;
  color: white;
  padding: 0.8rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  margin-top: 1rem;
}

.login-form button:hover {
  background-color: #4472C4;
}

.error-message {
  margin-top: 1rem;
  color: #ff5252;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }
  
  .hero-text {
    font-size: 1rem;
  }
  
  .mission h2, .welcome h2 {
    font-size: 1.5rem;
  }
}
</style>