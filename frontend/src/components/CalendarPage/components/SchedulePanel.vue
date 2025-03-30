<template>
  <aside class="w-full text-white max-md:mt-8">
    <section
      class="flex flex-col h-[400px] text-black bg-gray-100 border border-solid shadow-sm border-black border-opacity-0"
    >
      <header
        class="px-16 py-3 text-sm text-center bg-gray-100 border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5"
      >
        March {{ selectedDate }}
      </header>

      <div class="flex-1 overflow-y-auto px-0.5">
        <article
          v-for="event in dayEvents"
          :key="event.time"
          class="flex flex-col pt-2 pr-10 pb-4 pl-3.5 mt-2.5 mx-0.5 bg-green-100 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:pr-5"
        >
          <time class="self-start text-sm">{{ event.time }}</time>
          <p class="mt-2 text-xs">
            {{ event.description }}
          </p>
        </article>
      </div>
    </section>

    <div class="mt-4 space-y-3.5">
      <button
        type="button"
        @click="handleAddSchedule"
        class="flex justify-between items-center px-6 py-4 w-full h-[80px] bg-green-500 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5 hover:bg-green-600 transition-colors duration-200"
        style="background-color: #22c55e">
        <span class="text-lg font-bold whitespace-nowrap"
          >Add a Schedule Item</span
        >
        <span class="text-4xl">+</span>
      </button>

      <button
        type="button"
        @click="handleRemoveSchedule"
        class="flex justify-between items-center px-6 py-4 w-full h-[80px] bg-red-400 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5 hover:bg-red-500 transition-colors duration-200"
        style="background-color: #ef4444;">
        <span class="text-lg font-bold whitespace-nowrap"
          >Remove a Schedule Item</span
        >
        <span class="text-4xl">-</span>
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed } from "vue";
import type { ScheduleItem } from "./types";

const props = defineProps<{
  selectedDate: number;
  events: ScheduleItem[];
}>();

const emit = defineEmits<{
  (e: "add-schedule"): void;
  (e: "remove-schedule"): void;
}>();

const dayEvents = computed(() => {
  return props.events.filter((event) => event.date === props.selectedDate);
});

const handleAddSchedule = () => {
  emit("add-schedule");
  // This event can be handled by parent components later
  console.log("Add schedule clicked for date:", props.selectedDate);
};

const handleRemoveSchedule = () => {
  emit("remove-schedule");
  // This event can be handled by parent components later
  console.log("Remove schedule clicked for date:", props.selectedDate);
};

</script>

<style scoped>
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.2) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 3px;
}
</style>
