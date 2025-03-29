<template>
  <div class="change-password">
    <h2>Change Password</h2>
    <form @submit.prevent="handleChangePassword">
      <div class="form-group">
        <label for="current-password">Current Password:</label>
        <input type="password" id="current-password" v-model="currentPassword" required />
      </div>
      <div class="form-group">
        <label for="new-password">New Password:</label>
        <input type="password" id="new-password" v-model="newPassword" required />
      </div>
      <div class="form-group">
        <label for="confirm-password">Confirm New Password:</label>
        <input type="password" id="confirm-password" v-model="confirmPassword" required />
      </div>
      <button type="submit">Change Password</button>
    </form>
    <div v-if="message" class="message">{{ message }}</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ChangePassword",
  data() {
    return {
      currentPassword: "",
      newPassword: "",
      confirmPassword: "",
      message: "",
      error: ""
    };
  },
  methods: {
    async handleChangePassword() {
      this.message = "";
      this.error = "";
      if (this.newPassword !== this.confirmPassword) {
        this.error = "New passwords do not match.";
        return;
      }
      try {
        const response = await axios.post("/api/change-password/", {
          current_password: this.currentPassword,
          new_password: this.newPassword,
          confirm_password: this.confirmPassword
        });
        this.message = response.data.detail || "Password updated successfully.";
      } catch (err) {
        this.error =
          (err.response && err.response.data && err.response.data.detail) ||
          "An error occurred. Please try again.";
      }
    }
  }
};
</script>
