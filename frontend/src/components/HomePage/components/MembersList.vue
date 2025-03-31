<template>
  <section class="shadow-sm bg-zinc-300 h-[431px] max-md:w-full">
    <header class="p-1.5 text-sm text-center text-black bg-white shadow-sm">
      Members
    </header>
    <div class="h-[calc(100%_-_28px)] overflow-auto" role="list" aria-label="Members list">
      <ul class="p-2">
        <li v-for="(member, index) in members" :key="index" class="py-1 border-b border-gray-400">
          {{ member.username }}
        </li>
      </ul>
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
