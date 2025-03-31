<template>
  <section class="shadow-sm bg-zinc-300 h-[431px] w-full min-w-[200px]">
    <header class="p-1.5 text-sm text-center text-black bg-white shadow-sm">
      Members
    </header>
    <div
      class="members-list h-[calc(100%_-_28px)] overflow-y-auto p-2 space-y-2"
      role="list"
      aria-label="Members list"
    >
      <div
        v-for="member in members"
        :key="member.id"
        class="flex items-center justify-between p-2 bg-white rounded shadow-sm"
        role="listitem"
      >
        <!-- Left: Avatar + Name -->
        <div class="flex items-center gap-2">
          <div
            class="w-8 h-8 flex items-center justify-center rounded-full bg-gray-200 text-gray-600 text-base"
          >
            {{ member.username.charAt(0).toUpperCase() }}
          </div>
          <div class="text-sm font-medium text-gray-700">
            {{ member.username }}
          </div>
        </div>

        <!-- Right: Role badge -->
        <span class="px-2 py-1 text-xs bg-gray-100 text-gray-600 rounded">
          {{ member.role || "Member" }}
        </span>
      </div>

      <!-- Error Message -->
      <div v-if="errorMessage" class="text-red-500 text-center p-2">
        {{ errorMessage }}
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getPersonalVillageMembers } from '../../../services/villageServices.js';

const members = ref([]);
const errorMessage = ref("");

const displayMember = async () => {
  errorMessage.value = "";
  try {
    const data = await getPersonalVillageMembers();
    members.value = data.members;
    console.log("Fetched members:", data.members);
  } catch (error) {
    console.error('Fetch error:', error);
    errorMessage.value = error.message;
  }
};

onMounted(() => {
  displayMember();
});
</script>

<style scoped>
/* Scrollbar styling for Firefox */
.members-list {
  scrollbar-width: thin; /* Thin scrollbar */
  scrollbar-color: #d7d7d7 #F1F1F1; /* Thumb color and track color */
}

/* Webkit-based scrollbar styling for Chrome/Safari */
.members-list::-webkit-scrollbar {
  width: 8px; /* Set width for the vertical scrollbar */
}

.members-list::-webkit-scrollbar-track {
  background-color: #F1F1F1; /* Background color of the track */
}

.members-list::-webkit-scrollbar-thumb {
  background-color: #d7d7d7; /* Thumb color */
  border-radius: 4px; /* Rounded corners on the thumb */
}

.members-list::-webkit-scrollbar-thumb:hover {
  background-color: #d7d7d7; /* Hover effect on thumb */
}
</style>
