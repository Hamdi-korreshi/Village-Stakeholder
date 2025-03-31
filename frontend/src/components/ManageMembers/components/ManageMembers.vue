<template>
  <div class="min-w-screen min-h-screen bg-gray-100">
    <Header />
    <main class="px-20 py-8 max-md:p-5">
      <h1 class="mb-6 text-5xl text-center text-black max-sm:text-3xl">
        Manage Members
      </h1>

      <div class="flex gap-8 justify-center max-md:flex-col max-md:items-center">
        <MembersList :members="members" />

        <aside
          class="flex flex-col gap-3.5 pt-12 max-md:pt-0 max-md:mt-5 max-sm:gap-2.5 max-md:w-full"
        >
          <ActionButton
            text="Add a Member"
            variant="add"
            @click="handleAddMember"
          />
          <ActionButton
            text="Remove a Member"
            variant="remove"
            @click="showRemoveMemberPopup = true"
          />
        </aside>
      </div>
    </main>

    <AddMemberPopup v-model="showAddMemberPopup" @add="addMember" />
    <RemoveMemberPopup
      v-model="showRemoveMemberPopup"
      :members="members"
      @remove="removeMember"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Header from "./Header.vue";
import MembersList from "./MembersList.vue";
import ActionButton from "./ActionButton.vue";
import AddMemberPopup from "./AddMemberPopup.vue";
import RemoveMemberPopup from "./RemoveMemberPopup.vue";

import {
  addVillagerToVillage,
  removeVillagerFromVillage,
  getPersonalVillageMembers,
} from "../../../services/villageServices.js";

const showAddMemberPopup = ref(false);
const showRemoveMemberPopup = ref(false);
const members = ref([]);

// Function to refresh members from backend
const refreshMembers = async () => {
  try {
    const data = await getPersonalVillageMembers();
    console.log("Refreshed members:", data);
    members.value = data.members;
  } catch (error) {
    console.error("Failed to refresh members:", error);
    alert("Unable to reload members. Please make sure you're logged in.");
  }
};

// Load on mount
onMounted(() => {
  refreshMembers();
});

const handleAddMember = () => {
  console.log("Opening add member popup");
  showAddMemberPopup.value = true;
};

const addMember = async (memberData) => {
  try {
    const response = await addVillagerToVillage(memberData.username, memberData.role);
    console.log("Backend response:", response);
    await refreshMembers(); // 🔁 Refresh after adding
  } catch (err) {
    console.error("Failed to add member:", err);
    alert("Could not add member. Make sure the username is correct and you are logged in.");
  }
};

const removeMember = async (villagerUsername) => {
  try {
    const response = await removeVillagerFromVillage(villagerUsername);
    console.log("Removed successfully:", response);
    await refreshMembers(); // 🔁 Refresh after removing
  } catch (error) {
    console.error("Failed to remove member:", error);
    alert("Failed to remove villager.");
  }
};
</script>
