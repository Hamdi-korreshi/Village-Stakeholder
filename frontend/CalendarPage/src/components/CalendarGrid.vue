<template>
  <section
    class="w-full text-xs text-black whitespace-nowrap max-md:mt-8 max-md:max-w-full"
  >
    <div
      class="flex gap-5 justify-between mt-2 ml-8 max-w-full text-xs text-black whitespace-nowrap w-[583px]"
    >
      <div v-for="day in weekDays" :key="day">{{ day }}</div>
    </div>

    <div class="flex flex-wrap gap-1 mt-1.5">
      <CalendarCell
        v-for="day in calendarDays"
        :key="`${day.date}-${day.isCurrentMonth}`"
        :day="day"
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CalendarCell from "./CalendarCell.vue";
import type { DayCell } from "./types";

const weekDays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

const calendarDays = ref<DayCell[]>([
  // Previous month
  ...[23, 24, 25, 26, 27, 28].map((date) => ({
    date,
    isCurrentMonth: false,
  })),
  // Current month
  ...Array.from({ length: 31 }, (_, i) => ({
    date: i + 1,
    isCurrentMonth: true,
    scheduleType: i + 1 === 5 ? "blue" : i + 1 === 7 ? "green" : "default",
  })),
  // Next month
  ...[1, 2, 3, 4, 5].map((date) => ({
    date,
    isCurrentMonth: false,
  })),
]);
</script>
