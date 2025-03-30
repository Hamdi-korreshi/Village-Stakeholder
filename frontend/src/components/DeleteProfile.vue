<template>
  <div>
    <button @click="handleDelete">Delete Profile</button>
    <div v-if="message" class="message">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import { delete_profile } from '../services/authServices.js';

export default {
  name: "DeleteProfile",
  data() {
    return {
      message: "",
      error: ""
    };
  },
  methods: {
    async handleDelete() {
      this.message = "";
      this.error = "";
      try {
        const response = await delete_profile();
        this.message = response.message || "Profile deleted successfully.";
        this.$router.push({ name: "Login" }); // redirect to login after deletion
      } catch (err) {
        this.error =
          (err.response && err.response.data && err.response.data.detail) ||
          "An error occurred.";
      }
    }
  }
};
</script>

<style scoped>
.message {
  color: green;
  margin-top: 10px;
}
.error {
  color: red;
  margin-top: 10px;
}
</style>
