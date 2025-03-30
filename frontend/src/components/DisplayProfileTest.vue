<template>
  <div class="profile-display">
    <h2>My Profile</h2>
    <div v-if="loading">Loading profile...</div>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="profile && !loading">
      <p><strong>Full Name:</strong> {{ profile.full_name }}</p>
      <p><strong>Email:</strong> {{ profile.email }}</p>
      <p><strong>Username:</strong> {{ profile.username }}</p>
      <p v-if="profile.bio"><strong>Bio:</strong> {{ profile.bio }}</p>
      <div v-if="profile.profile_picture">
        <strong>Profile Picture:</strong>
        <img :src="profile.profile_picture" alt="Profile Picture" />
      </div>
      <div v-if="profile.profile_settings">
        <strong>Profile Settings:</strong>
        <pre>{{ profile.profile_settings }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import { get_profile } from '../services/authServices.js';

export default {
  name: "ProfileDisplay",
  data() {
    return {
      profile: null,
      loading: true,
      error: null,
    };
  },
  async created() {
    try {
      const data = await get_profile();
      this.profile = data;
    } catch (err) {
      this.error = err.response?.data?.error || "Failed to load profile.";
      console.error("Error fetching profile:", err);
    } finally {
      this.loading = false;
    }
  },
};
</script>

<style scoped>
.profile-display {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
}
.error {
  color: red;
  margin-top: 10px;
}
.profile-display img {
  max-width: 150px;
  margin-top: 10px;
}
</style>
