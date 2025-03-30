<template>
  <div class="dashboard"> 
    <h2>Dashboard</h2>
    <button @click="signoutUser">Sign Out</button>

    <!-- Add Villager Button Component -->
    <AddVillagerButton 
      :userId="currentUserId" 
      :associateId="targetVillagerId" 
      :relationId="selectedRelationId" 
    />

    <!-- Make Village Button Component -->
    <MakeVillageButton 
      :ownerId="currentUserId" 
      description="Welcome to my village!" 
    />

    <RandomStringDisplay />
  </div>
</template>

<script>
import { signout } from "../services/authServices"
import RandomStringDisplay from "./RandomStringDisplay.vue"
import AddVillagerButton from "./add_villager.vue"
import MakeVillageButton from "./make_village.vue"  //  import the new button

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