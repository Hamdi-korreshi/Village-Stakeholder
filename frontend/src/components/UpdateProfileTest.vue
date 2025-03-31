<template>
  <div class="UpdateProfile">
    <h2>Update Profile</h2>
    <form @submit.prevent="handleUpdate">
      <div>
        <label for="profile_picture">Profile Picture URL:</label>
        <input type="url" id="profile_picture" v-model="profile_picture" />
      </div>
      <!--
      <div>
        <label for="profile_settings">Profile Settings (JSON):</label>
        <textarea id="profile_settings" v-model="profile_settings"></textarea>
      </div>
      -->
      <div>
        <label for="full_name">Full Name:</label>
        <input type="text" id="full_name" v-model="full_name" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" />
      </div>
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" />
      </div>
      <div>
        <label for="bio">Bio:</label>
        <textarea id="bio" v-model="bio"></textarea>
      <button type="submit">Update Profile</button>
      </div>
    </form>
  </div>
</template>

<script>

import {update_profile} from '../services/authServices.js'
export default {
  name: "UpdateProfile",
  data() {
    return {
      full_name: "",
      email: "",
      username: "",
      profile_picture: "",
      //profile_settings: "",
      bio: "",
      message: "",
      error: ""
    };
  },
  methods: {
    async handleUpdate() {
      this.message = "";
      this.error = "";
      
      const payload = {
        full_name: this.full_name,
        email: this.email,
        username: this.username,
        profile_picture: this.profile_picture,
        //profile_settings: this.profile_settings
        bio: this.bio
      };

      try {
        const response = await update_profile(payload);
        this.message = response.message || "Profile updated successfully.";
      } catch (err) {
        this.error = (err.response && err.response.data && err.response.data.detail) ||
                     "An error occurred updating your profile.";
        console.error("Update profile error:", err);
      }
    }
  }
};
</script>


<style scoped>
.update-profile {
  max-width: 600px;
  margin: 0 auto;
}

.update-profile form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
