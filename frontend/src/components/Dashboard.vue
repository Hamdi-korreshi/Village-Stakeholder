<template>
    <div class="dashboard"> 
        <h2>Dashboard</h2>
        <button @click="signoutUser">Sign Out</button>
        <RandomStringDisplay />
        <router-link to='/change-pass'>Change Password</router-link>
        <div>
        <router-link to='/delete-profile'>Delete Profile</router-link>
        </div>
    </div>
</template>

<script>
    import { signout } from "../services/authServices"
    import RandomStringDisplay from "./RandomStringDisplay.vue"

export default {
  name: "Dashboard",
  components: {
    RandomStringDisplay,
    AddVillagerButton,
    MakeVillageButton
  },
  data() {
    return {
      currentUserId: 1,        // Replace with logic to get logged in user ID
      targetVillagerId: 2,     // Replace with selected villager/user to add
      selectedRelationId: 3    // Replace with selected relation ID
    }
  },
  methods: {
    async signoutUser() {
      try {
        const result = await signout();
        console.log(result.message)
        this.$router.push({ name: "Login" })
      } catch (error) {
        console.error("Sign out error", error);
      }
    }
  }
};
</script>