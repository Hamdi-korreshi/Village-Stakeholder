<template>
  <section class="shadow-sm bg-zinc-300 w-[621px] max-md:w-full">
    <header
      class="px-0 py-1.5 text-sm text-center text-black bg-white shadow-sm sticky top-0 z-10"
    >
      Members
    </header>
    <div class="h-[400px] p-4 overflow-y-auto custom-scrollbar">
      <ul class="space-y-2 overflow-hidden">
        <li
          v-for="member in members"
          :key="member.id"
          class="flex items-center justify-between bg-white rounded-lg p-3 shadow-sm"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 bg-gray-200 rounded-full flex items-center justify-center text-gray-600"
            >
              {{ member.username.charAt(0).toUpperCase() }}
            </div>
            <span class="text-gray-700">{{ member.username }}</span>
          </div>
          <span class="px-2 py-1 text-xs bg-gray-100 text-gray-600 rounded">{{
            member.role || "Member"
          }}</span>
        </li>
      </ul>
      <div
        v-if="members.length === 0"
        class="flex items-center justify-center h-[300px] text-gray-500"
      >
        No members found
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  members: {
    type: Array,
    required: true,
    default: () => [],
  },
});
</script>

<style scoped>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #cbd5e0 #edf2f7;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #edf2f7;
  border-radius: 3px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #cbd5e0;
  border-radius: 3px;
  border: 2px solid #edf2f7;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #a0aec0;
}
</style>
